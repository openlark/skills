# Agent Skills

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

At its core, a skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, templates, and reference materials.

## Agent Skills Structure Directory

```
my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources
```

## Agent Skills List

<details open>
<summary><h3 style="display:inline">Efficiency Tools</h3></summary>

- [Douyin Keyword Collector](./skills/douyin-keyword-collector/SKILL.md) - Accessing the Douyin homepage through browser automation, entering keywords in the search bar and collecting relevant keyword suggestions in the automated prompt box.
- [Jinri Toutiao Keyword Collector](./skills/jinritoutiao-keyword-collector/SKILL.md) - Automatically accesses the Jinri Toutiao homepage via browser automation, inputs keywords into the search bar, and collects related keyword suggestions from the auto-suggest dropdown.
- [Toutiao Automatic Article Publishing](./skills/toutiao-graphic-publisher/SKILL.md) - Automatically publishes graphic content on Toutiao through browser automation, supporting intelligent formatting, automatic generation of popular tags, and tag activation.
- [Xiaohongshu Keyword Collector](./skills/xiaohongshu-keyword-collector/SKILL.md) - Automatically accesses Xiaohongshu's Explore page via browser automation, inputs keywords into the search bar, and collects the list of related keywords from the auto-suggest dropdown.
- [Xiaohongshu Automatic Image-Text Post Publishing](./skills/xiaohongshu-image-auto/SKILL.md) - After users provide a title and body text, automatically completes the entire process: login detection, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing.
- [Xiaohongshu Automatic Long-Form Post Publishing](./skills/xiaohongshu-longpost-auto/SKILL.md) - When users have long-form content ready to publish on Xiaohongshu, automatically completes the entire process: login detection, long content segmentation optimization, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing.

- [Humanizer AI](./skills/humanizer-ai/SKILL.md) - Identify and eliminate traces of AI-generated text, making writing sound more natural and human.
- [Detector AI](./skills/detector-ai/SKILL.md) - AI Detection Tool - Detect AI-generated text with multiple analysis methods including perplexity analysis, burstiness detection, readability scoring, and AI fingerprint detection. 
- [Turnitin AI Checker](./skills/turnitin-ai-checker/SKILL.md) - Turnitin AI Detection Checker - Check if text would be flagged by Turnitin's AI detection before submitting. 
- [AI Paraphraser](./skills/ai-paraphraser/SKILL.md) - AI paraphrasing and de-AI tool.
- [AI Paragraph Rewriter](./skills/ai-paragraph-rewriter/SKILL.md) - Rewrite paragraphs to sound natural and human-written, bypassing AI detectors (GPTZero, Turnitin, Originality.ai). 
- [Word Counter](./skills/word-counter/SKILL.md) - A comprehensive text analysis tool that counts words, characters, sentences, and paragraphs. Calculates reading time, speaking time, reading level (Flesch-Kincaid), and keyword density.
- [Grammar Checker](./skills/grammar-checker/SKILL.md) - AI-powered English grammar, spelling, and style checker.
- [Plagiarism Checker](./skills/plagiarism-checker/SKILL.md) - AI-powered English grammar, spelling, and style checker.
- [Text Summarizer](./skills/text-summarizer/SKILL.md) - Extractive AI text summarizer. Automatically extracts the most important sentences from any text using a hybrid TextRank + TF-IDF algorithm.
- [AI Prompt Optimization](./skills/ai-prompt-optimization/SKILL.md) - Use when users need to optimize prompts for AI conversations, generate structured templates, create few-shot examples, design chain-of-thought guidance, or diagnose and improve existing prompts. Applicable to prompt optimization for various AI tools such as ChatGPT, Claude, Midjourney, etc.

- [Agent Creation](./skills/agent-creation/SKILL.md) - Create a new OpenClaw agent with a workspace directory and SOUL.md configuration. Use when you need to create a new agent, set up an agent workspace, configure SOUL.md, or initialize agent memory structure.
- [Agent Daily Review](./skills/agent-daily-review/SKILL.md) - Helps agents conduct structured end-of-day review, reflection, and documentation. Provides capabilities to scan today's records, categorize activities, perform reflective analysis, and generate review reports. Supports Cron auto-trigger for cumulative growth with each run.
- [Agent Monitor](./skills/agent-monitor/SKILL.md) - Agent work status monitoring and automatic activation system. Triggers when monitoring subagent runtime status, detecting prolonged unresponsive "stalled" states, and automatically activating them to resume operation. Suitable for long-running task monitoring, automated operations, agent health checks, and similar scenarios.
- [Agent Browser Assistant](./skills/agent-browser-assistant/SKILL.md) - For browser automation tasks, web data scraping, form filling, page screenshots, UI testing, and more.
- [Multi-Agent Communication](./skills/multi-agent-communication/SKILL.md) - Based on two core tools, sessions_spawn and sessions_send, to help users build, manage, and optimize distributed Agent systems, enabling task decomposition, parallel processing, and efficient coordination among Agents.
- [Multi-Agent Collaboration Communication](./skills/multi-agent-collaboration-communication/SKILL.md) - Focused on multi-agent collaboration and communication scenarios, helping users build and manage complex distributed agent systems to achieve task decomposition, parallel processing, and collaborative work. Use this skill when users need to design multi-agent system architectures, plan task distribution schemes, establish inter-agent communication protocols, or implement distributed collaboration workflows.

- [Competitive Dimensions Analysis](./skills/competitive-dimensions-analysis/SKILL.md) - Conduct comprehensive competitor research through feature comparison matrices, product positioning analysis, differentiation strategy, and competitive impact assessment.

- [Skill Workflow Orchestrator](./skills/skill-workflow-orchestrator/SKILL.md) - Multi-skill workflow orchestrator. Chain multiple skills into automated pipelines, triggering entire sequences like "search → summarize → generate report → send email" with a single phrase. Supports conditional branching and error handling; serves as foundational infrastructure for building complex Agent workflows.
- [Self Apply Pressure](./skills/self-apply-pressure/SKILL.md) - Multi-skill workflow orchestrator. Chain multiple skills into automated pipelines, triggering entire sequences like "search → summarize → generate report → send email" with a single phrase. Supports conditional branching and error handling; serves as foundational infrastructure for building complex Agent workflows.
- [Context Relay](./skills/context-relay/SKILL.md) - Solves the memory fragmentation problem for Agents during session restarts, sub-agent boundaries, and cron/heartbeat isolation.
- [Token Cost Optimization](./skills/token-cost-optimization/SKILL.md) - Token savings and API cost optimization. Provides token calculator, three-tier optimization strategies (prompt compression / cache reuse / model downgrade), specific configuration guides, and quantified effect analysis.
- [Lightweight Team Orchestration](./skills/lightweight-team-orchestration/SKILL.md) - Lightweight multi-agent team orchestration. Output structure simplified to two folders: agents/ and projects/.
- [Task Orchestrator](./skills/task-orchestrator/SKILL.md) - Intelligent task management and execution coordination officer. Automatically generates task lists, intelligently decomposes complex tasks, matches AI agents, makes priority decisions, and monitors progress.

- [Content Trend Analyzer](./skills/content-trend-analyzer/SKILL.md) - Cross-platform content trend analysis and outline generation tool. Platforms covered include but are not limited to: Google Trends, Reddit, YouTube, Medium, Substack, Twitter/X, Zhihu, Weibo, Douyin, Bilibili, Baidu Index, WeChat Official Accounts, GitHub Trending, Product Hunt.
- [Deep Article Analysis](./skills/deep-article-analysis/SKILL.md) - Conduct in-depth analysis and interpretation of articles, extracting core viewpoints, key data, and deep insights.

- [Windows WeChat MCP](./skills/windows-wechat-mcp/SKILL.md) - Windows WeChat message monitoring and sending. Achieved through window automation: screenshot, search contacts, send messages. Use when needing to send messages to WeChat contacts, check WeChat window status, or perform WeChat-related automation tasks.

</details>

<details open>
<summary><h3 style="display:inline">Content Creation</h3></summary>

- [Idea Validator](./skills/idea-validator/SKILL.md) - Startup idea validation skill. Helps indie developers validate product ideas, analyze competitive landscapes, and assess market saturation.
- [Xiaohongshu Insight](./skills/xiaohongshu-insight/SKILL.md) - Xiaohongshu viral content data insight tool. Continuously collects 2000+ viral posts daily across the platform, based on criteria: low-follower viral posts, periodic high-engagement posts, single-day interaction spikes, and sustained interaction growth. Use for: Xiaohongshu content creation, viral content analysis, data reference, traffic trend tracking, and creative inspiration.
- [Wechat Article Generation Expert](./skills/wechat-article-generation-expert/SKILL.md) - Automatically create complete WeChat Official Account articles (≥1600 words) based on topic, audience, and style, including title ideation, structural planning, content writing, and multimedia element planning.
- [PRD Writing Expert](./skills/prd-writing-expert/SKILL.md) - Product Requirements Document (PRD) writing expert. Write structured product requirements documents, including problem statements, user stories, requirement prioritization, and success metrics. Applicable for feature specification writing, defining acceptance criteria, or documenting product decisions.
- [WeChat Business Article Writer](./skills/wechat-business-article-writer/SKILL.md) - Create WeChat public account style business and technology articles with professional yet approachable tone. 

- [Batch Content Factory ](./skills/batch-content-factory/SKILL.md) - Multi-platform content production line. Automates the entire workflow from topic research to content creation. Suitable for self-media operators producing high-quality content in bulk, content team collaboration, and brand content matrix management.


</details>

<details open>
<summary><h3 style="display:inline">Data & APIs</h3></summary>

- [News Express](./skills/news-express/SKILL.md) - Use this skill when users ask for news updates, daily briefings, or what's happening in the world. Fetches news from reliable international and Chinese RSS feeds. No API key required.

</details>

<details open>
<summary><h3 style="display:inline">Business Marketing</h3></summary>

- [Auto Acquisition](./skills/auto-acquisition/SKILL.md) - Customer acquisition and marketing automation expert.
- [Market Research Automation](./skills/market-research-automation/SKILL.md) - Market research automation skill. Mine user pain points from social media and analyze competitors. Applicable for market validation before product launch, user needs analysis, and competitor feature comparison.
- [SEO Content Pipeline](./skills/seo-content-pipeline/SKILL.md) - SEO automated content pipeline skill. Automates the entire workflow from competitor research and keyword mining to article generation and publishing.
- [Financial Report Tracker](./skills/financial-report-tracker/SKILL.md) - Automatically track tech company financial reports and generate investment summaries. Supports retrieving earnings calendars, market expectation comparisons, key metric interpretation, and more.

</details>

<details open>
<summary><h3 style="display:inline">Dev Tools</h3></summary>

- [Microsoft Edge TTS](./skills/microsoft-edge-tts/SKILL.md) - Use Microsoft Edge online TTS service to convert text to speech. Supports command line and module invocation, no API key.
- [Microsoft MarkItDown](./skills/microsoft-markitdown/SKILL.md) - Use MarkItDown to convert various files (PDF, Word, Excel, PPT, images, audio, HTML, CSV, JSON, etc.) to Markdown format for LLM processing and text analysis. Also supports content extraction from ZIP archives, YouTube videos, and EPUB e-books.
- [ECharts](./skills/apache-echarts/SKILL.md) - Apache ECharts charting skill.
- [Chart.js](./skills/chartjs/SKILL.md) - Chart.js charting skill. Used to generate visual charts such as line charts, bar charts, pie charts, radar charts, scatter plots, etc.
- [Favicons](./skills/favicons/SKILL.md) - Use the favicons Node.js library to generate multi-platform website icons (Favicons).etc.

- [Vercel CLI](./skills/vercel-cli/SKILL.md) - Vercel CLI skill for deploying and managing Vercel projects from the terminal.

- [SQLite Client](./skills/sqlite-client/SKILL.md) - SQLite database operations. Use this skill when users need to create, read, query, or modify SQLite databases (.db files).

- [VitePress Static Website Generator](./skills/vitepress-generator/SKILL.md) - Quickly generate static websites using VitePress. Supports installing dependencies, initializing projects, local preview, building, and deployment.

- [Static Site Cloner](./skills/static-site-cloner/SKILL.md) - Static site reproduction expert - Analyze target websites and manually code their structure, visual style, and basic interactions using pure HTML/CSS/JavaScript.

- [Mustache](./skills/mustache/SKILL.md) - Use mustache.js (logic-less Mustache templates) for any templating task in JavaScript/Node.js environments.

- [HTML DOM To Image](./skills/dom-to-image/SKILL.md) - Convert HTML DOM nodes to images (PNG/JPEG/SVG/Blob). Supports rendering options such as filter, backgroundColor, quality, and pixelRatio.

- [DOM Capture Engine](./skills/snapdom/SKILL.md) - Convert HTML DOM nodes to images (PNG/JPEG/SVG/Blob). Supports rendering options such as filter, backgroundColor, quality, and pixelRatio.

</details>