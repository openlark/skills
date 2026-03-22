# skills

## Agent Skills 结构目录

```
skills/
├── SKILL.md          # 必须：说明 + 元数据
├── scripts/          # 可选：可执行脚本代码
├── references/       # 可选：参考文档
└── assets/           # 可选：模版或资源文件
```


## Skills 列表

<details open>
<summary><h3 style="display:inline">自媒体</h3></summary>

- [xhs-suggest-keywords](./skills/xhs-suggest-keywords/SKILL.md) - 通过浏览器自动化访问小红书探索页，在搜索栏输入关键词并收集自动提示框中的相关关键词列表。
- [xiaohongshu-image-auto](./skills/xiaohongshu-image-auto/SKILL.md) - 用户提供标题、正文后，自动完成登录检测、AI 生成配图、内容填充、AI 生成标签、标签激活、原创声明、执行发布的全流程。仅扫码登录需人工操作，其余步骤全自动化。
- [xiaohongshu-longpost-auto](./skills/xiaohongshu-longpost-auto/SKILL.md) - 用户已有长文内容需要发布到小红书时，自动完成登录检测、长文内容分段优化、AI 生成配图、内容填充、AI 生成标签、标签激活、原创声明、执行发布的全流程。
- [douyin-keyword-collector](./skills/douyin-keyword-collector/SKILL.md) - 通过浏览器自动化访问抖音首页，在搜索栏输入关键词并收集自动提示框中的相关关键词建议。
- [jinritoutiao-keyword-collector](./skills/jinritoutiao-keyword-collector/SKILL.md) - 通过浏览器自动化访问今日头条首页，在搜索栏输入关键词并收集自动提示框中的相关关键词建议。
- [toutiao-graphic-publisher](./skills/toutiao-graphic-publisher/SKILL.md) - 通过浏览器自动化实现头条号图文内容自动发布，支持智能排版、自动生成热门标签和激活标签。

</details>
<details open>

<summary><h3 style="display:inline">新闻</h3></summary>

- [news-express](./skills/news-express/SKILL.md) - 当用户询问新闻更新、每日简报或世界上发生的事情时，应使用此技能。从可靠的国际和中国 RSS 订阅源获取新闻。不需要 API Key。

</details>