# Microsoft Edge Source Code Understanding Guide

This document provides a comprehensive guide for AI agents and developers to understand and work with the Microsoft Edge source code repository. Edge is built on top of the Chromium project with Microsoft-specific enhancements and features.

## Table of Contents

1. [Repository Architecture](#repository-architecture)
2. [Directory Structure](#directory-structure)
3. [Edge-Specific Features Organization](#edge-specific-features-organization)
4. [Complete Feature Development Guide](#complete-feature-development-guide)
5. [Build System](#build-system)
6. [Testing Framework](#testing-framework)
7. [Internationalization (i18n)](#internationalization-i18n)
8. [Telemetry and Metrics](#telemetry-and-metrics)
9. [Feature Flags](#feature-flags)
10. [Platform-Specific Development](#platform-specific-development)
11. [Code Quality and Standards](#code-quality-and-standards)
12. [Chromium Upstream Relationship](#chromium-upstream-relationship)

## Repository Architecture

Microsoft Edge is based on the Chromium project with extensive Microsoft-specific customizations. The codebase follows Chromium's multi-process architecture with additional Edge-specific components.

### Key Principles
- **Layered Architecture**: Content layer, Chrome layer, Platform layer
- **Multi-Process**: Browser process, Renderer processes, GPU process, etc.
- **Component-Based**: Reusable components shared across different parts
- **Platform Abstraction**: Cross-platform support with platform-specific implementations

## Directory Structure

### Core Directories

```
src/
├── base/              # Foundation library (strings, files, threading, etc.)
├── build/             # Build configuration and tools
├── chrome/            # Main browser application code
│   ├── browser/       # Browser process code
│   ├── renderer/      # Renderer process code
│   ├── common/        # Shared code between processes
│   └── app/           # Application entry points
├── components/        # Reusable components (200+ components)
├── content/           # Content API layer
├── ui/                # User interface framework
├── net/               # Network stack
├── services/          # Mojo services
├── third_party/       # External dependencies
└── tools/             # Development and build tools
```

### Edge-Specific Directories

```
├── chrome/browser/edge_*/     # Browser-layer Edge features
├── components/edge_*/         # Reusable Edge components
├── edge_*/                    # Top-level Edge-specific modules
│   ├── edge_dlp/             # Data Loss Prevention
│   ├── edge_embedded_browser/ # Embedded browser functionality
│   ├── edge_pdf/             # PDF handling
│   ├── edge_pwahelper/       # PWA support
│   ├── edge_sync/            # Edge-specific sync
│   └── edge_webui/           # Edge WebUI components
└── microsoft_apis/            # Microsoft service integrations
```

## Edge-Specific Features Organization

### Naming Conventions
- **Directories**: `edge_feature_name/` (e.g., `edge_drop/`, `edge_wallet/`)
- **Namespaces**: `edge::feature_name` (e.g., `edge::drop`)
- **Feature Flags**: `kEdgeFeatureName` (e.g., `kEdgeDropEnabled`)
- **Classes**: `EdgeFeatureNameService` (e.g., `EdgeDropService`)

### Component Distribution
- **Browser Layer**: `chrome/browser/edge_*` - Browser process functionality
- **Components**: `components/edge_*` - Reusable, testable components
- **Content Integration**: Integration with Chromium's content layer
- **UI Layer**: WebUI and native UI implementations

## Complete Feature Development Guide

Let's walk through developing a complete Edge feature using "EDrop" (a hypothetical file sharing feature) as an example.

### Step 1: Planning and Architecture

```cpp
// Define the feature scope and architecture
namespace edge::drop {
  // Core service for file sharing functionality
  class EdgeDropService;
  
  // UI controller for drop interface
  class EdgeDropUIController;
  
  // Protocol handler for drop:// URLs
  class EdgeDropProtocolHandler;
}
```

### Step 2: Directory Structure Creation

```
components/edge_drop/
├── BUILD.gn                    # Build configuration
├── DEPS                        # Dependency declarations  
├── README.md                   # Component documentation
├── browser/                    # Browser process code
│   ├── edge_drop_service.cc
│   ├── edge_drop_service.h
│   └── edge_drop_manager.cc
├── common/                     # Shared code
│   ├── edge_drop_constants.cc
│   ├── edge_drop_constants.h
│   └── edge_drop_features.cc
├── public/                     # Public interfaces
│   └── edge_drop_service.h
├── resources/                  # UI resources
│   ├── edge_drop.html
│   ├── edge_drop.css
│   └── edge_drop.js
└── strings/                    # Internationalization
    ├── edge_drop_strings.grd
    └── translations/
```

### Step 3: Build Configuration (BUILD.gn)

```gn
# components/edge_drop/BUILD.gn
import("//build/config/chrome_build.gni")

if (is_msedge_branded) {
  component("edge_drop") {
    sources = [
      "browser/edge_drop_service.cc",
      "browser/edge_drop_service.h",
      "browser/edge_drop_manager.cc",
      "browser/edge_drop_manager.h",
      "common/edge_drop_constants.cc",
      "common/edge_drop_constants.h",
      "common/edge_drop_features.cc",
      "common/edge_drop_features.h",
    ]
    
    public_deps = [
      "//base",
      "//components/keyed_service/core",
      "//content/public/browser",
      "//services/network/public/cpp",
    ]
    
    deps = [
      "//chrome/browser/profiles:profile",
      "//components/prefs",
      "//net",
      "//url",
    ]
  }

  source_set("unit_tests") {
    testonly = true
    sources = [
      "browser/edge_drop_service_unittest.cc",
      "browser/edge_drop_manager_unittest.cc",
    ]
    
    deps = [
      ":edge_drop",
      "//base/test:test_support",
      "//content/test:test_support",
      "//testing/gtest",
    ]
  }
}
```

### Step 4: Feature Flags Implementation

```cpp
// components/edge_drop/common/edge_drop_features.h
#ifndef COMPONENTS_EDGE_DROP_COMMON_EDGE_DROP_FEATURES_H_
#define COMPONENTS_EDGE_DROP_COMMON_EDGE_DROP_FEATURES_H_

#include "base/feature_list.h"

namespace edge::drop::features {

// Enable Edge Drop file sharing functionality
BASE_DECLARE_FEATURE(kEdgeDropEnabled);
bool IsEdgeDropEnabled();

// Enable Edge Drop protocol handler (drop://)
BASE_DECLARE_FEATURE(kEdgeDropProtocolHandler);
bool IsEdgeDropProtocolHandlerEnabled();

// Enable Edge Drop UI in browser
BASE_DECLARE_FEATURE(kEdgeDropUI);
bool IsEdgeDropUIEnabled();

// Feature trigger for drop sharing events
BASE_DECLARE_FEATURE_TRIGGER(kEdgeDropShareTrigger);

}  // namespace edge::drop::features

#endif  // COMPONENTS_EDGE_DROP_COMMON_EDGE_DROP_FEATURES_H_
```

```cpp
// components/edge_drop/common/edge_drop_features.cc
#include "components/edge_drop/common/edge_drop_features.h"

namespace edge::drop::features {

BASE_FEATURE(kEdgeDropEnabled,
             "EdgeDropEnabled",
             base::FEATURE_DISABLED_BY_DEFAULT);

bool IsEdgeDropEnabled() {
  return base::FeatureList::IsEnabled(kEdgeDropEnabled);
}

BASE_FEATURE(kEdgeDropProtocolHandler,
             "EdgeDropProtocolHandler", 
             base::FEATURE_DISABLED_BY_DEFAULT);

bool IsEdgeDropProtocolHandlerEnabled() {
  return base::FeatureList::IsEnabled(kEdgeDropProtocolHandler);
}

BASE_FEATURE(kEdgeDropUI,
             "EdgeDropUI",
             base::FEATURE_DISABLED_BY_DEFAULT);

bool IsEdgeDropUIEnabled() {
  return base::FeatureList::IsEnabled(kEdgeDropUI);
}

BASE_FEATURE_TRIGGER(kEdgeDropShareTrigger, "EdgeDropShareTrigger");

}  // namespace edge::drop::features
```

### Step 5: Core Service Implementation

```cpp
// components/edge_drop/browser/edge_drop_service.h
#ifndef COMPONENTS_EDGE_DROP_BROWSER_EDGE_DROP_SERVICE_H_
#define COMPONENTS_EDGE_DROP_BROWSER_EDGE_DROP_SERVICE_H_

#include <memory>
#include <string>
#include <vector>

#include "base/memory/weak_ptr.h"
#include "components/keyed_service/core/keyed_service.h"
#include "third_party/abseil-cpp/absl/types/optional.h"

class Profile;

namespace edge::drop {

struct DropFile {
  std::string name;
  std::string path;
  int64_t size;
  std::string mime_type;
};

class EdgeDropService : public KeyedService {
 public:
  explicit EdgeDropService(Profile* profile);
  ~EdgeDropService() override;

  // KeyedService implementation
  void Shutdown() override;

  // Share files via Edge Drop
  void ShareFiles(const std::vector<DropFile>& files,
                 base::OnceCallback<void(bool success)> callback);

  // Receive shared files
  void ReceiveFiles(const std::string& share_id,
                   base::OnceCallback<void(std::vector<DropFile>)> callback);

  // Check if drop sharing is available
  bool IsDropSharingAvailable() const;

 private:
  void OnShareFilesComplete(base::OnceCallback<void(bool)> callback,
                           bool success);
  
  raw_ptr<Profile> profile_;
  base::WeakPtrFactory<EdgeDropService> weak_factory_{this};
};

}  // namespace edge::drop

#endif  // COMPONENTS_EDGE_DROP_BROWSER_EDGE_DROP_SERVICE_H_
```

### Step 6: Unit Testing

```cpp
// components/edge_drop/browser/edge_drop_service_unittest.cc
#include "components/edge_drop/browser/edge_drop_service.h"

#include "base/test/scoped_feature_list.h"
#include "components/edge_drop/common/edge_drop_features.h"
#include "content/public/test/browser_task_environment.h"
#include "testing/gtest/include/gtest/gtest.h"

namespace edge::drop {

class EdgeDropServiceTest : public testing::Test {
 public:
  void SetUp() override {
    scoped_feature_list_.InitWithFeatures(
        {features::kEdgeDropEnabled, features::kEdgeDropUI}, {});
  }

 protected:
  content::BrowserTaskEnvironment task_environment_;
  base::test::ScopedFeatureList scoped_feature_list_;
};

TEST_F(EdgeDropServiceTest, ServiceInitialization) {
  // Test service can be created and initialized
  auto service = std::make_unique<EdgeDropService>(nullptr);
  EXPECT_TRUE(service);
}

TEST_F(EdgeDropServiceTest, DropSharingAvailability) {
  auto service = std::make_unique<EdgeDropService>(nullptr);
  
  // Should be available when feature is enabled
  EXPECT_TRUE(service->IsDropSharingAvailable());
}

TEST_F(EdgeDropServiceTest, ShareFiles) {
  auto service = std::make_unique<EdgeDropService>(nullptr);
  
  std::vector<DropFile> files = {
    {"test.txt", "/path/to/test.txt", 1024, "text/plain"}
  };
  
  bool callback_called = false;
  service->ShareFiles(files, base::BindOnce([](bool* called, bool success) {
    *called = true;
    EXPECT_TRUE(success);
  }, &callback_called));
  
  // In real implementation, this would be async
  EXPECT_TRUE(callback_called);
}

}  // namespace edge::drop
```

### Step 7: Internationalization

```xml
<!-- components/edge_drop/strings/edge_drop_strings.grd -->
<?xml version="1.0" encoding="UTF-8"?>
<grit latest_public_release="0" current_release="1">
  <outputs>
    <output filename="grit/edge_drop_strings.h" type="rc_header">
      <emit emit_type='prepend'></emit>
    </output>
    <output filename="edge_drop_strings_am.pak" type="data_package" lang="am" />
    <output filename="edge_drop_strings_en-US.pak" type="data_package" lang="en" />
    <!-- Add more languages as needed -->
  </outputs>
  
  <translations>
    <file path="translations/edge_drop_strings_am.xtb" lang="am" />
    <file path="translations/edge_drop_strings_en-US.xtb" lang="en" />
  </translations>
  
  <release seq="1">
    <messages>
      <message name="IDS_EDGE_DROP_TITLE" desc="Title for Edge Drop feature">
        Edge Drop
      </message>
      <message name="IDS_EDGE_DROP_SHARE_FILES" desc="Button text to share files">
        Share Files
      </message>
      <message name="IDS_EDGE_DROP_RECEIVE_FILES" desc="Button text to receive files">
        Receive Files  
      </message>
      <message name="IDS_EDGE_DROP_SHARING_SUCCESS" desc="Message shown when sharing succeeds">
        Files shared successfully
      </message>
      <message name="IDS_EDGE_DROP_SHARING_ERROR" desc="Message shown when sharing fails">
        Failed to share files. Please try again.
      </message>
    </messages>
  </release>
</grit>
```

### Step 8: WebUI Implementation

```html
<!-- components/edge_drop/resources/edge_drop.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Edge Drop</title>
  <link rel="stylesheet" href="edge_drop.css">
</head>
<body>
  <div id="edge-drop-container">
    <h1 id="drop-title">$i18n{edgeDropTitle}</h1>
    
    <div class="drop-section">
      <h2>$i18n{shareFiles}</h2>
      <div id="file-drop-zone" class="drop-zone">
        <p>Drop files here or click to select</p>
        <input type="file" id="file-input" multiple style="display: none;">
      </div>
      <button id="share-btn" class="primary-button">$i18n{shareFiles}</button>
    </div>
    
    <div class="drop-section">
      <h2>$i18n{receiveFiles}</h2>
      <input type="text" id="share-code" placeholder="Enter share code">
      <button id="receive-btn" class="primary-button">$i18n{receiveFiles}</button>
    </div>
    
    <div id="status-message" class="status hidden"></div>
  </div>
  
  <script src="edge_drop.js"></script>
</body>
</html>
```

### Step 9: Telemetry and Metrics

```cpp
// components/edge_drop/browser/edge_drop_metrics.h
#ifndef COMPONENTS_EDGE_DROP_BROWSER_EDGE_DROP_METRICS_H_
#define COMPONENTS_EDGE_DROP_BROWSER_EDGE_DROP_METRICS_H_

namespace edge::drop::metrics {

// Histogram names
extern const char kEdgeDropShareAttempts[];
extern const char kEdgeDropShareSuccess[];
extern const char kEdgeDropFileCount[];
extern const char kEdgeDropFileSizeBytes[];

// UMA enums
enum class DropShareResult {
  kSuccess = 0,
  kNetworkError = 1,
  kAuthenticationError = 2,
  kFileTooLarge = 3,
  kUnsupportedFileType = 4,
  kMaxValue = kUnsupportedFileType,
};

// Record metrics
void RecordDropShareAttempt();
void RecordDropShareResult(DropShareResult result);
void RecordDropFileCount(int count);
void RecordDropFileSize(int64_t size_bytes);

}  // namespace edge::drop::metrics

#endif  // COMPONENTS_EDGE_DROP_BROWSER_EDGE_DROP_METRICS_H_
```

### Step 10: Integration with Browser

```cpp
// chrome/browser/edge_drop/edge_drop_factory.h
#ifndef CHROME_BROWSER_EDGE_DROP_EDGE_DROP_FACTORY_H_
#define CHROME_BROWSER_EDGE_DROP_EDGE_DROP_FACTORY_H_

#include "base/no_destructor.h"
#include "components/keyed_service/content/browser_context_keyed_service_factory.h"

namespace edge::drop {
class EdgeDropService;
}

class EdgeDropFactory : public BrowserContextKeyedServiceFactory {
 public:
  static EdgeDropFactory* GetInstance();
  static edge::drop::EdgeDropService* GetForProfile(Profile* profile);

 private:
  friend class base::NoDestructor<EdgeDropFactory>;

  EdgeDropFactory();
  ~EdgeDropFactory() override;

  // BrowserContextKeyedServiceFactory:
  std::unique_ptr<KeyedService> BuildServiceInstanceForBrowserContext(
      content::BrowserContext* context) const override;
  bool ServiceIsCreatedWithBrowserContext() const override;
};

#endif  // CHROME_BROWSER_EDGE_DROP_EDGE_DROP_FACTORY_H_
```

## Build System

Edge uses GN (Generate Ninja) as its meta-build system, inherited from Chromium.

### Key Build Files
- **BUILD.gn**: Build configuration for each directory
- **DEPS**: Dependency declarations and allowed includes
- **.gni files**: Shared build logic and templates
- **args.gn**: Build arguments configuration

### Common Build Patterns

```gn
# Component target
component("my_component") {
  sources = [ "file.cc", "file.h" ]
  public_deps = [ "//base" ]
  deps = [ "//content/public/browser" ]
}

# Test target  
source_set("unit_tests") {
  testonly = true
  sources = [ "test.cc" ]
  deps = [ ":my_component", "//testing/gtest" ]
}

# Conditional compilation
if (is_msedge_branded) {
  # Edge-specific code
}
```

## Testing Framework

Edge uses multiple testing frameworks:

### Unit Tests (GTest)
```cpp
class MyFeatureTest : public testing::Test {
 public:
  void SetUp() override {
    feature_list_.InitWithFeatures({kMyFeature}, {});
  }

 protected:
  base::test::ScopedFeatureList feature_list_;
};

TEST_F(MyFeatureTest, BasicFunctionality) {
  EXPECT_TRUE(IsMyFeatureEnabled());
}
```

### Browser Tests
```cpp
class MyFeatureBrowserTest : public InProcessBrowserTest {
 public:
  void SetUpOnMainThread() override {
    // Setup browser environment
  }
};

IN_PROC_BROWSER_TEST_F(MyFeatureBrowserTest, UserInteraction) {
  // Test user interactions
}
```

### Integration Tests
- End-to-end testing with real browser instances
- Cross-platform compatibility testing
- Performance regression testing

## Internationalization (i18n)

### String Resources
1. Define strings in `.grd` files
2. Use `$i18n{stringId}` in HTML templates
3. Use `l10n_util::GetStringUTF8()` in C++ code

### Localization Process
1. String extraction from source code
2. Translation by localization teams
3. Integration back into build system
4. Pseudo-localization testing

## Telemetry and Metrics

### UMA Histograms
```cpp
// Record user actions
base::UmaHistogramCounts100("Edge.MyFeature.UsageCount", count);

// Record timing
base::UmaHistogramTimes("Edge.MyFeature.LoadTime", duration);

// Record enums
base::UmaHistogramEnumeration("Edge.MyFeature.Result", result);
```

### UKM (User Keyed Metrics)
```cpp
ukm::SourceId source_id = ukm::GetSourceIdForWebContentsDocument(web_contents);
ukm::builders::Edge_MyFeature_Event(source_id)
    .SetActionType(static_cast<int64_t>(action))
    .Record(ukm::UkmRecorder::Get());
```

## Feature Flags

### Declaration
```cpp
BASE_DECLARE_FEATURE(kMyFeature);
```

### Definition  
```cpp
BASE_FEATURE(kMyFeature, "MyFeature", base::FEATURE_DISABLED_BY_DEFAULT);
```

### Usage
```cpp
if (base::FeatureList::IsEnabled(kMyFeature)) {
  // Feature-gated code
}
```

### Field Trials
- A/B testing framework
- Gradual rollout capability
- Remote configuration

## Platform-Specific Development

### Windows
```cpp
#if BUILDFLAG(IS_WIN)
  // Windows-specific code
  #include <windows.h>
#endif
```

### macOS
```cpp
#if BUILDFLAG(IS_MAC)
  // macOS-specific code
  #include <Cocoa/Cocoa.h>
#endif
```

### Cross-Platform Abstractions
- Use `base/` library for common operations
- Platform-specific implementations in separate files
- Conditional compilation with build flags

## Code Quality and Standards

### Style Guidelines
- Follow Chromium C++ style guide
- Use `clang-format` for consistent formatting
- Prefer composition over inheritance
- Use smart pointers for memory management

### Pre-submit Checks
- **PRESUBMIT.py**: Custom validation scripts
- **Linting**: Static analysis tools
- **Testing**: Automated test execution
- **Security Review**: For security-sensitive changes

### Code Review Process
1. Create change list (CL)
2. Run pre-submit checks
3. Get code review approval
4. Submit to repository

## Chromium Upstream Relationship

### Merge Strategy
- Regular merges from Chromium upstream
- Edge-specific changes preserved during merges
- Conflict resolution processes

### Contribution Guidelines
- Bug fixes contributed back to upstream when appropriate
- Edge-specific features kept separate
- Participation in Chromium community discussions

## Best Practices for AI Agents

### Code Analysis
1. **Start with Documentation**: Read README.md and design docs
2. **Understand Dependencies**: Check DEPS files and BUILD.gn
3. **Follow Examples**: Look for similar existing features
4. **Test Early**: Write tests alongside implementation

### Making Changes
1. **Small Increments**: Make small, focused changes
2. **Feature Flags**: Gate new features behind flags
3. **Cross-Platform**: Consider all supported platforms
4. **Performance**: Monitor impact on browser performance

### Common Pitfalls
- Don't modify Chromium core without understanding upstream impact
- Don't skip testing - both unit and integration tests
- Don't ignore build errors in other configurations
- Don't forget internationalization for user-facing strings

## Debugging and Development Tools

### Internal Pages
- `edge://version/` - Version and build information
- `edge://flags/` - Feature flag configuration  
- `edge://components/` - Component information
- `edge://net-internals/` - Network debugging

### Development Flags
```
--enable-logging=stderr
--log-level=0
--enable-features=EdgeMyFeature
--disable-features=SomeOtherFeature
```

### Debugging Tools
- **GDB/LLDB**: Native debugging
- **DevTools**: Web debugging
- **Tracing**: Performance analysis
- **Crash Dumps**: Post-mortem debugging

## Conclusion

This guide provides a comprehensive foundation for understanding and working with the Microsoft Edge source code. The key to successful development is:

1. Understanding the layered architecture
2. Following established patterns and conventions
3. Leveraging the robust build and test infrastructure
4. Maintaining compatibility with Chromium upstream
5. Considering cross-platform implications

For specific questions or advanced scenarios, refer to the documentation in the `docs/` directory or consult with the Edge development team.

---

*Last Updated: June 2025*
*Document Version: 1.0*
