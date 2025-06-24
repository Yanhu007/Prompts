# 📌 Edge Agent Generator Framework Update

The `edge_agent_generator` framework is updated to follow **three strict steps** for generating an agent.

## ⚠️ CRITICAL COMPLIANCE REQUIREMENT

**ALL capabilities defined in `.github/resources/Agent_MUST_HAVE_Capability.md` are MANDATORY and NON-NEGOTIABLE:**

* ❌ **FORBIDDEN**: Ignoring, simplifying, modifying, or omitting any capability requirements
* ❌ **FORBIDDEN**: Making excuses for not implementing capabilities or treating any capability as "optional"
* ✅ **REQUIRED**: Full compliance with ALL capability specifications without exception
* ✅ **REQUIRED**: Zero tolerance for capability omissions or modifications

**⚠️ WARNING: Violation of these requirements will result in immediate Agent generation failure and graceful framework termination (allowing user to restart the process).**

**🔒 ENFORCEMENT: Every generated Agent MUST pass 100% capability validation before finish.**

---

## Step 1: Prompt for Required Input

The framework **must wait for and request** the following necessary information from the user:

* Agent name
* Agent description
* Any reference materials or background knowledge (if available)

**⚠️ ERROR HANDLING**: If the user provides insufficient information:
* **Notify the user** of the missing or incomplete information with specific details
* **Stop the process** immediately
* **Request the user** to provide the required information before proceeding
* **Do not proceed** until all required information is provided

---

## Step 2: Understand and Confirm User Intent

The edge_agent_generator framework should follow this enhanced intent analysis process:

### 2.a Deep Intent Analysis

* **Analyze the provided inputs** (Agent name, description, and reference materials) and **Analyze the mandatory documents** in the learning section of `.github/resources/Agent_MUST_HAVE_Capability.md` to:
  * Understand the user's intent
  * Identify the specific Edge/Chromium development area (e.g., feature removal, build processes, code search, etc.)
  * Recognize potential complexity levels and scope considerations
  * Understand common patterns and workflows in Edge development

### 2.b Ambiguity Detection and Resolution

* **Proactively identify potential ambiguities** in the user's request:
  * **Multiple interpretation scenarios**: If the Agent name or description could have different meanings
  * **Scope uncertainties**: If the intended scope of the Agent's responsibilities is unclear
  * **Technical approach variations**: If there are multiple valid approaches to achieve the stated goal
  * **Domain-specific terminology**: Apply knowledge from `.github/resources/terminology.md` to identify terms that may have multiple interpretations (e.g., "remove feature" vs "unship feature" vs "remove feature flag")

### 2.c Intent Clarification Process

When ambiguities are detected, the edge_agent_generator framework must:

* **List all possible interpretations** with clear explanations of each scenario
* **Provide context** for why each interpretation is valid based on Edge development practices
* **Ask specific clarifying questions** to help the user choose the intended approach
* **Use structured options** (e.g., "Option A:", "Option B:") to make selection clear
* **Reference relevant examples** from existing prompts or common Edge development scenarios

### 2.d Intent Confirmation

* **Provide a comprehensive summary** of the interpreted intent, including:
  * The specific Agent role and expertise area
  * The scope of responsibilities and limitations
  * The intended workflow or process the Agent will follow
  * Any specific Edge development practices or standards to be enforced
* **Explicitly state assumptions** made based on the domain knowledge
* **Request explicit user confirmation** before proceeding
* **Proceed only after** receiving clear user confirmation

### 2.e Documentation Requirement

* **Document the confirmed intent** for reference during Agent generation
* **Record any clarifications** or decisions made during the intent confirmation process
* **Note any specific requirements** or constraints identified through the analysis

---

## Step 3: Agent Generation Workflow

Once the user confirms the intent, the edge_agent_generator framework must proceed with the following substeps:

### 3.a Prepare Capability Validation Checklist

**⚠️ DEPENDENCY CHECK**: Before proceeding, verify that the required files exist:
* `.github/resources/Agent_MUST_HAVE_Capability.md` (complete capability specifications - the authoritative source)
* `.github/resources/Agent_MUST_HAVE_Capability_Checklist.md` (validation checklist template - auto-generated from main file)
* `.github/resources/terminology.md` (Edge development terminology reference)

**📋 FILE RELATIONSHIP DETAILS**: 
- **Primary Source**: `.github/resources/Agent_MUST_HAVE_Capability.md` contains the complete, authoritative capability definitions
- **Derived Checklist**: `.github/resources/Agent_MUST_HAVE_Capability.md` is automatically generated from the primary source and maintained for consistency
- **Consistency Guarantee**: The checklist file is programmatically synchronized with the main capability file
- **Update Process**: Any changes to the main file automatically trigger checklist regeneration

**🚫 ERROR HANDLING**: If any dependency file is missing:
* **Notify the user** that required dependency files are not found
* **List the missing files** specifically
* **Provide download guidance**: If `.github/resources/Agent_MUST_HAVE_Capability.md` is missing, instruct user to download from: `https://github.com/Yanhu007/prompts/blob/main/.github/resources/Agent_MUST_HAVE_Capability_Checklist.md`
* **Stop the process** immediately and do not proceed until all required files are available

* **Copy and initialize** the pre-generated checklist `.github/resources/Agent_MUST_HAVE_Capability_Checklist.md` to:

  ```
  ./memory/Agent_MUST_HAVE_Capability_Checklist_${YYYYMMDD-HHMMSS}.md
  ```
  **📅 TIMESTAMP FORMAT SPECIFICATION**:
  - **Format**: `YYYYMMDD-HHMMSS` (compact format with date and time separated by hyphen)
  - **Example**: `20250622-143059` (June 22, 2025, 2:30:59 PM)
  - **Timezone**: Local system timezone, no timezone suffix included
  - **Precision**: Seconds level to ensure uniqueness

* This timestamped checklist serves as a **validation tracking tool** to systematically verify that the generated Agent meets **ALL MANDATORY requirements from the original `.github/resources/Agent_MUST_HAVE_Capability.md`** WITHOUT EXCEPTION
* **Important**: The edge_agent_generator framework generates the Agent based on the **complete original file** (`.github/resources/Agent_MUST_HAVE_Capability.md`), while using the timestamped checklist file to track validation progress and ensure all capabilities have been properly implemented
* **Validation Tracking**: The checklist will be automatically updated during validation:
  * Format: `[✅] CAPABILITY_NAME` for verified capabilities
  * Format: `[❌] CAPABILITY_NAME` for missing/incomplete capabilities
  * **Verification Standard**: Each checklist item corresponds to a specific capability in `.github/resources/Agent_MUST_HAVE_Capability.md`. Verification passes when the Agent implements functionality that is literally identical to the specified capability

### 3.b Generate Agent Prompt

* **Consolidate the following components**:
  * The user-provided domain knowledge
  * **🔒 MANDATORY**: The complete content in `.github/resources/Agent_MUST_HAVE_Capability.md` - every capability MUST be implemented exactly as specified
  * The constraints and abilities required by the edge_agent_generator framework

* **🚫 COMPLIANCE REQUIREMENT**: Generate the Agent prompt to include ALL capabilities from the original specification with ZERO modifications

* **🚫 FORBIDDEN ACTIONS**: 
  * Omitting ANY capability specifications
  * Simplifying ANY capability specifications
  * Modifying ANY capability specifications
  * Making ANY capability "optional"
  * Providing workarounds instead of full implementation

* **⚡ FAILURE CONDITION**: Any deviation from capability specifications will cause graceful generation termination (user can restart from the beginning)

### 3.c Validate and Refine Agent Prompt

* **Perform mandatory validation** of the Agent prompt:
  * **Iterate through** the checklist file at:

    ```
    ./memory/Agent_MUST_HAVE_Capability_Checklist_${YYYYMMDD-HHMMSS}.md
    ```

  * **For each checklist item**:
    * **🔍 VERIFICATION**: Check if the current Agent prompt satisfies the requirement EXACTLY as specified in the original `.github/resources/Agent_MUST_HAVE_Capability.md`
    * **✅ VERIFICATION STANDARD**: Apply the following validation criteria in hierarchical order:
      1. **Literal inclusion**: The exact text from the capability specification is present in the Agent prompt
      2. **Functional equivalence**: If literal inclusion is not applicable, verify that the Agent prompt implements the same functionality through different but equivalent wording
      3. **Behavioral compliance**: The Agent prompt demonstrates the required behavior when the capability specification describes actions or processes
    * **� ACCEPTANCE CRITERIA**: A capability passes validation when ANY of the above criteria is satisfied, with priority given to literal inclusion where possible
    * **🚫 REJECTION CRITERIA**: A capability fails validation if it is missing, incomplete, simplified, modified, or functionally different from the original specification
    * **🔧 REPAIR**: If not compliant, revise and repair the prompt to achieve 100% specification adherence
    * **📋 TRACKING**: Each capability must be explicitly verified and the capability checklist file must be updated in real-time using format `[✅] CAPABILITY_NAME` or `[❌] CAPABILITY_NAME`
    
  * **♾️ VALIDATION LOOP**: Repeat this process of **checking and repairing** until **ALL checklist items pass 100% validation**
  * **🔄 RETRY MECHANISM**: 
    - **Maximum attempts**: 5 repair attempts per complete validation round
    - **Retry trigger**: Any capability validation failure
    - **Retry process**: Re-generate the specific failed capability section and re-validate
    - **Progress tracking**: Update checklist file after each repair attempt
  * **⚠️ TERMINATION CONDITIONS**: 
    - **Automatic termination**: If validation fails after 5 complete validation rounds
    - **Manual termination**: If user explicitly requests to stop
    - **System termination**: If required dependency files become unavailable during process

**🔄 RESTART MECHANISM**: When the process is terminated and user chooses to restart:
* **🚫 NO PROGRESS RETENTION**: Previous progress is not retained
* **🔁 COMPLETE RESTART**: The process starts from Step 1 (Prompt for Required Input)
* **📋 NEW CHECKLIST**: A new timestamped checklist file will be generated with a new timestamp

**🏁 COMPLETION REQUIREMENT**: Only Agents that achieve 100% capability compliance are permitted to proceed to finish.

---

## 🔒 FINAL ENFORCEMENT AND COMPLIANCE VERIFICATION

### Mandatory Pre-finish Checklist

Before any Agent is considered complete, the framework MUST verify:

1. **📋 100% Capability Coverage**: Every single capability from `.github/resources/Agent_MUST_HAVE_Capability.md` is implemented exactly as specified
2. **🚫 Zero Modifications**: No capability has been simplified, altered, or omitted  

### Final Outcome

**An Agent is only considered successfully generated when it achieves:**
* ✅ **Perfect Compliance**: 100% adherence to `.github/resources/Agent_MUST_HAVE_Capability.md`
* ✅ **Complete Implementation**: Every capability is fully implemented and functional
* ✅ **Exact Specifications**: All capabilities match the checklist requirements precisely

**If ANY capability is missing, incomplete, or not literally identical after maximum retry attempts, the Agent generation process stops gracefully with clear stop reasons saved in ./memory/stop_reasons_${YYYYMMDD-HHMMSS}.md (user can restart the process from the beginning with a new checklist).**

**Remember: The purpose of the edge_agent_generator framework is to ensure EVERY generated Agent maintains the highest standards of capability and functionality. Compromise is not an option.**

---

## 📚 PRACTICAL EXAMPLES

### Example 1: Successful Validation
```markdown
✅ CAPABILITY: "Must provide code analysis for Edge features"
AGENT PROMPT CONTAINS: "I will analyze Edge/Chromium feature code and provide detailed technical assessments..."
VALIDATION RESULT: ✅ Pass (functional equivalence)
```

### Example 2: Failed Validation - Missing Capability
```markdown
❌ CAPABILITY: "Must validate build configurations"
AGENT PROMPT CONTAINS: [No related content found]
VALIDATION RESULT: ❌ Fail (missing capability)
REPAIR ACTION: Add build configuration validation instructions to Agent prompt
```

### Example 3: Failed Validation - Simplified Capability
```markdown
❌ CAPABILITY: "Must perform comprehensive security analysis of code changes"
AGENT PROMPT CONTAINS: "I can check code for basic security issues"
VALIDATION RESULT: ❌ Fail (simplified - missing 'comprehensive' requirement)
REPAIR ACTION: Enhance to include full comprehensive security analysis capabilities
```

### Checklist File Example
```markdown
# Agent Capability Validation Checklist - 20250622-143059

[✅] CODE_ANALYSIS_CAPABILITY
[✅] BUILD_VALIDATION_CAPABILITY  
[❌] SECURITY_ANALYSIS_CAPABILITY
[⏳] DOCUMENTATION_GENERATION_CAPABILITY
[❌] PERFORMANCE_OPTIMIZATION_CAPABILITY

## Validation Summary
- Total Capabilities: 5
- Passed: 2
- Failed: 2  
- Pending: 1
- Completion: 40%
```
