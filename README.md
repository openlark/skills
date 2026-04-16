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
- [ECharts](./skills/apache-echarts/SKILL.md) - Apache ECharts charting skill.
- [Chart.js](./skills/chartjs/SKILL.md) - Chart.js charting skill. Used to generate visual charts such as line charts, bar charts, pie charts, radar charts, scatter plots, etc.
- [favicons](./skills/favicons/SKILL.md) - Use the favicons Node.js library to generate multi-platform website icons (Favicons).etc.

- [Vercel CLI](./skills/vercel-cli/SKILL.md) - Vercel CLI skill for deploying and managing Vercel projects from the terminal.

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
<summary><h3 style="display:inline">Marketing</h3></summary>

- [Auto Acquisition](./skills/auto-acquisition/SKILL.md) - Customer acquisition and marketing automation expert.
- [Market Research Automation](./skills/market-research-automation/SKILL.md) - Market research automation skill. Mine user pain points from social media and analyze competitors. Applicable for market validation before product launch, user needs analysis, and competitor feature comparison.
- [SEO Content Pipeline](./skills/seo-content-pipeline/SKILL.md) - SEO automated content pipeline skill. Automates the entire workflow from competitor research and keyword mining to article generation and publishing.

</details>

