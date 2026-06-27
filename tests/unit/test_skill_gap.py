import pytest
from src.career_assistant.agents.skill_gap_agent import SkillGapAgent
from src.career_assistant.core.contracts import GapAnalysis, ResumeProfile, Skill, GapSeverity

@pytest.mark.asyncio
async def test_skill_gap_agent_mock():
    # Test using mock mode to avoid API calls
    config = {"llm_mode": "mock"}
    agent = SkillGapAgent(name="TestSkillGapAgent", config=config)
    
    # Create sample input
    resume_profile = ResumeProfile(
        full_name="John Doe",
        contact_info={"email": "john@example.com"},
        skills=[Skill(name="Python", level="advanced")],
        strengths=["Problem Solving"],
        experience_summary="Experienced software engineer.",
        experience_level="Senior"
    )
    
    gap_input = {
        "resume_profile": resume_profile,
        "target_role": "Cloud Engineer"
    }
    
    result = await agent.run(gap_input)
    
    assert isinstance(result, GapAnalysis)
    assert len(result.missing_skills) > 0
    assert result.missing_skills[0].name == "AWS"
    assert result.gap_severity["AWS"] == GapSeverity.CRITICAL
