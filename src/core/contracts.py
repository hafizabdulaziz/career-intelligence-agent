from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class GapSeverity(str, Enum):
    CRITICAL = "critical"
    IMPORTANT = "important"
    OPTIONAL = "optional"

class Skill(BaseModel):
    name: str
    level: str = "intermediate"  # e.g., beginner, intermediate, advanced

class ResumeProfile(BaseModel):
    """Extracted information from the user's resume."""
    full_name: str
    contact_info: Dict[str, str]
    skills: List[Skill] = Field(default_factory=list)
    strengths: List[str] = Field(default_factory=list)
    experience_summary: str
    experience_level: str  # e.g., Junior, Mid, Senior

class GapAnalysis(BaseModel):
    """Comparison between resume skills and target role requirements."""
    missing_skills: List[Skill] = Field(default_factory=list)
    matched_skills: List[Skill] = Field(default_factory=list)
    gap_severity: Dict[str, GapSeverity] = Field(default_factory=dict)
    rationale: str

class LearningMilestone(BaseModel):
    """A single step in a learning roadmap."""
    topic: str
    description: str
    estimated_effort: str  # e.g., "2 weeks", "10 hours"
    priority: int = Field(ge=1, le=5)

class LearningRoadmap(BaseModel):
    """A sequenced learning path to close skill gaps."""
    milestones: List[LearningMilestone] = Field(default_factory=list)
    resources_suggestions: List[str] = Field(default_factory=list)
    overall_estimated_timeline: str

class JobRecommendation(BaseModel):
    """A suggestion for a suitable job role."""
    role_title: str
    match_score: float = Field(ge=0.0, le=1.0)
    rationale: str

class JobRecommendations(BaseModel):
    """A collection of suggested job roles."""
    recommendations: List[JobRecommendation] = Field(default_factory=list)

class CareerStrategyReport(BaseModel):
    """The final aggregated report produced by the Orchestrator."""
    user_name: str
    resume_profile: ResumeProfile
    gap_analysis: Optional[GapAnalysis] = None
    learning_roadmap: Optional[LearningRoadmap] = None
    job_recommendations: Optional[JobRecommendations] = None
    summary: str
