# Edge Codebase Expert Agent Generation Framework

This framework provides a standardized approach to creating specialized AI agents for the Microsoft Edge/Chromium codebase. It emphasizes safety, accuracy, and consistency across all generated agents.

## Overview

The Edge Agent Generation Framework is designed to create production-ready AI agents that can safely and effectively work with the complex Edge/Chromium codebase. Each generated agent follows established patterns and includes built-in safety measures to prevent common issues like build breaks, test failures, and code quality problems.

## Core Principles

### Safety First
- **Branch Protection**: All agents work on feature branches, never directly on main
- **Incremental Changes**: Small, reviewable modifications that can be easily rolled back
- **Build Validation**: Continuous build verification throughout the process
- **Test Coverage**: Comprehensive testing before considering changes complete

### Accuracy and Quality
- **Component Awareness**: Deep understanding of Chromium component boundaries
- **Platform Considerations**: Cross-platform compatibility (Windows, macOS, Linux, mobile)
- **Performance Impact**: Memory, startup, and runtime performance considerations
- **Security Compliance**: Adherence to Chromium security best practices

### Consistency
- **Standardized Structure**: All agents follow the same organizational pattern
- **Common Resources**: Shared knowledge base and utility functions
- **Unified Error Handling**: Consistent approach to error recovery and user communication
- **Code Review Readiness**: Changes are always prepared for proper code review

## Framework Components

### 1. Agent Structure Template

Every generated agent follows this structure:

```yaml
---
mode: "agent"
description: "[Brief description of agent's purpose]"
---
```

#### Core Sections
- **Header and Description**: Clear identification and purpose
- **Step-by-Step Instructions**: Ordered, checkable process steps
- **Pre-execution Requirements**: Required resource reading and validation
- **Input Review and Validation**: Parameter parsing and safety checks
- **Domain-Specific Implementation**: Customized for the agent's purpose
- **Build and Test Validation**: Comprehensive verification steps
- **Error Handling**: Recovery procedures and user communication

### 2. Safety Mechanisms

#### Pre-execution Validation
- Verify working directory is Edge source root
- Check current branch state and cleanliness
- Validate user permissions and access rights
- Ensure all required tools and dependencies are available

#### Runtime Safety
- Create feature branches for all modifications
- Incremental change approach with frequent validation
- Continuous build verification
- Comprehensive test execution
- Clear rollback procedures

#### Post-execution Verification
- Build success confirmation
- Test pass verification
- Code quality validation
- Documentation completeness check

### 3. Resource Integration

All agents automatically integrate with established Edge development resources:

- **autoninja.md**: Build system guidelines and usage patterns
- **gtest.md**: Testing framework usage and best practices
- **haystack_readme.md**: Code search capabilities and setup
- **gtest_discovery.md**: Test discovery and execution methods

### 4. Error Handling Strategy

- **Iterative Resolution**: Fix issues systematically with clear progress tracking
- **Attempt Limits**: Stop after 3 failed attempts and request human intervention
- **Context Preservation**: Maintain state and context across error recovery cycles
- **Clear Communication**: Provide detailed status updates and next steps

## Usage Instructions

### Method 1: Using the Generator Agent

1. Use the `edge_agent_generator` prompt in VS Code
2. Provide agent name and description
3. The generator will create a complete agent prompt file

### Method 2: Using PowerShell Script (Windows)

```powershell
.\Generate-EdgeAgent.ps1 -AgentName "your_agent_name" -Description "Agent description"
```

### Method 3: Using Python Script (Cross-platform)

```bash
python generate_edge_agent.py your_agent_name "Agent description"
```

## Agent Customization

### Domain-Specific Sections

Each agent can be customized for its specific domain:

#### Code Discovery Patterns
- Component-specific file locations and naming conventions
- Relevant build targets and dependency chains
- Integration points with other Edge components
- Platform-specific implementation details

#### Implementation Guidelines
- Domain-specific coding patterns and best practices
- API usage guidelines and examples
- Integration strategies with existing systems
- Performance optimization techniques

#### Testing Strategies
- Unit test patterns and requirements
- Integration test scenarios
- Browser test considerations
- Performance and security test requirements

### Variable Management

Agents can define custom variables for their domain:
- `${out_dir}`: Build directory (standard across all agents)
- `${target_component}`: Component being modified
- `${feature_name}`: Feature or functionality name
- Domain-specific variables as needed

## Best Practices

### Agent Design
1. **Clear Purpose**: Each agent should have a single, well-defined purpose
2. **Comprehensive Coverage**: Include all necessary safety and validation steps
3. **User-Friendly**: Provide clear guidance and helpful error messages
4. **Maintainable**: Use consistent patterns and well-documented code

### Implementation Safety
1. **Always Use Feature Branches**: Never modify main branch directly
2. **Validate Before Acting**: Check current state before making changes
3. **Test Thoroughly**: Run comprehensive tests before completion
4. **Document Changes**: Provide clear summaries for code review

### Error Recovery
1. **Fail Fast**: Stop early when encountering unrecoverable errors
2. **Clear Messages**: Provide actionable error messages and next steps
3. **State Preservation**: Maintain context across recovery attempts
4. **Human Escalation**: Know when to ask for human intervention

## Example Agents

### Feature Flag Manager
Manages feature flags throughout the Edge codebase, including creation, modification, and removal with proper cleanup.

### Component Refactor Assistant
Helps refactor Edge components while maintaining API compatibility and ensuring all dependents continue to work.

### Test Infrastructure Helper
Assists with setting up and maintaining test infrastructure, including new test suites and CI/CD integration.

### Security Review Assistant
Helps identify and address security considerations in Edge code changes, following Chromium security guidelines.

## Extending the Framework

### Adding New Resources
1. Create resource files in `.github/resources/`
2. Update the framework template to reference new resources
3. Document usage patterns and best practices

### Custom Validation Steps
1. Define domain-specific validation requirements
2. Implement validation logic in agent templates
3. Add appropriate error handling and recovery

### Integration with External Tools
1. Identify tool integration requirements
2. Add tool setup and usage instructions
3. Include error handling for tool failures

## Troubleshooting

### Common Issues
- **Build Failures**: Ensure all dependencies are properly configured
- **Test Failures**: Verify test environment setup and prerequisites
- **Permission Issues**: Check file system and repository access rights
- **Path Problems**: Confirm working directory is Edge source root

### Getting Help
- Review existing agent examples for patterns
- Check `.github/resources/` for detailed documentation
- Consult Edge development team for domain-specific guidance
- Use Haystack search for finding similar implementations

## Version History

- **Version 1.0**: Initial framework release with core safety and accuracy features
- Future versions will include enhanced customization options and additional domain support

## Contributing

When contributing to the framework:
1. Follow established patterns and conventions
2. Include comprehensive safety measures
3. Test with multiple agent types
4. Document any new features or changes
5. Ensure backward compatibility with existing agents
