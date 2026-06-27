import pytest
from src.career_assistant.agents.roadmap_gen import RoadmapGeneratorAgent
from src.career_assistant.core.contracts import LearningRoadmap, GapAnalysis, Skill, GapSeverity

@pytest.mark.asyncio
async def test_roadmap_gen_agent_mock():
    # Test using mock mode to avoid API calls
    config = {"llm_mode": "mock"}
    agent = RoadmapGeneratorAgent(name="TestRoadmapGenAgent", config=config)
    
    # Create sample input
    gap_analysis = GapAnalysis(
        missing_skills=[Skill(name="AWS", level="intermediate")],
        matched_skills=[Skill(name="Python", level="advanced")],
        gap_severity={"AWS": GapSeverity.CRITICAL},
        rationale="User lacks cloud computing experience."
    )
    
    result = await agent.run(gap_analysis)
    
    assert isinstance(result, LearningRoadmap)
    assert len(result.milestones) > 0
    assert result.milestones[0].topic == "AWS Fundamentals"
    assert result.overall_estimated_timeline == "2 weeks"
