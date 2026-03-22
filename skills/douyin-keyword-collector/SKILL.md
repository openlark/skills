---
name: douyin-keyword-collector
description: 抖音搜索关键词收集工具。通过浏览器自动化访问抖音首页，在搜索栏输入关键词并收集自动提示框中的相关关键词建议。使用场景：用户需要收集抖音热门搜索词、关键词联想、SEO 关键词研究、内容创作灵感。触发词："抖音关键词"、"收集抖音关键词"、"抖音搜索建议"、"douyin keywords"。
---

# 抖音关键词收集工具

## 功能概述

本技能通过浏览器自动化访问抖音首页，在搜索栏输入关键词并收集自动提示框中的相关关键词建议。无需 API 密钥，完全基于浏览器自动化实现。

## 使用场景

- 抖音 SEO 关键词研究
- 内容创作灵感收集
- 热门话题趋势分析
- 竞品关键词调研
- 短视频选题策划

## 操作流程

### 1. 启动浏览器

使用 `browser` 工具的 `start` 或 `snapshot` 动作启动浏览器。

### 2. 访问抖音首页

导航到抖音官网：
```
https://www.douyin.com
```

### 3. 检查并关闭登录弹窗

使用 `browser` 工具的 `snapshot` 动作获取页面元素引用，检查是否存在登录弹窗。

如果存在登录弹窗（查找关闭按钮，通常为 `img` 或 `button` 元素），使用 `act` 动作点击关闭：
```
browser action=act request={"kind":"click","ref":"<关闭按钮引用>"}
```

### 4. 定位搜索栏

使用 `browser` 工具的 `snapshot` 动作获取页面元素引用，找到搜索栏输入框（textbox 类型，描述包含"搜索"）。

### 5. 输入关键词

使用 `browser` 工具的 `act` 动作，选择 `type` 类型，在搜索栏输入目标关键词：
```
browser action=act request={"kind":"type","ref":"<搜索栏引用>","text":"<关键词>"}
```

### 6. 等待提示框出现

等待 1-2 秒让自动提示框加载：
```
browser action=act request={"kind":"wait","timeMs":2000}
```

### 7. 收集自动提示

使用 `snapshot` 动作获取提示框中的关键词列表，查找 `list` 或 `generic` 元素中包含的关键词文本。

### 8. 整理输出

将收集到的关键词整理成列表格式输出给用户。

## 浏览器自动化命令示例

### 启动浏览器并访问抖音

```
browser action=start profile=openclaw
browser action=navigate targetUrl=https://www.douyin.com
```

### 获取页面快照（获取元素引用）

```
browser action=snapshot refs=aria
```

### 关闭登录弹窗（如存在）

查找弹窗中的关闭按钮（通常是 `img` 或 `button` 元素，靠近弹窗右上角），然后点击：
```
browser action=act request={"kind":"click","ref":"<关闭按钮引用>"}
```

### 在搜索栏输入关键词

```
browser action=act request={"kind":"type","ref":"<搜索栏引用>","text":"<关键词>"}
```

### 等待提示框加载

```
browser action=act request={"kind":"wait","timeMs":2000}
```

### 获取提示框内容

```
browser action=snapshot refs=aria
```

## 注意事项

1. **登录弹窗处理**：访问抖音首页后可能会弹出登录框，需先点击关闭按钮（通常是弹窗右上角的 X 图标）再继续操作。

2. **登录状态**：部分搜索功能可能需要登录。如关闭弹窗后仍无法获取提示，建议用户手动扫码登录。

3. **反爬虫机制**：抖音可能有反爬虫机制，操作时需适当添加延迟，避免触发风控。

4. **元素引用**：使用 `refs=aria` 获取稳定的元素引用，确保操作准确性。

5. **等待时间**：输入关键词后需等待 1-2 秒让自动提示框加载完成。

6. **移动端适配**：抖音可能有移动端和桌面端不同界面，建议使用桌面端模式。

## 输出格式

```
关键词：[输入的关键词]
搜索建议词：
1. 建议词1
2. 建议词2
3. 建议词3
...
```

## 触发条件

当用户提到以下任一关键词时触发本技能：
- 抖音关键词
- 收集抖音关键词
- 抖音搜索建议
- douyin keywords
- 抖音热门词
- 抖音 SEO
- 抖音话题
