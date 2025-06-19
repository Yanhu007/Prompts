---

# 📌 Edge Agent Generator Framework Update

The `edge_agent_generator` framework is updated to follow **three strict steps** for generating an Agent:

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

* Generate an Agent Capability Validation Checklist based on `../resources/Agent_Capability_Checklist.md`
* Save this checklist to:

  ```
  ./memory/agent_${agent_name}_gen_capability_checklist_${timestamp}.md
  ```
* This checklist is used to verify that the generated Agent meets all requirements

### 3.b Generate Agent Prompt

* Leverage:

  * The user-provided domain knowledge
  * The content in `Agent_Capability_Checklist.md`
  * The constraints and abilities required by the generation framework
* Generate the Agent prompt accordingly
* Update the capability checklist file in real-time as the Agent prompt is built

### 3.c Validate and Refine Agent Prompt

* Perform a **second-pass validation** of the Agent prompt:

  * Iterate through the checklist file at:

    ```
    ./memory/agent_${agent_name}_gen_capability_checklist_${timestamp}.md
    ```
  * For each checklist item:

    * Check if the current Agent prompt satisfies the requirement
    * If not, revise and repair the prompt accordingly
  * Repeat this loop of **checking and repairing** until **all checklist items** pass validation

---

