# Agent Design & Prompt Engineering Guide

This document explains the design principles and prompt strategy for the specialized agents in the AI Multi-Agent Career Assistant.

## Design Principle
Every agent follows the **Single Responsibility Principle**. It is designed as a stateless service that receives a Pydantic model as input, performs a single cognitive task, and returns a Pydantic model as output.

## Prompt Strategy

### 1. Resume Analyzer
- **Focus**: Extraction and Normalization.
- **Prompt Strategy**: "Extract core skills, experience level, and professional strengths. Output MUST strictly adhere to the `ResumeProfile` JSON schema. Do not hallucinate skills not explicitly stated."

### 2. Skill Gap Agent
- **Focus**: Delta Analysis.
- **Prompt Strategy**: "Compare `ResumeProfile` with `TargetRole` requirements. Identify missing skills. Categorize severity as 'Critical', 'Important', or 'Optional'. Include a clear rationale for each missing skill."

### 3. Roadmap Generator
- **Focus**: Sequencing and Prioritization.
- **Prompt Strategy**: "Convert identified skill gaps into a step-by-step learning path. Prioritize gaps based on impact. Provide clear milestones, descriptions, and estimated effort."

### 4. Job Match Agent
- **Focus**: Similarity Analysis.
- **Prompt Strategy**: "Analyze the user's `ResumeProfile`. Recommend 2-3 alternative job roles that align with their strengths, even if different from the target role. Provide match scores and rationales."

## LLM Interaction
Agents interact with the LLM through a unified `LLMWrapper` (currently a `MockLLM` for development). The wrapper enforces JSON output via strict schema passing to the LLM API, ensuring the orchestrator always receives predictable data structures.
