# 3 Agent Skills 完全指南：从概念到集成

## 第一章：什么是 Skills？

Skills 的核心是一个包含 SKILL.md 文件的文件夹。

这个文件包含元数据（至少包括 name 和 description），以及告诉 Agent 如何执行特定任务的指令。


Skills 还可以捆绑脚本、模板和参考材料。

```
my-skill/
├── SKILL.md          # 必需：指令 + 元数据
├── scripts/          # 可选：可执行代码
├── references/       # 可选：文档资料
└── assets/           # 可选：模板、资源
```

### Skills 的工作原理

Skills 使用渐进式披露来高效管理上下文：

1. 发现阶段：启动时，Agent 仅加载每个可用 skill 的名称和描述——刚好足以知道它何时可能相关。
2. 激活阶段：当任务匹配某个 skill 的描述时，Agent 将完整的 SKILL.md 指令读入上下文。
3. 执行阶段：Agent 按照指令操作，根据需要加载引用文件或执行捆绑的代码。

这种方法让 Agent 保持快速运行，同时能够按需获取更多上下文。

```
开始
  ↓
发现阶段（仅加载Skill名称+描述）
  ↓
任务匹配判断
├─不匹配 → 常规应答 → 输出结果
└─匹配   → 激活阶段（加载完整SKILL.md）
              ↓
          执行阶段（按需加载文件/代码）
              ↓
          输出结果
```

### SKILL.md 文件

每个 skill 都以一个包含 YAML frontmatter 和 Markdown 指令的 SKILL.md 文件开始：

```
---
name: pdf-processing  

description: Extract text and tables from PDF files, fill forms, merge documents.
---
# PDF Processing

## When to use this skill

Use this skill when the user needs to work with PDF files...

## How to extract text

-  Use pdfplumber for text extraction...

## How to fill forms
...
```

SKILL.md 顶部需要以下 frontmatter：

- name：简短标识符
- description：何时使用此 skill
- frontmatter 之后的 Markdown 正文包含实际指令，对结构或内容没有特定限制。

这种简单格式有几个关键优势：

- 自文档化：skill 作者或用户可以阅读 SKILL.md 并理解它的功能，使得 skills 易于审计和改进。
- 可扩展：Skills 的复杂度可以从纯文本指令到可执行代码、资产和模板不等。
- 可移植：Skills 只是文件，因此易于编辑、版本控制和共享。


## 第二章：规范


目录结构

一个 skill 是一个至少包含 SKILL.md 文件的目录：

```
skill-name/
└── SKILL.md          
# 必需
```

你可以选择性地包含额外目录，如 scripts/、references/ 和 assets/ 来支持你的 skill。

### SKILL.md 格式

SKILL.md 文件必须包含 YAML frontmatter，后跟 Markdown 内容。

Frontmatter（必需）

```
---
name: skill-name

description: A description of what this skill does and when to use it.
---
```

带有可选字段：

```
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---
```


| 字段 | 必需 | 约束 |
|------|------|------|
| `name` | 是 | 最多 64 个字符。仅限小写字母、数字和连字符。不能以连字符开头或结尾。 |
| `description` | 是 | 最多 1024 个字符。非空。描述 skill 的功能和使用场景。 |
| `license` | 否 | 许可证名称或对捆绑许可证文件的引用。 |
| `compatibility` | 否 | 最多 500 个字符。指示环境要求（目标产品、系统包、网络访问等）。 |
| `metadata` | 否 | 用于额外元数据的任意键值映射。 |
| `allowed-tools` | 否 | 以空格分隔的预批准工具列表。（实验性功能） |

| 字段 | 类型 | 约束/说明 |
|------|------|-----------|
| `name` | 必需 | skill-name（小写+连字符，≤64字符） |
| `description` | 必需 | 功能和使用场景（≤1024字符） |
| `license` | 可选 | 许可证 |
| `compatibility` | 可选 | 环境要求 |
| `metadata` | 可选 | 额外属性 |
| `allowed-tools` | 可选 | 预批准工具 |

**Markdown 正文内容：**

1. 分步指令
2. 输入输出示例
3. 边界情况


### name 字段

必需的 name 字段：

- 必须为 1-64 个字符
- 只能包含 Unicode 小写字母数字字符和连字符（a-z 和 -）
- 不能以 - 开头或结尾
- 不能包含连续连字符（--）
- 必须与父目录名称匹配



- name:  pdf-processing

- name:   data-analysis

- name:  code-review


**无效示例：**


- name: PDF-Processing # 不允许大写


- name: -pdf # 不能以连字符开头


- name: pdf—processing # 不允许连续连字符



有效示例：

```
---
name: example-skill
description: 这是一个示例技能，用于实现[具体功能]，适用场景为[使用场景]
license: Apache-2.0
compatibility: Python 3.10+, requires network access
metadata:
  author: your-name
  version: "1.0.0"
allowed-tools: python-requests json-parser
---
````

Example Skill 说明

#### 1. 分步指令

1.  接收用户输入的[参数A]和[参数B]
2.  调用内置工具完成[核心操作]
3.  格式化结果并返回

#### 2. 输入输出示例

- **输入**: `{"paramA": "value1", "paramB": "value2"}`
- **输出**: `{"result": "processed-value", "status": "success"}`

####  3. 边界情况

- 当参数为空时，返回错误提示：`请提供必填参数`
- 当网络请求失败时，重试 2 次后返回超时错误

### description 字段

必需的 description 字段：

- 必须为 1-1024 个字符
- 应描述 skill 的功能和使用场景
- 应包含帮助 Agent 识别相关任务的特定关键词

好的示例：

```
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.
```

不好的示例：

```
description: Helps with PDFs.
```

### license 字段

可选的 license 字段：

- 指定应用于 skill 的许可证
- 建议保持简短（许可证名称或捆绑许可证文件的名称）

示例：

```
license: Proprietary. LICENSE.txt has complete terms
```

### compatibility 字段

可选的 compatibility 字段：

- 如果提供，必须为 1-500 个字符
- 仅在 skill 有特定环境要求时才应包含
- 可以指示目标产品、所需系统包、网络访问需求等

```
compatibility: Designed for Claude Code (or similar products)
```

```
compatibility: Requires git, docker, jq, and access to the internet
```

大多数 skills 不需要 compatibility 字段。

**metadata 字段**

可选的 metadata 字段：

- 从字符串键到字符串值的映射
- 客户端可以使用它存储 Agent Skills 规范未定义的额外属性
- 建议使键名合理唯一，以避免意外冲突

示例：


```
metadata:
	author: example-org
    version: "1.0"
```

### allowed-tools 字段

可选的 allowed-tools 字段：

- 以空格分隔的预批准运行工具列表
- 实验性功能。不同 Agent 实现对此字段的支持可能不同

```
allowed-tools: Bash(git:*) Bash(jq:*) Read
```

### 正文内容

frontmatter 之后的 Markdown 正文包含 skill 指令。对格式没有限制。编写任何有助于 Agent 有效执行任务的内容。

推荐的章节：

- 分步指令
- 输入和输出示例
- 常见边界情况

请注意，Agent 一旦决定激活某个 skill，就会加载整个文件。考虑将较长的 SKILL.md 内容拆分到引用文件中。

### 可选目录

#### scripts/

包含 Agent 可以运行的可执行代码。脚本应该：

- 自包含或清楚地记录依赖关系
- 包含有用的错误消息
- 优雅地处理边界情况

支持的语言取决于 Agent 实现。常见选项包括 Python、Bash 和 JavaScript


#### references/

包含 Agent 在需要时可以读取的额外文档：

- REFERENCE.md - 详细的技术参考
- FORMS.md - 表单模板或结构化数据格式
- 领域特定文件（finance.md、legal.md 等）

保持单个引用文件的聚焦性。Agent 按需加载这些文件，因此较小的文件意味着较少的上下文使用

#### assets/

包含静态资源：

- 模板（文档模板、配置模板）
- 图片（图表、示例）
- 数据文件（查找表、Schema）

### 渐进式披露

Skills 应该被构造为高效使用上下文：

- 元数据（约 100 tokens）：所有 skills 的 name 和 description 字段在启动时加载
- 指令（建议 < 5000 tokens）：完整的 SKILL.md 正文在 skill 被激活时加载
- 资源（按需）：文件（例如 scripts/、references/ 或 assets/ 中的文件）仅在需要时加载

将主 SKILL.md 保持在 500 行以下。将详细的参考材料移到单独的文件中。


### 文件引用

在 skill 中引用其他文件时，使用从 skill 根目录开始的相对路径：

```
See [ the reference guide ]( references/REFERENCE.md ) for details.

Run the extraction script:
scripts/extract.py
```

将文件引用保持在距 SKILL.md 一层深度以内。避免深度嵌套的引用链。


### 验证

使用 skills-ref[https://github.com/agentskills/agentskills/tree/main/skills-ref] 参考库来验证你的 skills：

```
skills-ref validate ./my-skill
```

这会检查你的 SKILL.md frontmatter 是否有效并遵循所有命名约定。


## 第三章：将 Skills 集成到你的 Agent 中

本指南解释了如何将 skills 支持添加到 AI Agent 或开发工具中。

### 集成方式

将 skills 集成到 Agent 中有两种主要方式：

基于文件系统的 Agent 在计算机环境（bash/unix）中运行，是最强大的选项。当模型发出 shell 命令如 cat /path/to/my-skill/SKILL.md 时，skills 被激活。捆绑的资源通过 shell 命令访问。

基于工具的 Agent 没有专用的计算机环境。它们实现工具来让模型触发 skills 并访问捆绑的资产。具体的工具实现由开发者决定。

### 概览



一个兼容 skills 的 Agent 需要：

- 发现配置目录中的 skills
- 在启动时加载元数据（名称和描述）
- 将用户任务与相关 skills 进行匹配
- 通过加载完整指令来激活 skills
- 根据需要执行脚本和访问资源

### Skill 发现

Skills 是包含 SKILL.md 文件的文件夹。你的 Agent 应该扫描配置的目录以查找有效的 skills。

### 加载元数据

在启动时，仅解析每个 SKILL.md 文件的 frontmatter。这保持了较低的初始上下文使用量。

### 解析 frontmatter

```
function parseMetadata(skillPath):
    
	content = readFile(skillPath + "/SKILL.md")
    frontmatter = extractYAMLFrontmatter(content)

    return {
        name: frontmatter.name,
        description: frontmatter.description,
        path: skillPath
    }
```

### 注入到上下文中

在系统提示中包含 skill 元数据，以便模型知道哪些 skills 可用。

遵循你的平台对系统提示更新的指导。例如，对于 Claude 模型，推荐的格式使用 XML：

```
<available_skills>
  	<skill>
    	<name>pdf-processing</name>
    	<description>Extracts text and tables from PDF files, fills forms, merges documents.</description>
    	<location>/path/to/skills/pdf-processing/SKILL.md</location>
  	</skill>
  <skill>
    <name>data-analysis</name>
    <description>Analyzes datasets, generates charts, and creates summary reports.</description>
    <location>/path/to/skills/data-analysis/SKILL.md</location>
  </skill>
</available_skills>
```

对于基于文件系统的 Agent，包含 location 字段和 SKILL.md 文件的绝对路径。对于基于工具的 Agent，可以省略 location。

保持元数据简洁。每个 skill 应该向上下文添加大约 50-100 个 tokens。

### 安全考虑

脚本执行会引入安全风险。需要考虑：

- 沙箱化：在隔离环境中运行脚本
- 白名单：仅执行来自受信任 skills 的脚本
- 确认：在运行潜在危险操作之前询问用户
- 日志记录：记录所有脚本执行以供审计

参考实现

skills-ref库提供了用于处理 skills 的 Python 工具和 CLI。

例如：

验证 skill 目录：

```
skills-ref validate <path>
```

为 Agent 提示生成 <available_skills> XML：

```
skills-ref to-prompt <path>...
```