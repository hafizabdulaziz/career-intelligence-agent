<!--
Sync Impact Report:
- Version change: 1.1.0 -> 1.1.1
- List of modified principles:
    - Principle V: Software Craftsmanship (Replaced "OOP" with "Object Oriented Programming" for clarity)
- Added sections: None
- Templates requiring updates:
    - templates/plan-template.md (✅ checked)
    - templates/spec-template.md (✅ checked)
    - templates/tasks-template.md (✅ checked)
- Follow-up TODOs: None
-->

# Calculator Project Constitution

## Core Principles

### I. TDD First (NON-NEGOTIABLE)
TDD mandatory: Tests MUST be written and fail before any implementation begins. The Red-Green-Refactor cycle must be strictly followed for all new features and bug fixes. This ensures that every line of code is driven by a requirement and is fully testable.

### II. Strict Type Safety
All code MUST use Python 3.12+ (specifically targeting 3.13.14+) with comprehensive type hints. 
- **Type Hints**: All functions MUST include type hints on parameters and return types.
  - *Example*: `def add(a: float, b: float) -> float:`
- Type checking is a first-class citizen in our development workflow. Avoid `Any` and prefer explicit protocols or generics where appropriate.

### III. Clean Code & Readability
Code is read more often than it is written. We prioritize readability and maintainability over cleverness.
- **Docstrings**: All functions MUST include docstrings explaining what they do.
  - *Example*: `"""Add two numbers and return the sum."""`
- **Naming Conventions**: Follow PEP 8 naming conventions strictly (e.g., `lowercase_with_underscores` for functions and variables).
- **Line Length**: Lines MUST be under 100 characters.
- **No Magic Numbers**: Use named constants instead of literal values in logic.
  - *Bad*: `if x > 10:`
  - *Good*: `if x > MAX_POWER_EXPONENT:`
- Ensure that the code's intent is obvious. If a complex algorithm is necessary, document the *why* and the *how* clearly.

### IV. Architectural Decision Records (ADR)
All architecturally significant decisions MUST be documented via ADRs in `history/adr/`. We don't just record the decision, but also the context, alternatives considered, and the trade-offs made. This preserves the "why" for future developers.

### V. Software Craftsmanship (Object Oriented Programming Excellence)
Adhere to fundamental software design principles: SOLID, DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid). Prefer explicit composition and delegation over complex inheritance. We build modular, decoupled systems that are easy to extend and test.

## Technical Stack

### Core Technologies
- **Language**: Python 3.13.14+
- **Package Manager**: UV (for fast, reliable dependency management)
- **Testing**: pytest (our primary testing framework)
- **Version Control**: Git (all project files must be tracked)

## Quality Requirements

### Testing & Coverage
- **Pass Rate**: All tests MUST pass before any code is merged or deployed.
- **Coverage**: Maintain a minimum of 80% code coverage across the entire project. Coverage reports must be generated and reviewed regularly.
- **Data Structures**: Use Python `dataclasses` for data-heavy structures to ensure clean, idiomatic, and often immutable data handling.

## Governance

### Amendment Process
This constitution is a living document. Amendments require a version bump following semantic versioning rules (MAJOR.MINOR.PATCH) and must be documented in the Sync Impact Report.

### Compliance
Every Pull Request and code review must verify compliance with these principles. Non-compliant code will not be accepted into the main branch.

**Version**: 1.1.1 | **Ratified**: 2026-06-14 | **Last Amended**: 2026-06-14
