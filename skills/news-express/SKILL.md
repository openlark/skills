---
name: news-express
description: Use this skill when users ask for news updates, daily briefings, or what's happening in the world. Fetches news from reliable international and Chinese RSS feeds. No API key required.
---

# News Express

## Overview

Fetches and aggregates news from trusted domestic and international RSS feeds, **requiring no API keys**. Simply use the `web_fetch` tool to read RSS XML directly.

## Trigger Scenarios

- 用户问"今天有什么新闻"、"最新资讯"、"每日简报"
- 用户问"国内/国际发生了什么"
- 用户要求科技、财经、体育等分类新闻
- 用户要求"早报"、"晚报"、"新闻摘要"
- User asks "what's the news today", "latest updates", "daily briefing"
- User asks "what's happening domestically/internationally"
- User requests categorized news such as technology, finance, sports
- User asks for "morning briefing", "evening briefing", "news summary"

---

## RSS Feeds

### 🇨🇳 Domestic Sources

| Source | Category | URL |
|------|------|-----|
| 36Kr | Technology/Business | `https://36kr.com/feed` |
| Zhihu Daily | Animation/Games/Finance/Movies/Internet Security | `https://plink.anyfeeder.com/zhihu/daily` |
| Odaily | Flash News | `https://rss.odaily.news/rss/newsflash` |
| Zhidx | Flash News/Headlines/AI/Robotics | `https://zhidx.com/rss` |
| Solidot | Technology | `https://www.solidot.org/index.rss` |
| PANews | Flash News | `https://www.panewslab.com/rss.xml?lang=zh&type=NEWS&featured=true` |
| IT之家 | AI/Technology/Digital | `https://www.ithome.com/rss/` |
| cnBeta | AI/Technology/Digital | `https://plink.anyfeeder.com/cnbeta` |
| SSPAI | Technology/Digital | `https://sspai.com/feed` |
| IT桔子 | Finance | `https://www.itjuzi.com/api/telegraph.xml` |
| Huxiu | Business/Technology | `https://www.huxiu.com/rss/0.xml` |
| ifanr | Morning Briefing/Flash News | `https://www.ifanr.com/feed` |
| The Wall Street Journal | News/Headlines | `https://plink.anyfeeder.com/wsj/cn` |
| The New York Times | Technology/Business/Politics/Health | `https://plink.anyfeeder.com/nytimes/cn` |
| People's Daily | Headlines | `http://www.people.com.cn/rss/politics.xml` |

### 🌍 International Sources

| Source | Category | URL |
|------|------|-----|
| OpenAI | AI | `https://openai.com/news/rss.xml` |
| Al Jazeera | Global | `https://www.aljazeera.com/xml/rss/all.xml` |
| NPR | United States | `https://feeds.npr.org/1001/rss.xml` |
| The Guardian | Comprehensive | `https://www.theguardian.com/world/rss` |
| TechCrunch | Technology | `https://techcrunch.com/feed/` |
| Hacker News | Technology/Development | `https://hnrss.org/frontpage` |
| PANews | Flash News | `https://www.panewslab.com/rss.xml?lang=en&type=NEWS&featured=true` |
| ArXiv | AI | `https://rss.arxiv.org/rss/cs.AI` |
| China Daily | English/International | `https://www.chinadaily.com.cn/rss/china_rss.xml` |

---

## Workflow

### Step 1: Fetch RSS Content

Use the `web_fetch` tool to read RSS XML directly:

```
web_fetch(url="https://openai.com/news/rss.xml")
web_fetch(url="https://36kr.com/feed")
```

### Step 2: Parse Titles

In the RSS XML structure, news headlines are within `<title>` tags, summaries within `<description>` tags, and links within `<link>` tags. Simply extract them from the markdown text returned by `web_fetch`.

### Step 3: Compile and Output

Organize by domestic and international categories, taking 6-8 items each, outputting each headline with a concise summary.

---

## Output Format

```
📰 [Latest News]
🗓️ [Date] · [Day of Week]

🇨🇳 Domestic
• [Headline 1] 
[Summary 1]
• [Headline 2] 
[Summary 2]
• [Headline 3] 
[Summary 3]

🌍 International
• [Headline 1] 
[Summary 1]
• [Headline 2] 
[Summary 2]
• [Headline 3] 
[Summary 3]


---
Data Source: RSS Feeds · No API Required
```

---

## Important Notes

- **No API Key Required**: All data is obtained through public RSS feeds
- **Some domestic sources may require proper network access**: If access fails, automatically switch to backup sources
- **Content Timeliness**: RSS typically updates every 15-60 minutes
- **Language**: Domestic sources output in Chinese, international sources can be bilingual (Chinese/English)