# Claude Code基础使用教程：从安装到核心命令全掌握

Claude Code作为Anthropic推出的强大AI编程助手，能深度融合开发终端与IDE，实现代码编写、项目管理、多工具协同等多种能力，是提升开发效率的重要生产力工具。本文基于实操视角，从安装配置、核心命令、基础功能等维度，带你快速上手Claude Code的基础使用

## 一、学习资料准备

学习Claude Code的核心资料可参考GitHub上的**Claude Code guide**项目，该项目对Claude Code的功能讲解全面且细致。为了方便中文用户学习，可将该项目fork到自己的仓库并完成翻译，后续的学习可围绕项目文档的目录模块展开。 [https://code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview)

- [https://github.com/karminski/claude-code-guide-study](https://github.com/karminski/claude-code-guide-study)
- [https://github.com/Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide)

Claude Code guide的核心模块分为**快速开始、配置与环境、命令与使用、界面与输入、高级功能**五大块，其中高级功能包含思考模式、子代理、MCP、Hook等高阶能力，本次重点讲解前四个基础模块，高级功能将在后续单独讲解。


## 二、快速开始：安装与基础配置


快速开始模块的核心是完成Claude Code的安装和基础环境配置，整体操作流程简单，核心关注系统环境、环境变量、模型配置三大要点。

1. **系统安装**：针对Mac系统，可直接通过文档提供的两条命令完成安装，文档中会明确标注系统的基础要求，按要求执行即可。
	* `curl -fsSL https://claude.ai/install.sh | bash`
2. **核心配置项**：安装后需重点配置**Node.js环境变量、API Key、模型参数**，模型参数是切换不同大模型的关键，例如可将solid模型替换为dipstick v3.1，其他配置项可做基础了解，后续需要时按需查阅即可。
3. **跨系统配置注意事项**：配置全局参数时（如主题设置、任务结束时的铃声提醒等），Mac/Linux系统使用`export`命令，而Windows用户需要将命令中的`export`替换为`set`，这是跨系统配置的核心差异点。

## 三、核心命令：Claude Code的操作核心

Claude Code的所有操作均基于命令行完成，打开Claude Code后输入的各类命令是实现功能的关键，下面为大家讲解高频且实用的核心命令，按功能分类梳理如下：

### （一）工作目录管理命令

`add-dir`命令：可在当前对话中临时添加一个或多个额外的工作目录，让AI助手能同时访问和操作多个项目/文件夹的代码，无需重启Claude Code或切换对话窗口，大幅提升多项目并行开发的效率。

### （二）智能体相关命令

`agents`命令：调用平台的**专门化AI助手（Subagent）** 功能，Subagent是可被主智能体调用的独立AI实体，每个Subagent都有自己的专业领域、专属工具和独立的上下文窗口，能精准处理特定类型的开发任务，实现任务的专业化分工。

### （三）上下文与成本管理命令

这类命令的核心作用是优化上下文使用并节省API调用成本，是日常使用的高频命令：

1. `clear`：直接将当前对话的上下文清零，彻底释放上下文空间；
2. `compact`：对上下文进行压缩处理，也可指定具体的压缩内容，相比`clear`更灵活，可保留核心上下文；
3. `cost`：查看当前使用Claude Code产生的API调用费用，实时掌握成本消耗。

### （四）工具与数据源连接命令

`mcp`命令：是Claude Code中连接外部数据源和工具的核心命令。MCP（Model Context Protocol）就像USB为设备连接外设提供的标准化接口，为AI模型连接不同数据源、外部工具提供了统一的标准化方式。输入`mcp`命令可查看已安装的MCP服务数量及各服务的链接状态，本次实操中已安装3个MCP服务，均可正常连接。

### （五）长记忆管理命令

`memory`命令：用于管理Claude Code的长记忆功能，可查看、编辑或删除AI在当前项目中记录的**跨对话知识**，其记忆库分为四个优先级（从上到下）：企业整体知识库→项目知识库→用户知识库→本地内存（项目内存本地已废弃）。

- 企业知识库：适合企业级用户，可配置公司统一的知识体系，供所有团队成员使用；
- 项目知识库：通过`init`命令生成，包含项目的整体介绍、各模块功能、开发规范等核心信息；
- 用户知识库：可自行添加个人/部门的专属文档，让Claude Code具备贴合个人工作场景的知识储备。

### （六）知识库与模型查看命令

1. `model`命令：查看当前Claude Code使用的大模型，实操中使用的是桑奈斯模型，该模型性价比更高，其他模型的API调用成本相对较高；
2. 配合`memory`命令，可分别查看用户知识库和项目知识库的具体内容，确认知识储备的完整性。

### （七）命令行核心操作命令

1. `claude c`：Claude Code最基础的命令，退出Claude Code后再次执行该命令，可恢复上一次的对话上下文，也可结合管道命令实现更灵活的操作；
2. `claude p`：代码解读专用命令，可直接读取本地代码文件并让AI完成代码的详细解读，是快速理解陌生代码的高效工具。

## 四、基础操作：快捷键与特殊模式

### （一）常用快捷键

`ctrl + c`：中断当前的AI对话，当AI的响应不符合预期或需要终止当前任务时，可快速执行该快捷键。

### （二）VM模式

Claude Code支持VM模式，输入`vm`命令即可进入该模式，再次输入`vm`命令则退出VM模式，VM模式可为开发提供更隔离、更安全的操作环境。

## 五、高级模式入门：思考关键词的使用

Claude Code的高级模式中，**思考关键词**是基础且实用的功能，在对话中输入指定关键词，可触发AI不同程度的思考，适配不同难易程度的开发任务。

本次实操以**代码重构**为例，输入思考关键词`think`，可触发AI的**轻度思考**，AI会基于代码的现有结构，给出详细、可落地的重构思路，满足日常代码优化的核心需求。后续还会讲解更多思考关键词，适配复杂的开发任务（如深度代码调试、架构设计等）。

## 六、学习总结与后续规划

通过以上内容，我们已掌握Claude Code的**基础安装配置、核心命令使用、基础操作技巧和思考关键词入门**，接下来可将这些功能应用到实际的开发项目中，通过实操进一步熟悉各类命令的使用场景和技巧。

后续我们将重点讲解Claude Code的**高级功能**，包括MCP集成、Agent Hook、子代理的高级配置、复杂思考模式的触发等内容，帮助大家挖掘Claude Code的更多潜力，实现开发效率的最大化提升。


我直接把你这篇 **Medium 英文全文** 做成一篇**干净、通顺、可直接发布的中文技术博客**，结构完全对齐原文，只做专业翻译+技术润色，不瞎改逻辑。



# 5 分钟内让 Claude Code 跑在本地/云端开源模型上

（Ollama / LM Studio / llama.cpp / OpenRouter 完整教程）

在早期版本里，想让 Claude Code 脱离 Anthropic 官方 API 运行，简直是一团糟。
集成很脆弱，配置像搞科研，而且每次一更新，工作流就可能直接崩掉。

但现在不一样了： **Claude Code 已经大幅增强了对第三方模型服务商的支持**，包括 Ollama、LM Studio、llama.cpp、OpenRouter 等。

这也让我们的核心问题从：

> “我能不能让它跑起来？”

变成了：

> “根据我的场景（成本 / 速度 / 效果 / 隐私），我该选哪种方案？并且怎么在 5 分钟内配好？”

这就是一篇**最新、最实用、带主观推荐**的教程。

我的测试设备：

- MacBook Pro M1（32GB 统一内存）
- Nvidia DGX Spark（120GB 内存 + GB10 显卡）

我会先讲**最简单的方案**（Ollama 本地 + 云端一键转发），再讲更灵活的自定义部署。



## 本地跑代码模型的最低配置建议

如果你想让 **Claude Code + 本地 LLM** 真正能用（不只是演示），我建议：

- 内存：**32GB**（Apple Silicon 统一内存 或 PC 内存）
- 模型参数：**24B 左右起步**

**16GB 也能跑更小的模型，但体验通常很糟糕： 错误更多、重试更频繁、整体反而更慢。**

### 推荐入门模型

- `devstral-small-2`（24B）→ 代码能力均衡，入门首选
- `qwen3-coder:30b` → 代码能力更强，32GB 设备仍可流畅运行
- `GLM4.7-flash:q8_0` → 性价比与延迟平衡优秀（量化版）


### 为什么要折腾第三方模型？

说实话，Claude Code 搭配官方 API 非常好用，但**烧钱速度也很快**。
我只是做些功能测试，额度就蹭蹭往下掉。

于是我开始找替代方案。

结果发现：**只要兼容 Anthropic API 格式的服务商，Claude Code 全都能接**。

现在这类平台已经非常多了。

一句话总结：

第三方方案相比 Claude Opus 4.5 **最多能省 98% 成本**。

- DeepSeek V3.2 最便宜，约 **$0.28/$0.28/$0.42 每百万 tokens**
- 本地方案（如 Ollama）**完全免费**
- 订阅制：低至 **`$3/月（智谱 GLM）**、$10/月（MiniMax）`



### 方案 1：Ollama 本地运行

耗时：5 分钟｜成本：免费｜适合：强隐私、无网环境

如果你想要**简单、稳定、不用折腾**，Ollama 是最佳选择。

#### Step 1：安装 Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Step 2：拉取模型

我在 32GB 内存上跑 24B 模型非常舒服：

```bash
ollama pull devstral-small-2
```

根据内存选择建议：

- 32GB：`devstral-small-2`、`glm-4.7-flash:bf16`
- 更小内存：跑小模型，但体验会下降


#### Step 3：连接 Claude Code

**最简单方式：**

```bash
ollama launch claude --model devstral-small-2

ollama launch claude --model llama3.1:8b
```



**手动配置（写入 ~/.zshrc 或 ~/.bashrc）：**

```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL="http://localhost:11434"
```

生效并启动：

```bash
source ~/.zshrc
claude --model devstral-small-2
```

搞定！现在 Claude Code 完全跑在本地。

#### 我在 M1 / DGX 上的实测速度

- Mac M1 32GB：`qwen3-coder-32b` 偏慢，换成 `devstral-small-2` 速度可接受
- Nvidia DGX Spark：`glm-4.7-flash:bf16`（30B）速度**接近 Claude Opus 4.5**



### 方案 2：llama.cpp + HuggingFace

耗时：15–20 分钟｜成本：免费｜适合：想用 HuggingFace 任意模型

Ollama 很方便，但如果你想**指定特定模型**，llama.cpp 更灵活。

#### Step 1：编译 llama.cpp

**macOS（Apple Silicon）：**

```bash
brew install cmake
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build -DGGML_METAL=ON
cmake --build llama.cpp/build --config Release -j
cp llama.cpp/build/bin/llama-* llama.cpp/
```

**Linux（NVIDIA GPU）：**

```bash
sudo apt-get update && sudo apt-get install build-essential cmake git -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build -DGGML_CUDA=ON
cmake --build llama.cpp/build --config Release -j
cp llama.cpp/build/bin/llama-* llama.cpp/
```

#### Step 2：启动 API 服务

示例（自动下载模型 + 启动服务，端口 8000）：
```bash
llama-server -hf bartowski/cerebras_Qwen3-Coder-REAP-25B-A3B-GGUF:Q4_K_M \
    --alias "Qwen3-Coder-REAP-25B-A3B-GGUF" \
    --port 8000 \
    --jinja \
    --kv-unified \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    --flash-attn on \
    --batch-size 4096 --ubatch-size 1024 \
    --ctx-size 64000
```

重点：

**必须加 `--jinja`，否则工具调用（function calling）不能用**。

#### Step 3：接入 Claude Code

```bash
export ANTHROPIC_BASE_URL="http://localhost:8000"
source ~/.zshrc
claude --model Qwen3-Coder-REAP-25B-A3B-GGUF
```

#### 实测速度

- Nvidia DGX：速度不错
- Mac M1：偏慢，不适合日常开发



### 方案 3：LM Studio

耗时：5 分钟｜成本：免费｜适合：喜欢 GUI、不想记命令

LM Studio 是我很喜欢的工具，GUI 友好，模型筛选非常直观。

#### Step 1：安装
GUI 版：lmstudio.ai/download

服务器版：

```bash
curl -fsSL https://lmstudio.ai/install.sh | sh
```

#### Step 2：下载模型

- GUI：直接搜索、点下载
- 命令行：`lms chat` → `/download`

#### Step 3：启动服务

```bash
lms server start --port 1234
```

#### Step 4：连接 Claude Code

```bash
export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
claude --model qwen/qwen3-coder-30b
```



### 方案 4：Ollama Cloud 云端模型

耗时：2 分钟｜成本：按需付费｜适合：本地体验 + 云端算力

Ollama 自带云端模型版本，命令和本地完全一样，不用管 API Key。

#### Step 1：拉取云端模型

```bash
ollama pull kimi-k2.5:cloud
ollama pull minimax-m2.1:cloud

ollama pull qwen3-coder-next:cloud
```

#### Step 2：一键启动

```bash
ollama launch claude --model kimi-k2.5:cloud

ollama launch claude --model qwen3-coder-next:cloud

ollama launch claude --model minimax-m2.1:cloud
```

体验和本地完全一致，但算力在云端。

免费额度可用于应急、轻量测试。

---

### 方案 5：直接对接第三方云 API

耗时：2 分钟｜成本：按需付费｜适合：追求最低价格

#### OpenRouter（万能转接器）

```bash
export ANTHROPIC_BASE_URL=https://openrouter.ai/api
export ANTHROPIC_AUTH_TOKEN=你的_OPENROUTER_KEY
export ANTHROPIC_API_KEY=
export ANTHROPIC_MODEL="openai/gpt-oss-120b:free"
```

`ANTHROPIC_API_KEY` 留空是故意的，避免冲突官方认证。

#### MiniMax（性价比极高）

```bash
export ANTHROPIC_BASE_URL=https://openrouter.ai/api
export ANTHROPIC_AUTH_TOKEN=你的_MINIMAX_KEY
export ANTHROPIC_MODEL="MiniMax-M2.1"
```

GLM、DeepSeek、Kimi 配置逻辑完全一样，只改：

- `ANTHROPIC_BASE_URL`
- `ANTHROPIC_AUTH_TOKEN`
- `ANTHROPIC_MODEL`


### 总结：你该选哪种？

- 想要**本地 + 隐私 + 简单**：
  → **Ollama + devstral-small-2 / glm-4.7-flash**
- 想要**自定义 HF 模型**：
  → **llama.cpp**
- 喜欢 **GUI、不想敲命令**：
  → **LM Studio**
- 想要**快、强、便宜，不在意本地运行**：
  → **Ollama Cloud / MiniMax / DeepSeek / GLM**
- 追求**最强代码能力**：
  → 目前还是 **Opus 4.5** 综合最强

一句话：

**Claude Code 现在真的很灵活，你不再被绑在 Anthropic 官方 API 上。**

# 使用 Claude Code

```
ollama launch claude --model qwen3-coder-next:cloud
