# Specification: AI Multi-Agent Career Assistant

## 1. Project Vision
The AI Multi-Agent Career Assistant is a production-grade system designed to automate the career growth cycle. By utilizing a multi-agent orchestration pattern, the system transforms a static resume into a dynamic, personalized career strategy, providing users with a clear path from their current skill set to their target professional role.

## 2. Problem Statement
Job seekers and professionals often struggle with:
- **Resume Blindness**: Not knowing how their skills are perceived by automated systems or recruiters.
- **The "Gap" Paradox**: Knowing they aren't qualified for a role but not knowing *exactly* which skills are missing.
- **Information Overload**: Finding too many learning resources without a prioritized, personalized roadmap.
- **Role Misalignment**: Applying for roles that don't align with their actual strengths.

## 3. Target Users
- **Fresh Graduates**: Looking to enter the industry and identify entry-level gaps.
- **Career Switchers**: Moving from one domain to another (e.g., QA to DevOps).
- **Mid-Level Professionals**: Seeking promotion or specialization.

## 4. User Stories
- **As a user**, I want to upload my resume so that the system can understand my professional background.
- **As a user**, I want to specify a target job role so that the system can compare my current state to the target state.
- **As a user**, I want to see a list of missing skills so that I know exactly what to learn.
- **As a user**, I want a step-by-step learning roadmap so that I can efficiently close my skill gaps.
- **As a user**, I want suggestions for alternative roles that match my current skills better than my target role.

## 5. Functional Requirements

### 5.1 Resume Analysis
- **FR1**: The system shall extract text from resume files (PDF/Docx/Text).
- **FR2**: The system shall identify core competencies, technical skills, and soft skills.
- **FR3**: The system shall summarize the professional strengths of the candidate.

### 5.2 Skill Gap Analysis
- **FR4**: The system shall fetch or define the required skill set for a given target role.
- **FR5**: The system shall perform a delta analysis between the extracted resume skills and the target role requirements.
- **FR6**: The system shall categorize gaps into "Critical," "Important," and "Optional."

### 5.3 Roadmap Generation
- **FR7**: The system shall generate a sequenced learning path to address identified gaps.
- **FR8**: The system shall provide specific topics to study for each gap.
- **FR9**: The system shall estimate the time/effort required for each learning milestone.

### 5.4 Job Matching
- **FR10**: The system shall suggest 2-3 alternative job roles that align closely with the user's current extracted skills.
- **FR11**: The system shall provide a "match percentage" and rationale for each suggestion.

### 5.5 Orchestration
- **FR12**: The Orchestrator shall manage the sequential execution of agents: Resume $ightarrow$ Gap $ightarrow$ Roadmap $ightarrow$ Job Match.
- **FR13**: The Orchestrator shall aggregate all agent outputs into a single, comprehensive Career Strategy Report.

## 6. Non-Functional Requirements

### 6.1 Reliability
- **NFR1**: The system shall handle malformed resumes gracefully without crashing.
- **NFR2**: The system shall provide fallback mechanisms if an agent fails to produce a structured output.

### 6.2 Maintainability
- **NFR3**: All agent logic shall be encapsulated in separate modules.
- **NFR4**: The system shall use Pydantic models for all inter-agent data exchange.

### 6.3 Transparency
- **NFR5**: Every output from a specialized agent must include a "Rationale" field explaining the logic.

## 7. Acceptance Criteria
- [ ] **Successful End-to-End Flow**: A user provides a resume and target role, and receives a complete Career Strategy Report.
- [ ] **Data Integrity**: Extracted skills from the resume are accurately reflected in the Gap Analysis.
- [ ] **Logical Consistency**: The Roadmap directly addresses the gaps identified in the Gap Analysis.
- [ ] **Structured Output**: All agents return JSON-compatible structured data.

## 8. Edge Cases
- **Empty Resume**: The system should notify the user that no professional data was found.
- **Irrelevant Target Role**: If the target role is completely unrelated to the user's background (e.g., Chef $ightarrow$ Quantum Physicist), the system should flag a "High Pivot" warning.
- **Over-qualified Candidate**: If the user already possesses all required skills, the system should suggest "Advanced Specializations" instead of a basic roadmap.

## 9. Constraints
- **Language**: Python 3.13+.
- **Agent Logic**: For the prototype, LLM calls will be simulated or handled via a unified API wrapper.

## 10. Future Expansion Strategy
- **Real-time Job API**: Integration with LinkedIn/Indeed APIs for live job matching.
- **Course Integration**: Linking roadmap items to actual Coursera/Udemy courses.
- **Interview Simulation**: Adding an "Interview Prep Agent" that generates questions based on the identified gaps.
