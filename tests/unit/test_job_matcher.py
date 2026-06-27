import pytest
from src.career_assistant.agents.job_matcher import JobMatcherAgent
from src.career_assistant.core.contracts import JobRecommendations, ResumeProfile, Skill

@pytest.mark.asyncio
async def test_job_matcher_agent_mock():
    # Test using mock mode to avoid API calls
    config = {"llm_mode": "mock"}
    agent = JobMatcherAgent(name="TestJobMatcherAgent", config=config)
    
    # Create sample input
    resume_profile = ResumeProfile(
        full_name="John Doe",
        contact_info={"email": "john@example.com"},
        skills=[Skill(name="Python", level="advanced")],
        strengths=["Problem Solving"],
        experience_summary="Experienced software engineer.",
        experience_level="Senior"
    )
    
    result = await agent.run(resume_profile)
    
    assert isinstance(result, JobRecommendations)
    assert len(result.recommendations) > 0
    assert result.recommendations[0].role_title == "Cloud Engineer"
    assert result.recommendations[0].match_score > 0.5
