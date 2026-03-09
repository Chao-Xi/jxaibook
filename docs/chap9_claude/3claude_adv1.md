# Connecting Claude Code to External Tools

[https://github.com/nyisztor/novatech-demo](https://github.com/nyisztor/novatech-demo)


## 实战项目搭建：NovaTech 演示项目完整配置

在开始学习 MCP 与高级 Claude Code 技巧前，我们先统一配置**全程通用的演示项目**，后续所有章节都基于该项目展开，请务必完成。

### 一、项目介绍
本课程使用虚构技术咨询公司 **NovaTech Solutions** 作为演示项目：

- 极简官网：首页、服务、案例、团队、联系我们 共 5 个页面
- 技术栈：HTML + CSS + JavaScript
- 项目本身不复杂，主要作为**Claude Code 高级功能练习环境**
- 最终目标：完成外部工具集成、专属智能代理、自动化工作流

### 二、一键拉取项目

打开终端，克隆项目：
```bash
git clone https://github.com/nyisztor/novatech-demo.git
cd novatech-demo
```

### 三、安装依赖并启动

```bash
npm install
npm run dev
```
启动后在浏览器访问：

`http://localhost:3000/pages/index.html`

### 四、项目结构说明

- `src/`：网站源码（HTML、CSS、JS）
- `.claude/`：Claude Code 核心配置目录（**需开启显示隐藏文件**）
  - Mac：`Cmd + Shift + .`
- `scripts/`：Shell 脚本，用于后续并行开发
- `CLAUDE.md`：项目说明文档，帮助 Claude 快速理解代码库

### 五、验证环境是否正常

1. 在项目目录启动 Claude Code
2. 简单提问，例如：
   > 这个网站有哪些页面？
3. 如果 Claude 能正确识别 `src/pages` 下的 HTML 文件，说明配置成功。

一切正常后，我们就可以正式开始：**将 Claude Code 连接外部工具**。


