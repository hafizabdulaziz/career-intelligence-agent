import pytest
import asyncio
from src.career_assistant.orchestrator import CareerOrchestrator
from src.career_assistant.core.contracts import CareerStrategyReport

@pytest.mark.asyncio
async def test_career_orchestrator_integration():
    # Setup the central orchestrator
    orchestrator = CareerOrchestrator(config={"llm_mode": "mock"})
    
    # Define sample user inputs
    sample_resume = "John Doe, Senior Software Engineer. Expert in Python, REST APIs, and basic SQL."
    sample_target_role = "Cloud Engineer"

    # Execute the workflow
    report = await orchestrator.run_career_strategy_flow(sample_resume, sample_target_role)

    # Verify that the final aggregated report contains correct, structured data
    assert isinstance(report, CareerStrategyReport)
    assert report.user_name == "John Doe"
    assert report.resume_profile.full_name == "John Doe"
    assert len(report.resume_profile.skills) > 0
    assert report.resume_profile.skills[0].name == "Python"
    
    # Gap Analysis validation
    assert report.gap_analysis is not None
    assert len(report.gap_analysis.missing_skills) > 0
    assert report.gap_analysis.missing_skills[0].name == "AWS"
    
    # Learning Roadmap validation
    assert report.learning_roadmap is not None
    assert len(report.learning_roadmap.milestones) > 0
    assert report.learning_roadmap.milestones[0].topic == "AWS Fundamentals"
    
    # Job Recommendations validation
    assert report.job_recommendations is not None
    assert len(report.job_recommendations.recommendations) > 0
    assert report.job_recommendations.recommendations[0].role_title == "Cloud Engineer"
    
    # Overall summary verification
    assert "Cloud Engineer" in report.summary
