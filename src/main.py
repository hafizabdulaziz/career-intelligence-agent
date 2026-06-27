from __future__ import annotations

import asyncio
import sys
import os
from typing import List

from src.career_assistant.orchestrator import CareerOrchestrator
from src.career_assistant.core.contracts import CareerStrategyReport
from src.career_assistant.utils.file_handler import FileParser

def print_banner():
    print("=" * 70)
    print("               AI MULTI-AGENT CAREER ASSISTANT")
    print("=" * 70)
    print(" Transform your resume into a personalized, strategic career plan.")
    print("=" * 70)
    print()

async def main_async():
    import argparse
    parser = argparse.ArgumentParser(description="AI Multi-Agent Career Assistant CLI")
    parser.add_argument("--mock", action="store_true", help="Run in mock mode using simulated LLM responses.")
    args, _ = parser.parse_known_args()

    print_banner()

    # Determine LLM mode based on CLI arguments and API key structure
    llm_mode = "live"
    if args.mock:
        llm_mode = "mock"
        print("[*] Running in explicit MOCK mode.")
    else:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key:
            print("[!] No Gemini API Key detected in environment.")
            print("[*] Automatically falling back to MOCK mode for local demonstration.")
            llm_mode = "mock"
        else:
            print("[✓] Gemini API Key detected. Running in LIVE mode.")

    # Simple interactive CLI
    print("[*] Please enter your target professional role:")
    target_role = input("Target Role: ").strip()
    while not target_role:
        print("[!] Target role cannot be empty. Please enter a valid role.")
        target_role = input("Target Role: ").strip()

    print("\n[*] Would you like to:")
    print("  1. Provide a path to a resume text file")
    print("  2. Paste your resume text directly")
    choice = input("Choice (1 or 2): ").strip()

    resume_text = ""
    if choice == "1":
        path = input("Enter the file path of your resume: ").strip()
        try:
            resume_text = FileParser.parse_file(path)
            print(f"[✓] Successfully parsed resume from {path}.")
        except Exception as e:
            print(f"[!] Error parsing file: {e}")
            sys.exit(1)
    else:
        print("\n[*] Please paste your resume text below (press Ctrl+D on Unix or Ctrl+Z on Windows + Enter when finished):")
        try:
            resume_text = sys.stdin.read()
        except Exception as e:
            print(f"[!] Error reading input: {e}")
            sys.exit(1)

    if not resume_text.strip():
        print("[!] Resume text cannot be empty. Exiting.")
        sys.exit(1)

    print(f"\n[*] Initializing specialized agents in {llm_mode.upper()} mode and starting analysis...")
    
    # Run orchestrator
    orchestrator = CareerOrchestrator(config={"llm_mode": llm_mode})
    try:
        report: CareerStrategyReport = await orchestrator.run_career_strategy_flow(
            resume_text=resume_text,
            target_role=target_role
        )
        
        # Display the aggregated report beautifully
        print("\n" + "="*70)
        print("                   CAREER STRATEGY REPORT")
        print("="*70)
        print(f"Candidate Name : {report.user_name}")
        print(f"Target Role    : {target_role}")
        print(f"Summary        : {report.summary}")
        print("-" * 70)
        
        print("\n[ Extracted Resume Profile ]")
        print(f"Experience Level: {report.resume_profile.experience_level}")
        print(f"Experience Summary: {report.resume_profile.experience_summary}")
        print("Core Skills Identified:")
        for s in report.resume_profile.skills:
            print(f"  - {s.name} ({s.level})")
        print("Key Strengths:")
        for strg in report.resume_profile.strengths:
            print(f"  - {strg}")
            
        if report.gap_analysis:
            print("\n" + "-" * 70)
            print("[ Skill Gap Analysis ]")
            print(f"Rationale: {report.gap_analysis.rationale}")
            print("Missing Skills:")
            for s in report.gap_analysis.missing_skills:
                severity = report.gap_analysis.gap_severity.get(s.name, "unknown")
                print(f"  - {s.name} ({s.level}) [Severity: {severity}]")
            print("Matched Skills:")
            for s in report.gap_analysis.matched_skills:
                print(f"  - {s.name} ({s.level})")
                
        if report.learning_roadmap:
            print("\n" + "-" * 70)
            print("[ Personalized Learning Roadmap ]")
            print(f"Overall Estimated Timeline: {report.learning_roadmap.overall_estimated_timeline}")
            print("Actionable Milestones:")
            for m in sorted(report.learning_roadmap.milestones, key=lambda x: x.priority):
                print(f"  Milestone {m.priority}: {m.topic} ({m.estimated_effort})")
                print(f"    Description: {m.description}")
            print("Suggested Resources:")
            for r in report.learning_roadmap.resources_suggestions:
                print(f"  - {r}")
                
        if report.job_recommendations:
            print("\n" + "-" * 70)
            print("[ Alternative Job Roles Suggestions ]")
            for r in report.job_recommendations.recommendations:
                print(f"  - Role: {r.role_title} (Match Score: {int(r.match_score * 100)}%)")
                print(f"    Why? {r.rationale}")
                
        print("="*70)
        print("                  END OF REPORT")
        print("="*70)

    except Exception as e:
        print(f"[!] An error occurred during orchestration: {e}")
        sys.exit(1)

def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\n[!] Execution interrupted by user. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
