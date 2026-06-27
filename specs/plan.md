# Architectural Plan: AI Multi-Agent Career Assistant

## 1. System Architecture
The system follows the **Orchestrator-Worker Pattern**. A central `CareerOrchestrator` manages the lifecycle of the request, invoking specialized worker agents in a deterministic sequence. Each agent is a stateless service that takes a structured input and produces a structured output.

### High-Level Component Diagram
`User Input (Resume + Target Role)` $ightarrow$ `Orchestrator` $ightarrow$ [`ResumeAnalyzer` $ightarrow$ `SkillGapAnalyzer` $ightarrow$ `RoadmapGenerator` $ightarrow$ `JobMatcher`] $ightarrow$ `Final Report`

## 2. Agent Architecture

### 2.1 Resume Analyzer Agent
- **Responsibility**: Parse raw text and extract structured professional data.
- **Input**: Raw resume text.
- **Output**: `ResumeProfile` (Dataclass: skills, strengths, experience_level).

### 2.2 Skill Gap Agent
- **Responsibility**: Compare user profile against role requirements.
- **Input**: `ResumeProfile` + `TargetRole`.
- **Output**: `GapAnalysis` (Dataclass: missing_skills, matched_skills, gap_severity).

### 2.3 Roadmap Generator Agent
- **Responsibility**: Convert gaps into a learning sequence.
- **Input**: `GapAnalysis`.
- **Output**: `LearningRoadmap` (Dataclass: milestones, resources_suggestions, estimated_timeline).

### 2.4 Job Match Agent
- **Responsibility**: Suggest roles based on current strengths.
- **Input**: `ResumeProfile`.
- **Output**: `JobRecommendations` (Dataclass: suggested_roles, match_scores, rationales).

### 2.5 Orchestrator Agent
- **Responsibility**: State management, sequence control, and data aggregation.
- **Input**: User request.
- **Output**: `CareerStrategyReport` (Combined data from all agents).

## 3. Folder Structure
```text
src/career_assistant/
├── __init__.py
├── main.py                 # Entry point
├── orchestrator.py         # CareerOrchestrator logic
├── core/
│   ├── __init__.py
│   ├── base_agent.py       # Abstract Base Class for all agents
│   └── contracts.py        # Pydantic models/Dataclasses for inter-agent communication
├── agents/
│   ├── __init__.py
│   ├── resume_analyzer.py  # ResumeAnalyzer implementation
│   ├── skill_gap_agent.py  # SkillGapAgent implementation
│   ├── roadmap_gen.py      # RoadmapGenerator implementation
│   └── job_matcher.py      # JobMatcher implementation
├── utils/
│   ├── __init__.py
│   ├── llm_wrapper.py      # Unified interface for LLM calls (mockable)
│   └── file_handler.py     # Resume parsing utilities
└── config/
    ├── __init__.py
    └── settings.py         # Configuration management
tests/
├── __init__.py
├── unit/
│   ├── test_resume_analyzer.py
│   ├── test_skill_gap.py
│   ├── test_roadmap_gen.py
│   └── test_job_matcher.py
└── integration/
    └── test_orchestrator.py
```

## 4. Workflow Design (Deterministic Sequence)
1. **Initialize**: Orchestrator receives `resume_text` and `target_role`.
2. **Phase 1 (Analysis)**: Call `ResumeAnalyzer` $ightarrow$ returns `ResumeProfile`.
3. **Phase 2 (Comparison)**: Call `SkillGapAnalyzer` using `ResumeProfile` and `target_role` $ightarrow$ returns `GapAnalysis`.
4. **Phase 3 (Planning)**: Call `RoadmapGenerator` using `GapAnalysis` $ightarrow$ returns `LearningRoadmap`.
5. **Phase 4 (Discovery)**: Call `JobMatcher` using `ResumeProfile` $ightarrow$ returns `JobRecommendations`.
6. **Finalization**: Orchestrator aggregates all results into `CareerStrategyReport` and returns it to the user.

## 5. Data Flow & Contracts
We use **Pydantic models** to ensure strict type safety between agents.

- `ResumeProfile` $ightarrow$ `SkillGapAnalyzer`
- `GapAnalysis` $ightarrow$ `RoadmapGenerator`
- `ResumeProfile` $ightarrow$ `JobMatcher`

## 6. Technology Decisions
- **Language**: Python 3.13+.
- **Data Validation**: Pydantic v2 for strict schema enforcement.
- **Testing**: pytest for unit and integration tests.
- **LLM Interface**: A wrapper class that can switch between OpenAI, Anthropic, or a Mock LLM for testing.

## 7. Testing Strategy
- **Unit Tests**: Each agent will be tested with fixed mock inputs to verify logic.
- **Integration Tests**: The orchestrator will be tested with a "Golden Path" resume and role to verify the sequence.
- **Contract Tests**: Verify that agent outputs match the Pydantic models defined in `contracts.py`.

## 8. Risk Assessment & Mitigation
| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| LLM Hallucinations | High | Use strict JSON schemas and "Rationale" fields to force reasoning. |
| Poor Parsing | Medium | Use robust PDF/Text extraction libraries with fallback to plain text. |
| Token Limits | Low | Send only necessary summaries to subsequent agents. |
| Orchestration Fail | Medium | Implement try-except blocks at each agent step with a "Partial Report" fallback. |
