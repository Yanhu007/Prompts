# Edge Codebase Agent Generation Framework Checklist

## 🚨 CRITICAL COMPLIANCE REQUIREMENTS

### Mandatory Capability Compliance
- [ ] **ABSOLUTE COMPLIANCE**: Framework MUST enforce 100% compliance with `Agent_MUST_HAVE_Capability.md`
- [ ] **ZERO TOLERANCE**: Framework MUST NOT allow any deviation, simplification, or omission of capabilities
- [ ] **IMMEDIATE TERMINATION**: Framework MUST terminate if ANY capability requirement is violated
- [ ] **COMPLETE VALIDATION**: Framework MUST validate 100% capability coverage before deployment
- [ ] **NO EXCEPTIONS**: Framework MUST NOT accept technical difficulties or time constraints as valid excuses

### Prohibited Actions (Strictly Forbidden)
- [ ] **VERIFY**: Framework does NOT ignore any capability requirements
- [ ] **VERIFY**: Framework does NOT simplify or reduce capability requirements
- [ ] **VERIFY**: Framework does NOT modify capability requirements without explicit authorization
- [ ] **VERIFY**: Framework does NOT omit any capability from generated Agents
- [ ] **VERIFY**: Framework does NOT make excuses for not implementing any capability
- [ ] **VERIFY**: Framework does NOT treat any capability as "optional" or "nice-to-have"

## Step 1: Input Collection Requirements

### Required User Input Prompting
- [ ] Framework MUST prompt for and wait for Agent name
- [ ] Framework MUST prompt for and wait for Agent description
- [ ] Framework MUST prompt for and wait for reference materials or background knowledge (if available)
- [ ] Framework MUST NOT proceed without collecting all required inputs
- [ ] Framework MUST validate that all inputs are provided before proceeding

## Step 2: Intent Analysis and Confirmation

### Deep Intent Analysis
- [ ] Framework MUST analyze provided inputs (Agent name, description, reference materials)
- [ ] Framework MUST apply domain knowledge from reference materials in "Before You Start" section
- [ ] Framework MUST identify specific Edge/Chromium development area (feature removal, build processes, code search, etc.)
- [ ] Framework MUST recognize potential complexity levels and scope considerations
- [ ] Framework MUST understand common patterns and workflows in Edge development

### Ambiguity Detection and Resolution
- [ ] Framework MUST proactively identify potential ambiguities in user requests
- [ ] Framework MUST detect multiple interpretation scenarios
- [ ] Framework MUST identify scope uncertainties
- [ ] Framework MUST recognize technical approach variations
- [ ] Framework MUST apply knowledge from `terminology.md` to identify terms with multiple interpretations

### Intent Clarification Process
- [ ] Framework MUST list all possible interpretations with clear explanations when ambiguities detected
- [ ] Framework MUST provide context for why each interpretation is valid based on Edge development practices
- [ ] Framework MUST ask specific clarifying questions to help user choose intended approach
- [ ] Framework MUST use structured options (e.g., "Option A:", "Option B:") for clear selection
- [ ] Framework MUST reference relevant examples from existing prompts or common Edge development scenarios

### Intent Confirmation
- [ ] Framework MUST provide comprehensive summary of interpreted intent including:
  - [ ] Specific Agent role and expertise area
  - [ ] Scope of responsibilities and limitations
  - [ ] Intended workflow or process the Agent will follow
  - [ ] Specific Edge development practices or standards to be enforced
- [ ] Framework MUST explicitly state assumptions made based on domain knowledge
- [ ] Framework MUST request explicit user confirmation before proceeding
- [ ] Framework MUST proceed ONLY after receiving clear user confirmation

### Documentation Requirement
- [ ] Framework MUST document the confirmed intent for reference during Agent generation
- [ ] Framework MUST record any clarifications or decisions made during intent confirmation process
- [ ] Framework MUST note any specific requirements or constraints identified through analysis

## Step 3: Agent Generation Workflow

### 3.a Capability Validation Checklist Generation
- [ ] Framework MUST generate Agent Capability Validation Checklist based on `Agent_MUST_HAVE_Capability.md`
- [ ] Framework MUST include every capability from checklist without ANY modification
- [ ] Framework MUST NOT ignore, simplify, alter, or omit ANY capability requirements
- [ ] Framework MUST implement ALL capabilities exactly as specified with zero interpretation allowed
- [ ] Framework MUST save checklist to: `./memory/agent_${agent_name}_gen_capability_checklist_${timestamp}.md`
- [ ] Framework MUST use this checklist to verify ALL MANDATORY requirements are met

### 3.b Agent Prompt Generation
- [ ] Framework MUST leverage user-provided domain knowledge
- [ ] Framework MUST include complete content from `Agent_MUST_HAVE_Capability.md`
- [ ] Framework MUST implement ALL capabilities from checklist with ZERO modifications
- [ ] Framework MUST NOT omit ANY capability requirements
- [ ] Framework MUST NOT simplify ANY capability requirements
- [ ] Framework MUST NOT modify ANY capability requirements
- [ ] Framework MUST NOT make ANY capability "optional"
- [ ] Framework MUST NOT provide workarounds instead of full implementation
- [ ] Framework MUST update capability checklist file in real-time as Agent prompt is built
- [ ] Framework MUST terminate immediately if ANY deviation from capability requirements occurs

### 3.c Validation and Refinement
- [ ] Framework MUST perform mandatory second-pass validation of Agent prompt
- [ ] Framework MUST iterate through checklist file at specified location
- [ ] For each checklist item, Framework MUST:
  - [ ] Check if current Agent prompt satisfies requirement EXACTLY as specified
  - [ ] Reject Agent if ANY requirement is missing, incomplete, or modified
  - [ ] Revise and repair prompt to achieve 100% specification adherence if not compliant
  - [ ] Explicitly verify and mark each capability as "COMPLIANT" before proceeding
- [ ] Framework MUST repeat checking and repairing loop until ALL checklist items pass 100% validation
- [ ] Framework MUST terminate entire Agent generation if any capability cannot be implemented exactly as specified

## Agent Professional Capabilities Requirements

### Edge Codebase Expertise
- [ ] Generated prompt MUST represent an Edge codebase expert
- [ ] Agent MUST be familiar with common modification workflows for Edge codebase
- [ ] Agent MUST follow and advocate for safe and accurate code modification practices
- [ ] Agent MUST consider common considerations and best practices when modifying Edge code
- [ ] Agent MUST clearly describe role as Edge codebase expert
- [ ] Agent MUST explain responsibility to guide users in making safe and accurate code modifications
- [ ] Agent MUST specify development standards followed and Edge project's code modification processes

## Output Requirements

### File Generation Standards
- [ ] Framework MUST generate markdown file containing agent's prompt
- [ ] Framework MUST save file to `.github/prompts` directory
- [ ] Framework MUST use filename that exactly matches user-provided Agent Name (format: `${Agent Name}_agent.md`)
- [ ] Framework MUST ensure content format is unified and standardized
- [ ] Framework MUST conform to style and structure used for GPT agent initialization

### Content Customization
- [ ] Framework MUST customize prompt content by incorporating additional reference information provided by user
- [ ] Framework MUST ensure all user-provided context is appropriately integrated
- [ ] Framework MUST maintain consistency with Edge development standards throughout customization

## Final Enforcement and Compliance Verification

### Mandatory Pre-Deployment Checklist
- [ ] Framework MUST verify 100% capability coverage from `Agent_MUST_HAVE_Capability.md`
- [ ] Framework MUST verify zero modifications to capabilities
- [ ] Framework MUST verify full functionality of each capability
- [ ] Framework MUST verify complete documentation of all capability implementations

### Success Criteria Validation
- [ ] Framework MUST ensure perfect compliance with capability checklist (100% adherence)
- [ ] Framework MUST ensure complete implementation of every capability
- [ ] Framework MUST ensure exact specifications match checklist requirements precisely
- [ ] Framework MUST ensure validated performance of all capabilities through testing and verification

### Failure Handling
- [ ] Framework MUST immediately terminate if ANY capability is missing, incomplete, or modified
- [ ] Framework MUST NOT accept partial implementations under any circumstances
- [ ] Framework MUST reject alternative implementations that don't meet exact specifications
- [ ] Framework MUST NOT allow exceptions for technical difficulties or time constraints

## Quality Assurance Requirements

### Process Integrity
- [ ] Framework MUST follow the three strict steps without deviation
- [ ] Framework MUST not skip or combine any required steps
- [ ] Framework MUST maintain audit trail of all decisions and validations
- [ ] Framework MUST ensure reproducible and consistent results

### Error Prevention
- [ ] Framework MUST validate all inputs before processing
- [ ] Framework MUST handle edge cases and error conditions gracefully
- [ ] Framework MUST provide clear error messages when validation fails
- [ ] Framework MUST prevent generation of non-compliant agents under any circumstances

---

**🔒 FRAMEWORK COMPLIANCE CERTIFICATION**

This checklist ensures the Edge Agent Generation Framework maintains the highest standards of capability and functionality. Every item must be verified and completed before the framework can be considered operational. Compromise is not an option.

**Framework Status: [ ] FULLY COMPLIANT [ ] NON-COMPLIANT**

*Date of Last Verification: _______________*
*Verified By: _______________*
