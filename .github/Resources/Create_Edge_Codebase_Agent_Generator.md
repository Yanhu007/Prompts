# Edge Codebase Agent Generator Creation Process

This document outlines the step-by-step process for creating an Edge Codebase Agent Generator that can automatically generate specialized AI agents for different codebases.

## Overview

The Edge Codebase Agent Generator is designed to create intelligent agents that can understand and work with specific codebases by analyzing existing prompt structures and requirements.

## Step-by-Step Process

1. **Extract and Analyze Existing Prompts**
   - Reference and extract all existing prompts from the `.github/prompts` directory
   - Extract common structures and styles from these prompts to form a standard template for Edge codebase expert agents
   - Summarize the standard template as the Edge Codebase Agent Generation Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.md` with standard markdown format

2. **Integrate Requirements (Phase 1)**
   - Reference and understand the requirements described in `.github/Resources/Edge_Codebase_Agent_Gen_Requirements_1.md`
   - Update the Edge Codebase Agent Generation Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.md` with standard markdown format

3. **Integrate Requirements (Phase 2)**
   - Reference and understand the requirements described in `.github/Resources/Edge_Codebase_Agent_Gen_Requirements_2.md`
   - Update the Edge Codebase Agent Generation Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.md` with standard markdown format

4. **Validation Process**
   - Copy `.github/Resources/Edge_Codebase_Agent_Gen_Checklist.md` as `.github/Resources/Edge_Codebase_Agent_Gen_Checklist_${YYYYMMDD-HHMMSS}.md`
   - Validate the `.github/Prompts/Edge_Codebase_Agent_Generator.md` against the timestamped checklist
   - Update the checklist file in real-time as the validation is executed

5. **Iterative Refinement**
   - Revisit and repeat steps 2-3 until the validation passes
   - Ensure all requirements are properly integrated and the generator meets quality standards

## Expected Outcome

Upon completion, the Edge Codebase Agent Generator will be able to create specialized AI agents tailored to specific codebases, following standardized templates and meeting all defined requirements. 
