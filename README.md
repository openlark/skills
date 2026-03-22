# Agent Skills

Agent Skills 是一种轻量级的开放格式，用于通过专门的知识和工作流扩展 AI 代理的能力。

从本质上讲，技能是包含一个 `SKILL.md` 文件的文件夹。该文件包含元数据（至少包括 `name` 和 `description`）以及指导代理如何执行特定任务的说明。技能还可以捆绑脚本、模板和参考材料。

## Agent Skills 列表

<details open>
<summary><h3 style="display:inline">自媒体</h3></summary>

- [小红书搜索建议关键词收集工具](./skills/xhs-suggest-keywords/SKILL.md) - 通过浏览器自动化访问小红书探索页，在搜索栏输入关键词并收集自动提示框中的相关关键词列表。
- [小红书自动发布图文](./skills/xiaohongshu-image-auto/SKILL.md) - 用户提供标题、正文后，自动完成登录检测、AI 生成配图、内容填充、AI 生成标签、标签激活、原创声明、执行发布的全流程。仅扫码登录需人工操作，其余步骤全自动化。
- [小红书自动长文发布工具](./skills/xiaohongshu-longpost-auto/SKILL.md) - 用户已有长文内容需要发布到小红书时，自动完成登录检测、长文内容分段优化、AI 生成配图、内容填充、AI 生成标签、标签激活、原创声明、执行发布的全流程。
- [抖音搜索关键词收集工具](./skills/douyin-keyword-collector/SKILL.md) - 通过浏览器自动化访问抖音首页，在搜索栏输入关键词并收集自动提示框中的相关关键词建议。
- [今日头条搜索关键词收集工具](./skills/jinritoutiao-keyword-collector/SKILL.md) - 通过浏览器自动化访问今日头条首页，在搜索栏输入关键词并收集自动提示框中的相关关键词建议。
- [今日头条自动发布文章技能](./skills/toutiao-graphic-publisher/SKILL.md) - 通过浏览器自动化实现头条号图文内容自动发布，支持智能排版、自动生成热门标签和激活标签。

</details>
<details open>

<summary><h3 style="display:inline">新闻</h3></summary>

- [新闻快报](./skills/news-express/SKILL.md) - 当用户询问新闻更新、每日简报或世界上发生的事情时，应使用此技能。从可靠的国际和中国 RSS 订阅源获取新闻。不需要 API Key。

</details>


## Agent Skills 结构目录

```
skills/
├── SKILL.md          # 必须：说明 + 元数据
├── scripts/          # 可选：可执行脚本代码
├── references/       # 可选：参考文档
└── assets/           # 可选：模版或资源文件
```
