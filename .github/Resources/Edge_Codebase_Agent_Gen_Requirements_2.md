

# 📌 Edge Agent Generator Framework Update

**🚨 CRITICAL NOTICE: MANDATORY CAPABILITY COMPLIANCE 🚨**

**This framework enforces ABSOLUTE compliance with `Agent_MUST_HAVE_Capability_Checklist.md`. ANY deviation, simplification, or omission of capabilities is STRICTLY PROHIBITED and will result in immediate framework termination.**

The `edge_agent_generator` framework is updated to follow **three strict steps** for generating an Agent:

## ⚠️ CRITICAL COMPLIANCE REQUIREMENT

**ALL capabilities defined in `Agent_MUST_HAVE_Capability_Checklist.md` are MANDATORY and NON-NEGOTIABLE:**

* ❌ **STRICTLY FORBIDDEN**: Ignoring any capability requirements
* ❌ **STRICTLY FORBIDDEN**: Simplifying or reducing capability requirements  
* ❌ **STRICTLY FORBIDDEN**: Modifying capability requirements without explicit authorization
* ❌ **STRICTLY FORBIDDEN**: Omitting any capability from the generated Agent
* ❌ **STRICTLY FORBIDDEN**: Making excuses for not implementing any capability
* ❌ **STRICTLY FORBIDDEN**: Treating any capability as "optional" or "nice-to-have"
* ✅ **ABSOLUTELY REQUIRED**: Full compliance with ALL checklist items
* ✅ **ABSOLUTELY REQUIRED**: Complete implementation of every capability without exception
* ✅ **ABSOLUTELY REQUIRED**: Exact adherence to all capability specifications
* ✅ **ABSOLUTELY REQUIRED**: Zero tolerance for capability omissions

**⚠️ CRITICAL WARNING: Violation of these requirements will result in immediate Agent generation failure and framework rejection. There are NO EXCEPTIONS to this rule.**

**🔒 COMPLIANCE ENFORCEMENT: Every generated Agent MUST pass 100% capability validation before deployment.**

---

## Step 1: Prompt for Required Input

The framework **must wait for and request** the following necessary information from the user:

* Agent name
* Agent description
* Any reference materials or background knowledge (if available)

---

## Step 2: Understand and Confirm User Intent

The framework should:

* Interpret the user’s input
* Provide a clear summary of the interpreted intent back to the user for confirmation
* Proceed **only after** receiving user confirmation

---

## Step 3: Agent Generation Workflow

Once the user confirms the intent, the framework must proceed with the following substeps:

### 3.a Generate Capability Validation Checklist

* Generate an Agent Capability Validation Checklist based on `../resources/Agent_MUST_HAVE_Capability_Checklist.md`
* **🚫 ABSOLUTE PROHIBITION**: Every capability from `Agent_MUST_HAVE_Capability_Checklist.md` MUST be included without ANY modification
* **🚫 ZERO TOLERANCE**: Do not ignore, simplify, alter, or omit ANY capability requirements under ANY circumstances
* **🔒 MANDATORY INCLUSION**: ALL capabilities must be implemented exactly as specified - no interpretation allowed
* **⚠️ NO EXCUSES**: Performance concerns, complexity, or implementation difficulty are NOT valid reasons to skip capabilities
* Save this checklist to:

  ```
  ./memory/agent_${agent_name}_gen_capability_checklist_${timestamp}.md
  ```
* This checklist is used to verify that the generated Agent meets **ALL MANDATORY requirements WITHOUT EXCEPTION**

### 3.b Generate Agent Prompt

* Leverage:
  * The user-provided domain knowledge
  * **🔒 MANDATORY**: The complete content in `Agent_MUST_HAVE_Capability_Checklist.md` - every capability MUST be implemented exactly as specified
  * The constraints and abilities required by the generation framework
* **🚫 COMPLIANCE REQUIREMENT**: Generate the Agent prompt to include ALL capabilities from the checklist with ZERO modifications
* **🚫 ABSOLUTELY FORBIDDEN ACTIONS**: 
  * Omitting ANY capability requirements
  * Simplifying ANY capability requirements
  * Modifying ANY capability requirements
  * Making ANY capability "optional"
  * Providing workarounds instead of full implementation
* **⚡ IMMEDIATE FAILURE**: Any deviation from capability requirements will cause instant generation termination
* Update the capability checklist file in real-time as the Agent prompt is built

### 3.c Validate and Refine Agent Prompt

* Perform a **mandatory second-pass validation** of the Agent prompt:
  * Iterate through the checklist file at:

    ```
    ./memory/agent_${agent_name}_gen_capability_checklist_${timestamp}.md
    ```

  * For each checklist item:
    * **🔍 STRICT VERIFICATION**: Check if the current Agent prompt satisfies the requirement EXACTLY as specified
    * **🚫 ZERO TOLERANCE**: If ANY requirement is missing, incomplete, or modified, the Agent MUST be rejected
    * **🔧 MANDATORY REPAIR**: If not compliant, revise and repair the prompt to achieve 100% specification adherence
    * **📋 CAPABILITY TRACKING**: Each capability must be explicitly verified and marked as "COMPLIANT" before proceeding
  * **♾️ CONTINUOUS VALIDATION**: Repeat this loop of **checking and repairing** until **ALL checklist items pass 100% validation**
  * **⚠️ FAILURE CONDITION**: If any capability cannot be implemented exactly as specified, the entire Agent generation MUST be terminated

**🏁 FINAL REQUIREMENT**: Only Agents that achieve 100% capability compliance are permitted to proceed to deployment.

---

## 🔒 FINAL ENFORCEMENT AND COMPLIANCE VERIFICATION

### Mandatory Pre-Deployment Checklist

Before any Agent is considered complete, the framework MUST verify:

1. **📋 100% Capability Coverage**: Every single capability from `Agent_MUST_HAVE_Capability_Checklist.md` is implemented exactly as specified
2. **🚫 Zero Modifications**: No capability has been simplified, altered, or omitted
3. **✅ Full Functionality**: Each capability is fully functional and tested
4. **📝 Complete Documentation**: All capability implementations are properly documented

### Failure Consequences

**If ANY capability is missing, incomplete, or modified:**

* ❌ **Immediate Termination**: Agent generation process stops immediately
* ❌ **No Partial Acceptance**: Incomplete Agents are NOT acceptable under any circumstances  
* ❌ **No Workarounds**: Alternative implementations that don't meet exact specifications are rejected
* ❌ **No Exceptions**: Technical difficulties or time constraints are NOT valid excuses

### Success Criteria

**An Agent is only considered successfully generated when:**

* ✅ **Perfect Compliance**: 100% adherence to `Agent_MUST_HAVE_Capability_Checklist.md`
* ✅ **Complete Implementation**: Every capability is fully implemented and functional
* ✅ **Exact Specifications**: All capabilities match the checklist requirements precisely
* ✅ **Validated Performance**: All capabilities have been tested and verified

**Remember: The purpose of this framework is to ensure EVERY generated Agent maintains the highest standards of capability and functionality. Compromise is not an option.**
