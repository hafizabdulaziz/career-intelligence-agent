# Implementation Tasks: AI Multi-Agent Career Assistant

## Phase 1: Core Infrastructure & Contracts
*Goal: Establish the foundational types and base classes to ensure type safety across all agents.*

- [ ] **Task 1.1: Define Data Contracts**
  - Create `src/career_assistant/core/contracts.py`.
  - Implement Pydantic models for: `ResumeProfile`, `GapAnalysis`, `LearningRoadmap`, `JobRecommendations`, and `CareerStrategyReport`.
  - *Verification*: Run a script to instantiate and validate these models with sample data.

- [ ] **Task 1.2: Create Base Agent Abstract Class**
  - Create `src/career_assistant/core/base_agent.py`.
  - Define `BaseAgent` ABC with an abstract `run()` method.
  - *Verification*: Ensure no concrete agent can be instantiated without implementing `run()`.

- [ ] **Task 1.3: Implement LLM Wrapper**
  - Create `src/career_assistant/utils/llm_wrapper.py`.
  - Implement a class that handles prompts and returns structured JSON.
  - Include a `MockLLM` mode for testing without API costs.
  - *Verification*: Verify that `MockLLM` returns the expected structured data.

- [ ] **Task 1.4: Setup Configuration Management**
  - Create `src/career_assistant/config/settings.py`.
  - Handle environment variables for API keys and system prompts.

## Phase 2: Individual Agent Implementation (Surgical/TDD)
*Goal: Implement each worker agent in isolation, following a Red-Green-Refactor cycle.*

- [ ] **Task 2.1: Resume Analyzer Agent**
  - Implement `src/career_assistant/agents/resume_analyzer.py`.
  - Logic: Extract skills, strengths, and experience.
  - *Test*: `tests/unit/test_resume_analyzer.py`.

- [ ] **Task 2.2: Skill Gap Agent**
  - Implement `src/career_assistant/agents/skill_gap_agent.py`.
  - Logic: Delta analysis between `ResumeProfile` and `TargetRole`.
  - *Test*: `tests/unit/test_skill_gap.py`.

- [ ] **Task 2.3: Roadmap Generator Agent**
  - Implement `src/career_assistant/agents/roadmap_gen.py`.
  - Logic: Sequence gaps into a learning path.
  - *Test*: `tests/unit/test_roadmap_gen.py`.

- [ ] **Task 2.4: Job Match Agent**
  - Implement `src/career_assistant/agents/job_matcher.py`.
  - Logic: Suggest alternative roles based on `ResumeProfile`.
  - *Test*: `tests/unit/test_job_matcher.py`.

## Phase 3: Orchestration & Integration
*Goal: Connect the agents into a deterministic workflow.*

- [ ] **Task 3.1: Implement CareerOrchestrator**
  - Create `src/career_assistant/orchestrator.py`.
  - Implement the sequential workflow: Resume $ightarrow$ Gap $ightarrow$ Roadmap $ightarrow$ Match.
  - Implement error handling and partial report logic.
  - *Test*: `tests/integration/test_orchestrator.py`.

- [ ] **Task 3.2: Implement CLI Entry Point**
  - Create `src/career_assistant/main.py`.
  - Handle user input (resume file path and target role).
  - Format the final `CareerStrategyReport` as a readable summary.

## Phase 4: Validation & Polishing
*Goal: Ensure production-grade quality and full documentation.*

- [ ] **Task 4.1: End-to-End Integration Testing**
  - Create a set of "Golden Resumes" and "Target Roles" to verify overall system coherence.
  - *Verification*: Final report must be logically consistent.

- [ ] **Task 4.2: Final Documentation**
  - Generate `README.md` with architecture diagrams and usage guides.
  - Create `docs/AGENT_GUIDE.md` explaining the prompt engineering for each agent.

- [ ] **Task 4.3: GitHub Readiness Review**
  - Check folder structure, `.gitignore`, and `pyproject.toml`.
  - Ensure all tests pass.
