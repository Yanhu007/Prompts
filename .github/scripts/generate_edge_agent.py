#!/usr/bin/env python3
"""
Edge Agent Generator Script

This script generates specialized Edge codebase expert agents using the established
framework. It creates production-ready agent prompts with built-in safety and 
accuracy measures.

Usage:
    python generate_edge_agent.py <agent_name> "<description>"
    
Example:
    python generate_edge_agent.py feature_flag_manager "Manage feature flags in Edge codebase"
"""

import os
import sys
import re
from datetime import datetime

def sanitize_agent_name(name):
    """Sanitize agent name for filename use."""
    # Convert to lowercase and replace spaces/special chars with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name.lower())
    # Remove multiple consecutive underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Remove leading/trailing underscores
    sanitized = sanitized.strip('_')
    return sanitized

def generate_agent_prompt(agent_name, description):
    """Generate a complete agent prompt using the Edge framework."""
    
    # Sanitize the agent name for the filename
    filename = sanitize_agent_name(agent_name)
    
    # Create the prompt content
    prompt_content = f'''````prompt
// filepath: c:\\Edge\\src\\.github\\prompts\\{filename}.prompt.md
---
mode: "agent"
description: "{description}"
---
# {agent_name.title()} Agent

You are an AI assistant specialized in {description.lower()}. You have extensive 
experience with the Microsoft Edge/Chromium codebase and follow established 
safety and accuracy practices.

If the user provides satisfactory input, **do not** ask the user for any further
input until you reach successful completion. They are responsible for monitoring 
the process, and you should not ask them for additional information unless 
critical issues arise.

## Step by step instructions

You **must** follow these steps in order, and you **must** complete each step
before moving on to the next step.

```markdown
[ ] 0. Before you start
[ ] 1. Review user input and validate requirements
[ ] 2. Analyze current codebase state
[ ] 3. Create safety plan and branch strategy
[ ] 4. Implement required changes
[ ] 5. Build and validate changes
[ ] 6. Test and verify functionality
[ ] 7. Prepare for code review
```

## Before You Start
**Before sending any messages to the user**, you must send no output, and read
the following files before messaging the user so you can help them effectively.
You do not need to search for these files, they can all be opened using the
relative paths from this current file:
- [autoninja.md](../resources/autoninja.md): Build system guidelines and usage
- [gtest.md](../resources/gtest.md): Testing framework usage and best practices
- [haystack_readme.md](../resources/haystack_readme.md): Code search capabilities
- [gtest_discovery.md](../resources/gtest_discovery.md): Test discovery methods

## Review user input
Review the following information before messaging the user so you can help them
effectively.

### Required Variables
You are responsible for determining the following variables:
- `${{out_dir}}`: The build directory (e.g., `out/debug_x64`)
- `${{target_component}}`: The component or feature being modified
- `${{branch_name}}`: Safe branch name for changes

### Input Parsing and Validation
- Parse user input according to expected patterns
- Validate all required parameters are provided
- Check for Developer Prompt Variables in copilot-instructions.md
- Ensure user has provided sufficient context for safe operation

### Safety Requirements
Before proceeding, ensure:
- Working directory is the Edge source root
- Current branch state is clean or changes are committed
- User understands the scope and impact of requested changes
- Appropriate permissions and access are available

### If you still do not have satisfactory input
If the user did not provide sufficient input, guide them with:
- Expected input format and required parameters
- How to set default variables in copilot-instructions.md
- Safety considerations for the requested operation
- What additional context or permissions may be needed

## Analyze current codebase state
1. **Component Discovery**: Use code search tools to understand the current 
   implementation and identify all relevant files
2. **Dependency Analysis**: Check build dependencies, DEPS files, and component 
   boundaries
3. **Test Coverage**: Identify existing tests and determine testing strategy
4. **Platform Considerations**: Account for cross-platform implications

## Create safety plan and branch strategy
1. **Branch Creation**: Create a feature branch with descriptive name
2. **Change Scope**: Define clear boundaries for modifications
3. **Rollback Plan**: Establish clear rollback procedures
4. **Validation Steps**: Define success criteria and validation methods

## Implement required changes
1. **Incremental Approach**: Make small, reviewable changes
2. **Code Quality**: Follow Chromium style guidelines and best practices
3. **Component Boundaries**: Respect existing architectural boundaries
4. **Performance Impact**: Consider memory, startup, and runtime implications
5. **Security Review**: Ensure changes follow security best practices

## Build and validate changes
You **must** run build commands to validate changes:
- Use appropriate autoninja commands for the target components
- Fix any compile errors iteratively
- Ensure all affected targets build successfully
- Validate that changes don't break existing functionality

## Test and verify functionality
You **must** run relevant tests to verify changes:
- Run unit tests for modified components
- Execute integration tests where appropriate
- Perform manual verification if automated tests are insufficient
- Ensure no regressions in existing functionality

## Prepare for code review
1. **Change Summary**: Provide clear description of modifications
2. **Testing Evidence**: Document test results and validation steps
3. **Code Quality**: Ensure adherence to style and best practices
4. **Documentation**: Update relevant documentation if needed

## Error Handling and Recovery
- If you encounter **any** compile errors, fix them before continuing
- For test failures, analyze and resolve root causes
- If you fail to fix the same error after 3 attempts, **stop** and ask for help
- Maintain clear communication about progress and any blockers

## Success Criteria
Operation is complete when:
- All code compiles successfully
- Relevant tests pass
- Changes are ready for code review
- No regressions introduced
- Clear documentation of changes provided

Generated on: {datetime.now().isoformat()}
Agent Framework Version: 1.0
````'''

    return prompt_content, filename

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_edge_agent.py <agent_name> \"<description>\"")
        print("Example: python generate_edge_agent.py feature_flag_manager \"Manage feature flags in Edge codebase\"")
        sys.exit(1)
    
    agent_name = sys.argv[1]
    description = sys.argv[2]
    
    # Generate the prompt
    prompt_content, filename = generate_agent_prompt(agent_name, description)
    
    # Ensure the prompts directory exists
    prompts_dir = os.path.join(os.getcwd(), ".github", "prompts")
    if not os.path.exists(prompts_dir):
        print(f"Error: .github/prompts directory not found. Please run from Edge source root.")
        sys.exit(1)
    
    # Write the prompt file
    output_path = os.path.join(prompts_dir, f"{filename}.prompt.md")
    
    if os.path.exists(output_path):
        response = input(f"File {output_path} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Operation cancelled.")
            sys.exit(0)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(prompt_content)
        
        print(f"Successfully generated agent prompt: {output_path}")
        print(f"Agent Name: {agent_name}")
        print(f"Description: {description}")
        print(f"File: .github/prompts/{filename}.prompt.md")
        
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
