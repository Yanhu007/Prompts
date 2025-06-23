# Edge Agent Generator Framework Creation Process

This document outlines the step-by-step process for creating the prompt for Edge Agent Generator Framework that can automatically generate specialized AI agents for different codebases.

## Overview

The Edge Agent Generator Framework is designed to create intelligent agents that can understand and work with specific codebases by analyzing existing prompt structures and requirements.

## 📖 Key Definitions

**🤖 Agent**: A specialized AI assistant prompt designed to help with specific Edge/Chromium development tasks. The Agent is implemented as a structured prompt containing domain knowledge, capabilities, and behavioral instructions.

**🔧 edge_agent_generator framework**: An automated system/process that generates compliant Agent prompts by following strict validation procedures and mandatory capability requirements.

## Sequential Step-by-Step Process

⚠️ **MANDATORY SEQUENTIAL EXECUTION**: Each step must be fully completed and validated before proceeding to the next step. No parallel execution or step skipping is allowed.

### Step 1. **Extract and Analyze Existing Prompts**
   - Reference and extract all existing prompts from the `.github/Prompts` directory
   - Extract common structures and styles from these prompts to form a standard template for Edge codebase expert agents
   - Summarize the standard template as the Edge Agent Generator Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` with standard markdown format
   
   **✅ Completion Requirement**: File `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` must exist with initial template structure before proceeding to Step 2.

### Step 2. **Integrate Requirements (Phase 1)**
   - ⚠️ **PREREQUISITE**: Step 1 must be completed successfully
   - Reference and understand the requirements described in `.github/resources/Edge_Codebase_Agent_Gen_Requirements_1.md`
   - Update the Edge Agent Generator Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` with standard markdown format
   
   **✅ Completion Requirement**: All Phase 1 requirements must be fully integrated into the prompt file before proceeding to Step 3.

### Step 3. **Integrate Requirements (Phase 2)**
   - ⚠️ **PREREQUISITE**: Step 2 must be completed successfully
   - Reference and understand the requirements described in `.github/resources/Edge_Codebase_Agent_Gen_Requirements_2.md`
   - Update the Edge Agent Generator Framework prompt in `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` with standard markdown format
   
   **✅ Completion Requirement**: All Phase 2 requirements must be fully integrated into the prompt file before proceeding to Step 4.

### Step 4. **Validation Process**
   - ⚠️ **PREREQUISITE**: Step 3 must be completed successfully
   - Copy `.github/resources/Edge_Codebase_Agent_Gen_Checklist.md` as `.memory/Edge_Codebase_Agent_Gen_Checklist_${YYYYMMDD-HHMMSS}.md`
   - Validate the `.github/Prompts/Edge_Codebase_Agent_Generator.prompt.md` against the timestamped checklist
   - Update the checklist file in real-time using format `[✅]` or `[❌]` as the validation is executed
   
   **✅ Completion Requirement**: All checklist items must pass validation (`[✅]`) before proceeding to Step 5.

### Step 5. **Iterative Refinement**
   - ⚠️ **PREREQUISITE**: Step 4 must be completed successfully
   - If validation in Step 4 fails (`[❌]` items exist), revisit and repeat steps 2-4 until all validation passes
   - Ensure all requirements are properly integrated and the generator meets quality standards
   
   **✅ Final Completion Requirement**: Process is complete only when all checklist validations show `[✅]` and no `[❌]` items remain.

**📅 TIMESTAMP FORMAT SPECIFICATION**:
  - **Format**: `YYYYMMDD-HHMMSS` (compact format with date and time separated by hyphen)
  - **Example**: `20250622-143059` (June 22, 2025, 2:30:59 PM)
  - **Timezone**: Local system timezone, no timezone suffix included
  - **Precision**: Seconds level to ensure uniqueness

