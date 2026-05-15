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
- [WeChat Official Account Article Auto-Publisher](./skills/wechat-mp-article-publisher/SKILL.md) - Complete the creation, editing, and publishing of WeChat Official Account articles through browser automation simulating manual operation. No API key required; operates directly on the Official Account platform backend.

- [Social Media Automation Operations Assistant](./skills/social-auto-publisher/SKILL.md) - Social media automation operations assistant. Automatically generate and publish content for Xiaohongshu, Weibo, and Twitter, with scheduled posting and interactive replies. Covers the full chain from content creation → AI illustration → scheduled publishing → interaction monitoring → data review.

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

- [OpenClaw 7x24 Watchdog & Auto-Healer](./skills/guardian-auto-healer/SKILL.md) - OpenClaw 7x24 watchdog & auto-healer. Monitors gateway health, memory usage, zombie sessions, and disk space every 5 minutes with automatic restart when stuck.

- [Competitive Dimensions Analysis](./skills/competitive-dimensions-analysis/SKILL.md) - Conduct comprehensive competitor research through feature comparison matrices, product positioning analysis, differentiation strategy, and competitive impact assessment.

- [Marketing Psychology Expert](./skills/marketing-psychology-expert/SKILL.md) - Helps deeply understand consumer psychology and behavioral patterns based on psychological principles, providing strategic guidance on price anchoring, scarcity effect, social proof, reciprocity principle, loss aversion, framing effect, and more.

- [Skill Workflow Orchestrator](./skills/skill-workflow-orchestrator/SKILL.md) - Multi-skill workflow orchestrator. Chain multiple skills into automated pipelines, triggering entire sequences like "search → summarize → generate report → send email" with a single phrase. Supports conditional branching and error handling; serves as foundational infrastructure for building complex Agent workflows.
- [Self Apply Pressure](./skills/self-apply-pressure/SKILL.md) - Multi-skill workflow orchestrator. Chain multiple skills into automated pipelines, triggering entire sequences like "search → summarize → generate report → send email" with a single phrase. Supports conditional branching and error handling; serves as foundational infrastructure for building complex Agent workflows.
- [Context Relay](./skills/context-relay/SKILL.md) - Solves the memory fragmentation problem for Agents during session restarts, sub-agent boundaries, and cron/heartbeat isolation.
- [Token Cost Optimization](./skills/token-cost-optimization/SKILL.md) - Token savings and API cost optimization. Provides token calculator, three-tier optimization strategies (prompt compression / cache reuse / model downgrade), specific configuration guides, and quantified effect analysis.
- [Lightweight Team Orchestration](./skills/lightweight-team-orchestration/SKILL.md) - Lightweight multi-agent team orchestration. Output structure simplified to two folders: agents/ and projects/.
- [Task Orchestrator](./skills/task-orchestrator/SKILL.md) - Intelligent task management and execution coordination officer. Automatically generates task lists, intelligently decomposes complex tasks, matches AI agents, makes priority decisions, and monitors progress.

- [Content Trend Analyzer](./skills/content-trend-analyzer/SKILL.md) - Cross-platform content trend analysis and outline generation tool. Platforms covered include but are not limited to: Google Trends, Reddit, YouTube, Medium, Substack, Twitter/X, Zhihu, Weibo, Douyin, Bilibili, Baidu Index, WeChat Official Accounts, GitHub Trending, Product Hunt.
- [Deep Article Analysis](./skills/deep-article-analysis/SKILL.md) - Conduct in-depth analysis and interpretation of articles, extracting core viewpoints, key data, and deep insights.

- [Windows WeChat MCP](./skills/windows-wechat-mcp/SKILL.md) - Windows WeChat message monitoring and sending. Achieved through window automation: screenshot, search contacts, send messages. Use when needing to send messages to WeChat contacts, check WeChat window status, or perform WeChat-related automation tasks.

- [Prompt Optimizer Claude](./skills/prompt-optimizer-claude/SKILL.md) - Professional-grade Claude prompt optimization engine. Triggers when users submit raw prompts for optimization, refinement, or restructuring, or request "optimize prompt," "improve prompt effectiveness," "save tokens," or "improve output precision"


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
<summary><h3 style="display:inline">Security</h3></summary>

- [Code and System Security Review](./skills/code-security-review/SKILL.md) - Report only real risks, not manufactured panic. Covers injection, XSS, path traversal, insecure deserialization, authentication and authorization flaws, key leaks, insecure logging, command execution, and other common vulnerabilities.

</details>

<details open>
<summary><h3 style="display:inline">Business Marketing</h3></summary>

- [Auto Acquisition](./skills/auto-acquisition/SKILL.md) - Customer acquisition and marketing automation expert.
- [Market Research Automation](./skills/market-research-automation/SKILL.md) - Market research automation skill. Mine user pain points from social media and analyze competitors. Applicable for market validation before product launch, user needs analysis, and competitor feature comparison.
- [SEO Content Pipeline](./skills/seo-content-pipeline/SKILL.md) - SEO automated content pipeline skill. Automates the entire workflow from competitor research and keyword mining to article generation and publishing.
- [AI Citation Strategist](./skills/ai-citation-strategist/SKILL.md) - AI Recommendation Engine Optimization (AEO/GEO) expert. Audit brand visibility on platforms such as ChatGPT, Claude, Gemini, and Perplexity. Analyze why competitors are cited and provide content optimization strategies to improve AI citation rates.
- [Financial Report Tracker](./skills/financial-report-tracker/SKILL.md) - Automatically track tech company financial reports and generate investment summaries. Supports retrieving earnings calendars, market expectation comparisons, key metric interpretation, and more.
- [Data Analysis Report Generator](./skills/data-analysis-report-generator/SKILL.md) - Intelligent data analysis report generator. Auto-identifies Excel/CSV data structure (dimensions, metrics, timelines), performs multi-dimensional parallel analysis, and generates professional HTML reports with ECharts interactive charts. 
- [Full-Link Data Analysis](./skills/full-link-data-analysis/SKILL.md) - Full-Link Data Analysis Engine: From business议题 to analytical report with complete seven-layer architecture. Built-in 15 analysis methods, supports data-aware routing (议题 semantics + data structure + problem type three dimensions), built-in quality assurance, outputs Feishu doc format analytical reports.

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

- [ZX](./skills/zx/SKILL.md) - Comprehensive guide for writing shell scripts with Google zx — a tool for writing better scripts using JavaScript/TypeScript. Use when writing, debugging, or refactoring zx scripts (.mjs, .js, .ts files using zx), executing shell commands from JavaScript, working with ProcessPromise/ProcessOutput APIs, piping streams, configuring zx options, or using zx CLI.  Do NOT use for general Node.js questions unrelated to shell scripting.

- [@clack/prompts](./skills/clack-prompts/SKILL.md) - Build beautiful interactive Node.js command-line apps with @clack/prompts. Use when building CLI apps, wizards, setup scripts, or any interactive terminal prompt flow in Node.js. Covers text input, password, confirm, select, autocomplete, multiselect, spinner, progress bars, grouped prompts, task runners, and styled logging.

- [Google Web Fonts](./skills/google-web-fonts/SKILL.md) - Use the Google Fonts API to add fonts to web pages.

- [VitePress Static Website Generator](./skills/vitepress-generator/SKILL.md) - Quickly generate static websites using VitePress. Supports installing dependencies, initializing projects, local preview, building, and deployment.

- [Static Site Cloner](./skills/static-site-cloner/SKILL.md) - Static site reproduction expert - Analyze target websites and manually code their structure, visual style, and basic interactions using pure HTML/CSS/JavaScript.

- [Mustache](./skills/mustache/SKILL.md) - Use mustache.js (logic-less Mustache templates) for any templating task in JavaScript/Node.js environments.

- [HTML DOM To Image](./skills/dom-to-image/SKILL.md) - Convert HTML DOM nodes to images (PNG/JPEG/SVG/Blob). Supports rendering options such as filter, backgroundColor, quality, and pixelRatio.

- [DOM Capture Engine](./skills/snapdom/SKILL.md) - Convert HTML DOM nodes to images (PNG/JPEG/SVG/Blob). Supports rendering options such as filter, backgroundColor, quality, and pixelRatio.

- [Gray Matter](./skills/gray-matter/SKILL.md) - Parse YAML/JSON/TOML front-matter from strings or files using the gray-matter library.

- [Social Media Cover Image Generator](./skills/social-media-cover-generator/SKILL.md) - Social media cover image generator. Generates HTML pages based on title content and automatically converts them to PNG images, suitable for creating cover images and graphics for platforms such as Xiaohongshu, WeChat Official Accounts, Weibo, Douyin, Bilibili, Zhihu, Twitter/X, Instagram, and LinkedIn.

- [LEGO Pixel Art Generator](./skills/lego-pixel-art/SKILL.md) - Convert any image into LEGO brick pixel art, generating a complete building plan and material purchase list. Built-in standard LEGO color system, supports custom sizes (10-200 studs) and color precision adjustment, outputs a row-by-row building guide. Pure frontend implementation, zero dependencies, ready to use out of the box. Suitable for LEGO enthusiasts, craft creators, and educators.

- [Mermaid Diagram Generation](./skills/mermaid-chart/SKILL.md) - Generate various diagrams using Mermaid syntax (flowcharts, sequence diagrams, Gantt charts, class diagrams, state diagrams, pie charts, ER diagrams, mind maps, timelines, C4 architecture diagrams, user journey maps, Git graphs, Sankey diagrams, quadrant charts, etc.). Supports inline rendering in Markdown.

- [Tesseract OCR Image Text Extraction](./skills/tesseract-image-ocr/SKILL.md) - Extract text from images using Tesseract.js (OCR). Supports multi-language recognition including Chinese and English, region recognition, character whitelist filtering, text orientation detection, and can run in a Node.js environment.

- [Node Cron](./skills/node-cron/SKILL.md) - Node.js cron job scheduling with the `cron` npm package. Use when the user needs to schedule recurring tasks, create cron jobs, validate cron expressions, set up timed callbacks, or work with cron syntax in a Node.js/TypeScript project. 

- [ImapFlow](./skills/imapflow/SKILL.md) - Modern Node.js IMAP client library (imapflow) for email integration.Covers authentication, mailbox locking, streaming fetches, async iterators, reconnection strategies, proxy support, and provider-specific configs (Gmail, Outlook, Yahoo, etc.).

- [Archiver — Streaming Archive Packaging](./skills/archiver/SKILL.md) - Use the Archiver library for streaming archive packaging in Node.js. Supports creating ZIP/TAR archives, appending content from streams, strings, buffers, file paths, directories, and glob patterns, as well as registering custom formats. 

- [WebTorrent — Streaming Torrent Client](./skills/webtorrent/SKILL.md) - Use WebTorrent to implement streaming BitTorrent client functionality in Node.js and the browser. Supports torrent downloading, seeding, magnet links, streaming media playback, and peer-to-peer transfer (via WebRTC Data Channel in the browser, and TCP/UDP in Node.js). 

- [dotenv — Node.js Environment Variable Loader](./skills/dotenv/SKILL.md) - Use dotenv to manage environment variables for Node.js projects.

- [Fully Automated Collaborative Code Development Pipeline](./skills/auto-collaboration-dev-pipeline/SKILL.md) - Fully automated collaborative code development pipeline for complex code development tasks. Must be used when users request code development, program writing, feature implementation, or have code quality requirements.

- [Macaron Card Generator](./skills/macaron-card-generator/SKILL.md) - Generate beautiful macaron-color cartoon illustration-style card images from text content. Supports various types such as book recommendation cards, concept cards, quote cards, and comparison cards, with multiple aspect ratios including 3:4, 9:16, and 1:1.

- [Tarot Card Reader](./skills/tarot-card-reader/SKILL.md) - Based on a complete tarot knowledge base and systematic interpretation guide, provides accurate readings for various classic spreads along with comprehensive advice, helping seekers engage in self-exploration, gain inspiration, and receive directional guidance through tarot cards.

- [Crawl4AI Web Crawler](./skills/crawl4ai-web-crawler/SKILL.md) - Use Crawl4AI for web scraping and content extraction. Use when users need to scrape web content, extract structured data, convert web pages to Markdown, perform batch crawling, or use AI-driven web data collection.

- [Open RAGFlow](./skills/open-ragflow/SKILL.md) - Open-source RAG engine fusing RAG with Agent capabilities. Full-stack: Python backend (Flask), React/TypeScript frontend, Docker-deployed microservices.

- [Web Push Notifications](./skills/web-push/SKILL.md) - Send Web Push notifications from a Node.js backend using the web-push npm library (VAPID authentication, payload encryption). Covers generating VAPID keys, subscribing browsers, sending notifications, CLI usage, browser compatibility, and common pitfalls.

- [markdown-it](./skills/markdown-it/SKILL.md) - Use markdown-it to render Markdown to HTML, configure plugins, custom rendering rules, syntax highlighting.

- [minimatch](./skills/minimatch/SKILL.md) - Use minimatch (glob pattern matching library) for file path matching, such as *.js, **/*.ts and other glob patterns. Note: Do NOT use user input as pattern source to prevent ReDoS attacks.

</details>