# Requirements Document: Edge Agent Generator Framework

## Background

We need to build an `edge_agent_generator` framework for automatically generating prompts for **Edge Codebase Expert Agents**. These prompts are designed to guide agents in assisting users with Edge code modifications, with a focus on correctness, security, and adherence to common development standards.

## Scope

This `edge_agent_generator` framework should generate a new prompt file based on user input and save it to the `.github/prompts` directory. The generated prompt should be customized according to the information provided by the user while following best practices for Edge code modification and maintaining full compliance with mandatory capability requirements.

## Requirements

### 1. Agent Professional Capabilities

- The generated prompt should represent an **Edge codebase expert**.
- The agent should:
  - Be familiar with common **modification workflows** for the Edge codebase;
  - Follow and advocate for **safe and accurate** code modification practices;
  - Consider **best practices and common considerations** when modifying Edge code.

### 2. User Input

The `edge_agent_generator` framework should accept the following user inputs with **mandatory validation**:

- `Agent Name` — Used as the filename for the generated `.prompt.md` file;
- `Agent Description` — A brief description of the agent's purpose;
- `Reference Information` — Additional context or reference information that the agent should consider during prompt generation (if available).

**⚠️ Input Validation Requirements**:
- The framework **must wait for and request** all necessary information from the user
- If the user provides insufficient information, the framework must notify the user of missing details and stop the process
- The framework must not proceed until all required information is provided

### 3. Output Requirements

- The `edge_agent_generator` framework should generate a markdown file containing the agent's prompt;
- The generated file must meet the following requirements:
  - Save path: `.github/prompts` directory;
  - Filename format: `${Agent Name}_agent.prompt.md`;
  - Content format should be unified and standardized, conforming to the style and structure used for GPT agent initialization.

**⚠️ Compliance Requirements**:
- All generated agents must implement **ALL capabilities** defined in `Agent_MUST_HAVE_Capability.md` without exception
- The framework must perform **100% capability validation** before completion
- Validation tracking files will be stored in `./memory/` directory with timestamps

### 4. Prompt Content Guidelines

The generated prompt should include the following content with **mandatory compliance**:

- Clearly describe the agent's role as an Edge codebase expert;
- Explain that its responsibility is to guide users in making **safe and accurate** code modifications;
- Clearly specify the development standards the agent follows and the Edge project's code modification processes;
- Incorporate additional reference information provided by the user to customize the prompt content;
- **⚠️ CRITICAL**: Include **ALL capabilities** from `Agent_MUST_HAVE_Capability.md` exactly as specified without modifications, omissions, or simplifications.

### 5. Process Requirements

The `edge_agent_generator` framework must follow **three strict steps**:

1. **Prompt for Required Input**: Collect and validate all necessary user inputs
2. **Understand and Confirm User Intent**: Perform deep intent analysis, detect ambiguities, and obtain explicit user confirmation
3. **Agent Generation Workflow**: Generate agent with mandatory capability validation and compliance verification

**⚠️ Enforcement**: Any deviation from capability specifications will result in immediate generation failure and graceful framework termination.