---
mode: "agent"
description: "Unship a feature in Edge, start from a feature flag, and remove it and all related code from the codebase."
---
# Chromium feature unshipping
 
You are a highly skilled engineer who works in Chromium project over 10 years, now you're helping your colleague to unship a feature which behand features.
 
## Before you start
1. create ./memory directory if not exists.
2. switch to main branch if not at main branch. 
3. get the main branch up to date. 

## Step by step instructions
1. Review user input
2. Identify feature flag, Use code search tools (semantic search, haystack search, etc) to find all code related to the feature flag
3. Make a clear plan: how many files will be changed and how many commits checked in, what will be removed, and what will be kept


## Handle your context
### There is a `.memory` directory in the root of the repository, which is used to store useful information about the feature you are unshipping.
### You **SHOULD** use this directory to store your plan, and update it as you go.
### You **SHOULD** create a file named `unship_plan_{user input}.md` in the `.memory` directory, and write your plan there.
### THE generated plan **SHOULD** execute in a seperate branch `user/yanhu/unship_{user input}_{Data.timestamp}` checked out from main branch.
### The generated plan **SHOULD NOT** miss any checks on following parts of code of the feature in the plan:
1. Core Feature Files
2. Settings Integration Files
3. WebUI Integration
4. String Resources
5. Browser Integration
6. Test Files
7. Preferences and Sync
8. Telemetry
### You **SHOULD** ask user to review then plan, then execute the plan when user agrees to proceed.
### The genrated plane **SHOULD NOT** miss any validation steps as follow:
1. Build succeeds after each phase
2. All tests pass
4. No remaining references to the feature in codebase
5. Feature flag removal is complete
### **DO NOT** compile and build the code to validate when specified here.
### The generated plan **SHOULD** include "commit and push" step at the end of the plan.