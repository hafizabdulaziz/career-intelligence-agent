from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, Optional

from src.career_assistant.core.contracts import (
    CareerStrategyReport,
    ResumeProfile,
    GapAnalysis,
    LearningRoadmap,
    JobRecommendations
)
from src.career_assistant.agents.resume_analyzer import ResumeAnalyzerAgent
from src.career_assistant.agents.skill_gap_agent import SkillGapAgent
from src.career_assistant.agents.roadmap_gen import RoadmapGeneratorAgent
from src.career_assistant.agents.job_matcher import JobMatcherAgent

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("CareerOrchestrator")

class CareerOrchestrator:
    """
    Central orchestrator coordinating the sequential execution of specialized career agents.
    """

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        # Instantiate worker agents
        self.resume_analyzer = ResumeAnalyzerAgent(name="ResumeAnalyzer", config=self.config)
        self.skill_gap_agent = SkillGapAgent(name="SkillGapAgent", config=self.config)
        self.roadmap_generator = RoadmapGeneratorAgent(name="RoadmapGenerator", config=self.config)
        self.job_matcher = JobMatcherAgent(name="JobMatcher", config=self.config)

    async def run_career_strategy_flow(self, resume_text: str, target_role: str) -> CareerStrategyReport:
        """
        Runs the full end-to-end multi-agent career assessment workflow.
        
        Args:
            resume_text: Raw text content extracted from the user's resume.
            target_role: The user's desired job role/title.
            
        Returns:
            A CareerStrategyReport containing aggregated analysis from all agents.
        """
        logger.info("Starting Career Strategy Workflow...")
        
        if not resume_text.strip():
            raise ValueError("Resume text cannot be empty.")
        if not target_role.strip():
            raise ValueError("Target role cannot be empty.")

        # Phase 1: Analyze Resume
        logger.info("Step 1: Running Resume Analyzer Agent...")
        resume_profile: ResumeProfile = await self.resume_analyzer.run(resume_text)
        logger.info(f"Resume Analyzer successfully completed. User: {resume_profile.full_name}")
        await asyncio.sleep(15)  # Delay to respect free tier quota

        # Phase 2: Run Skill Gap Analysis
        logger.info("Step 2: Running Skill Gap Agent...")
        gap_input = {
            "resume_profile": resume_profile,
            "target_role": target_role
        }
        gap_analysis: GapAnalysis = await self.skill_gap_agent.run(gap_input)
        logger.info("Skill Gap Analysis completed.")
        await asyncio.sleep(15)  # Delay to respect free tier quota

        # Phase 3: Generate Learning Roadmap
        logger.info("Step 3: Running Roadmap Generator Agent...")
        roadmap: LearningRoadmap = await self.roadmap_generator.run(gap_analysis)
        logger.info("Learning Roadmap generation completed.")
        await asyncio.sleep(15)  # Delay to respect free tier quota

        # Phase 4: Job Matching Recommendations
        logger.info("Step 4: Running Job Matcher Agent...")
        job_recommendations: JobRecommendations = await self.job_matcher.run(resume_profile)
        logger.info("Job recommendations completed.")

        # Final Phase: Aggregation
        logger.info("Step 5: Aggregating Career Strategy Report...")
        report = CareerStrategyReport(
            user_name=resume_profile.full_name,
            resume_profile=resume_profile,
            gap_analysis=gap_analysis,
            learning_roadmap=roadmap,
            job_recommendations=job_recommendations,
            summary=f"Successfully generated career strategy report for {resume_profile.full_name} targeting '{target_role}'."
        )
        logger.info("Career Strategy Workflow completed successfully.")
        return report
