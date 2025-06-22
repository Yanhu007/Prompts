# Edge Agent Generator Framework Creation Process

This document outlines the step-by-step process for creating the prompt for Edge Agent Generator Framework that can automatically generate specialized AI agents for different codebases.

## Overview

The Edge Agent Generator Framework is designed to create intelligent agents that can understand and work with specific codebases by analyzing existing prompt structures and requirements.

## Step-by-Step Process

1. **Extract and Analyze Existing Prompts**
   - Reference and extract all existing prompts from the `.github/Prompts` directory
   - Extract common structures and styles from these prompts to form a standard template for Edge codebase expert agents
   - Summarize the standard template as the Edge Agent Generator Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` with standard markdown format

2. **Integrate Requirements (Phase 1)**
   - Reference and understand the requirements described in `.github/Resources/Edge_Codebase_Agent_Gen_Requirements_1.md`
   - Update the Edge Agent Generator Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` with standard markdown format

3. **Integrate Requirements (Phase 2)**
   - Reference and understand the requirements described in `.github/Resources/Edge_Codebase_Agent_Gen_Requirements_2.md`
   - Update the Edge Agent Generator Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` with standard markdown format

4. **Validation Process**
   - Copy `.github/Resources/Edge_Codebase_Agent_Gen_Checklist.md` as `.github/Resources/Edge_Codebase_Agent_Gen_Checklist_${YYYYMMDD-HHMMSS}.md`
   - Validate the `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` against the timestamped checklist
   - Update the checklist file in real-time using format `[✅]` or `[❌]` as the validation is executed

5. **Iterative Refinement**
   - Revisit and repeat steps 2-4 until the validation passes
   - Ensure all requirements are properly integrated and the generator meets quality standards

**📅 TIMESTAMP FORMAT SPECIFICATION**:
  - **Format**: `YYYYMMDD-HHMMSS` (compact format with date and time separated by hyphen)
  - **Example**: `20250622-143059` (June 22, 2025, 2:30:59 PM)
  - **Timezone**: Local system timezone, no timezone suffix included
  - **Precision**: Seconds level to ensure uniqueness

