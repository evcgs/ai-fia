#!/usr/bin/env python3
"""
Agent Tracker - 全面的 Agent 任务追踪系统
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path

class AgentTracker:
    def __init__(self, base_path=None):
        if base_path is None:
            base_path = Path(__file__).parent
        self.base_path = Path(base_path)
        self.state_path = self.base_path / "state"
        self.logs_path = self.base_path / "logs"
        self.reports_path = self.base_path / "reports"
        
        # 确保目录存在
        for path in [self.state_path, self.logs_path, self.reports_path]:
            path.mkdir(exist_ok=True)
        
        # 今日日志目录
        today = datetime.now().strftime("%Y-%m-%d")
        self.today_logs = self.logs_path / today
        self.today_logs.mkdir(exist_ok=True)
    
    def log_activity(self, activity_type, data=None):
        """记录活动日志"""
        if data is None:
            data = {}
        
        log_entry = {
            "timestamp": int(time.time()),
            "timestamp_iso": datetime.now().isoformat(),
            "type": activity_type,
            "data": data
        }
        
        log_file = self.today_logs / "agent-activity.jsonl"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        
        return log_entry
    
    def save_agents_state(self, agents):
        """保存 Agent 状态"""
        state = {
            "lastUpdated": int(time.time()),
            "lastUpdated_iso": datetime.now().isoformat(),
            "agents": agents,
            "version": "1.0"
        }
        
        with open(self.state_path / "agents.json", "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        
        self.log_activity("agents-state-saved", {"count": len(agents)})
        return state
    
    def save_sessions_state(self, sessions):
        """保存会话状态"""
        state = {
            "lastUpdated": int(time.time()),
            "lastUpdated_iso": datetime.now().isoformat(),
            "sessions": sessions,
            "version": "1.0"
        }
        
        with open(self.state_path / "sessions.json", "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        
        self.log_activity("sessions-state-saved", {"count": len(sessions)})
        return state
    
    def save_tasks_state(self, tasks):
        """保存任务状态"""
        state = {
            "lastUpdated": int(time.time()),
            "lastUpdated_iso": datetime.now().isoformat(),
            "tasks": tasks,
            "version": "1.0"
        }
        
        with open(self.state_path / "current-tasks.json", "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        
        self.log_activity("tasks-state-saved", {"count": len(tasks)})
        return state
    
    def load_agents_state(self):
        """加载 Agent 状态"""
        try:
            with open(self.state_path / "agents.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"lastUpdated": 0, "agents": [], "version": "1.0"}
    
    def load_sessions_state(self):
        """加载会话状态"""
        try:
            with open(self.state_path / "sessions.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"lastUpdated": 0, "sessions": [], "version": "1.0"}
    
    def load_tasks_state(self):
        """加载任务状态"""
        try:
            with open(self.state_path / "current-tasks.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"lastUpdated": 0, "tasks": [], "version": "1.0"}
    
    def generate_daily_summary(self):
        """生成每日摘要"""
        today = datetime.now().strftime("%Y-%m-%d")
        agents_state = self.load_agents_state()
        sessions_state = self.load_sessions_state()
        tasks_state = self.load_tasks_state()
        
        summary = f"""# Agent 追踪系统 - 每日摘要

日期: {today}

## 🤖 Agent 状态

- 最后更新: {agents_state.get('lastUpdated_iso', 'N/A')}
- 可用 Agent 数量: {len(agents_state.get('agents', []))}

"""
        
        for agent in agents_state.get('agents', []):
            summary += f"- {agent.get('name', 'Unknown')} (ID: {agent.get('id', 'Unknown')})\n"
        
        summary += f"""
## 💬 会话状态

- 最后更新: {sessions_state.get('lastUpdated_iso', 'N/A')}
- 活跃会话数量: {len(sessions_state.get('sessions', []))}

"""
        
        total_tokens = 0
        for session in sessions_state.get('sessions', []):
            summary += f"- {session.get('displayName', 'Unknown')}\n"
            summary += f"  - 模型: {session.get('model', 'N/A')}\n"
            summary += f"  - Token 使用: {session.get('totalTokens', 0)}\n"
            total_tokens += session.get('totalTokens', 0)
        
        summary += f"""
## 📊 统计汇总

- 总 Token 使用: {total_tokens}

## ⚠️ 需要关注

"""
        
        # 检查需要干预的情况
        needs_attention = []
        for session in sessions_state.get('sessions', []):
            if session.get('abortedLastRun', False):
                needs_attention.append(f"- 会话异常终止: {session.get('displayName')}")
        
        if needs_attention:
            summary += "\n".join(needs_attention)
        else:
            summary += "暂无需要关注的事项\n"
        
        summary += f"""
---
生成时间: {datetime.now().isoformat()}
"""
        
        report_file = self.reports_path / f"daily-summary-{today}.md"
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(summary)
        
        self.log_activity("daily-summary-generated", {"file": str(report_file)})
        return summary, report_file
    
    def check_interventions(self):
        """检查需要干预的情况"""
        sessions_state = self.load_sessions_state()
        interventions = []
        
        for session in sessions_state.get('sessions', []):
            if session.get('abortedLastRun', False):
                interventions.append({
                    "type": "aborted_session",
                    "session": session.get('displayName'),
                    "sessionKey": session.get('key'),
                    "severity": "high",
                    "description": "会话异常终止"
                })
        
        interventions_file = self.today_logs / "interventions.json"
        with open(interventions_file, "w", encoding="utf-8") as f:
            json.dump({
                "checkedAt": int(time.time()),
                "checkedAt_iso": datetime.now().isoformat(),
                "interventions": interventions
            }, f, ensure_ascii=False, indent=2)
        
        self.log_activity("interventions-checked", {"count": len(interventions)})
        return interventions


def main():
    """主函数 - 完整扫描和记录"""
    tracker = AgentTracker()
    
    print("=" * 60)
    print("Agent 追踪系统 - 状态扫描")
    print("=" * 60)
    
    # 记录开始
    tracker.log_activity("scan-started")
    
    print(f"\n扫描时间: {datetime.now().isoformat()}")
    print("\n请在 OpenClaw 中运行以下命令并更新状态:")
    print("\n1. agents_list")
    print("2. sessions_list")
    print("3. subagents")
    print("\n然后将结果保存到追踪系统中")
    
    print("\n" + "=" * 60)
    print("扫描完成 - 请手动更新状态数据")
    print("=" * 60)


if __name__ == "__main__":
    main()
