# AI Multi-Agent Career Assistant

Transform your resume into a personalized, strategic career plan using autonomous AI agents.

## Project Overview

The AI Multi-Agent Career Assistant is a modular, production-grade application that leverages multi-agent orchestration to analyze professional resumes and generate actionable career strategies. Built using Spec-Driven Development (SDD) and Spec Kit Plus methodologies, the project demonstrates scalable software architecture, structured AI engineering, and robust software design principles.

## Features

- **Multi-Agent Orchestration:** Coordinated workflow between specialized agents for Resume Analysis, Skill Gap Analysis, Learning Roadmap Generation, and Job Recommendation.
- **Spec-Driven Development (SDD):** Complete engineering lifecycle, including Constitution, Specifications, Planning, ADRs, Task Management, and Documentation.
- **Dual Mode Operation:**
    - **LIVE Mode:** Uses Google Gemini API for real-time, intelligent analysis.
    - **MOCK Mode:** Simulates responses for local demonstration and testing without API consumption.
- **Production-Ready Architecture:** Type-safe Python, modular design, structured configuration management, and robust retry logic.

## Technology Stack

- **Language:** Python 3.13+
- **AI/LLM:** Google Gemini API (`gemini-2.0-flash`)
- **Orchestration:** Custom Multi-Agent Orchestrator
- **Data Modeling:** Pydantic (for structured output enforcement)
- **Workflow Methodology:** SDD, Spec Kit Plus
- **Tooling:** `uv` (package management/runner)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd calculator-project
   ```

2. **Install Dependencies:**
   ```bash
   uv sync
   ```

## Configuration

To run the application in LIVE mode, you must set your Gemini API key.

1. Create a `.env` file in the project root:
   ```text
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

## Usage

### Run in LIVE Mode (Requires API Key)
```bash
uv run python -m src.career_assistant.main
```

### Run in MOCK Mode (Demo)
```bash
uv run python -m src.career_assistant.main --mock
```

## Engineering Philosophy

This repository strictly adheres to **Spec-Driven Development (SDD)**. Every feature and architectural change is documented through specifications, planning, and Architecture Decision Records (ADRs). This ensures maintainability, traceability, and high code quality.

## Project Structure

- `.specify/`: Spec Kit Plus methodology artifacts.
- `specs/`: Feature requirements, plans, and documentation.
- `history/`: Prompt History Records (PHRs) and ADRs.
- `src/`: Core source code.
- `tests/`: Unit and integration tests.

## Contributing

Contributions are welcome. Please ensure that all contributions follow the established SDD methodology, maintain type safety, and include relevant tests.

## Author

**Abdul Aziz**
- [GitHub](https://github.com/hafizabdulaziz)
- [LinkedIn](https://linkedin.com/in/hafizabdulaziz33)
