# Agent MUST-HAVE Capability Checklist

## 🚫 Mandatory Compliance Requirements

### 📘 Learning and Build

1. The generated Agent **must learn from `../Resources/edgebuild.md`** and master how to build Edge code according to its documented instructions.

2. The generated Agent **must learn from the following mandatory documents**:
   * `../Resources/terminology.md` - Essential terminology and definitions
   * `../instructions/chromium.instructions.md` - Chromium-specific instructions and guidelines
   * `../instructions/embedder.instructions.md` - Embedder-related instructions and best practices
   * `../instructions/haystack.instructions.md` - haystack-specific instructions and guidelines

3. The Agent **is not responsible for branch maintenance**. All actions should be performed on the **current branch only**. The Agent must:

   * Explicitly inform the user that **branch creation or switching is their responsibility**.
   * Remind the user to **create or switch to the correct target branch**.
   * If a new branch name and base branch are provided, the Agent may create or switch to that branch.
   * If the current branch is `main`, the Agent must **warn the user** and instruct them to switch to or create a non-main branch.

4. When combining multiple `git` commands, the Agent **must use `;` instead of `&&`**.

### 🔍 Search Behavior

1. The Agent **must always use Haystack Search** for both **text search** and **file search** for **any task**, **any step**, and **any scenario**, including validation.

2. **It is strictly forbidden** to use **VSCode's default text search or file search features** in any context.

### 🖥️ Terminal Usage

1. The Agent **must only create and use one terminal session** for executing all CLI commands.

2. **Creating multiple terminals is strictly prohibited**, and violations will be penalized.

### 🏗️ Build Process Guidelines

1. After completing code modifications, the Agent must enter the build phase, following these rules:

   #### Allowed Commands and Flow

   * Use only the commands from `../Resources/edgebuild.md`.
   * Follow the documented procedure **exactly**. No improvisation or custom command combinations are allowed.

   #### Environment Checks Before Build

   * **Check if the build environment is initialized:**
     * Run `git ms format --upstream=origin/main`.
     * If it fails with the message `git: 'ms' is not a git command.`, then the build environment is not initialized.
     * In that case, run `initEdgeEnv` to initialize the environment.

   * **Check if output directory needs to be created:**
     * Run `cd ${Edge_Repo}/src/out/debug_x64` or `cd ${Edge_Repo}/src/out/release_x64`.
     * If it fails with `Cannot find path`, then run `autogn` to create the output folder.

2. Before building, confirm with the user whether to build `debug` or `release`.

3. Based on the user-selected `build_type`:

   * If the output folder check `cd ${Edge_Repo}/src/out/${build_type}_x64` fails:
     * Run `autogn` to create it.
   * Then run one of the following:
     * `autoninja -C out/${build_type}_x64 chrome` or
     * `autoninja -C out/${build_type}_x64 mini_installer.exe`

4. The `initEdgeEnv` script should be changed to **PowerShell** (`initEdgeEnv.ps1`), not CMD.

5. The Agent must **pause and wait** for the user's input when asking for `build_type`. Resume only after the input is received.

### 🧭 Task Understanding & Ambiguity Resolution

1. The Agent must analyze the **given name and description** and explain its understanding of the user's intent.
2. If the intent is ambiguous or insufficient, or has multiple interpretations:

   * The Agent must **proactively communicate** with the user to clarify.
   * **Only proceed with Agent creation after user confirmation.**

### 🧹 Code Cleanup and Scope Control

The Agent must:

* Avoid confusion:

  * Do **not retain tests for disabled features**.
* Reduce maintenance burden:

  * **Do not maintain meaningless tests**.
* Ensure code cleanliness:

  * **Thoroughly remove deprecated code and files**.
* **Strictly follow the task scope**—do not make unrelated changes.
* Ensure all code changes are:

  * Clean
  * Well-documented
  * Aligned with project coding standards
* Do **not refactor or fix code outside the task scope**.
* **Proactively communicate with peers** if dependencies or uncertainties arise.
* Log the plan, progress, and decisions for traceability.

---

## 📋 Step-by-Step Process

### Agent Must Follow the Step-by-Step Process

#### 1. Task Understanding & Ambiguity Resolution

Wait and ask for the user's input, then based on the Agent's own capabilities, the user input, and any references provided in the "Before you start" section, attempt to interpret the task.

* If multiple possible interpretations of the task exist, list them all for user confirmation.
* Do not make assumptions or choose on behalf of the user—the user must decide.

#### 2. Comprehensive Code Understanding

The Agent must demonstrate comprehensive understanding of the codebase, including:

##### 2.a. File-Level Understanding

* Locate all related files, including:
  * Header files (.h)
  * Code files (Frontend, WebUI, C++, Android, iOS)
  * Test files
  * Documentation files (.md)
  * Configuration files (.xml, .gn, .json)
* Understand the purpose of each file and the dependencies between them.
* Save the analysis to:
  `.memory/${agent_name}_${task_name}_file_understanding_${timestamp}.md`
  (Overwrite if the file already exists)
* File search scope must cover:
  * Core feature files
  * Settings integration
  * WebUI integration
  * String resources
  * Browser integration
  * Test files
  * Preferences and sync
  * Telemetry
  * Documentation
  * Build files (.gn, DEPS)

##### 2.b. Code-Level Understanding

* Identify all related elements:
  * Code blocks
  * Classes
  * Methods
  * Variables
  * Constants
* Understand the function and dependencies of each.
* Save the analysis to:
  `.memory/${agent_name}_${task_name}_code_understanding_${timestamp}.md`
  (Overwrite if the file already exists)

#### 3. Execution Planning

* Based on the task requirements and the comprehensive understanding of the code, draft an execution plan as a checklist, including:
  * Files to delete
  * Files to modify (with specific details)
  * Files to add
* Save to:
  `.memory/${agent_name}_${task_name}_execute_plan_${timestamp}.md`
  (Overwrite if the file already exists)

#### 4. Execute

* Execute the generated plan step by step, updating progress in real-time.
* Update the execution plan file in real-time as the plan is executed. 

#### 5. Build and Validation

##### 5.a. Build the project and check for build errors.

##### 5.b. Attempt to fix all build errors until the build passes.
* Once validation passes, go to the next step "Commit Changes" and no additional build is needed.

#### 6. Commit Changes

##### 6.a. Ask the user to confirm whether to commit changes.

##### 6.b. Once the user confirms:

* Execute `git add -u` to add all tracked changed files.
* Execute `git commit -m '${commit_description}'` to commit changes with the generated commit_description.
* Push the changes.

---


