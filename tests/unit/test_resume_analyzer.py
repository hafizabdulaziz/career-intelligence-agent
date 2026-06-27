import pytest
from src.career_assistant.agents.resume_analyzer import ResumeAnalyzerAgent
from src.career_assistant.core.contracts import ResumeProfile

@pytest.mark.asyncio
async def test_resume_analyzer_mock():
    # Test using mock mode to avoid API calls
    config = {"llm_mode": "mock"}
    agent = ResumeAnalyzerAgent(name="TestResumeAnalyzer", config=config)
    
    resume_text = "Experienced software engineer with Python skills."
    
    result = await agent.run(resume_text)
    
    assert isinstance(result, ResumeProfile)
    assert result.full_name == "John Doe"
    assert len(result.skills) > 0
    assert result.skills[0].name == "Python"
