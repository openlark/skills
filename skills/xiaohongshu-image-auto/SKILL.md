---
name: xiaohongshu-image-auto
description: 小红书自动发布图文。用户提供标题、正文后，自动完成登录检测、AI 生成配图、内容填充、AI 生成标签、标签激活、原创声明、执行发布的全流程。仅扫码登录需人工操作，其余步骤全自动化。使用场景：用户已有笔记内容需要发布到小红书。
---

# 小红书自动发布图文

## 核心定位
**纯浏览器自动化，无需API和代码**。你只需提供标题和正文，剩下的步骤全部自动化完成。

| 输入项 | 说明 | 是否必填 |
|--------|------|----------|
| 标题 | 笔记标题，不超过20字 | ✅ 必填 |
| 正文 | 笔记正文，不超过1000字 | ✅ 必填 |

## 工作流程
```
你提供内容 → 启动浏览器 → 检测登录 → AI生成配图 → 自动填充 → AI生成标签 → 激活标签 → 声明原创 → 发布笔记
            ↑
    仅扫码登录需手动操作
```

## 前置准备
### 浏览器环境
- 使用host模式启动浏览器
- 打开小红书创作平台：https://creator.xiaohongshu.com/publish/publish

### 账号登录
- **只需手动扫码登录**
- 检测到未登录时自动暂停并提示
- 登录成功后自动继续执行

## 自动化执行步骤

### 1. 启动浏览器并检测登录状态
```bash
browser start profile=openclaw target=host
browser navigate https://creator.xiaohongshu.com/publish/publish
browser snapshot refs=aria
```
**登录检测逻辑**：
- 检查页面是否包含登录表单
- 如未登录则截图提示用户扫码
- 每15秒自动轮询检测，登录后继续

### 2. 切换到图文发布模式
```bash
browser act ref=<上传图文按钮> kind=click
```

### 3. AI自动生成配图
```bash
# 点击“文字配图”
browser act ref=<文字配图按钮> kind=click

# 输入图片描述
browser act ref=<文本框> kind=type text="<用户标题>"

# 生成图片并选择样式（默认“基础”）
browser act ref=<生成按钮> kind=click
browser act ref=<样式按钮> kind=click
browser act ref=<下一步按钮> kind=click
```

### 4. 自动填充标题和正文
```bash
browser act ref=<标题输入框> kind=type text="<用户标题>"
browser act ref=<正文输入框> kind=type text="<用户正文>"
```
**字数检查**：
- 标题超过20字 → 自动裁剪并提示
- 正文超过1000字 → 自动裁剪并提示

### 5. AI生成标签（如用户未提供）
```bash
# 分析标题和正文，生成5-10个相关标签
# 标签类型：核心话题、场景标签、情绪标签
```
**生成规则**：
- 从标题提取核心关键词
- 从正文提取高频词
- 补充热门相关标签

### 6. 激活话题标签

**关键规则**：必须点击弹窗推荐项的第一项，标签才能变为可搜索链接

```bash
# 对每个标签执行以下流程
for each 标签 in 标签列表:
    # 步骤 1：点击话题按钮，打开输入框
    browser act ref=<话题按钮> kind=click
    
    # 步骤 2：输入标签名（含#号）
    browser act ref=<话题输入框> kind=type text="#标签名"
    
    # 步骤 3：等待推荐弹窗出现（约 1 秒）
    browser snapshot refs=aria
    
    # 步骤 4：点击推荐列表中的第一项（必须！）
    browser act ref=<推荐列表第一项> kind=click
    
    # 步骤 5：确认标签已激活（显示为蓝色链接）
    # 继续下一个标签
```

**激活成功标志**：
- 标签变为蓝色可点击链接
- 格式：`[话题]#标签名`

**注意事项**：
- ⚠️ 必须点击推荐弹窗，直接输入无效
- ⚠️ 必须点击第一项，确保标签标准化
- ⚠️ 每个标签都需要单独激活

### 7. 勾选原创声明
```bash
browser act ref=<原创声明checkbox> kind=click
browser act ref=<同意checkbox> kind=click
browser act ref=<声明原创按钮> kind=click
```

### 8. 执行发布
```bash
browser act ref=<发布按钮> kind=click
browser snapshot refs=aria
```
**发布成功标志**：页面显示“发布成功”或跳转到“笔记管理”页面

## 异常处理

| 问题 | 处理方式 |
|------|----------|
| 登录超时 | 截图提示，自动轮询检测登录状态 |
| 标题超长 | 自动裁剪至20字，提示用户确认 |
| 发布失败 | 截图记录，提示用户重试或转人工 |

## 发布后工作

### 自动记录日志
在 `memory/xhs-YYYY-MM-DD.md` 中写入：
```markdown
## 发布记录
| 项目 | 内容 |
|------|------|
| 标题 | 用户标题 |
| 图片 | AI生成1张 |
| 标签 | 共X个 |
| 发布时间 | xhs-YYYY-MM-DD HH:MM |
| 状态 | ✅ 已发布 |
```

## 核心注意事项
### 账号安全
- 仅扫码登录需人工操作
- 发布间隔建议≥30分钟
- 发布前自动检查内容合规

### 内容合规
- 标题≤20字，正文≤1000字
- 避免绝对化用语、医疗功效词、价格诱导语

### 发布频率建议
- 新号：日更或隔日更
- 成熟号：根据粉丝活跃时间调整

## 常用命令速查
```bash
browser navigate <URL>        # 打开页面
browser snapshot refs=aria     # 获取页面元素
browser act ref=<元素> kind=click  # 点击元素
browser act ref=<元素> kind=type text="内容"  # 输入文本
browser screenshot             # 截图
```

## 示例
```
使用 xiaohongshu-image-auto 技能。汇总今日国内AI领域重要发布。
```