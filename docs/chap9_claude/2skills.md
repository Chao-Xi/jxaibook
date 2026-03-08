
```

```


```
$ openskills install anthropics/skills --global
Installing from: anthropics/skills
Location: global (~/.claude/skills)
Global install selected (~/.claude/skills). Omit --global for ./.claude/skills.

✔ Repository cloned
Found 17 skill(s)

✔ Select skills to install algorithmic-art           58.4KB, brand-guidelines          13.3KB, canvas-design        
     5.3MB, doc-coauthoring           15.4KB, docx                      1.1MB, frontend-design           14.3KB,
internal-comms            21.9KB, mcp-builder               118.9KB, pdf                       57.3KB, pptx         
             1.1MB, skill-creator             218.6KB, slack-gif-creator         42.7KB, theme-factory            
140.7KB, web-artifacts-builder     44.8KB, webapp-testing            21.9KB, xlsx                      1.0MB,
template                  140B

⚠️  Warning: 'algorithmic-art' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: algorithmic-art

⚠️  Warning: 'brand-guidelines' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: brand-guidelines

⚠️  Warning: 'canvas-design' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: canvas-design
✅ Installed: doc-coauthoring

⚠️  Warning: 'docx' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: docx
✅ Installed: frontend-design

⚠️  Warning: 'internal-comms' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: internal-comms

⚠️  Warning: 'mcp-builder' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: mcp-builder

⚠️  Warning: 'pdf' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: pdf

⚠️  Warning: 'pptx' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: pptx

⚠️  Warning: 'skill-creator' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: skill-creator

⚠️  Warning: 'slack-gif-creator' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: slack-gif-creator

⚠️  Warning: 'theme-factory' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: theme-factory
✅ Installed: web-artifacts-builder

⚠️  Warning: 'webapp-testing' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: webapp-testing

⚠️  Warning: 'xlsx' matches an Anthropic marketplace skill
   Installing globally may conflict with Claude Code plugins.
   If you re-enable Claude plugins, this will be overwritten.
   Recommend: Use --project flag for conflict-free installation.

✅ Installed: xlsx
✅ Installed: template

✅ Installation complete: 17 skill(s) installed

Read skill: npx openskills read <skill-name>
```

```
openskills install anthropics/skills --universal
```


```
% openskills list

Available Skills:

  algorithmic-art           (project)
    Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

  brand-guidelines          (project)
    Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.

  canvas-design             (project)
    Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

  doc-coauthoring           (project)
    Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

  docx                      (project)
    "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation."

  frontend-design           (project)
    Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

  internal-comms            (project)
    A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

  mcp-builder               (project)
    Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

  pdf                       (project)
    Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

  pptx                      (project)
    "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill."

  skill-creator             (project)
    Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

  slack-gif-creator         (project)
    Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."

  template                  (project)
    Replace with description of the skill and when Claude should use it.

  theme-factory             (project)
    Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

  web-artifacts-builder     (project)
    Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

  webapp-testing            (project)
    Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

  xlsx                      (project)
    "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved."

Summary: 17 project, 0 global (17 total)
```