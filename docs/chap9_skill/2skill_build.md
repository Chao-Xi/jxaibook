# 1 Claude Skills 从使用到创建

## 1 Claude Skills 完全指南：从使用到创建

**Skills 就是为了解决这个问题而生的。**


它是一种让 AI 从"通用助手"变成"领域专家"的扩展机制——你只需要教 Claude 一次，以后它就记住了你的最佳实践。无论你是想使用现成的 Skills，还是打算创建自己的专属 Skill，这篇文章都能帮到你。

### 2 目录


1. 背景：为什么需要 Skills
2. 核心概念：Skills 的组成结构
3. 环境准备：安装 openskills CLI
4. 使用 Skills：安装、启用与管理
5. 创建 Skills：从 0 到 1 的完整流程
6. 实战演示：创建「深度研究报告」Skill
7. 最佳实践：写出高质量的 Skill
8. 故障排除

## 1. 背景：为什么需要 Skills

> Claude 很聪明，但缺少"你的方法论"

Claude 能写代码、改文档、做分析，这些它都很擅长。但它不知道你是怎么做事的——你团队的规范、你偏好的工具、你积累的最佳实践。

举个真实的例子

```
你让 Claude 帮你生成一份 PDF 报告，它可能会：

• 第一次：用 reportlab 库写了一堆代码
• 第二次：换成 fpdf，API 完全不一样
• 第三次：又换回 reportlab，但参数写错了
每次都在"重新发明轮子"，效果时好时坏。
```

问题不在于 Claude 不会写代码，**而是它没有被告知你的最佳实践**。比如你团队统一用 weasyprint，或者你有一套固定的报告模板——这些"程序性知识"Claude 并不知道。

### Skills：AI 的"入职培训手册"

Skills 就是解决这个问题的。

你可以把 Skills 理解成给 Claude 的"入职培训手册"。新员工入职时会拿到一堆文档：公司规范、开发流程、常用工具……Skills 做的是同样的事，只不过对象是 AI。


| 场景/用途         | 关联资源/配置信息             |
| ----------------- | ---------------------------- |
| 新员工入职        | Claude + Skills              |
| 公司代码规范      | `references/coding-style.md` |
| 常用脚本模板      | `scripts/generate_report.py` |
| 品牌素材          | `assets/logo.png`            |
| 工作流程说明      | `SKILL.md`（主文件）         |

有了 Skills，Claude 就从一个"什么都能干但什么都不精"的通才，变成了"这个领域我很熟"的专家。

> Skills vs Prompt vs Custom Instructions

你可能会问：我直接写个详细的 Prompt 不行吗？或者用 Custom Instructions？

当然可以，但 Skills 解决的是不同层面的问题：

| 特性       | 普通 Prompt       | Custom Instructions | Skills                    |
| ---------- | ----------------- | ------------------- | ------------------------- |
| 复用性     | ❌ 一次性         | ✅ 会话级           | ✅ 永久可复用             |
| 携带文件   | ❌ 纯文本         | ❌ 纯文本           | ✅ 脚本/模板/资料         |
| 按需加载   | ❌ 全量塞入       | ❌ 全量塞入         | ✅ 渐进式披露             |
| 分享给他人 | ❌ 复制粘贴       | ❌ 手动配置         | ✅ 一键安装               |
| 版本管理   | ❌ 无             | ❌ 无               | ✅ Git 管理               |

核心区别：Prompt 是一次性的指令，而 Skills 是模块化、可复用、可分享的知识包。

### 什么时候该用 Skills？

不是所有任务都需要 Skills。简单问题用简单办法就好。

✅ 适合用 Skills 的场景：

* 重复性任务 —— 同样的工作每次都要重新解释
* 多步骤流程 —— 需要固定的执行顺序
* 特定输出格式 —— PDF、DOCX、PPT 等文件生成
* 团队协作 —— 希望统一大家使用 Claude 的方式
* 领域专业知识 —— 需要特定的 schema、API、业务逻辑

❌ 不需要 Skills 的场景：

* 简单问答 —— "Python 怎么读取 JSON？"
* 一次性任务 —— 只做一次，以后不会再用
* 快速查询 —— 查个资料、翻译一句话

### 支持的平台

Skills 目前支持两个主要平台：

| 平台 | 说明 |
| ---- | ---- |
| Claude Code | 终端/IDE 中的 Claude，支持完整的文件操作和脚本执行 |
| Claude.ai | Web 界面，通过 Connectors 可以访问部分 Skills 功能 |

两者的核心概念是一样的，只是执行环境略有差异。本文会同时覆盖这两个平台。

Skills 生态
目前 Skills 的来源有两个：

1. Anthropic 官方 Marketplace —— 官方维护的高质量 Skills
2. 社区开源 —— GitHub 上的第三方 Skills

通过 openskills 这个 CLI 工具，你可以方便地安装、管理这些 Skills。

## 2. 核心概念：Skills 的组成结构

### 2-1 Skill 的目录结构

每个 Skill 本质上就是一个文件夹，包含以下内容：

```
skill-name/
├── SKILL.md          # 必需：主文件，包含元信息和指令
├── scripts/          # 可选：可执行脚本（Python/Bash 等）
├── references/       # 可选：参考文档（按需加载）
└── assets/           # 可选：输出素材（模板/图片/字体等）
```

结构看着简单，但每个部分都有明确的分工。

### 2-2 SKILL.md：Skill 的灵魂

SKILL.md 是每个 Skill 必须有的文件，由两部分组成：

**1. YAML Frontmatter（元信息）**

```
---
name: deep-research
description: 生成结构化的深度研究报告。支持多来源信息整合、
  自动生成大纲、分章节撰写。当用户需要研究某个主题、
  撰写调研报告、或进行竞品分析时使用此 Skill。
---
```

这里有两个字段：

| 字段 | 作用 | 重要程度 |
| ---- | ---- | -------- |
| `name` | Skill 的唯一标识 | ⭐⭐⭐ |
| `description` | 触发条件，决定何时启用此 Skill | ⭐⭐⭐⭐⭐ |


### 2-2. Markdown Body（指令正文）

```
# Deep Research Skill

## 工作流程
1. 确认研究主题和范围
2. 生成研究大纲
3. 分章节收集资料
4. 整合撰写报告
5. 生成参考文献

## 输出格式
使用 scripts/generate_report.py 生成最终 PDF...
```

正文部分是给 Claude 看的"操作手册"，告诉它具体怎么执行任务。

**scripts/：可复用的脚本**

这个目录放的是可执行代码，适合那些：

*  每次都要重写的代码 —— 比如 PDF 生成、图片处理
* 需要确定性结果的操作 —— 不能让 AI 每次写不一样的代码
* 复杂的技术操作 —— 比如调用特定 API

```
scripts/
├── generate_report.py    # 生成 PDF 报告
├── fetch_data.py         # 获取外部数据
└── validate_output.sh    # 校验输出格式
```

优点：脚本可以直接执行，不需要加载到上下文窗口，省 token 又稳定。

**references/：参考文档**

这个目录放的是 Claude 可能需要参考的文档资料：

```
references/
├── report_template.md    # 报告模板
├── style_guide.md        # 写作风格指南
└── api_docs.md           # API 文档
```

重点：references 里的文件不会一开始就加载，而是 Claude 按需读取。这就是"渐进式披露"的设计理念——需要的时候再加载，不占用宝贵的上下文空间。

**assets/：输出素材**


这个目录放的是最终输出会用到的素材：

```
assets/
├── logo.png              # 品牌 Logo
├── template.docx         # Word 模板
├── fonts/                # 自定义字体
└── cover_template.html   # 封面模板
```

这些文件不会被读取到上下文里，而是在生成最终产物时直接使用。

```
┌─────────────────────────────────────────────────┐
│  第 1 层：元信息（始终在上下文中）                │
│  name + description，约 100 词                  │
├─────────────────────────────────────────────────┤
│  第 2 层：SKILL.md 正文（触发后加载）             │
│  建议控制在 500 行以内                          │
├─────────────────────────────────────────────────┤
│  第 3 层：bundled resources（按需加载）          │
│  scripts/、references/、assets/                │
│  无上限，因为脚本可以直接执行不占上下文           │
└─────────────────────────────────────────────────┘
```

**为什么这么设计？**

上下文窗口是稀缺资源。如果把所有信息一股脑塞进去，不仅浪费 token，还可能"淹没"真正重要的信息。渐进式披露让 Claude 先看到概要，需要细节时再深入——就像人类读文档一样。


> 💡 提示：`description` 是决定 Skill 能否被正确触发的关键，描述要清晰、具体，便于 Claude 判断何时启用。

Skills 组件结构与加载逻辑

| 组件 | 作用 | 加载/执行时机 |
| :--- | :--- | :--- |
| `SKILL.md`（frontmatter） | 触发判断 | 始终加载 |
| `SKILL.md`（body） | 执行指令 | 触发后加载 |
| `scripts/` | 可执行代码 | 按需执行 |
| `references/` | 参考资料 | 按需读取 |
| `assets/` | 输出素材 | 生成时使用 |


## 3. 环境准备：安装 openskills CLI

openskills 是一个命令行工具，用于安装、管理和同步 Skills。在开始之前，你需要先把它装好。

前置要求

- • Node.js 16.0 或更高版本
- • npm 或其他包管理器（yarn、pnpm）
- • 推荐使用 nvm 管理 Node.js 版本


```
npm install -g openskills

openskills --version
1.5.0


% openskills --help

Usage: openskills [options] [command]

Universal skills loader for AI coding agents

Options:
  -V, --version               output the version number
  -h, --help                  display help for command

Commands:
  list                        List all installed skills
  install [options] <source>  Install skill from GitHub or Git URL
  read <skill-names...>       Read skill(s) to stdout (for AI agents)
  update [skill-names...]     Update installed skills from their source (default: all)
  sync [options]              Update AGENTS.md with installed skills (interactive,
                              pre-selects current state)
  manage                      Interactively manage (remove) installed skills
  remove|rm <skill-name>      Remove specific skill (for scripts, use manage for
                              interactive)
  help [command]              display help for command
```

## 4. 使用 Skills：安装、启用与管理

### 4.1 安装 Skills

从 GitHub 安装

最常见的方式是从 GitHub 安装。比如安装 Anthropic 官方的 Skills 合集：

```
openskills install anthropics/skills --global
```

参数说明：

- • anthropics/skills：GitHub 仓库地址（用户名/仓库名）
- • --global：安装到全局目录 ~/.claude/skills/

运行后会出现交互式选择界面：

```
% openskills install anthropics/skills          

Installing from: anthropics/skills
Location: project (.claude/skills)
Default install is project-local (./.claude/skills). Use --global for ~/.claude/skills.

✔ Repository cloned
Found 18 skill(s)

? Select skills to install
❯◉ algorithmic-art           58.4KB
 ◉ brand-guidelines          13.3KB
 ◉ canvas-design             5.3MB
 ◉ claude-api                481.2KB
 ◉ doc-coauthoring           15.4KB
 ◉ docx                      1.1MB
 ◉ frontend-design           14.3KB
 ◉ internal-comms            21.9KB
 ◉ mcp-builder               118.9KB
 ◉ pdf                       57.3KB
 ◉ pptx                      1.1MB
 ◉ skill-creator             219.7KB
 ◉ slack-gif-creator         42.7KB
 ◉ theme-factory             140.7KB
 ◉ web-artifacts-builder     44.8KB

Creating algorithmic art using p5.js with seeded randomness and interactive para
↑↓ navigate • space select • a all • i invert • ⏎ submit
```

### 安装位置：全局 vs 项目

```
# 全局安装（所有项目都能用）
openskills install anthropics/skills --global

# 项目级安装（只在当前项目可用）
openskills install anthropics/skills --project
```

| 安装方式    | 路径                  | 适用场景         |
| ----------- | --------------------- | ---------------- |
| `--global`  | `~/.claude/skills/`   | 通用工具类 Skill |
| `--project` | `./.skills/`          | 项目专属 Skill   |


```
$ openskills list
```

### 4.3 启用 Skills：同步到 AGENTS.md

重点来了：安装了 Skills 不代表就能用了，还需要同步到 AGENTS.md 文件才能让 Claude 识别。

```
 % openskills sync

Created AGENTS.md
? Select skills to sync to AGENTS.md
❯◉ find-skills               (project)
 ◯ algorithmic-art           (global)
 ◯ brand-guidelines          (global)
 ◯ canvas-design             (global)
 ◯ doc-coauthoring           (global)
 ◯ docx                      (global)
 ◯ frontend-design           (global)
 ◯ internal-comms            (global)
 ◯ mcp-builder               (global)
 ◯ pdf                       (global)
 ◯ pptx                      (global)
 ◯ skill-creator             (global)
 ◯ slack-gif-creator         (global)
 ◯ template                  (global)
 ◯ theme-factory             (global)

Helps users discover and install agent skills when they ask questions 
↑↓ navigate • space select • a all • i invert • ⏎ submit
```

```
% openskills sync

Created AGENTS.md
✔ Select skills to sync to AGENTS.md find-skills               (project)
✅ Added skills section to AGENTS.md (1 skill(s))
```

这会打开交互式界面，选择要启用的 Skills：

**选中的 Skills 会被写入当前目录的 AGENTS.md 文件**

生成的 AGENTS.md 长这样：

```
<available_skills>

<skill>
<name>find-skills</name>
<description>Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.</description>
<location>project</location>
</skill>

</available_skills>
<!-- SKILLS_TABLE_END -->

</skills_system>
```

**🔧 Stage 1：安装 Skills**

这是流程的起点，你通过命令行工具 `openskills install` 把需要的技能包下载到本地。

- 图里示例了 docx、pdf、xlsx 这类文件处理技能，本质就是把对应的功能文件安装到本地目录。
- 这一步只是“下载文件”，技能还没真正被 Claude 识别到。

**🔄 Stage 2：同步到 AGENTS.md**

安装完成后，你需要用 `openskills sync` 命令，选择要启用的技能（比如勾选 docx 技能，按空格选中）。

- 这一步的核心作用，是**把你选中的技能信息，同步到 Claude 的配置文件 `AGENTS.md` 里**。
- 你可以理解为：告诉 Claude“我要开启这些技能”，而不是单纯把文件丢进文件夹。

**📄 Stage 3：生成配置文件**

确认选择后，工具会自动在 `AGENTS.md` 里生成标准化的技能配置代码（XML/Markdown 格式）。

- 图里的 `<skills>` 标签、`<skill name="docx">` 就是典型的配置片段，Claude 就是靠读取这段配置，知道“我有这些技能可以用”。
- 这一步相当于把你选的技能，转换成 Claude 能读懂的“技能清单”。

**🤖 Stage 4：Claude 识别并使用**

Claude 启动/运行时，会主动读取 `AGENTS.md` 里的配置，识别到可用的技能，然后在对话中触发对应的功能。

- 比如你上传一个 Word 文件，Claude 会调用 docx 技能解析它，背后就是这个配置在生效。

⚠️ 关键提醒

图底部的黄色警告非常重要：**安装 ≠ 启用，必须 sync 后才能用！**

很多人会误以为“把文件下载好就完事了”，但 OpenSkills 的设计逻辑是：

- `install` = 下载技能文件（只是把文件放到本地）
- `sync` = 把技能写入 Claude 的配置，让它“看见”并启用

### 4.4 读取 Skill 内容


```
openskills read docx

```

这会输出完整的 SKILL.md 内容，包括所有指令和说明。主要用于：

- 了解某个 Skill 的功能
- AI Agent 运行时加载 Skill 内容

### 4.5 管理和删除 Skills

```
% openskills manage

✔ Select skills to remove slack-gif-creator         (global)
✅ Removed: slack-gif-creator (global)

✅ Removed 1 skill(s)
```

**直接删除**

```
openskills rm docx
# 或
openskills remove docx
```

### 4.6 完整工作流示例

让我们串起来走一遍完整流程：

```
# 1. 安装官方 Skills
openskills install anthropics/skills --global

# 2. 选择要安装的（按空格选中，回车确认）
#    假设选了 docx, pdf, xlsx

# 3. 进入你的项目目录
cd ~/my-project

# 4. 同步 Skills 到 AGENTS.md
openskills sync
#    选择要在这个项目启用的 Skills

# 5. 验证 AGENTS.md 已生成
cat AGENTS.md

# 6. 现在可以使用了！
#    在 Claude Code 或 Cursor 中打开项目
#    Claude 会自动识别可用的 Skills

```


### 4.7 在 Claude 中使用


一切配置好后，使用 Skills 就很简单了——直接用自然语言描述你的需求，Claude 会自动判断是否需要调用 Skill。

```
用户："帮我把这份报告转成 Word 文档，要有目录和页眉"

Claude：（检测到 docx skill 适用）→ 自动加载 docx skill → 按照 skill 的指令生成文档

```


**你不需要手动说"使用 docx skill"，Claude 会根据 description 自动判断。**

这也是为什么 description 写得好不好很重要——它直接决定了 Skill 能否被正确触发。

```
1. 理解需求 → 2. 规划内容 → 3. 初始化 → 4. 编辑实现 → 5. 打包发布 → 6. 迭代优化
```

#### 步骤 1：理解需求——从具体例子出发

创建 Skill 的第一步不是动手写代码，而是搞清楚这个 Skill 到底要解决什么问题。

最好的方法是收集具体的使用场景：

❓ 这个 Skill 会被怎么用？

❓ 用户会说什么话来触发它？

❓ 期望的输出是什么样的？


例子：假设你要创建一个"深度研究报告"Skill


| 触发场景 | 期望输出 |
| :--- | :--- |
| "帮我研究一下 AI Agent 的发展趋势" | 一份 3000 字的研究报告 |
| "做个竞品分析：Cursor vs Windsurf" | 结构化的对比分析文档 |
| "调研一下 MCP 协议的生态" | 包含多来源信息的综述 |


当你能列出 5-10 个具体场景时，就说明你对需求理解得足够清楚了。


#### 步骤 2：规划内容——决定放什么进去

有了具体场景后，开始规划 Skill 的内容。对每个场景问自己：

然后识别出可复用的部分：


| 类型 | 问题 | 解决方案 |
| :--- | :--- | :--- |
| **重复代码** | 每次都要重写相同的代码？ | → 放入 `scripts/` |
| **参考资料** | 每次都要重新解释某些知识？ | → 放入 `references/` |
| **输出模板** | 每次都要重新设计格式？ | → 放入 `assets/` |


例子：深度研究报告 Skill 的规划


```
deep-research/
├── SKILL.md                      # 研究流程指令
├── scripts/
│   └── generate_pdf.py           # 生成 PDF 报告
├── references/
│   ├── research_methodology.md   # 研究方法论
│   └── citation_format.md        # 引用格式规范
└── assets/
    └── report_template.html      # 报告模板
```

#### 步骤 3：初始化——创建目录结构

手动创建目录也行，但推荐使用初始化脚本（如果你安装了 skill-creator）：

```
npx skills add https://github.com/anthropics/skills --skill skill-creator

/skill-creator create    # 创建新技能
/skill-creator eval      # 评估现有技能
/skill-creator improve   # 优化技能（含 description 触发精度）
/skill-creator benchmark # 基准测试与方差分析
```

手动创建：

```
mkdir -p deep-research/{scripts,references,assets}
touch deep-research/SKILL.md
```

#### 步骤 4：编辑实现——写 SKILL.md 和资源文件

**4.1 编写 Frontmatter**

```
---
name: deep-research
description: |
  生成结构化的深度研究报告，支持多来源信息整合、自动生成大纲、
  分章节撰写。当用户需要：(1) 研究某个技术/产品/趋势，
  (2) 撰写调研报告或白皮书，(3) 进行竞品分析，
  (4) 综合多个来源写综述时，使用此 Skill。
---
```

写好 description 的关键

✅ 要包含

- Skill 能做什么
- 触发的场景/关键词
- 适用的任务类型


❌ 不要包含

- 实现细节
- 冗长的背景介绍
- "当用户说 XX 时" 这种机械表述


**4.2 编写 Markdown Body**


正文是给 Claude 看的操作手册。结构建议：

```
# Deep Research Skill

## 工作流程

### 第 1 步：确认研究范围
- 与用户确认研究主题
- 明确深度要求（概述 / 深度分析）
- 确定输出格式（Markdown / PDF / Word）

### 第 2 步：生成研究大纲
- 先生成 3-5 个主要章节
- 每章包含 2-3 个子话题
- 与用户确认大纲后再继续

### 第 3 步：分章节研究
对每个章节：
1. 搜索相关资料
2. 整理关键信息
3. 撰写章节内容

### 第 4 步：整合与输出
- 检查章节间的逻辑连贯性
- 生成参考文献列表
- 使用 scripts/generate_pdf.py 输出最终报告

## 参考资源
- 研究方法论: 见 references/research_methodology.md
- 引用格式: 见 references/citation_format.md

## 输出要求
- 每个章节 500-800 字
- 必须包含数据/案例支撑
- 引用来源需标注
```

**4.3 实现脚本和资源**

`scripts/generate_pdf.py`：

```
#!/usr/bin/env python3
"""生成研究报告 PDF"""

import sys
from weasyprint import HTML

def generate_report(html_content: str, output_path: str):
    HTML(string=html_content).write_pdf(output_path)
    print(f"Report generated: {output_path}")

if __name__ == "__main__":
    # 从 stdin 读取 HTML，输出到指定路径
    html = sys.stdin.read()
    output = sys.argv[1] if len(sys.argv) > 1 else "report.pdf"
    generate_report(html, output)
```

**步骤 5：打包发布**

开发完成后，可以打包成 .skill 文件分享给他人：

```
cd skills/.agents/skills/skill-creator

# 如果有官方打包脚本
python scripts/package_skill.py ./deep-research

# 或者直接压缩
cd my-skills
zip -r deep-research.skill deep-research/
```

```
cd .agents/skills/skill-creator


$ python -m scripts.package_skill ../../../deep-research
📦 Packaging skill: ../../../deep-research

🔍 Validating skill...
✅ Skill is valid!

  Added: deep-research/SKILL.md
  Added: deep-research/references/research_methodology.md
  Added: deep-research/scripts/generate_pdf.py

✅ Successfully packaged skill to: /Users/jacob/learnspace/ai/skills/.agents/skills/skill-creator/deep-research.skill
```


```
# 或者直接压缩
cd my-skills
zip -r deep-research.skill deep-research/
```


打包脚本会自动验证：

- • Frontmatter 格式是否正确
- • 必需字段是否完整
- • 文件结构是否规范


#### 步骤 6：迭代优化

创建 Skill 不是一锤子买卖。发布后要根据实际使用情况持续优化：

```
使用 Skill → 发现问题 → 分析原因 → 更新内容 → 再次测试
```

| 问题                | 可能的原因                   | 解决方案                         |
| ------------------- | ---------------------------- | -------------------------------- |
| Skill 没有被触发    | description 写得不够明确     | 补充触发关键词                   |
| 输出质量不稳定      | 指令太模糊                   | 增加具体的格式要求               |
| 执行效率低          | 加载了太多不必要的内容       | 拆分到 references，按需加载      |
| 脚本报错            | 环境依赖问题                 | 补充依赖安装说明                 |


┌──────────────────────────────────────────────────────────┐
│  1. 理解需求    收集 5-10 个具体使用场景                   │
├──────────────────────────────────────────────────────────┤
│  2. 规划内容    决定 scripts/references/assets 放什么     │
├──────────────────────────────────────────────────────────┤
│  3. 初始化      创建目录结构                              │
├──────────────────────────────────────────────────────────┤
│  4. 编辑实现    写 SKILL.md + 资源文件                    │
├──────────────────────────────────────────────────────────┤
│  5. 打包发布    生成 .skill 文件                          │
├──────────────────────────────────────────────────────────┤
│  6. 迭代优化    根据实际使用持续改进                       │
└──────────────────────────────────────────────────────────┘

### 6. 实战演示：创建「深度研究报告」Skill

**需求分析**

目标用户：需要快速产出高质量研究报告的人

**核心场景：**

1. "帮我研究一下 XX 技术的发展趋势"
2. "做一份 XX 和 YY 的竞品分析"
3. "写一篇关于 XX 的深度报告"

**期望输出**：

- 结构清晰的 Markdown/PDF 报告
- 包含大纲、正文、参考文献
- 3000-5000 字的深度内容

目录结构设计

```
deep-research/
├── SKILL.md                          # 主文件
├── references/
│   ├── methodology.md                # 研究方法论
│   └── outline_templates.md          # 大纲模板
└── assets/
    └── report_style.css              # PDF 样式
```

这个 Skill 不需要 scripts，因为 Markdown 输出足够满足需求。如果需要 PDF，可以后续扩展。

### 7. 最佳实践：写出高质量的 Skill

#### 7.1 简洁至上：上下文窗口是稀缺资源

核心原则：Claude 已经很聪明了，只告诉它不知道的东西。


❌ 常见错误：写了一大堆 Claude 本来就知道的内容

```
什么是 Markdown
Markdown 是一种轻量级标记语言，由 John Gruber 于 2004 年创建...
（这种基础知识 Claude 早就知道，写了就是浪费 token）
```

✅ 正确做法：只写特定于你场景的内容

```
Markdown 格式要求
- 标题层级不超过 3 级
- 表格必须有表头
- 代码块必须标注语言
（这些是你的特定要求，Claude 不知道）
```

检查清单：写完每一段后问自己——

#### 7.2 避免 AI 味：输出要像人写的

这是很多人踩的坑——Skill 写得很详细，但生成的内容一股"AI 味"，空洞、泛泛而谈。

AI 味的典型特征：

| 特征         | 例子                                     |
| ------------ | ---------------------------------------- |
| 空洞的开场白 | "在当今快速发展的技术领域中..."          |
| 过度使用副词 | "非常"、"极其"、"显著地"                 |
| 泛泛而谈     | "这是一个重要的趋势"                     |
| 列举堆砌     | "提高效率、降低成本、增强体验..."        |
| 模板化结构   | 每段都是"首先...其次...最后..."          |

#### **如何在 Skill 中解决这个问题**

**方法 1：在指令中明确禁止**

```
写作规范

禁止事项
- 不要使用"在当今..."、"随着...的发展"等开场白
- 不要使用"非常"、"极其"等空洞副词
- 不要泛泛而谈，每个观点必须有数据或案例支撑

必须事项
- 直接切入主题，第一句话就提供信息
- 用具体数字替代模糊描述
- 用实际案例替代抽象论述
```

**方法 2：提供对比示例**

```
写作示例

不好的写法：
人工智能技术正在快速发展，对各行各业产生了深远影响...

好的写法：
2025 年全球 AI 市场规模达到 1840 亿美元，其中企业级应用占比 62%。
制造业是采用最快的行业，AI 质检系统将缺陷检出率从 87% 提升到 99.2%。
```

**方法 3：要求引用来源**

```
引用规范

每个关键数据/观点必须标注来源：
格式：[内容]（来源：[出处], [时间]）
示例：全球 AI 市场规模达 1840 亿美元（来源：Gartner, 2025 Q1）
```

#### 7.3 渐进式披露：别一次塞太多

反模式：把所有内容都写在 SKILL.md 里

```
# My Skill

（2000 行的内容...）

```


这样做的问题：

1. 每次触发都要加载全部内容，浪费 token
2. 重要信息被淹没在大量细节中
3. 难以维护和更新

```
# My Skill

核心流程
（只放最重要的 200 行）

详细参考
- 场景 A 的详细指南：见 references/scenario_a.md
- 场景 B 的详细指南：见 references/scenario_b.md
- 完整 API 文档：见 references/api.md
```

Claude 会先看到核心流程，需要时再按需加载详细内容。

#### 7.4 设置合适的自由度

不是所有任务都需要严格的步骤。根据任务特性选择指令的"松紧度"：

例子：

```
# 高自由度（创意写作）
风格指南
- 语言风格：专业但不失活泼
- 可以使用类比和比喻
- 鼓励加入独特观点

# 低自由度（数据导出）
执行步骤
1. 运行 scripts/export_data.py --format csv
2. 校验输出文件行数
3. 如果行数 < 100，报错并终止
```

#### 7.5 写好 Description：决定生死的 100 词

description 是 Claude 决定是否使用 Skill 的唯一依据。写不好，Skill 就是摆设。

写 description 的公式：

```
[做什么] + [怎么做/输出什么] + [什么时候用]

```

❌ 不好的 description：

```
description: 生成研究报告的工具
```

✅ 好的 description：


```
description: |
  生成结构化的深度研究报告，支持技术调研、趋势分析、竞品对比。
  输出为多章节 Markdown，包含大纲、正文、数据支撑和参考来源。
  当用户需要：(1) 研究某个技术/产品/领域，(2) 撰写调研报告，
  (3) 进行竞品分析，(4) 做趋势洞察时使用。
```

检查清单：

- 说明了 Skill 能做什么
- 说明了输出是什么样的
- 列举了 3-5 个触发场景
- 包含了用户可能说的关键词


#### 7.6 测试、测试、再测试

写完 Skill 后，一定要实际测试。

测试方法：

```
# 1. 先读取 Skill 内容，检查格式
openskills read my-skill

# 2. 在实际环境中测试触发
#    尝试不同的问法，看能否正确触发

# 3. 测试边界情况
#    - 模糊的需求能否处理？
#    - 超出范围的请求如何响应？
```

**常见问题**

| 问题 | 可能原因 |
| :--- | :--- |
| Skill 没被触发 | description 没覆盖用户的说法 |
| 触发了但执行效果差 | SKILL.md 指令不够明确 |
| 输出格式不对 | 没有提供具体的格式要求 |
| 脚本执行失败 | 环境依赖没装 / 路径问题 |

**小结**


| 原则 | 核心要点 |
| :--- | :--- |
| 简洁 | 只写 Claude 不知道的，每段都要问"删了会怎样" |
| 去 AI 味 | 禁止空话、要求数据支撑、提供对比示例 |
| 分层加载 | 核心内容放 SKILL.md，详细内容放 references |
| 适度自由 | 创意任务松一些，精确任务紧一些 |
| 好的触发 | description 要全面，覆盖各种说法 |
| 持续测试 | 用真实场景测试，根据反馈迭代 |


### 8. 故障排除

**8.1 安装相关问题**

问题：npm 安装时权限错误 (EACCES)

```
npm error code EACCES
npm error syscall mkdir
```

原因：npm 全局安装路径权限不足

解决方案：

```
# 方案 1：如果使用 nvm，删除自定义 prefix
npm config delete prefix
npm install -g openskills

# 方案 2：修复目录权限
sudo chown -R $(whoami) ~/.npm ~/.npm-global
npm install -g openskills
```

问题：Git clone 失败

错误：RPC 失败。curl 55 Failed sending data to the peer

原因：网络问题或 Git buffer 太小


解决方案：

```
# 增大 buffer
git config --global http.postBuffer 524288000

# 如果在国内，可能需要配置代理
git config --global http.proxy http://127.0.0.1:7890
```

#### 8.2 openskills 命令问题

问题：sync 后 AGENTS.md 是空的

原因：没有按空格键选中 Skill

解决方案：

在交互式界面中，上下键只是移动光标，必须按空格键才能选中。选中后 ◯ 会变成 ◉。

**问题：Skill 没有被触发**

可能原因：

1. AGENTS.md 没有包含该 Skill
2. description 没有覆盖用户的说法


排查步骤：

```
# 1. 检查 AGENTS.md 是否包含该 Skill
cat AGENTS.md | grep "skill-name"

# 2. 检查 description 是否完整
openskills read skill-name
```

解决方案：

- 如果 AGENTS.md 没有，重新运行 openskills sync
- 如果 description 不够全面，编辑 SKILL.md 补充触发场景

#### 8.3 Skill 执行问题

问题：脚本执行失败

常见原因：

1. 缺少 Python 依赖
2. 路径问题
3. 权限问题

排查步骤：

```
# 1. 检查脚本是否可执行
ls -la scripts/

# 2. 手动运行脚本测试
python scripts/your_script.py

# 3. 检查依赖
pip list | grep package-name
```

**问题：references 文件没有被读取**

原因：SKILL.md 中没有正确引用

解决方案：确保使用相对路径引用：

```
# 正确
见 [references/guide.md](references/guide.md)

# 错误
见 references/guide.md（没有链接格式）
```

#### **8.4 输出质量问题**

问题：输出内容太"AI 味"

原因：SKILL.md 没有明确禁止空洞表达

解决方案：在 SKILL.md 中增加：


```
写作禁忌
- 不要使用"在当今..."开头
- 不要使用"非常"、"极其"等副词
- 每个观点必须有数据或案例支撑
```

**问题：输出格式不符合预期**

原因：格式要求不够具体

解决方案：提供明确的格式示例：

```
## 输出格式

必须使用以下结构：

# 标题
## 1. 第一章
内容...
## 2. 第二章
内容...
## 参考资料
- [1] 来源1
- [2] 来源2
```

#### 8.5 环境兼容问题

问题：Claude Code 和 Claude.ai 行为不一致

原因：两个平台的能力不同

解决方案：在 SKILL.md 中针对不同平台给出不同的指令：

```
执行方式

在 Claude Code 中
直接运行 scripts/generate.py

在 Claude.ai 中
手动执行以下步骤：
1. ...
2. ...
```

故障排除速查表

| 问题 | 快速检查 | 解决方案 |
| :--- | :--- | :--- |
| npm 权限错误 | `npm config get prefix` | 删除自定义 prefix 或修复权限 |
| sync 不生效 | 检查是否按了空格 | 空格选中，回车确认 |
| Skill 没触发 | `cat AGENTS.md` | 重新 sync 或改进 description |
| 脚本报错 | 手动运行脚本 | 安装依赖 / 修复路径 |
| AI 味太重 | 检查写作规范 | 增加禁止条款和示例 |

