# AI Multi-Agent Career Assistant Constitution

## Core Principles

### I. Single Responsibility Agents
Each agent MUST have a single, well-defined purpose. An agent should do one thing and do it excellently. If an agent's scope begins to creep, it MUST be split into smaller, specialized agents.
- **Resume Analyzer**: Only extracts and analyzes resume data.
- **Skill Gap Agent**: Only compares current skills against target roles.
- **Roadmap Generator**: Only creates learning paths.
- **Job Match Agent**: Only recommends roles.
- **Orchestrator**: Only coordinates the flow and aggregates results.

### II. Explainable Outputs
Agents MUST NOT provide "black box" answers. Every recommendation, gap analysis, or roadmap item MUST be accompanied by a clear rationale. The user should understand *why* a certain conclusion was reached.

### III. Modular Architecture
The system MUST be decoupled. Agents should communicate via standardized data contracts (schemas). This ensures that any single agent can be replaced or upgraded without impacting the rest of the system.

### IV. Testability (TDD Approach)
All agent logic MUST be testable in isolation. We follow a Red-Green-Refactor cycle.
- Unit tests for individual agent logic.
- Integration tests for the Orchestrator's workflow.
- Validation tests for the quality of LLM-generated outputs.

### V. Scalability & Maintainability
The architecture MUST support the addition of new agents (e.g., an "Interview Coach Agent") without requiring a rewrite of the Orchestrator. Code MUST adhere to SOLID principles and use clear type hints for maintainability.

### VI. Deterministic Workflows
While LLM outputs are probabilistic, the *workflow* (the sequence of agent calls) MUST be deterministic. The Orchestrator must follow a strict, predictable state machine to ensure consistency in the user experience.

### VII. Clean Documentation
Every agent, interface, and workflow must be documented. Documentation is not an afterthought; it is a deliverable. The README and architecture docs must be kept in sync with the implementation.

## Technical Stack

### Core Technologies
- **Language**: Python 3.13+
- **Type System**: Strict Type Hints & Pydantic/Dataclasses for contracts.
- **Orchestration**: Custom Orchestrator Pattern.
- **Testing**: pytest.
- **Environment**: UV for dependency management.

## Quality Requirements

### Acceptance Criteria
- **Accuracy**: Agent extractions must match source data.
- **Coherence**: The final aggregated report must be logically consistent.
- **Performance**: End-to-end career analysis should complete within acceptable latency limits.

**Version**: 1.0.0 | **Ratified**: 2026-06-25 | **Status**: Active
