from typing import Any, Dict
from src.career_assistant.core.base_agent import BaseAgent
from src.career_assistant.core.contracts import GapAnalysis
from src.career_assistant.utils.llm_wrapper import GeminiLLM

class SkillGapAgent(BaseAgent):
    """
    Agent responsible for analyzing the skill gap between a resume profile and a target role.
    """

    def __init__(self, name: str, config: Any = None):
        super().__init__(name, config)
        self.llm = GeminiLLM(config=self.config)

    async def run(self, input_data: Dict[str, Any]) -> GapAnalysis:
        """
        Analyzes the skill gap and returns a GapAnalysis object.
        
        Args:
            input_data: Dict containing 'resume_profile' (ResumeProfile) and 'target_role' (str).
        """
        resume_profile = input_data["resume_profile"]
        target_role = input_data["target_role"]
        
        prompt = f"""
        Analyze the skill gap between the user's resume profile and the target role.
        
        Resume Profile:
        {resume_profile.model_dump_json()}
        
        Target Role:
        {target_role}
        
        Provide the gap analysis in the required structured format.
        """
        
        # Using the LLM wrapper to get structured output
        return self.llm.generate_structured_output(prompt, GapAnalysis)
