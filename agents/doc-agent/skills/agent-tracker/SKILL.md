---
name: agent-tracker
description: 全面的 Agent 任务追踪和监控系统。实时监控所有 Agent 的执行情况、活跃状态、完成进度，并提供详细的进展记录。支持及时干预和管理。使用当需要追踪多 Agent 协作、监控任务执行状态、记录详细进展、或需要及时干预时。
---

# Agent 任务追踪系统

全面监控和记录所有 Agent 的任务执行情况。

## 核心功能

### 1. 实时状态监控
- 所有可用 Agent 列表和状态
- 活跃会话监控
- 子 Agent 运行状态
- Token 使用统计

### 2. 任务执行追踪
- 正在执行的任务详情
- 任务进度记录
- 执行时间统计
- 成功/失败状态

### 3. 详细进展记录
- 每个任务的里程碑
- 关键决策点记录
- 遇到的问题和解决方案
- 输出结果摘要

### 4. 干预支持
- 异常状态及时告警
- 需要人工干预的标记
- 历史记录查询
- 状态对比分析

## 使用流程

### 初始化追踪系统

首次使用时，创建追踪数据结构：

```
agent-tracker/
├── state/
│   ├── agents.json          # Agent 状态快照
│   ├── sessions.json        # 会话状态
│   └── current-tasks.json   # 当前任务
├── logs/
│   ├── YYYY-MM-DD/          # 按日期组织的日志
│   │   ├── agent-activity.jsonl
│   │   ├── task-execution.jsonl
│   │   └── interventions.json
│   └── archive/              # 归档历史
└── reports/
    ├── daily-summary.md      # 每日摘要
    └── intervention-alerts.md # 干预提醒
```

### 定期检查流程

**每 15-30 分钟执行一次：**

1. **检查 Agent 状态**
   ```bash
   # 使用 agents_list 工具
   # 使用 sessions_list 工具
   # 使用 subagents 工具
   ```

2. **记录活动日志**
   - 时间戳
   - Agent ID
   - 活动类型
   - 详情描述
   - 状态变化

3. **生成状态快照**
   - 保存当前状态
   - 与上一次状态对比
   - 检测异常变化

4. **检查干预需求**
   - 长时间运行的任务
   - 失败的任务
   - 异常的 Token 使用
   - 无响应的 Agent

### 任务追踪记录

对于每个任务，记录：

```json
{
  "taskId": "唯一标识符",
  "agentId": "执行 Agent",
  "sessionKey": "会话键",
  "startTime": "开始时间戳",
  "endTime": "结束时间戳（如完成）",
  "status": "pending|running|completed|failed|interrupted",
  "description": "任务描述",
  "progress": {
    "current": 0,
    "total": 100,
    "milestones": []
  },
  "metrics": {
    "tokensUsed": 0,
    "executionTime": 0,
    "toolCalls": 0
  },
  "output": "结果摘要",
  "warnings": [],
  "needsIntervention": false,
  "interventionNotes": ""
}
```

## 关键工具使用

### agents_list
获取所有可用 Agent 的列表和配置状态。

**使用场景：**
- 初始化追踪系统时
- 检测新 Agent 加入时
- 验证 Agent 配置状态时

### sessions_list
获取所有活跃会话的状态。

**使用场景：**
- 监控会话活跃度
- 追踪会话更新时间
- 统计 Token 使用情况

**关键信息提取：**
- `key` - 会话唯一标识
- `kind` - 会话类型
- `updatedAt` - 最后更新时间
- `model` - 使用的模型
- `totalTokens` - 总 Token 使用
- `abortedLastRun` - 是否异常终止

### sessions_history
获取特定会话的详细历史记录。

**使用场景：**
- 任务完成后记录详情
- 调试问题时回溯
- 生成详细报告时

### subagents
管理和监控子 Agent。

**使用场景：**
- 监控子 Agent 运行状态
- 需要干预子 Agent 时
- 终止异常子 Agent 时

### session_status
查看会话的详细状态和统计。

**使用场景：**
- 深度分析特定会话
- 性能监控和优化
- 成本追踪

## 干预触发条件

当出现以下情况时，标记为需要干预：

1. **任务运行超时**
   - 超过预期时间 2 倍
   - 超过 1 小时无进展

2. **任务执行失败**
   - 明确的错误状态
   - 异常终止的会话

3. **异常资源使用**
   - Token 使用突增
   - 超出正常范围

4. **无响应状态**
   - Agent 长时间不活动
   - 会话卡住无更新

5. **用户明确要求**
   - 标记为需要关注的任务
   - 关键业务流程

## 报告生成

### 每日摘要报告

包含：
- 当日活跃 Agent 列表
- 执行的任务统计
- 成功/失败比例
- Token 使用总量
- 需要干预的事项
- 建议和改进点

### 干预提醒报告

包含：
- 需要立即关注的任务
- 问题描述和影响
- 建议的干预措施
- 历史类似案例参考

## 数据存储规范

### JSON 日志格式

使用 JSON Lines 格式存储日志，便于解析和查询：

```jsonl
{"timestamp": 1700000000, "type": "agent-check", "agentId": "calendaragent", "status": "active"}
{"timestamp": 1700000001, "type": "task-start", "taskId": "task-001", "agentId": "calendaragent", "description": "..."}
{"timestamp": 1700000002, "type": "task-progress", "taskId": "task-001", "progress": 25}
```

### 状态快照

每小时保存完整状态快照，用于历史对比：

```json
{
  "snapshotTime": 1700000000,
  "agents": [...],
  "sessions": [...],
  "tasks": [...],
  "metrics": {...}
}
```

## 快速启动

### 首次设置

1. 创建目录结构
2. 初始化状态文件
3. 进行首次完整扫描

### 日常使用

1. 运行状态检查
2. 记录新的活动
3. 检查干预需求
4. 生成摘要报告

---

**记住：** 这个技能的目标是让你能够全面、及时地了解所有 Agent 的状态，以便进行有效的管理和干预。
