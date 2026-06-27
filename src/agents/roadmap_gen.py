from typing import Any
from src.career_assistant.core.base_agent import BaseAgent
from src.career_assistant.core.contracts import LearningRoadmap, GapAnalysis
from src.career_assistant.utils.llm_wrapper import GeminiLLM

class RoadmapGeneratorAgent(BaseAgent):
    """
    Agent responsible for generating a learning roadmap based on skill gaps.
    """

    def __init__(self, name: str, config: Any = None):
        super().__init__(name, config)
        self.llm = GeminiLLM(config=self.config)

    async def run(self, gap_analysis: GapAnalysis) -> LearningRoadmap:
        """
        Generates a learning roadmap and returns a LearningRoadmap object.
        
        Args:
            gap_analysis: GapAnalysis object containing missing skills.
        """
        
        prompt = f"""
        Generate a learning roadmap to bridge the following skill gaps:
        
        Gap Analysis:
        {gap_analysis.model_dump_json()}
        
        Provide the roadmap in the required structured format.
        """
        
        # Using the LLM wrapper to get structured output
        return self.llm.generate_structured_output(prompt, LearningRoadmap)
