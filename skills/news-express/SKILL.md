---
name: news-express
description: 当用户询问新闻更新、每日简报或世界上发生的事情时，应使用此技能。从可靠的国际和中国 RSS 订阅源获取新闻。不需要 API Key。
---

# 新闻快报

## 概览

从国内外可信 RSS 订阅源获取并汇总新闻，**无需任何 API Key**，直接通过 `web_fetch` 工具读取 RSS XML 即可。

## 触发场景

- 用户问"今天有什么新闻"、"最新资讯"、"每日简报"
- 用户问"国内/国际发生了什么"
- 用户要求科技、财经、体育等分类新闻
- 用户要求"早报"、"晚报"、"新闻摘要"

---

## RSS 订阅源

### 🇨🇳 国内源

| 来源 | 分类 | URL |
|------|------|-----|
| 36氪 | 科技/商业 | `https://36kr.com/feed` |
| 知乎日报 | 动漫/游戏/财经/电影/互联网安全 | `https://plink.anyfeeder.com/zhihu/daily` |
| Odaily星球日报 | 快讯 | `https://rss.odaily.news/rss/newsflash` |
| 智东西 | 快讯/头条/人工智能/机器人 | `https://zhidx.com/rss` |
| 奇客 | 科技 | `https://www.solidot.org/index.rss` |
| PANews | 快讯 | `https://www.panewslab.com/rss.xml?lang=zh&type=NEWS&featured=true` |
| IT之家 | AI/科技/数码 | `https://www.ithome.com/rss/` |
| cnBeta | AI/科技/数码 | `https://plink.anyfeeder.com/cnbeta` |
| 少数派 | 科技/数码 | `https://sspai.com/feed` |
| IT桔子 | 金融 | `https://www.itjuzi.com/api/telegraph.xml` |
| 虎嗅 | 商业/科技 | `https://www.huxiu.com/rss/0.xml` |
| 爱范儿 | 早报/快讯 | `https://www.ifanr.com/feed` |
| 华尔街日报 | 资讯/要闻 | `https://plink.anyfeeder.com/wsj/cn` |
| 纽约时报 | 科技/商业/政治/健康 | `https://plink.anyfeeder.com/nytimes/cn` |
| 人民日报 | 头条 | `http://www.people.com.cn/rss/politics.xml` |

### 🌍 国际源

| 来源 | 分类 | URL |
|------|------|-----|
| OpenAI | AI | `https://openai.com/news/rss.xml` |
| Al Jazeera | 全球 | `https://www.aljazeera.com/xml/rss/all.xml` |
| NPR | 美国 | `https://feeds.npr.org/1001/rss.xml` |
| The Guardian | 综合 | `https://www.theguardian.com/world/rss` |
| TechCrunch | 科技 | `https://techcrunch.com/feed/` |
| Hacker News | 科技/开发 | `https://hnrss.org/frontpage` |
| PANews | 快讯 | `https://www.panewslab.com/rss.xml?lang=en&type=NEWS&featured=true` |
| ArXiv | AI | `https://rss.arxiv.org/rss/cs.AI` |
| 中国日报 | 英文/国际 | `https://www.chinadaily.com.cn/rss/china_rss.xml` |

---

## 工作流程

### 第一步：获取 RSS 内容

使用 `web_fetch` 工具直接读取 RSS XML：

```
web_fetch(url="https://openai.com/news/rss.xml")
web_fetch(url="https://36kr.com/feed")
```

### 第二步：解析标题

RSS XML 结构中，新闻标题在 `<title>` 标签内，摘要在 `<description>` 标签内，链接在 `<link>` 标签内。直接从 `web_fetch` 返回的 markdown 文本中提取即可。

### 第三步：汇总输出

按国内、国际整理，各取 6-8 条，每条输出标题和简洁摘要。

---

## 输出格式

```
📰 [最新资讯]
🗓️ [日期] · [星期]

🇨🇳 国内
• [标题1] 
[摘要1]
• [标题2] 
[摘要2]
• [标题3] 
[摘要3]

🌍 国际
• [标题1] 
[摘要1]
• [标题2] 
[摘要2]
• [标题3] 
[摘要3]


---
数据来源：RSS 订阅 · 无需 API
```

---

## 注意事项

- **无需 API Key**：所有数据通过公开 RSS 订阅获取
- **部分国内源可能需要网络环境支持**：如遇访问失败，自动切换备用源
- **内容时效性**：RSS 通常每 15-60 分钟更新一次
- **语言**：国内源中文输出，国际源可中英双语
