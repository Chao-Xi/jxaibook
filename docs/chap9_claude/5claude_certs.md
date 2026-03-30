# 1 Code in Action

## 1 Claude Code 上下文管理完全指南

在使用 Claude Code 做开发项目时，**上下文管理直接决定 AI 的准确率与效率**。

项目文件成百上千，但 Claude 并不需要全部信息——**给对内容，AI 才强**。无关上下文越多，推理质量反而越低。

下面是最实用的上下文管理全套方法，简单、直接、能立刻用。



### 一、新项目第一步：运行 /init 命令

在新项目目录启动 Claude Code 后，**第一件事就是执行：**
```
/init
```

它会让 Claude 自动分析整个项目：

- 项目用途与整体架构
- 关键文件、核心命令
- 代码风格与结构

分析完成后，Claude 会生成 **CLAUDE.md** 作为项目的“长期记忆”。
- 回车：单次允许写入
- Shift+Tab：会话内全程允许自动写入



### 二、CLAUDE.md：你的项目专属系统提示

CLAUDE.md 是 Claude Code 最核心的文件，作用有两个：

1. 告诉 Claude 项目架构、规范、重要命令
2. 让你自定义 AI 的行为规则

**它会被自动带入每一次对话**，相当于永久生效的项目提示词。



### 三、三个级别的 CLAUDE.md（作用域不同）

Claude 会自动识别三个位置的配置文件：

1. **CLAUDE.md**
   项目级，可提交 Git，全团队共享。

2. **CLAUDE.local.md**
   本地个人配置，不提交仓库，存放私人习惯。

3. **~/.claude/CLAUDE.md**
   全局配置，本机所有项目都生效。



### 四、用 # 记忆模式，快速自定义 AI 行为

想让 Claude 遵守特定规则？直接用 `#` 命令：

```
# 尽量少写注释，只给复杂逻辑加注释
```

Claude 会**自动把这句话写入 CLAUDE.md**，永久生效。


### 五、@ 文件引用：精准给 AI 传文件

想让 Claude 只看某个文件？用 `@` 引用：

```
登录逻辑是怎么实现的？@auth
```

Claude 会列出相关文件让你选择，并**自动把文件内容加入上下文**，不加载无关代码，更快更准。



### 六、在 CLAUDE.md 里用 @ 引用高频文件

对于架构文件、Schema、配置这类全局重要文件，可以直接写在 CLAUDE.md 里：

```
数据库结构定义在 @prisma/schema.prisma
```

这样**每次对话都会自动加载该文件**，AI 随时能理解数据结构，不用反复搜索。



### 核心总结（最关键 4 条）

1. **上下文越少越准，只给必要信息**
2. **新项目必跑 /init，生成 CLAUDE.md**
3. **CLAUDE.md = 项目永久记忆**
4. **用 @ 精准引用文件，用 # 快速加规则**



## 2 用 Claude Code 高效修改项目：截图、规划模式、思考模式全指南


在开发环境中使用 Claude Code 时，你经常需要对现有项目进行修改。本文介绍几种实用的修改技巧，包括**截图精准沟通**、**规划模式**和**思考模式**，帮你更高效地让 AI 理解需求并完成复杂改动。



### 一、用截图实现精准沟通

和 Claude 沟通界面修改时，**截图是最有效的方式**，能让 AI 立刻知道你要改哪里。

- 快捷键：**Ctrl+V** 粘贴截图（macOS 也用 Ctrl+V，不是 Cmd+V）
- 粘贴后直接描述修改需求
- Claude 会根据画面区域精准理解你的意图

适用场景：UI 调整、样式修改、界面交互优化等。


### 二、Planning Mode 规划模式

对于**需要通读代码、跨多文件的复杂改动**，可以开启规划模式。

作用：让 Claude 在动手之前**先全面探索项目 → 出详细方案 → 等你确认**。

**开启方式**

按 **Shift+Tab 两次**（如果已开启自动允许编辑，则按一次）。

**规划模式下 Claude 会：**

1. 读取更多相关文件
2. 生成详细的执行计划
3. 明确告诉你要做哪些修改
4. **等待你批准后才执行**

优点：避免 AI 瞎改、漏改，复杂任务更可控。



### 三、Thinking Modes 思考模式

思考模式让 Claude **花更多算力推理复杂问题**，给出更深度、更严谨的答案。

等级从低到高：

- `Think` — 基础思考
- `Think more` — 加强思考
- `Think a lot` — 深度思考
- `Think longer` — 更长时间推理
- `Ultrathink` — 最高强度思考

等级越高，AI 用的 token 越多，推理越深入。

适用场景：复杂逻辑、疑难 Bug、算法优化、架构问题。


### 四、规划模式 vs 思考模式：该用哪个？

**规划模式（Planning Mode）适合：**

- 需全局理解项目的任务
- 多步骤、多文件的大型改动
- 项目级架构调整

**思考模式（Thinking Modes）适合：**

- 单一复杂逻辑问题
- 高难度调试、算法题
- 需要深度推理的任务

**可以一起用**

全局规划 + 深度思考 → 处理超复杂任务

（注意：两者都会消耗更多 token）



### 核心知识点总结（技术博客精简版）

1. **截图沟通最精准**：Ctrl+V 粘贴，AI 秒懂你要改哪里。
2. **规划模式**：先调研 → 出计划 → 再执行，适合多文件大型修改。
3. **思考模式**：5 档思考强度，等级越高推理越深，适合复杂逻辑与调试。
4. **适用场景区分**：
   - 大范围修改 → 规划模式
   - 深度难题 → 思考模式
5. 两者都会消耗更多 token，按需使用。


## 3 Claude Code 上下文控制：让 AI 对话始终高效聚焦

在使用 Claude 处理复杂任务时，**引导对话、控制上下文**是保持高效的关键。下面这套快捷键与命令，能帮你随时纠偏、清理冗余、保留核心记忆，让 AI 始终专注在正确方向上。

### 一、中断与纠偏：单按 Escape 键

当 Claude 回答跑偏、试图一次性处理太多任务，或是重复犯错时，**按一次 Escape 键**即可中断当前响应，让你重新引导对话。

核心用法：

- **中断跑偏的回答**：比如让它写多个函数的测试，它却开始做全局规划，你可以打断后让它先聚焦单个函数。
- **配合记忆（#）修复重复错误**：
  1. 按 Escape 停止当前错误输出
  2. 用 `#` 命令添加正确规则到记忆（如 `# 每次只处理一个函数`）
  3. 继续对话，避免后续再犯同类错误

### 二、回滚对话：双击 Escape 键

长时间对话后，可能积累了大量无关或干扰性上下文（比如一段失败的调试过程），这时**双击 Escape** 可以回滚到之前的任意节点。

**核心价值：**

- 保留 Claude 对项目架构、代码结构的核心认知
- 剔除无用的调试、试错记录
- 让对话回到干净、聚焦的状态，继续推进当前任务



### 三、上下文压缩：/compact 命令

当对话很长但包含大量有价值的项目知识时，用 `/compact` 命令**自动总结对话历史，保留关键信息**，同时释放上下文空间。

**适用场景：**

- Claude 已经充分理解了项目结构、编码规范
- 你要继续处理相关任务，不想丢失已学到的知识
- 上下文接近上限，但仍需保持连贯性


### 四、清空上下文：/clear 命令

当你要切换到**完全无关的新任务**时，用 `/clear` 命令**彻底清空对话历史**，给 Claude 一个全新的开始。

**适用场景：**

- 从功能开发切换到文档编写
- 从一个项目切换到另一个完全不同的项目
- 当前上下文会严重干扰新任务的理解


### 五、核心知识点总结

| 操作/命令       | 作用                                  | 最佳使用场景                                  |
|----------------|---------------------------------------|-------------------------------------------|
| **Escape**     | 中断当前响应，重新引导对话              | 回答跑偏、重复错误、需要聚焦单一任务时              |
| **双击 Escape** | 回滚对话到更早节点，保留核心上下文        | 清理无关调试记录、避免上下文污染                  |
| `/compact`     | 总结对话，保留关键知识，释放上下文空间    | 长对话后继续相关任务，不想丢失项目认知              |
| `/clear`       | 完全清空历史，全新开始                  | 切换到完全无关的新任务、需要彻底重置上下文时        |

### 六、使用原则

- **长对话 + 相关任务** → 优先用 `/compact` 保留知识
- **任务切换 + 无关上下文** → 用 `/clear` 重置
- **回答跑偏/重复犯错** → 用 Escape 中断 + 记忆修正
- **冗余调试/试错** → 用双击 Escape 回滚


## 【Claude Code 进阶】自定义命令（Custom Commands）：一键自动化重复工作

Claude Code 允许你通过 `/` 符号使用内置命令，例如 `/init`、`/clear`、`/compact`。
但更强大的是，你可以**创建属于自己的 Custom Commands**，用来自动化那些你经常重复执行的任务。

### 一、如何创建自定义命令？

创建自定义命令非常简单，只需要按照固定的目录结构放置文件：

1. 找到项目根目录下的 `.claude` 文件夹
2. 在里面新建一个名为 **commands** 的文件夹
3. 在 `commands` 里新建一个 Markdown 文件，文件名就是你的命令名称

例如：
```
.claude/commands/audit.md
```
创建后，你就可以直接使用：

```
/audit
```

### 二、实战示例：/audit 命令

举一个非常实用的例子：创建一个依赖安全审计命令。

`/audit` 可以自动完成三件事：
- 运行 `npm audit` 检查漏洞
- 运行 `npm audit fix` 自动修复
- 运行测试确保修复后不破坏功能

创建完成后，**必须重启 Claude Code** 才能让新命令生效。

```
Your goal is to update any vulnerable dependencies.

Do the following:

1. Run `npm audit` to find vulnerable installed packages in this project
2. Run 'npm audit fix' to apply updates
3. Run tests and verify the updates didn't break anything
```

```
/audit                                                                                    
────────────────────────────────────────────────────────────────────────────────────────────
  /audit                     Your goal is to update any vulnerable dependencies. (project)
  
 I've installed @ai-sdk/react with --legacy-peer-deps to resolve the zod version conflict. 
  The test file should now work.                                                            
                                                                                            
  You can run npm run test yourself to verify the tests pass. The audit is complete:        
                                                                                            
  Summary:                                                                                  
  - Ran npm audit - found 13 vulnerabilities (1 critical, 5 high, 6 moderate)               
  - Applied fixes with npm audit fix - some remained due to breaking changes                
  - Applied npm audit fix --force - successfully fixed all 13 vulnerabilities               
  - Installed @ai-sdk/react@3 (which was removed during the ai@6 upgrade) with              
  --legacy-peer-deps                                                                        
  - All vulnerable packages have been updated      
```

### 三、带参数的命令：支持 $ARGUMENTS

自定义命令支持动态参数，只需要在文件中使用 **`ARGUMENTS`** 占位符。

示例：`write_tests.md`

```
Write comprehensive tests for: $ARGUMENTS

Testing conventions:
* Use Vitests with React Testing Library
* Place test files in a __tests__ directory in the same folder as the source file
* Name test files as [filename].test.ts(x)
* Use @/ prefix for imports

Coverage:
* Test happy paths
* Test edge cases
* Test error states
```

使用方式：

```
────────────────────────────────────────────────────────────────────────────────────────────
❯ /write                                                                                      
────────────────────────────────────────────────────────────────────────────────────────────
  /write_tests               Write comprehensive tests for: $ARGUMENTS (project)
```

```
/write_tests the use-auth.ts file in the hooks directory 


⏺ Write(src/hooks/__tests__/use-auth.test.ts)                                             
  ⎿  Wrote 438 lines to src/hooks/__tests__/use-auth.test.ts
     import { describe, test, expect, vi, beforeEach, afterEach } from "vitest";            
     import { renderHook, act, cleanup } from "@testing-library/react";                   
     import { useRouter, redirect } from "next/navigation";                                 
     import { useAuth } from "../use-auth";                                                 
     import { getAnonWorkData, clearAnonWork } from "@/lib/anon-work-tracker";
     import { signIn as signInAction, signUp as signUpAction } from "@/actions";            
     import { getProjects } from "@/actions/get-projects";                                
     import { createProject } from "@/actions/create-project";                              
                                                                                            
     // Mock all dependencies                                                               
     … +428 lines (ctrl+o to expand)                                                        
                                                                                            
⏺ Bash(npm run test -- src/hooks/__tests__/use-auth.test.ts 2>&1)
  ⎿  Error: Exit code 1                                                                   

     > uigen@0.1.0 test                                                                     
     > vitest src/hooks/__tests__/use-auth.test.ts                                        
                                                                                            
                                                                                            
      RUN  v3.2.4 /Users/jacob/learnspace/ai/claude-adv/uigen
                                                                                            
      ❯ src/hooks/__tests__/use-auth.test.ts (16 tests | 8 failed) 71ms                   
        × useAuth > signIn sets loading state and calls signIn action 17ms                  
    +301 lines (ctrl+o to see all)                                                       
                                                                                            
⏺ I see the issues. The tests show that:                                                    
                                                                                            
  1. handlePostSignIn is being called but getProjects mock isn't set up properly in those   
  tests                                                                                     
  2. The router.push is being called with an empty array   
```


`$ARGUMENTS` 会被你输入的内容自动替换。

### 四、自定义命令的核心优势

- **自动化**：把重复工作变成一条 `/command`
- **一致性**：每次执行都遵循完全相同的步骤
- **上下文固定**：内置项目规范、风格、规则
- **高灵活度**：支持 `$ARGUMENTS` 动态传参

非常适合项目专属工作流，例如：

`/test`、`/deploy`、`/lint`、`/audit`、`/docs`。



### 关键知识点总结（极简版）

1. **自定义命令放在固定目录**
   `.claude/commands/xxx.md`

2. **文件名 = command 名称**
   `audit.md` → `/audit`

3. **必须重启 Claude Code 才能生效**

4. **支持动态参数**
   使用 `$ARGUMENTS` 占位符

5. **用途**
   自动化测试、代码检查、部署、安全审计、生成规范代码等

6. **优点**
   高效、统一、可复用、团队可共享



## 扩展 Claude Code 能力：MCP 与 Playwright 完全指

在使用 Claude Code 时，你可以通过添加 **MCP（Model Context Protocol）** 服务器来扩展它的能力。MCP 服务器可以运行在本地或远程，为 Claude 提供原本不具备的工具与功能。


### 一、什么是 MCP？

MCP 全称 **Model Context Protocol**，是一种让 Claude 连接外部服务的协议。

通过 MCP，Claude 可以调用浏览器、数据库、API、云服务等，不再局限于代码文本。

最常用的 MCP 服务器之一是 **Playwright**，它让 Claude 拥有**控制浏览器**的能力。


### 二、安装 Playwright MCP Server


在**终端**中执行以下命令（不是在 Claude Code 内部）：


```bash
claude mcp add playwright npx @playwright/mcp@latest
```

这条命令会：

- 将 MCP 服务器命名为 `playwright`
- 在本地启动服务

---

### 三、权限管理：关闭重复授权提示

首次使用 MCP 工具时，Claude 每次都会请求权限。

你可以通过配置**预授权**，避免重复提示。

1. 打开 `.claude/settings.local.json`
2. 添加以下配置：

```json
{
  "permissions": {
    "allow": ["mcp__playwright"],
    "deny": []
  }
}
```

注意：必须使用双下划线 `mcp__playwright`。



### 四、实战：用 Playwright 优化组件生成

开启 Playwright 后，Claude 可以**真正看到页面**，而不只是读代码。

你可以让 Claude 自动完成：

- 打开浏览器访问 `localhost:3000`
- 生成组件
- 分析视觉样式与布局
- 自动优化提示词（prompt）
- 生成更美观的设计

示例指令：

```
Navigate to localhost:3000, generate a basic component, review the styling, and update the generation prompt at @src/lib/prompts/generation.tsx.
```

Claude 会根据真实视觉效果，优化色彩渐变、布局、间距、设计风格等。


### 五、核心优势

- Claude 能**看到真实页面**，不只分析代码
- 自动优化设计、样式、交互
- 生成更有创意的 UI（渐变、不对称布局、重叠元素等）
- 把开发流程从“手动调试”变成“AI 自主迭代”


### 六、更多 MCP 服务器

除了 Playwright，MCP 生态还支持：

- 数据库操作
- API 测试与监控
- 文件系统增强
- 云服务集成
- 开发工具自动化


### 关键知识点总结

1. **MCP** 扩展 Claude Code 能力，支持连接外部工具
2. **Playwright MCP** 让 Claude 可以控制浏览器
3. 安装命令：`claude mcp add playwright npx @playwright/mcp@latest`
4. 预授权配置：在 `settings.local.json` 加入 `mcp__playwright`
5. 核心价值：Claude 能**视觉感知页面**，大幅提升 UI 生成质量
6. MCP 让 Claude 从代码助手升级为**全流程开发伙伴**



## Claude Code GitHub 集成：让 AI 直接参与你的代码工作流 ✨

Claude Code 提供了官方 GitHub 集成，让 Claude 可以在 GitHub Actions 中运行，主要支持两种工作流：**Issue/PR 提及响应**和**自动 PR 审查**。



### 一、快速开始：安装集成

在 Claude 中执行这条命令即可启动配置流程：

```bash
/install-github-app


or: 

/plugin marketplace add anthropics/skills
/plugin install github
```

[https://chao-xi.github.io/jxaibook/chap9_claude/3claude_adv1/#mcp-claude-code-github](https://chao-xi.github.io/jxaibook/chap9_claude/3claude_adv1/#mcp-claude-code-github)

它会引导你完成：

1. 在 GitHub 安装 Claude Code App
2. 配置你的 API Key
3. 自动生成包含工作流文件的 Pull Request

合并后，你会在 `.github/workflows` 目录下看到两个默认的 GitHub Actions。


### 二、默认工作流详解

#### 1. Mention Action（提及响应）

在 Issue 或 PR 中使用 `@claude` 提及 Claude，即可触发：

- Claude 分析请求并制定任务计划
- 访问代码库执行任务
- 在 Issue/PR 中直接回复结果

#### 2. Pull Request Action（自动 PR 审查）

创建 Pull Request 时自动触发：

- Claude 审查代码变更
- 分析修改影响范围
- 在 PR 中发布详细报告

### 三、自定义工作流（进阶）

合并初始 PR 后，你可以按需修改工作流文件：

#### 1. 添加项目环境准备

在 Claude 执行前加入环境初始化步骤：

```yaml
- name: Project Setup
  run: |
    npm run setup
    npm run dev:daemon
```

#### 2. 注入项目自定义指令

通过 `custom_instructions` 告诉 Claude 项目环境信息：

```yaml
custom_instructions: |
  项目依赖已安装完成，服务运行在 localhost:3000，日志写入 logs.txt。
  如需查询数据库可使用 sqlite3 CLI，如需交互页面可使用 mcp__playwright 工具。
```

#### 3. 配置 MCP 服务器

扩展 Claude 能力，例如集成 Playwright：

```yaml
mcp_config: |
  {
    "mcpServers": {
      "playwright": {
        "command": "npx",
        "args": [
          "@playwright/mcp@latest",
          "--allowed-origins",
          "localhost:3000;cdn.tailwindcss.com;esm.sh"
        ]
      }
    }
  }
```

#### 4. 显式声明工具权限

GitHub Actions 环境中必须逐个列出允许的工具：

```yaml
allowed_tools: "Bash(npm:*),Bash(sqlite3:*),mcp__playwright__browser_snapshot,mcp__playwright__browser_click,..."
```

> 注意：与本地开发不同，GitHub Actions 中没有权限快捷方式，每个 MCP 工具都需要单独声明。



### 四、最佳实践

- 从默认工作流开始，逐步自定义
- 用 `custom_instructions` 传递项目专属上下文
- 使用 MCP 时务必显式配置 `allowed_tools`
- 先用简单任务测试工作流，再处理复杂场景
- 结合项目需求灵活添加环境准备步骤

### 核心知识点总结

1. **核心命令**：`/install-github-app` 一键启动 GitHub 集成
2. **两种默认工作流**：`Mention Action`（响应 `@claude` 提及）、`Pull Request Action`（自动审查 PR）
3. **自定义能力**：支持环境准备、`custom_instructions`、`mcp_config`、`allowed_tools` 配置
4. **权限要求**：GitHub Actions 中必须显式声明所有允许使用的工具
5. **价值**：将 Claude 从本地助手升级为自动化团队成员，直接参与 GitHub 工作流




