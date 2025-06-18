以下是将你提供的内容整理成一份**结构清晰、表达规范的需求文档**：

---

# Edge Agent Generator Prompt 框架调整需求文档

## 一、背景与目标

为了提升由 `edge_agent_generator.prompt.md` 生成的 Agent 在执行任务时的准确性、完整性与规范性，现需对该框架进行一系列调整与增强，确保 Agent 能够更好地理解、执行并验证 Edge 代码库相关任务，并符合代码安全性、规范性、执行可控性等各方面的要求。

---

## 二、总体调整方向

1. **增强代码构建能力**
2. **限制行为边界（如终端数量、Git 操作方式等）**
3. **严格使用 Haystack 与文件索引工具**
4. **构建流程与环境校验标准化**
5. **代码与文件的理解能力增强**
6. **生成流程加入验证闭环机制**
7. **Agent 执行计划可溯、可追、可检查**
8. **用户意图确认与反馈机制**

---

## 三、详细修改需求

### 1. 构建能力增强

* Agent 必须能够学习并使用 `../resources/edgebuild.md` 中提供的知识与构建流程，作为构建 Edge 代码的唯一依据。
* 所有构建指令必须严格遵守文档流程，不允许添加或修改命令组合。

### 2. 分支管理行为调整

* Agent 不再负责分支创建或管理，所有操作默认在当前分支执行。
* Agent 需提醒用户确保当前所处分支为正确的目标分支，并提供切换或新建分支的建议（可接受新分支名与 base 分支信息，由用户授权切换）。
* **禁止在 `main` 分支上操作**，若检测到当前为 `main` 分支，必须中止操作并提示用户切换分支。

### 3. Git 命令合并格式调整

* 禁止使用 `&&` 合并命令，统一改为使用 `;` 进行命令拼接执行。

### 4. 搜索能力限制

* **严禁使用 VSCode 的默认文件搜索与文本搜索功能**。
* 所有任务（包括验证）必须使用：

  * **Haystack search（全文检索）**
  * **文件系统索引（file search）**

### 5. Terminal 限制

* 生成的 Agent **只能使用一个 Terminal** 来执行所有命令行操作。
* **禁止创建多个 Terminal**，违反者将被视为执行失败。

### 6. 构建前环境检查规范

构建前必须进行以下环境准备检查：

* **环境是否初始化检查**：

  * 执行 `git ms format --upstream=origin/main`，若返回 “git: 'ms' is not a git command.”，说明未初始化，需执行 `initEdgeEnv.ps1` 进行初始化。

* **输出目录检查**（根据 build\_type）：

  * 执行 `cd ${Edge_Repo}/src/out/${build_type}_x64`，若返回路径不存在，则需执行 `autogn` 创建输出目录。

### 7. 构建流程增强

* 在每次完成代码修改后，必须进入 build 阶段。
* build 前需确认用户选择是 `debug` 还是 `release`，并等待输入。
* 使用 `autoninja -C out/${build_type}_x64 chrome` 或 `autoninja -C out/${build_type}_x64 mini_installer.exe` 执行编译。

### 8. 初始化脚本调整

* 初始化操作统一使用 PowerShell 脚本 `initEdgeEnv.ps1`，不再使用 CMD 脚本。

---

## 四、智能理解与任务规划能力要求

Agent 需具备如下理解与规划能力：

### 1. 文件级理解（写入 `${agent_name}_${task_name}_file_understanding_${timestamp}.md`）

* 能够识别并整理与任务相关的文件（如 `.h`, `.cc`, `.md`, `.xml`, `.json`, `.gn` 等），并分析其作用与依赖关系。
* 涵盖的模块包括：

  * Core Feature
  * WebUI
  * Settings
  * Preferences
  * Telemetry
  * Integration
  * Testing
  * Build 相关配置等

### 2. 代码级理解（写入 `${agent_name}_${task_name}_code_understanding_${timestamp}.md`）

* 能识别任务相关类、函数、常量、变量、调用关系等。
* 保证与文件级分析结果形成互补。

### 3. 任务执行计划生成（写入 `${agent_name}_${task_name}_execute_plan_${timestamp}.md`）

* 基于前两项理解，给出精确执行计划，明确每个文件的增删改细节。

### 4. 实时反馈与进度更新

* 在执行计划过程中，需实时同步进度与已完成工作项。

---

## 五、意图确认机制

生成 Agent 前，Agent 必须完成以下步骤：

1. 请求用户输入 Agent 名与描述。
2. 对描述内容进行意图解析与推理。
3. 如存在歧义、不明确或不完整，主动向用户确认。
4. 用户确认后再生成 Agent Prompt。

示例解析方式：

> 对“unship feature flag”的描述进行多种理解并给出示例后，再确认用户真实意图。

---

## 六、Agent Prompt 生成流程标准化（Checklist 驱动）

生成过程须遵循以下流程：

1. 请求并等待用户输入 Agent 名与描述。
2. 意图确认并记录。
3. **生成 Agent Validation Checklist**（写入 `/memory/agent_${agent name}_gen_validation_checklist_${timestamp}.md`）
4. 使用框架和领域知识生成 Prompt 并实时更新 Checklist。
5. 对 Prompt 做多轮 Checklist 检查与修复，直到全部项通过。

---

## 七、执行过程质量控制与自我检查

### 1. 计划项执行 Checklist 驱动

* Agent 执行执行计划时，需根据对应的执行 checklist 对每项逐一检查，修复遗漏后再循环检查直至无遗漏。

### 2. 注意事项 Checklist

* Agent 执行任务时，还需生成任务注意事项 checklist（`agent_${agent_name}_required_checks_${timestamp}.md`）
* 在执行完任务后，再对这些注意项进行反思检查，如发现遗漏或可改进项，则继续完善并重新回顾 checklist。

---

## 八、额外执行要求

* **避免混淆**：不保留已禁用功能的测试代码
* **降低维护成本**：移除无意义测试与冗余代码
* **保持代码清洁性**：彻底清除不再需要的代码、文档与文件
* **严格执行任务范围**：不引入不相关修改
* **遵循代码规范**，记录改动原因、进展与执行意图
* **如遇不确定情况，主动与同事沟通确认**

---

## 九、总结

通过上述改动，`edge_agent_generator.prompt.md` 框架将能够更智能、更安全、更有体系地生成适用于 Edge 项目的高质量 Agent，确保从理解、执行到验证的每一个环节都可控、可回溯、符合规范。

---
