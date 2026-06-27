from typing import Any
from src.career_assistant.core.base_agent import BaseAgent
from src.career_assistant.core.contracts import JobRecommendations, ResumeProfile
from src.career_assistant.utils.llm_wrapper import GeminiLLM

class JobMatcherAgent(BaseAgent):
    """
    Agent responsible for recommending suitable job roles based on a resume profile.
    """

    def __init__(self, name: str, config: Any = None):
        super().__init__(name, config)
        self.llm = GeminiLLM(config=self.config)

    async def run(self, resume_profile: ResumeProfile) -> JobRecommendations:
        """
        Recommends job roles and returns a JobRecommendations object.
        
        Args:
            resume_profile: ResumeProfile object containing user's skills and experience.
        """
        
        prompt = f"""
        Recommend suitable job roles based on the following resume profile:
        
        Resume Profile:
        {resume_profile.model_dump_json()}
        
        Provide the job recommendations in the required structured format.
        """
        
        # Using the LLM wrapper to get structured output
        return self.llm.generate_structured_output(prompt, JobRecommendations)
