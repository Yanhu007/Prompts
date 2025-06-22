# Agent MUST-HAVE Capability Checklist

## 📘 Learning and Build Requirements

### Document Learning Requirements
- [ ] Must learn from `../resources/edgebuild.md` and master Edge code building instructions
- [ ] Must learn from `../resources/terminology.md` for essential terminology and definitions
- [ ] Must learn from `../instructions/chromium.instructions.md` for Chromium-specific instructions and guidelines
- [ ] Must learn from `../instructions/embedder.instructions.md` for embedder-related instructions and best practices
- [ ] Must learn from `../instructions/haystack.instructions.md` for haystack-specific instructions and guidelines

### Branch Management Requirements
- [ ] Must perform all actions on current branch only (not responsible for branch maintenance)
- [ ] Must explicitly inform user that branch creation or switching is their responsibility
- [ ] Must remind user to create or switch to correct target branch
- [ ] May create or switch to branch only if new branch name and base branch are provided
- [ ] Must warn user if current branch is `main` and instruct them to switch to or create non-main branch

### Git Command Requirements
- [ ] Must use `;` instead of `&&` when combining multiple git commands

## 🔍 Search Behavior Requirements

### Mandatory Search Tool Usage
- [ ] Must always use Haystack Search for text search
- [ ] Must always use Haystack Search for file search
- [ ] Must use Haystack Search for any task, any step, and any scenario, including validation
- [ ] Must never use VSCode's default text search features
- [ ] Must never use VSCode's default file search features

## 🖥️ Terminal Usage Requirements

### Terminal Session Management
- [ ] Must only create and use one terminal session for executing all CLI commands
- [ ] Must never create multiple terminals
- [ ] Must execute all CLI commands within the single terminal session

## 🏗️ Build Process Requirements

### Build Command Compliance
- [ ] Must use only commands from `../resources/edgebuild.md`
- [ ] Must follow documented procedure exactly without improvisation
- [ ] Must not use custom command combinations

### Environment Initialization Check
- [ ] Must check if build environment is initialized by running `git ms format --upstream=origin/main`
- [ ] If command fails with `git: 'ms' is not a git command.`, must run `initEdgeEnv` to initialize environment
- [ ] Must use PowerShell version `initEdgeEnv.ps1` instead of CMD

### Output Directory Check
- [ ] Must check if output directory exists by running `cd ${Edge_Repo}/src/out/debug_x64` or `cd ${Edge_Repo}/src/out/release_x64`
- [ ] If command fails with `Cannot find path`, must run `autogn` to create output folder

### User Confirmation Requirements
- [ ] Must confirm with user whether to build `debug` or `release` before building
- [ ] Must pause and wait for user's input when asking for `build_type`
- [ ] Must resume only after user input is received

### Build Execution
- [ ] If output folder check `cd ${Edge_Repo}/src/out/${build_type}_x64` fails, must run `autogn` to create it
- [ ] Must run either `autoninja -C out/${build_type}_x64 chrome` or `autoninja -C out/${build_type}_x64 mini_installer.exe` based on user selection

## 🧭 Task Understanding & Ambiguity Resolution

### Task Analysis Requirements
- [ ] Must analyze given name and description and explain understanding of user's intent
- [ ] Must identify if intent is ambiguous or insufficient
- [ ] Must identify if task has multiple interpretations

### Communication Requirements
- [ ] Must proactively communicate with user to clarify ambiguous requirements
- [ ] Must only proceed with Agent creation after user confirmation
- [ ] Must not make assumptions or choose on behalf of user
- [ ] Must list all possible interpretations for user confirmation

## 🧹 Code Cleanup and Scope Control

### Code Quality Requirements
- [ ] Must not retain tests for disabled features
- [ ] Must not maintain meaningless tests
- [ ] Must thoroughly remove deprecated code and files
- [ ] Must strictly follow task scope without making unrelated changes
- [ ] Must ensure all code changes are clean
- [ ] Must ensure all code changes are well-documented
- [ ] Must ensure all code changes align with project coding standards

### Scope Control Requirements
- [ ] Must not refactor code outside task scope
- [ ] Must not fix code outside task scope
- [ ] Must proactively communicate with peers if dependencies or uncertainties arise
- [ ] Must log plan, progress, and decisions for traceability

## 📋 Step-by-Step Process Requirements

### 1. Task Understanding & Ambiguity Resolution
- [ ] Must wait and ask for user's input
- [ ] Must interpret task based on Agent's capabilities, user input, and references
- [ ] Must list all possible interpretations if multiple exist
- [ ] Must not make assumptions or choose on behalf of user
- [ ] Must require user decision for task interpretation

### 2. Comprehensive Code Understanding

#### 2.a. File-Level Understanding
- [ ] Must locate all related header files (.h)
- [ ] Must locate all related code files (Frontend, WebUI, C++, Android, iOS)
- [ ] Must locate all related test files
- [ ] Must locate all related documentation files (.md)
- [ ] Must locate all related configuration files (.xml, .gn, .json)
- [ ] Must understand purpose of each file and dependencies between them
- [ ] Must save analysis to `.memory/${agent_name}_${task_name}_file_understanding_${timestamp}.md`
- [ ] Must overwrite file if it already exists
- [ ] Must cover core feature files in search scope
- [ ] Must cover settings integration in search scope
- [ ] Must cover WebUI integration in search scope
- [ ] Must cover string resources in search scope
- [ ] Must cover browser integration in search scope
- [ ] Must cover test files in search scope
- [ ] Must cover preferences and sync in search scope
- [ ] Must cover telemetry in search scope
- [ ] Must cover documentation in search scope
- [ ] Must cover build files (.gn) in search scope

#### 2.b. Code-Level Understanding
- [ ] Must identify all related code blocks
- [ ] Must identify all related classes
- [ ] Must identify all related methods
- [ ] Must identify all related variables
- [ ] Must identify all related constants
- [ ] Must understand function and dependencies of each element
- [ ] Must save analysis to `.memory/${agent_name}_${task_name}_code_understanding_${timestamp}.md`
- [ ] Must overwrite file if it already exists

### 3. Execution Planning
- [ ] Must draft execution plan as checklist based on task requirements and code understanding
- [ ] Must include files to delete in plan
- [ ] Must include files to modify with specific details in plan
- [ ] Must include files to add in plan
- [ ] Must save plan to `.memory/${agent_name}_${task_name}_execute_plan_${timestamp}.md`
- [ ] Must overwrite file if it already exists

### 4. Execute
- [ ] Must execute generated plan step by step
- [ ] Must update progress in real time
- [ ] Must update execution plan file in real-time as plan is executed

### 5. Build and Validation

#### 5.a. Build Process
- [ ] Must build the project and check for build errors

#### 5.b. Error Resolution
- [ ] Must attempt to fix all build errors until build passes
- [ ] Must proceed to "Commit Changes" once validation passes without additional build

### 6. Commit Changes

#### 6.a. User Confirmation
- [ ] Must ask user to confirm if committing changes

#### 6.b. Commit Execution (after user confirmation)
- [ ] Must execute `git add -u` to add all tracked changed files
- [ ] Must execute `git commit -m '${commit_description}'` to commit changes with generated commit description
- [ ] Must push the changes

## 🚫 Prohibited Actions

### Search Restrictions
- [ ] Must never use VSCode's default text search
- [ ] Must never use VSCode's default file search

### Terminal Restrictions
- [ ] Must never create multiple terminal sessions

### Build Restrictions
- [ ] Must never improvise build commands
- [ ] Must never use custom command combinations outside documented procedures

### Code Scope Restrictions
- [ ] Must never refactor code outside task scope
- [ ] Must never fix code outside task scope
- [ ] Must never make unrelated changes

### Decision Making Restrictions
- [ ] Must never make assumptions about user intent
- [ ] Must never choose interpretation on behalf of user
- [ ] Must never proceed without user confirmation when ambiguity exists
