# 浏览器自动化最佳实践

## 等待策略

### 固定等待

适用于已知延迟的操作：

```
action: act
kind: wait
timeMs: 2000
```

### 条件等待

等待特定元素出现或消失：

```
action: act
kind: wait
textGone: 加载中...
```

## 元素定位

### 使用 ARIA 引用

```
action: snapshot
refs: aria
```

优点：
- 更稳定的元素标识
- 不受页面结构变化影响
- 支持无障碍访问元素

### 使用角色引用（默认）

```
action: snapshot
refs: role
```

适用于标准 HTML 元素。

## 输入优化

### 慢速输入

触发自动完成和动态加载：

```
action: act
kind: type
text: 关键词
slowly: true
```

### 清空输入框

在重新输入前清空：

```
action: act
ref: <input-ref>
kind: fill
fields: []
```

## 性能优化

### 保持会话

多次操作时复用浏览器会话：

1. 第一次启动浏览器
2. 后续操作使用相同的 `targetId`
3. 最后统一关闭

### 延迟请求

避免触发反爬机制：

- 单次操作间隔：2-3 秒
- 批量操作间隔：5-10 秒
- 避免高峰时段高频访问

## 错误处理

### 超时设置

长操作增加超时：

```
action: navigate
targetUrl: https://www.toutiao.com
timeoutMs: 30000
```

### 重试策略

失败后重试 2-3 次：

1. 等待 3 秒
2. 刷新页面
3. 重新执行操作

## 调试技巧

### 截图辅助

遇到问题时截图：

```
action: screenshot
fullPage: true
```

### 控制台日志

检查页面错误：

```
action: console
```
