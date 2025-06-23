# How to Setup Edge Build Environment & Build

This guide provides step-by-step instructions for setting up the Microsoft Edge build environment and building Edge from source.

## Prerequisites

- Windows development machine
- Git for Windows
- Visual Studio with C++ development tools
- Sufficient disk space (100+ GB recommended)

## Setup Build Environment

### 1. Initialize Edge Build Environment

First, you need to initialize the Edge build environment using the provided setup script:

```powershell
${Edge_Repo}\depot_tools\scripts\setup\initEdgeEnv.cmd ${Edge_Repo}
```

Where:
- **`${Edge_Repo}`** - Edge repository root folder on your local machine (e.g., `E:\Edge`)
- **`${Edge_Repo}\src`** - Edge source code folder where all build commands should be executed

> **Important**: All subsequent commands (`gclient sync`, `autogn`, `autoninja`, `git ms format`) must be run from the `${Edge_Repo}\src` directory.

## Build Process

### 2. Update Dependencies

Keep your dependencies up-to-date by syncing with the latest sources:

```powershell
gclient sync [-D]
```

**When to run `gclient sync`:**
- After `git pull`, `git rebase`, or `git checkout` operations
- When DEPS files have changed
- To ensure all dependencies are current

> **Note**: If your changes are small and no DEPS files changed, `gclient sync` may be a no-op and not necessary.

### 3. Generate Build Configuration

Generate the appropriate build configuration based on your target:

#### Debug Build (x64)
```powershell
autogn x64 debug
```
- Creates component build for x64 with debug symbols
- Generates build folder: `${Edge_Repo}/src/out/debug_x64`
- Only run if the output directory doesn't exist

#### Release Build (x64)
```powershell
autogn x64 release
```
- Creates local release build for x64 with release symbols
- Generates build folder: `${Edge_Repo}/src/out/release_x64`
- Only run if the output directory doesn't exist

### 4. Build Edge

#### Build Debug Version
```powershell
# Build Edge browser (debug)
autoninja -C out\debug_x64 chrome

# Build mini installer (debug)
autoninja -C out\debug_x64 mini_installer
```

#### Build Release Version
```powershell
# Build Edge browser (release)
autoninja -C out\release_x64 chrome

# Build mini installer (release)
autoninja -C out\release_x64 mini_installer
```

## Code Formatting

Before committing your changes, format the code using:

```powershell
git ms format --upstream=origin/main
```

This ensures your code follows the project's formatting standards before adding and committing changes.

## Build Targets Summary

| Target | Debug Command | Release Command | Output |
|--------|---------------|-----------------|--------|
| Edge Browser | `autoninja -C out\debug_x64 chrome` | `autoninja -C out\release_x64 chrome` | Edge executable |
| Mini Installer | `autoninja -C out\debug_x64 mini_installer` | `autoninja -C out\release_x64 mini_installer` | `mini_installer.exe` |

## Directory Structure

```
${Edge_Repo}/
├── depot_tools/
│   └── scripts/setup/initEdgeEnv.cmd
└── src/
    ├── out/
    │   ├── debug_x64/    # Debug build output
    │   └── release_x64/  # Release build output
    └── ... (source files)
```

## Troubleshooting

- **Build Errors**: If you encounter compile errors, fix them iteratively and rebuild
- **Dependency Issues**: Run `gclient sync` to ensure all dependencies are current
- **Disk Space**: Ensure sufficient disk space for build outputs
- **Environment**: Make sure you're running commands from the `${Edge_Repo}\src` directory

## Quick Reference

1. Initialize: `${Edge_Repo}\depot_tools\scripts\setup\initEdgeEnv.cmd ${Edge_Repo}`
2. Navigate: `cd ${Edge_Repo}\src`
3. Sync: `gclient sync`
4. Configure: `autogn x64 debug` or `autogn x64 release`
5. Build: `autoninja -C out\debug_x64 chrome` or `autoninja -C out\release_x64 chrome`
6. Format: `git ms format --upstream=origin/main`
