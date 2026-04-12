# Agent Skills

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

At its core, a skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, templates, and reference materials.

## Agent Skills List

<details open>
<summary><h3 style="display:inline">Self-media</h3></summary>

- [Douyin Keyword Collector](./skills/douyin-keyword-collector/SKILL.md) - Accessing the Douyin homepage through browser automation, entering keywords in the search bar and collecting relevant keyword suggestions in the automated prompt box.
- [Jinri Toutiao Keyword Collector](./skills/jinritoutiao-keyword-collector/SKILL.md) - Automatically accesses the Jinri Toutiao homepage via browser automation, inputs keywords into the search bar, and collects related keyword suggestions from the auto-suggest dropdown.
- [Toutiao Automatic Article Publishing](./skills/toutiao-graphic-publisher/SKILL.md) - Automatically publishes graphic content on Toutiao through browser automation, supporting intelligent formatting, automatic generation of popular tags, and tag activation.
- [Xiaohongshu Keyword Collector](./skills/xiaohongshu-keyword-collector/SKILL.md) - Automatically accesses Xiaohongshu's Explore page via browser automation, inputs keywords into the search bar, and collects the list of related keywords from the auto-suggest dropdown.
- [Xiaohongshu Automatic Image-Text Post Publishing](./skills/xiaohongshu-image-auto/SKILL.md) - After users provide a title and body text, automatically completes the entire process: login detection, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing.
- [Xiaohongshu Automatic Long-Form Post Publishing](./skills/xiaohongshu-longpost-auto/SKILL.md) - When users have long-form content ready to publish on Xiaohongshu, automatically completes the entire process: login detection, long content segmentation optimization, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing.

</details>

<details open>
<summary><h3 style="display:inline">News</h3></summary>

- [News Express](./skills/news-express/SKILL.md) - Use this skill when users ask for news updates, daily briefings, or what's happening in the world. Fetches news from reliable international and Chinese RSS feeds. No API key required.

</details>

<details open>
<summary><h3 style="display:inline">Tools</h3></summary>

- [Microsoft Edge TTS](./skills/microsoft-edge-tts/SKILL.md) - Use Microsoft Edge online TTS service to convert text to speech. Supports command line and module invocation, no API key.
- [Microsoft MarkItDown](./skills/microsoft-markitdown/SKILL.md) - Use MarkItDown to convert various files (PDF, Word, Excel, PPT, images, audio, HTML, CSV, JSON, etc.) to Markdown format for LLM processing and text analysis. Also supports content extraction from ZIP archives, YouTube videos, and EPUB e-books.
- [Vercel CLI](./skills/vercel-cli/SKILL.md) - Vercel CLI skill for deploying and managing Vercel projects from the terminal.
- [ECharts](./skills/apache-echarts/SKILL.md) - Apache ECharts charting skill.
- [Chart.js](./skills/chartjs/SKILL.md) - Chart.js charting skill. Used to generate visual charts such as line charts, bar charts, pie charts, radar charts, scatter plots, etc.

</details>


## Agent Skills Structure Directory

```
my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources
```
