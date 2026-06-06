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
<summary><h3 style="display:inline">Social Media Automation</h3></summary>

- [Douyin Keyword Collector](./skills/douyin-keyword-collector/SKILL.md) - Accessing the Douyin homepage through browser automation, entering keywords in the search bar and collecting relevant keyword suggestions in the automated prompt box.
- [Jinri Toutiao Keyword Collector](./skills/jinritoutiao-keyword-collector/SKILL.md) - Automatically accesses the Jinri Toutiao homepage via browser automation, inputs keywords into the search bar, and collects related keyword suggestions from the auto-suggest dropdown.
- [Toutiao Automatic Article Publishing](./skills/toutiao-graphic-publisher/SKILL.md) - Automatically publishes graphic content on Toutiao through browser automation, supporting intelligent formatting, automatic generation of popular tags, and tag activation.
- [Xiaohongshu Keyword Collector](./skills/xiaohongshu-keyword-collector/SKILL.md) - Automatically accesses Xiaohongshu's Explore page via browser automation, inputs keywords into the search bar, and collects the list of related keywords from the auto-suggest dropdown.
- [Xiaohongshu Automatic Image-Text Post Publishing](./skills/xiaohongshu-image-auto/SKILL.md) - After users provide a title and body text, automatically completes the entire process: login detection, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing.
- [Xiaohongshu Automatic Long-Form Post Publishing](./skills/xiaohongshu-longpost-auto/SKILL.md) - When users have long-form content ready to publish on Xiaohongshu, automatically completes the entire process: login detection, long content segmentation optimization, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing.
- [WeChat Official Account Article Auto-Publisher](./skills/wechat-mp-article-publisher/SKILL.md) - Complete the creation, editing, and publishing of WeChat Official Account articles through browser automation simulating manual operation. No API key required; operates directly on the Official Account platform backend.
- [Social Media Automation Operations Assistant](./skills/social-auto-publisher/SKILL.md) - Social media automation operations assistant. Automatically generate and publish content for Xiaohongshu, Weibo, and Twitter, with scheduled posting and interactive replies. Covers the full chain from content creation → AI illustration → scheduled publishing → interaction monitoring → data review.
- [Xiaohongshu Insight](./skills/xiaohongshu-insight/SKILL.md) - Xiaohongshu viral content data insight tool. Continuously collects 2000+ viral posts daily across the platform, based on criteria: low-follower viral posts, periodic high-engagement posts, single-day interaction spikes, and sustained interaction growth.

</details>

<details open>
<summary><h3 style="display:inline">AI Writing & Text Tools</h3></summary>

- [Humanizer AI](./skills/humanizer-ai/SKILL.md) - Identify and eliminate traces of AI-generated text, making writing sound more natural and human.
- [Detector AI](./skills/detector-ai/SKILL.md) - AI Detection Tool - Detect AI-generated text with multiple analysis methods including perplexity analysis, burstiness detection, readability scoring, and AI fingerprint detection.
- [Turnitin AI Checker](./skills/turnitin-ai-checker/SKILL.md) - Turnitin AI Detection Checker - Check if text would be flagged by Turnitin's AI detection before submitting.
- [AI Paraphraser](./skills/ai-paraphraser/SKILL.md) - AI paraphrasing and de-AI tool.
- [AI Paragraph Rewriter](./skills/ai-paragraph-rewriter/SKILL.md) - Rewrite paragraphs to sound natural and human-written, bypassing AI detectors (GPTZero, Turnitin, Originality.ai).
- [Word Counter](./skills/word-counter/SKILL.md) - A comprehensive text analysis tool that counts words, characters, sentences, and paragraphs. Calculates reading time, speaking time, reading level (Flesch-Kincaid), and keyword density.
- [Grammar Checker](./skills/grammar-checker/SKILL.md) - AI-powered English grammar, spelling, and style checker.
- [Plagiarism Checker](./skills/plagiarism-checker/SKILL.md) - AI-powered English grammar, spelling, and style checker.
- [Text Summarizer](./skills/text-summarizer/SKILL.md) - Extractive AI text summarizer. Automatically extracts the most important sentences from any text using a hybrid TextRank + TF-IDF algorithm.

</details>

<details open>
<summary><h3 style="display:inline">Prompt Engineering</h3></summary>

- [Lyra — Cognitive Architect](./skills/lyra-prompt-architect/SKILL.md) - Advanced prompt architect (Lyra v2) that builds precise, high-performance prompts from scratch through structured dialogue and advanced reasoning frameworks (CoT/ToT/GoT/AoT). Uses a four-phase architectural process: Dialogue → Blueprint → Synthesis → Refinement. Suitable for complex prompt engineering, task decomposition, and cognitive architecture design.
- [AI Prompt Optimization](./skills/ai-prompt-optimization/SKILL.md) - Use when users need to optimize prompts for AI conversations, generate structured templates, create few-shot examples, design chain-of-thought guidance, or diagnose and improve existing prompts. Applicable to prompt optimization for various AI tools such as ChatGPT, Claude, Midjourney, etc.
- [Prompt Optimizer Claude](./skills/prompt-optimizer-claude/SKILL.md) - Professional-grade Claude prompt optimization engine. Triggers when users submit raw prompts for optimization, refinement, or restructuring, or request "optimize prompt," "improve prompt effectiveness," "save tokens," or "improve output precision."
- [AI Prompt Optimization Expert](./skills/ai-prompt-optimization-expert/SKILL.md) - Professional AI prompt optimization expert that analyzes and optimizes user prompts using the CRISP framework (Clarity/Role/Instructions/Structure/Precision). Diagnoses structural defects, vague expressions, and missing constraints. Outputs clear, precisely crafted optimized versions.
- [Game Design Expert](./skills/game-design-expert/SKILL.md) - A game design expert that comprehensively analyzes and designs HTML5 game proposals based on game name input. Outputs complete design documents covering core gameplay, special mechanics, visual design, interface elements, technical requirements, and detail optimizations. 

</details>

<details open>
<summary><h3 style="display:inline">Agent Management & Infrastructure</h3></summary>

- [Agent Creation](./skills/agent-creation/SKILL.md) - Create a new OpenClaw agent with a workspace directory and SOUL.md configuration. Use when you need to create a new agent, set up an agent workspace, configure SOUL.md, or initialize agent memory structure.
- [Agent Daily Review](./skills/agent-daily-review/SKILL.md) - Helps agents conduct structured end-of-day review, reflection, and documentation. Provides capabilities to scan today's records, categorize activities, perform reflective analysis, and generate review reports. Supports Cron auto-trigger for cumulative growth with each run.
- [Agent Monitor](./skills/agent-monitor/SKILL.md) - Agent work status monitoring and automatic activation system. Triggers when monitoring subagent runtime status, detecting prolonged unresponsive "stalled" states, and automatically activating them to resume operation. Suitable for long-running task monitoring, automated operations, agent health checks, and similar scenarios.
- [Agent Browser Assistant](./skills/agent-browser-assistant/SKILL.md) - For browser automation tasks, web data scraping, form filling, page screenshots, UI testing, and more.
- [Multi-Agent Communication](./skills/multi-agent-communication/SKILL.md) - Based on two core tools, sessions_spawn and sessions_send, to help users build, manage, and optimize distributed Agent systems, enabling task decomposition, parallel processing, and efficient coordination among Agents.
- [Multi-Agent Collaboration Communication](./skills/multi-agent-collaboration-communication/SKILL.md) - Focused on multi-agent collaboration and communication scenarios, helping users build and manage complex distributed agent systems to achieve task decomposition, parallel processing, and collaborative work. Use this skill when users need to design multi-agent system architectures, plan task distribution schemes, establish inter-agent communication protocols, or implement distributed collaboration workflows.
- [OpenClaw 7x24 Watchdog & Auto-Healer](./skills/guardian-auto-healer/SKILL.md) - OpenClaw 7x24 watchdog & auto-healer. Monitors gateway health, memory usage, zombie sessions, and disk space every 5 minutes with automatic restart when stuck.
- [Skill Workflow Orchestrator](./skills/skill-workflow-orchestrator/SKILL.md) - Multi-skill workflow orchestrator. Chain multiple skills into automated pipelines, triggering entire sequences like "search → summarize → generate report → send email" with a single phrase. Supports conditional branching and error handling; serves as foundational infrastructure for building complex Agent workflows.
- [Self Apply Pressure](./skills/self-apply-pressure/SKILL.md) - Multi-skill workflow orchestrator. Chain multiple skills into automated pipelines, triggering entire sequences like "search → summarize → generate report → send email" with a single phrase. Supports conditional branching and error handling; serves as foundational infrastructure for building complex Agent workflows.
- [Context Relay](./skills/context-relay/SKILL.md) - Solves the memory fragmentation problem for Agents during session restarts, sub-agent boundaries, and cron/heartbeat isolation.
- [Lightweight Team Orchestration](./skills/lightweight-team-orchestration/SKILL.md) - Lightweight multi-agent team orchestration. Output structure simplified to two folders: agents/ and projects/.
- [Task Orchestrator](./skills/task-orchestrator/SKILL.md) - Intelligent task management and execution coordination officer. Automatically generates task lists, intelligently decomposes complex tasks, matches AI agents, makes priority decisions, and monitors progress.

</details>

<details open>
<summary><h3 style="display:inline">Skill Development</h3></summary>

- [Agent Skills](./skills/agent-skills/SKILL.md) - Agent Skills standard reference guide. Covers SKILL.md specification format, progressive disclosure mechanism, skill discovery and activation, frontmatter metadata fields, directory structure conventions.
- [Skill Distiller](./skills/skill-distiller/SKILL.md) - Skill Distiller. Triggered when users encounter repetitive problems, need to systematize a solution in a certain domain, or want to solidify someone's methodology into a reusable operational process.
- [Personality Distiller](./skills/personality-distiller/SKILL.md) - Personality Distiller — Automatically distill from name/vague requirement/link/existing Skill/local corpus into complete Agent persona file pack via deep research to framework extraction, directly overwriting current workspace persona files.

</details>

<details open>
<summary><h3 style="display:inline">Content Strategy & Writing</h3></summary>

- [Content Trend Analyzer](./skills/content-trend-analyzer/SKILL.md) - Cross-platform content trend analysis and outline generation tool. Platforms covered include but are not limited to: Google Trends, Reddit, YouTube, Medium, Substack, Twitter/X, Zhihu, Weibo, Douyin, Bilibili, Baidu Index, WeChat Official Accounts, GitHub Trending, Product Hunt.
- [Deep Article Analysis](./skills/deep-article-analysis/SKILL.md) - Conduct in-depth analysis and interpretation of articles, extracting core viewpoints, key data, and deep insights.
- [Search Synthesis Expert](./skills/search-synthesis-expert/SKILL.md) - Uses sequential-thinking to decompose tasks and formulate search strategies, browser automation (Playwright) for multi-source information search and collection, and final review of synthesized results. Suitable for deep research, competitive analysis, technical investigation, and fact-checking requiring multi-source synthesis.
- [Competitive Dimensions Analysis](./skills/competitive-dimensions-analysis/SKILL.md) - Conduct comprehensive competitor research through feature comparison matrices, product positioning analysis, differentiation strategy, and competitive impact assessment.
- [Marketing Psychology Expert](./skills/marketing-psychology-expert/SKILL.md) - Helps deeply understand consumer psychology and behavioral patterns based on psychological principles, providing strategic guidance on price anchoring, scarcity effect, social proof, reciprocity principle, loss aversion, framing effect, and more.
- [Idea Validator](./skills/idea-validator/SKILL.md) - Startup idea validation skill. Helps indie developers validate product ideas, analyze competitive landscapes, and assess market saturation.

</details>

<details open>
<summary><h3 style="display:inline">Content Creation</h3></summary>

- [Wechat Article Generation Expert](./skills/wechat-article-generation-expert/SKILL.md) - Automatically create complete WeChat Official Account articles (≥1600 words) based on topic, audience, and style, including title ideation, structural planning, content writing, and multimedia element planning.
- [WeChat Business Article Writer](./skills/wechat-business-article-writer/SKILL.md) - Create WeChat public account style business and technology articles with professional yet approachable tone.
- [Batch Content Factory](./skills/batch-content-factory/SKILL.md) - Multi-platform content production line. Automates the entire workflow from topic research to content creation. Suitable for self-media operators producing high-quality content in bulk, content team collaboration, and brand content matrix management.
- [PRD Writing Expert](./skills/prd-writing-expert/SKILL.md) - Product Requirements Document (PRD) writing expert. Write structured product requirements documents, including problem statements, user stories, requirement prioritization, and success metrics. Applicable for feature specification writing, defining acceptance criteria, or documenting product decisions.
- [Technical Documentation Translator](./skills/tech-translator/SKILL.md) - Professional technical documentation translation expert, proficient in internet industry terminology. Translates user-provided files, preserves original formatting, and performs professional accuracy and format validation.
- [Mind Map Creation Expert](./skills/mindmap-creation/SKILL.md) - Mind map creation expert that produces structured, hierarchical mind maps based on user-provided topics. Breaks down complex knowledge into logically clear tree structures.
- [AI Note Assistant](./skills/note-ai-assistant/SKILL.md) - Advanced AI-powered note assistant built into a note editor. Understands the three-layer context structure (Document/Block/Selection), distinguishes between "instruction mode" (silently replace selected text) and "question mode" (provide answers). Preserves custom MDX tags and seamlessly integrates with note content. Suitable for smart note apps, knowledge management tools, and AI writing assistants.

</details>

<details open>
<summary><h3 style="display:inline">Novel & Creative Writing</h3></summary>

- [Multi-Dimensional Novel Evaluation System](./skills/novel-reviewer/SKILL.md) - Multi-dimensional novel evaluation based on provided content, assessing across plot, characters, writing quality, worldbuilding, pacing, originality, emotional resonance, dialogue quality, structure, and reader appeal, producing a total score. Use for book reviews, work evaluation, creative feedback, web novel assessment, and similar scenarios.
- [Professional Novel Writing Techniques](./skills/novel-writing-techniques/SKILL.md) - Covers six core writing techniques — dual narrative/mirroring, character biography method, foreshadowing (Cao Xueqin's "gray thread" technique), poetic language style, morally gray character development, and hardcore intellectual duel design. Helps writers enhance the depth, logic, and literary quality of their novels.
- [Web Novel Writing Assistant](./skills/web-novel-writing-assistant/SKILL.md) - Web novel writing assistant, solving core pain points: context loss, inconsistent style, setting conflicts, pacing issues, multi-plot confusion, unstable quality, and inability to internalize reader feedback.
- [Anime Storyboard Prompt Generation](./skills/storyboard-prompt-generator/SKILL.md) - Parse anime storyboard scripts and generate four types of prompts: character prompts, scene prompts, Sora video generation prompts, and standard storyboard prompts.
- [Contrast Poster Prompt Generator](./skills/contrast-poster-prompt/SKILL.md) - Match the most suitable type from 15 contrast gameplay styles (gender, age, identity, image, scene, object, role, consumption/economy, pre-post state, skill level, cognitive common sense, time-space dislocation, tone/attitude, item function, physique/appearance) based on user needs, generate high-quality English AI drawing prompts and Chinese poster copy.

</details>

<details open>
<summary><h3 style="display:inline">Storyboarding & Video</h3></summary>

- [Storyboard Master — Video Storyboard Script Expert](./skills/storyboard-master/SKILL.md) - Senior video storyboard expert turning creative briefs into visual storyboard scripts. Covers short films, commercials, promotional videos. Output includes shot number, shot size, camera movement, visual description, dialogue, duration, lighting and color. Suitable for video production, advertising planning, pre-production.

</details>

<details open>
<summary><h3 style="display:inline">Utility Tools</h3></summary>

- [Windows WeChat MCP](./skills/windows-wechat-mcp/SKILL.md) - Windows WeChat message monitoring and sending. Achieved through window automation: screenshot, search contacts, send messages. Use when needing to send messages to WeChat contacts, check WeChat window status, or perform WeChat-related automation tasks.
- [Token Cost Optimization](./skills/token-cost-optimization/SKILL.md) - Token savings and API cost optimization. Provides token calculator, three-tier optimization strategies (prompt compression / cache reuse / model downgrade), specific configuration guides, and quantified effect analysis.
- [News Express](./skills/news-express/SKILL.md) - Use this skill when users ask for news updates, daily briefings, or what's happening in the world. Fetches news from reliable international and Chinese RSS feeds. No API key required.
- [UI Scanner — Website Design System Extraction](./skills/ui-scanner/SKILL.md) - Given a website URL, crawl and analyze its visual design system — identify design style, color system, typography, component styles, and UI patterns. Outputs a structured design specification document for UI generation.
- [Bazi Qimen](./skills/bazi-qimen/SKILL.md) - Bazi (Four Pillars Astrology) and Qi Men Dun Jia chart calculation and interpretation skills. Provides data analysis and cognitive science based calculations and interpretations, serving as an auxiliary decision-making reference rooted in traditional Chinese metaphysics.
- [Tarot Card Reader](./skills/tarot-card-reader/SKILL.md) - Based on a complete tarot knowledge base and systematic interpretation guide, provides accurate readings for various classic spreads along with comprehensive advice, helping seekers engage in self-exploration, gain inspiration, and receive directional guidance through tarot cards.

</details>

<details open>
<summary><h3 style="display:inline">Security</h3></summary>

- [Code and System Security Review](./skills/code-security-review/SKILL.md) - Report only real risks, not manufactured panic. Covers injection, XSS, path traversal, insecure deserialization, authentication and authorization flaws, key leaks, insecure logging, command execution, and other common vulnerabilities.

</details>

<details open>
<summary><h3 style="display:inline">Marketing & Business Strategy</h3></summary>

- [Auto Acquisition](./skills/auto-acquisition/SKILL.md) - Customer acquisition and marketing automation expert.
- [Market Research Automation](./skills/market-research-automation/SKILL.md) - Market research automation skill. Mine user pain points from social media and analyze competitors. Applicable for market validation before product launch, user needs analysis, and competitor feature comparison.
- [SEO Content Pipeline](./skills/seo-content-pipeline/SKILL.md) - SEO automated content pipeline skill. Automates the entire workflow from competitor research and keyword mining to article generation and publishing.
- [AI Citation Strategist](./skills/ai-citation-strategist/SKILL.md) - AI Recommendation Engine Optimization (AEO/GEO) expert. Audit brand visibility on platforms such as ChatGPT, Claude, Gemini, and Perplexity. Analyze why competitors are cited and provide content optimization strategies to improve AI citation rates.
- [Business Model Canvas Analysis](./skills/business-model-canvas-analysis/SKILL.md) - Business Model Canvas analysis tool. Use when users need to analyze company business models, perform business model canvas modeling, deconstruct business logic, evaluate profit models, or write business analysis reports.
- [Marketing Copywriting Master](./skills/marketing-copywriting-master/SKILL.md) - Professional marketing copywriter. Analyzes product features to extract core selling points, crafts compelling headlines and copy, and adapts content for multiple distribution channels. Use when users need to write product marketing copy, advertising copy, promotional content, or social media marketing copy.
- [Planning Document Writing Assistant](./skills/write-planning-document/SKILL.md) - Compose a complete planning document based on a given topic, including core elements such as planning objectives, detailed plans, resource budgets, performance evaluation, and risk response. Use when the user needs to write a strategic plan, event plan, project proposal, or planning document.
- [Promotion Strategy Writing Assistant](./skills/write-promotion-strategy/SKILL.md) - Write a comprehensive promotion strategy based on provided product information, including product selling point extraction, multi-channel promotion planning, goal setting, and expected outcome evaluation. Use when the user needs to write a product promotion strategy, develop a marketing plan, or plan promotion channels.

</details>

<details open>
<summary><h3 style="display:inline">Data Analysis & Financial</h3></summary>

- [Financial Report Tracker](./skills/financial-report-tracker/SKILL.md) - Automatically track tech company financial reports and generate investment summaries. Supports retrieving earnings calendars, market expectation comparisons, key metric interpretation, and more.
- [Data Analysis Report Generator](./skills/data-analysis-report-generator/SKILL.md) - Intelligent data analysis report generator. Auto-identifies Excel/CSV data structure (dimensions, metrics, timelines), performs multi-dimensional parallel analysis, and generates professional HTML reports with ECharts interactive charts.
- [Full-Link Data Analysis](./skills/full-link-data-analysis/SKILL.md) - Full-Link Data Analysis Engine: From business Agenda to analytical report with complete seven-layer architecture. Built-in 15 analysis methods, supports data-aware routing (Agenda semantics + data structure + problem type three dimensions), built-in quality assurance, outputs Feishu doc format analytical reports.
- [Intelligent Data Analysis Assistant](./skills/data-analyst-visualization/SKILL.md) - LLM-powered intelligent data analysis assistant supporting natural language queries, SQL generation, visualization, and multi-turn conversation. Suitable for business analysis, report automation, and data exploration. Supports MySQL, PostgreSQL, Snowflake, and Excel/JSON file reading.
- [Data Visualization Designer](./skills/data-viz-designer/SKILL.md) - A data visualization designer that transforms complex data into clear, intuitive charts and visualizations. Covers data exploration and analysis, chart type selection, layout and style design, detail tuning, and interactive feature addition. 

</details>

<details open>
<summary><h3 style="display:inline">Charts & Data Visualization</h3></summary>

- [ECharts](./skills/apache-echarts/SKILL.md) - Apache ECharts charting skill.
- [Chart.js](./skills/chartjs/SKILL.md) - Chart.js charting skill. Used to generate visual charts such as line charts, bar charts, pie charts, radar charts, scatter plots, etc.
- [D3.js — A JavaScript library for data visualization](./skills/d3js/SKILL.md) - D3.js (Data-Driven Documents) — A JavaScript library for data visualization. Covers installation, selections, data binding, scales, shapes, transitions, 30+ module reference, chart templates, React/Svelte integration. For custom SVG/Canvas visualizations.
- [Mermaid Diagram Generation](./skills/mermaid-chart/SKILL.md) - Generate various diagrams using Mermaid syntax (flowcharts, sequence diagrams, Gantt charts, class diagrams, state diagrams, pie charts, ER diagrams, mind maps, timelines, C4 architecture diagrams, user journey maps, Git graphs, Sankey diagrams, quadrant charts, etc.). Supports inline rendering in Markdown.
- [Markmap — Build mindmaps with plain text](./skills/markmap/SKILL.md) - markmap — Render Markdown as interactive SVG mindmaps. Use when users need to convert Markdown documents into mindmaps, generate HTML files via CLI, or navigate mindmap nodes interactively in the browser.

</details>

<details open>
<summary><h3 style="display:inline">3D & Graphics</h3></summary>

- [Three.js 3D](./skills/threejs-3d/SKILL.md) - Comprehensive Three.js 3D graphics reference. Use when building 3D web apps, games, or visualizations with Three.js.
- [PlayCanvas](./skills/playcanvas/SKILL.md) - Comprehensive guide for PlayCanvas, the web-first 3D graphics platform including the Engine API, Editor, React wrapper, and Web Components. Use when building 3D web applications, games, or interactive experiences with PlayCanvas.
- [LeaferJS — Canvas 2D Engine](./skills/leaferjs/SKILL.md) - LeaferJS — Canvas 2D Engine. Lightweight and high-performance Canvas 2D graphics engine, supporting multiple platforms such as Web, Worker, Node.js, and Mini Programs.

</details>

<details open>
<summary><h3 style="display:inline">Image & Media Generation</h3></summary>

- [Favicons](./skills/favicons/SKILL.md) - Use the favicons Node.js library to generate multi-platform website icons (Favicons).
- [HTML DOM To Image](./skills/dom-to-image/SKILL.md) - Convert HTML DOM nodes to images (PNG/JPEG/SVG/Blob). Supports rendering options such as filter, backgroundColor, quality, and pixelRatio.
- [DOM Capture Engine](./skills/snapdom/SKILL.md) - Convert HTML DOM nodes to images (PNG/JPEG/SVG/Blob). Supports rendering options such as filter, backgroundColor, quality, and pixelRatio.
- [Macaron Card Generator](./skills/macaron-card-generator/SKILL.md) - Generate beautiful macaron-color cartoon illustration-style card images from text content. Supports various types such as book recommendation cards, concept cards, quote cards, and comparison cards, with multiple aspect ratios including 3:4, 9:16, and 1:1.
- [Social Media Cover Image Generator](./skills/social-media-cover-generator/SKILL.md) - Social media cover image generator. Generates HTML pages based on title content and automatically converts them to PNG images, suitable for creating cover images and graphics for platforms such as Xiaohongshu, WeChat Official Accounts, Weibo, Douyin, Bilibili, Zhihu, Twitter/X, Instagram, and LinkedIn.
- [LEGO Pixel Art Generator](./skills/lego-pixel-art/SKILL.md) - Convert any image into LEGO brick pixel art, generating a complete building plan and material purchase list. Built-in standard LEGO color system, supports custom sizes (10-200 studs) and color precision adjustment, outputs a row-by-row building guide. Pure frontend implementation, zero dependencies, ready to use out of the box. Suitable for LEGO enthusiasts, craft creators, and educators.
- [Text-to-SVG — Natural Language to SVG Vector Graphic Code](./skills/text-to-svg/SKILL.md) - Generate logos, icons, illustrations and other vector graphics from natural language descriptions. Supports style directives (flat monochrome/gradient/stroke/rounded/minimal/tech). For design mockups, brand logos, UI icons, info illustrations.

</details>

<details open>
<summary><h3 style="display:inline">Speech & Audio</h3></summary>

- [Microsoft Edge TTS](./skills/microsoft-edge-tts/SKILL.md) - Use Microsoft Edge online TTS service to convert text to speech. Supports command line and module invocation, no API key.
- [fish-speech](./skills/fish-speech/SKILL.md) - Fish Audio S2 Pro TTS.
- [VoxCPM2 — Tokenizer-Free Multilingual TTS](./skills/voxcpm/SKILL.md) - VoxCPM2 — Tokenizer-Free TTS model guide. Covers installation, Python/CLI API (TTS/Voice Design/Controllable Cloning/Ultimate Cloning/Streaming), vLLM-Omni deployment, fine-tuning (SFT/LoRA). Use when synthesizing speech, multilingual TTS, voice cloning/design.

</details>

<details open>
<summary><h3 style="display:inline">AI/ML & Data Processing</h3></summary>

- [Microsoft MarkItDown](./skills/microsoft-markitdown/SKILL.md) - Use MarkItDown to convert various files (PDF, Word, Excel, PPT, images, audio, HTML, CSV, JSON, etc.) to Markdown format for LLM processing and text analysis. Also supports content extraction from ZIP archives, YouTube videos, and EPUB e-books.
- [Tesseract OCR Image Text Extraction](./skills/tesseract-image-ocr/SKILL.md) - Extract text from images using Tesseract.js (OCR). Supports multi-language recognition including Chinese and English, region recognition, character whitelist filtering, text orientation detection, and can run in a Node.js environment.
- [Crawl4AI Web Crawler](./skills/crawl4ai-web-crawler/SKILL.md) - Use Crawl4AI for web scraping and content extraction. Use when users need to scrape web content, extract structured data, convert web pages to Markdown, perform batch crawling, or use AI-driven web data collection.
- [Open RAGFlow](./skills/open-ragflow/SKILL.md) - Open-source RAG engine fusing RAG with Agent capabilities. Full-stack: Python backend (Flask), React/TypeScript frontend, Docker-deployed microservices.
- [Google MediaPipe](./skills/mediapipe/SKILL.md) - On-device ML pipeline framework for vision, text, audio, and LLM inference. Cross-platform deployment to Android, iOS, web, desktop, edge devices, and IoT.
- [LocateAnything — Vision-Language Grounding](./skills/locateanything/SKILL.md) - NVIDIA LocateAnything-3B vision-language grounding model. Covers inference API (detect/ground/point/detect_text/ground_gui), data preparation (JSONL+Recipe 8 tasks), training/fine-tuning, evaluation. For object detection, visual grounding, GUI recognition, OCR, etc.
- [Claude Code Agent SDK](./skills/claude-code-agent-sdk/SKILL.md) - Claude Agent SDK documentation — build production AI agents with Claude Code as a library in Python or TypeScript. Use when building, configuring, or debugging agents with the Claude Agent SDK.

</details>

<details open>
<summary><h3 style="display:inline">Node.js Libraries & Utilities</h3></summary>

- [Gray Matter](./skills/gray-matter/SKILL.md) - Parse YAML/JSON/TOML front-matter from strings or files using the gray-matter library.
- [minimatch](./skills/minimatch/SKILL.md) - Use minimatch (glob pattern matching library) for file path matching, such as *.js, **/*.ts and other glob patterns. Note: Do NOT use user input as pattern source to prevent ReDoS attacks.
- [picomatch](./skills/picomatch/SKILL.md) - Picomatch — A fast and accurate glob pattern matching library.
- [undici](./skills/undici/SKILL.md) - Use undici for HTTP requests, fetch, connection pooling, proxies, Mock testing, interceptors, caching. Note that undici's fetch differs from built-in fetch (no CORS, must consume body).
- [agent-base](./skills/agent-base/SKILL.md) - Create custom http.Agent.
- [dotenv — Node.js Environment Variable Loader](./skills/dotenv/SKILL.md) - Use dotenv to manage environment variables for Node.js projects.
- [Mustache](./skills/mustache/SKILL.md) - Use mustache.js (logic-less Mustache templates) for any templating task in JavaScript/Node.js environments.
- [Node Cron](./skills/node-cron/SKILL.md) - Node.js cron job scheduling with the `cron` npm package. Use when the user needs to schedule recurring tasks, create cron jobs, validate cron expressions, set up timed callbacks, or work with cron syntax in a Node.js/TypeScript project.
- [markdown-it](./skills/markdown-it/SKILL.md) - Use markdown-it to render Markdown to HTML, configure plugins, custom rendering rules, syntax highlighting.
- [Archiver — Streaming Archive Packaging](./skills/archiver/SKILL.md) - Use the Archiver library for streaming archive packaging in Node.js. Supports creating ZIP/TAR archives, appending content from streams, strings, buffers, file paths, directories, and glob patterns, as well as registering custom formats.
- [WebTorrent — Streaming Torrent Client](./skills/webtorrent/SKILL.md) - Use WebTorrent to implement streaming BitTorrent client functionality in Node.js and the browser. Supports torrent downloading, seeding, magnet links, streaming media playback, and peer-to-peer transfer (via WebRTC Data Channel in the browser, and TCP/UDP in Node.js).
- [ImapFlow](./skills/imapflow/SKILL.md) - Modern Node.js IMAP client library (imapflow) for email integration. Covers authentication, mailbox locking, streaming fetches, async iterators, reconnection strategies, proxy support, and provider-specific configs (Gmail, Outlook, Yahoo, etc.).
- [Web Push Notifications](./skills/web-push/SKILL.md) - Send Web Push notifications from a Node.js backend using the web-push npm library (VAPID authentication, payload encryption). Covers generating VAPID keys, subscribing browsers, sending notifications, CLI usage, browser compatibility, and common pitfalls.
- [Fuse.js Fuzzy Search](./skills/fusejs/SKILL.md) - Implement fuzzy search in JavaScript/TypeScript projects using Fuse.js. Use when users need client-side search, fuzzy matching, search highlighting, multi-field weighted search, tokenized search, or Web Worker parallel search.

</details>

<details open>
<summary><h3 style="display:inline">CLI & Terminal Tools</h3></summary>

- [ZX](./skills/zx/SKILL.md) - Comprehensive guide for writing shell scripts with Google zx — a tool for writing better scripts using JavaScript/TypeScript. Use when writing, debugging, or refactoring zx scripts (.mjs, .js, .ts files using zx), executing shell commands from JavaScript, working with ProcessPromise/ProcessOutput APIs, piping streams, configuring zx options, or using zx CLI. Do NOT use for general Node.js questions unrelated to shell scripting.
- [@clack/prompts](./skills/clack-prompts/SKILL.md) - Build beautiful interactive Node.js command-line apps with @clack/prompts. Use when building CLI apps, wizards, setup scripts, or any interactive terminal prompt flow in Node.js. Covers text input, password, confirm, select, autocomplete, multiselect, spinner, progress bars, grouped prompts, task runners, and styled logging.
- [ink](./skills/ink-tui/SKILL.md) - Ink — React for interactive command-line apps. Build rich terminal UIs with React components.
- [Commander.js](./skills/commander/SKILL.md) - Commander.js is the most popular command-line interface (CLI) framework for Node.js.
- [OpenTUI — Native Terminal UI Framework](./skills/opentui/SKILL.md) - OpenTUI — Zig-native terminal UI framework. Covers installation, renderer, components (Text/Box/Input/Select/Code/ScrollBox), Constructs declarative API, Flexbox layout, React/Solid bindings.
- [Vercel CLI](./skills/vercel-cli/SKILL.md) - Vercel CLI skill for deploying and managing Vercel projects from the terminal.

</details>

<details open>
<summary><h3 style="display:inline">Web Development</h3></summary>

- [Google Web Fonts](./skills/google-web-fonts/SKILL.md) - Use the Google Fonts API to add fonts to web pages.
- [VitePress Static Website Generator](./skills/vitepress-generator/SKILL.md) - Quickly generate static websites using VitePress. Supports installing dependencies, initializing projects, local preview, building, and deployment.
- [TanStack Libraries](./skills/tanstack-libraries/SKILL.md) - Use when users ask about TanStack libraries, TanStack Start/Router/Query/Table/Form/Virtual/Store/DB/Pacer/Config/DevTools/CLI/Intent/Hotkeys/AI usage, package names, framework adapters, maturity status, documentation URLs, installation methods, core APIs, code examples.
- [NestJS Development Guide](./skills/nestjs-dev-guide/SKILL.md) - NestJS Node.js server-side framework development guide.
- [@shopify/draggable — Drag & Drop Interaction Skill](./skills/shopify-draggable/SKILL.md) - Implement drag-and-drop interactions with @shopify/draggable. Supports Draggable (basic drag), Sortable (reordering), Droppable (drop zones), Swappable (swapping), Plugins (mirror/snapping/collision/scroll, etc.), Sensors (mouse/touch/force touch).
- [SQLite Client](./skills/sqlite-client/SKILL.md) - SQLite database operations. Use this skill when users need to create, read, query, or modify SQLite databases (.db files).

</details>

<details open>
<summary><h3 style="display:inline">Website Cloning & Static Sites</h3></summary>

- [Clone Website](./skills/clone-website/SKILL.md) - Clone, copy, rebuild, or reverse engineer any website. Use when users request to clone a website, copy a page, replicate a webpage, or recreate one from scratch.
- [Static Site Cloner](./skills/static-site-cloner/SKILL.md) - Static site reproduction expert - Analyze target websites and manually code their structure, visual style, and basic interactions using pure HTML/CSS/JavaScript.
- [AI Data Visualizer](./skills/ai-data-visualizer/SKILL.md) - Automatically analyze and recommend optimal chart combinations based on data characteristics, generate beautiful interactive HTML dashboards (including line charts, bar charts, scatter plots, pie charts, etc.), support dark/light theme switching, CSV and JSON input, and data statistical summaries.

</details>

<details open>
<summary><h3 style="display:inline">Programming Languages & Compilers</h3></summary>

- [PerryTS — Native TypeScript Compiler](./skills/perryts/SKILL.md) - PerryTS native TypeScript compiler guide. Covers installation, compilation, perry/ui, perry/tui, multi-threading, standard library, cross-platform compilation, project configuration, CLI commands.

</details>

<details open>
<summary><h3 style="display:inline">IDE & Extensions</h3></summary>

- [VS Code Copilot Custom Agent Creator](./skills/vscode-agents-creator/SKILL.md) - Create VS Code Copilot custom Agent (.agent.md) files.

</details>

<details open>
<summary><h3 style="display:inline">Code Development Pipeline</h3></summary>

- [Fully Automated Collaborative Code Development Pipeline](./skills/auto-collaboration-dev-pipeline/SKILL.md) - Fully automated collaborative code development pipeline for complex code development tasks. Must be used when users request code development, program writing, feature implementation, or have code quality requirements.

</details>

<details open>
<summary><h3 style="display:inline">Mobile & Mini Programs</h3></summary>

- [WeChat Mini Program to uni-app](./skills/wmp-to-uniapp/SKILL.md) - Convert native WeChat Mini Program projects into uni-app + Vue3 + TypeScript cross-platform projects.
- [WeChat Mini Program CI](./skills/miniprogram-ci/SKILL.md) - A compilation module extracted from WeChat DevTools for uploading/previewing mini program/mini game code, building npm, deploying cloud functions, and managing cloud containers. Enables CI/CD without opening DevTools. For automated publishing, CI/CD pipelines, pre-release preview.
- [WeChat Mini Program Automation SDK](./skills/miniprogram-automator/SKILL.md) - Automate UI operations and data validation of mini programs at runtime. Supports page navigation, element selection and interaction, data injection, screenshots, event listening. For E2E testing, UI automation, regression testing.

</details>