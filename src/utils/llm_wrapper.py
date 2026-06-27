from __future__ import annotations

import copy
import logging
from typing import Any, Type, TypeVar, Dict
from pydantic import BaseModel
from google import genai
from google.genai import types
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log
)

from src.career_assistant.config.settings import settings

# Setup logging
logger = logging.getLogger("GeminiLLM")
logger.setLevel(settings.LOG_LEVEL)

T = TypeVar("T", bound=BaseModel)

class LLMAPIError(Exception):
    """Custom exception for LLM API related issues."""
    pass

def clean_and_dereference_schema(schema_class: Type[BaseModel]) -> Dict[str, Any]:
    """
    Generates a JSON schema from a Pydantic model, dereferences any local $ref definitions,
    and strips out forbidden 'additionalProperties' keys for Gemini Developer API compatibility.
    """
    schema = schema_class.model_json_schema()
    defs = schema.pop("$defs", {})
    
    def resolve_refs(node: Any) -> Any:
        if isinstance(node, dict):
            if "$ref" in node:
                ref_path = node["$ref"]
                ref_key = ref_path.split("/")[-1]
                resolved = defs.get(ref_key, {})
                resolved = resolve_refs(resolved)
                node = copy.deepcopy(resolved)
            else:
                for k, v in list(node.items()):
                    node[k] = resolve_refs(v)
            
            node.pop("additionalProperties", None)
            
        elif isinstance(node, list):
            return [resolve_refs(item) for item in node]
            
        return node

    return resolve_refs(schema)

class GeminiLLM:
    """
    Production-ready Gemini LLM client using the latest SDK and robust retry logic.
    """

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.mode = self.config.get("llm_mode", "live")
        
        if self.mode == "live":
            # Direct usage of API key from settings; let the SDK handle validation
            api_key = settings.GEMINI_API_KEY
            if not api_key:
                raise LLMAPIError("GEMINI_API_KEY is not set in environment.")
            try:
                self.client = genai.Client(api_key=api_key)
            except Exception as e:
                logger.error(f"Failed to initialize Gemini client: {e}")
                raise LLMAPIError("Failed to initialize Gemini client") from e
        else:
            logger.info("Initializing GeminiLLM in mock mode.")
            self.client = None

    def _retry_on_rate_limit(retry_state):
        return isinstance(retry_state.outcome.exception(), Exception) and \
               ("429" in str(retry_state.outcome.exception()) or "Quota" in str(retry_state.outcome.exception()))

    @retry(
        stop=stop_after_attempt(settings.RETRY_COUNT),
        wait=wait_exponential(multiplier=settings.RETRY_DELAY_SECONDS, min=5, max=60),
        retry=retry_if_exception_type((Exception)), # Broad retry for API transients
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True
    )
    def generate_structured_output(
        self, 
        prompt: str, 
        response_schema: Type[T]
    ) -> T:
        """
        Sends a prompt to Gemini and enforces structured output using Pydantic.
        """
        if self.mode == "mock":
            return self._generate_mock_output(response_schema, prompt)

        if not self.client:
            raise LLMAPIError("Gemini client is not initialized.")

        try:
            # Clean and dereference the schema for Gemini Developer API compatibility
            clean_schema = clean_and_dereference_schema(response_schema)
            
            # Using the new google.genai SDK
            response = self.client.models.generate_content(
                model=settings.LLM_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=clean_schema,
                    temperature=settings.TEMPERATURE,
                    max_output_tokens=settings.MAX_TOKENS,
                )
            )
            
            if not response.text:
                raise LLMAPIError("Gemini API returned an empty response.")
            
            # Validate and parse directly into the Pydantic model
            return response_schema.model_validate_json(response.text)
            
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}")
            raise LLMAPIError(f"API call failed after retries: {e}") from e

    def _generate_mock_output(self, response_schema: Type[T], prompt: str = "") -> T:
        """Generates mock structured data based on the requested schema."""
        from src.career_assistant.core.contracts import (
            ResumeProfile, GapAnalysis, LearningRoadmap, JobRecommendations,
            Skill, GapSeverity, LearningMilestone, JobRecommendation
        )
        
        schema_name = response_schema.__name__
        
        if schema_name == "ResumeProfile":
            # Dynamic extraction using regex
            import re
            match = re.search(r"Name:\s*([^\n\r]+)", prompt, re.IGNORECASE)
            name = match.group(1).strip() if match else "John Doe"
            return ResumeProfile(
                full_name=name,
                contact_info={"email": "test@example.com"},
                skills=[Skill(name="Python", level="advanced")],
                strengths=["Problem Solving"],
                experience_summary="Experienced engineer.",
                experience_level="Senior"
            )
        elif schema_name == "GapAnalysis":
            return GapAnalysis(
                missing_skills=[Skill(name="AWS", level="intermediate")],
                matched_skills=[Skill(name="Python", level="advanced")],
                gap_severity={"AWS": GapSeverity.CRITICAL},
                rationale="User lacks cloud computing experience."
            )
        elif schema_name == "LearningRoadmap":
            return LearningRoadmap(
                milestones=[
                    LearningMilestone(
                        topic="AWS Fundamentals",
                        description="Learn basic services like EC2, S3, RDS.",
                        estimated_effort="2 weeks",
                        priority=1
                    )
                ],
                resources_suggestions=["AWS Certified Cloud Practitioner course"],
                overall_estimated_timeline="2 weeks"
            )
        elif schema_name == "JobRecommendations":
            return JobRecommendations(
                recommendations=[
                    JobRecommendation(
                        role_title="Cloud Engineer",
                        match_score=0.8,
                        rationale="Python skills are highly relevant for Cloud development/DevOps."
                    )
                ]
            )
        else:
            try:
                return response_schema()
            except Exception:
                raise LLMAPIError(f"Mock output not implemented for schema: {schema_name}")
