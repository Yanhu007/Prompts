# Edge Agent Generator PowerShell Script
# 
# This script generates specialized Edge codebase expert agents using the established
# framework. It creates production-ready agent prompts with built-in safety and 
# accuracy measures.
#
# Usage:
#     .\Generate-EdgeAgent.ps1 -AgentName "agent_name" -Description "description"
#     
# Example:
#     .\Generate-EdgeAgent.ps1 -AgentName "feature_flag_manager" -Description "Manage feature flags in Edge codebase"

param(
    [Parameter(Mandatory=$true)]
    [string]$AgentName,
    
    [Parameter(Mandatory=$true)]
    [string]$Description
)

function Sanitize-AgentName {
    param([string]$Name)
    
    # Convert to lowercase and replace spaces/special chars with underscores
    $sanitized = $Name.ToLower() -replace '[^a-zA-Z0-9_]', '_'
    # Remove multiple consecutive underscores
    $sanitized = $sanitized -replace '_+', '_'
    # Remove leading/trailing underscores
    $sanitized = $sanitized.Trim('_')
    
    return $sanitized
}

function Generate-AgentPrompt {
    param(
        [string]$AgentName,
        [string]$Description
    )
    
    $filename = Sanitize-AgentName -Name $AgentName
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
    
    $promptContent = @"
````prompt
// filepath: c:\Edge\src\.github\prompts\$filename.prompt.md
---
mode: "agent"
description: "$Description"
---
# $($AgentName.Substring(0,1).ToUpper() + $AgentName.Substring(1)) Agent

You are an AI assistant specialized in $($Description.ToLower()). You have extensive 
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
- `${'$'}{out_dir}`: The build directory (e.g., `out/debug_x64`)
- `${'$'}{target_component}`: The component or feature being modified
- `${'$'}{branch_name}`: Safe branch name for changes

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

Generated on: $timestamp
Agent Framework Version: 1.0
````
"@

    return @{
        Content = $promptContent
        Filename = $filename
    }
}

# Main execution
try {
    # Check if we're in the right directory
    $promptsDir = Join-Path $PWD ".github\prompts"
    if (-not (Test-Path $promptsDir)) {
        Write-Error "Error: .github\prompts directory not found. Please run from Edge source root."
        exit 1
    }
    
    # Generate the prompt
    $result = Generate-AgentPrompt -AgentName $AgentName -Description $Description
    
    # Check if file already exists
    $outputPath = Join-Path $promptsDir "$($result.Filename).prompt.md"
    if (Test-Path $outputPath) {
        $response = Read-Host "File $outputPath already exists. Overwrite? (y/N)"
        if ($response.ToLower() -ne 'y') {
            Write-Host "Operation cancelled."
            exit 0
        }
    }
    
    # Write the prompt file
    $result.Content | Out-File -FilePath $outputPath -Encoding UTF8
    
    Write-Host "Successfully generated agent prompt: $outputPath" -ForegroundColor Green
    Write-Host "Agent Name: $AgentName" -ForegroundColor Cyan
    Write-Host "Description: $Description" -ForegroundColor Cyan
    Write-Host "File: .github\prompts\$($result.Filename).prompt.md" -ForegroundColor Cyan
    
} catch {
    Write-Error "Error generating agent: $($_.Exception.Message)"
    exit 1
}
