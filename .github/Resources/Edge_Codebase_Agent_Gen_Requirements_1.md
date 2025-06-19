# 需求文档：Edge Codebase Expert Agent 的初始 Prompt 生成框架

## 背景

我们需要构建一个框架，用于自动生成 **Edge 代码库专家 Agent** 的 prompt。该 prompt 旨在指导该 Agent 协助用户修改 Edge 代码，重点关注代码修改的正确性、安全性以及遵循通用的开发规范。

## 范围

该框架应根据用户输入，生成一个新的 prompt 文件，并将其保存至 `.github/prompts` 目录中。生成的 prompt 应根据用户提供的信息进行定制，同时遵循 Edge 代码修改的最佳实践。

## 需求

### 1. 参考资料

* 框架必须**参考并提炼** `.github/prompts` 目录下所有现有的 prompt。
* 必须从这些 prompt 中**提取通用结构和风格**，形成 Edge codebase expert agent 的标准模板。

### 2. Agent 专业能力

* 生成的 prompt 应代表一个 **Edge 代码库专家（Edge codebase expert）**。
* Agent 需要：

  * 熟悉 Edge 代码库的通用**修改流程**；
  * 遵循并倡导**安全、准确**的代码修改方式；
  * 考虑修改 Edge 代码时的通用**注意事项和最佳实践**。

### 3. 用户输入

Prompt 生成框架应接收以下用户输入：

* `Agent 名称` —— 用作生成的 `.md` 文件名；
* `Agent 描述` —— 对该 Agent 作用的简要说明；
* `参考信息` —— Agent 在生成时需要考虑的额外上下文或目标信息。

### 4. 输出要求

* 框架应生成一个 markdown 文件，内容为该 Agent 的 prompt；
* 生成的文件需满足以下要求：

  * 保存路径为 `.github/prompts` 目录；
  * 文件名必须与用户输入的 `Agent 名称` 完全一致（例如：`my_edge_fix_agent.md`）；
  * 内容格式需统一规范，符合 GPT Agent 初始化使用的风格和结构。

### 5. Prompt 内容准则

生成的 prompt 应包含以下内容：

* 明确描述该 Agent 的角色：Edge 代码库专家；
* 说明其职责是引导用户进行**安全且准确**的代码修改；
* 明确该 Agent 遵循的开发规范和 Edge 项目的代码修改流程；
* 结合用户提供的额外参考信息，定制 prompt 内容。



