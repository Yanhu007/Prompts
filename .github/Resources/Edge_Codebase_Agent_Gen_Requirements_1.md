# Requirements Document: Edge Agent Generation Framework

## Background

We need to build a framework for automatically generating prompts for **Edge Codebase Expert Agents**. These prompts are designed to guide agents in assisting users with Edge code modifications, with a focus on correctness, security, and adherence to common development standards.

## Scope

This framework should generate a new prompt file based on user input and save it to the `.github/prompts` directory. The generated prompt should be customized according to the information provided by the user while following best practices for Edge code modification.

## Requirements

### 1. Agent Professional Capabilities

- The generated prompt should represent an **Edge codebase expert**.
- The agent should:
  - Be familiar with common **modification workflows** for the Edge codebase;
  - Follow and advocate for **safe and accurate** code modification practices;
  - Consider common **considerations and best practices** when modifying Edge code.

### 2. User Input

The prompt generation framework should accept the following user inputs:

- `Agent Name` — Used as the filename for the generated `.md` file;
- `Agent Description` — A brief description of the agent's purpose;
- `Reference Information` — Additional context or target information that the agent should consider during generation.

### 3. Output Requirements

- The framework should generate a markdown file containing the agent's prompt;
- The generated file must meet the following requirements:
  - Save path: `.github/prompts` directory;
  - Filename must exactly match the user-provided `Agent Name` (e.g., `${Agent Name}_agent.md`);
  - Content format should be unified and standardized, conforming to the style and structure used for GPT agent initialization.

### 4. Prompt Content Guidelines

The generated prompt should include the following content:

- Clearly describe the agent's role: Edge codebase expert;
- Explain that its responsibility is to guide users in making **safe and accurate** code modifications;
- Clearly specify the development standards the agent follows and the Edge project's code modification processes;
- Customize prompt content by incorporating additional reference information provided by the user.