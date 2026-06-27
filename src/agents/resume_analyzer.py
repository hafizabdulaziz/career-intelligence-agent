from typing import Any
from src.career_assistant.core.base_agent import BaseAgent
from src.career_assistant.core.contracts import ResumeProfile
from src.career_assistant.utils.llm_wrapper import GeminiLLM

class ResumeAnalyzerAgent(BaseAgent):
    """
    Agent responsible for extracting structured profile information from resume text.
    """

    def __init__(self, name: str, config: Any = None):
        super().__init__(name, config)
        self.llm = GeminiLLM(config=self.config)

    async def run(self, resume_text: str) -> ResumeProfile:
        """
        Analyzes the resume text and returns a ResumeProfile object.
        """
        prompt = f"""
        Analyze the following resume text and extract the required structured information.
        
        Resume text:
        {resume_text}
        """
        
        # Using the LLM wrapper to get structured output
        return self.llm.generate_structured_output(prompt, ResumeProfile)
