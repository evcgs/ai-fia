#!/usr/bin/env python3
"""
FIA创新流程自动化助手
功能：交互式引导用户完成FIA十步创新全流程，自动生成各阶段输出物
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any

class FIAInnovationAssistant:
    def __init__(self, project_name: str = None):
        self.project_name = project_name or input("请输入项目名称：")
        self.project_dir = f"./fia-projects/{self.project_name}"
        os.makedirs(self.project_dir, exist_ok=True)
        self.project_data = {
            "basic_info": {
                "name": self.project_name,
                "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "current_step": 0
            },
            "steps": [
                {"name": "问题本质拆解", "completed": False, "outputs": []},
                {"name": "跨领域知识扫描", "completed": False, "outputs": []},
                {"name": "共识假设挑战", "completed": False, "outputs": []},
                {"name": "多维方案碰撞", "completed": False, "outputs": []},
                {"name": "可行性快速验证", "completed": False, "outputs": []},
                {"name": "方案迭代优化", "completed": False, "outputs": []},
                {"name": "价值复盘沉淀", "completed": False, "outputs": []},
                {"name": "场景适应调整", "completed": False, "outputs": []},
                {"name": "协作执行落地", "completed": False, "outputs": []},
                {"name": "学习进化循环", "completed": False, "outputs": []}
            ]
        }
        self._load_project_data()

    def _load_project_data(self):
        """加载已有的项目数据"""
        data_file = f"{self.project_dir}/project_data.json"
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                self.project_data = json.load(f)

    def _save_project_data(self):
        """保存项目数据"""
        data_file = f"{self.project_dir}/project_data.json"
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(self.project_data, f, ensure_ascii=False, indent=2)

    def _save_output(self, step: int, filename: str, content: str):
        """保存输出文件"""
        file_path = f"{self.project_dir}/Step{step+1}_{filename}"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        self.project_data['steps'][step]['outputs'].append(filename)
        self._save_project_data()
        print(f"✅ 已保存：{file_path}")

    def _generate_step1_report(self, data: Dict) -> str:
        """生成步骤1：问题本质拆解报告"""
        report = ["# 问题本质拆解报告\n"]
        report.append(f"## 项目名称：{self.project_name}")
        report.append(f"## 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        report.append("### 1. 核心问题定义")
        report.append(f">{data['core_problem']}\n")
        
        report.append("### 2. 目标-约束-假设矩阵")
        report.append("| 类型 | 内容 | 验证状态 |")
        report.append("|------|------|----------|")
        report.append(f"| **核心目标** | {data['core_target']} | 待验证 |")
        report.append(f"| **刚性约束** | {data['constraints']} | 待验证 |")
        report.append(f"| **隐含假设** | {data['assumptions']} | 待验证 |\n")
        
        report.append("### 3. 第一性原理拆解")
        report.append(f"底层规律：{data['first_principle']}\n")
        report.append("适用边界：" + data.get('boundary', '待明确'))
        
        return "\n".join(report)

    def _generate_step2_report(self, data: Dict) -> str:
        """生成步骤2：跨领域知识扫描报告"""
        report = ["# 跨领域知识扫描报告\n"]
        report.append(f"## 项目名称：{self.project_name}")
        report.append(f"## 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        report.append("### 1. 关联领域识别")
        report.append("| 领域 | 核心知识/方法 | 与核心问题的关联 |")
        report.append("|------|--------------|------------------|")
        for i, domain in enumerate(data['domains'], 1):
            report.append(f"| {domain['name']} | {domain['knowledge']} | {domain['relation']} |")
        
        report.append("\n### 2. 方法迁移清单")
        report.append("| 来源领域 | 方法/模型名称 | 迁移应用场景 | 预期价值 |")
        report.append("|----------|--------------|--------------|----------|")
        for i, method in enumerate(data['methods'], 1):
            report.append(f"| {method['domain']} | {method['name']} | {method['scenario']} | {method['value']} |")
        
        return "\n".join(report)

    def _generate_step3_report(self, data: Dict) -> str:
        """生成步骤3：共识假设挑战报告"""
        report = ["# 共识假设挑战报告\n"]
        report.append(f"## 项目名称：{self.project_name}")
        report.append(f"## 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        report.append("### 1. 行业共识梳理")
        for i, consensus in enumerate(data['consensus'], 1):
            report.append(f"{i}. **{consensus['content']}**")
            report.append(f"   形成原因：{consensus['reason']}\n")
        
        report.append("### 2. 反共识机会评估")
        report.append("| 反共识假设 | 价值大小 | 可行性 | 风险等级 | 优先级 |")
        report.append("|------------|----------|--------|----------|--------|")
        for i, anti in enumerate(data['anti_consensus'], 1):
            report.append(f"| {anti['hypothesis']} | {anti['value']} | {anti['feasibility']} | {anti['risk']} | {anti['priority']} |")
        
        return "\n".join(report)

    def step1_problem_definition(self):
        """执行步骤1：问题本质拆解"""
        print("\n" + "="*50)
        print("📝 Step 1: 问题本质拆解")
        print("="*50)
        
        data = {}
        data['core_problem'] = input("1. 请描述核心问题（具体、可量化）：")
        data['core_target'] = input("2. 请描述核心目标（遵循SMART原则）：")
        data['constraints'] = input("3. 请列出刚性约束（成本、时间、合规、安全等）：")
        data['assumptions'] = input("4. 请列出当前的隐含假设（默认成立但未验证的）：")
        data['first_principle'] = input("5. 请描述第一性原理拆解得到的底层规律：")
        data['boundary'] = input("6. 请描述该规律的适用边界：")
        
        report = self._generate_step1_report(data)
        self._save_output(0, "问题本质拆解报告.md", report)
        
        self.project_data['steps'][0]['completed'] = True
        self.project_data['basic_info']['current_step'] = 1
        self._save_project_data()
        
        print("\n✅ 步骤1完成！下一步：跨领域知识扫描")

    def step2_knowledge_scan(self):
        """执行步骤2：跨领域知识扫描"""
        print("\n" + "="*50)
        print("🔍 Step 2: 跨领域知识扫描")
        print("="*50)
        
        data = {}
        domains = []
        domain_count = int(input("1. 请输入关联领域数量："))
        for i in range(domain_count):
            print(f"\n领域 {i+1}:")
            domain = {
                "name": input("  领域名称："),
                "knowledge": input("  核心知识/方法："),
                "relation": input("  与核心问题的关联：")
            }
            domains.append(domain)
        data['domains'] = domains
        
        methods = []
        method_count = int(input("\n2. 请输入可迁移方法数量："))
        for i in range(method_count):
            print(f"\n方法 {i+1}:")
            method = {
                "domain": input("  来源领域："),
                "name": input("  方法/模型名称："),
                "scenario": input("  迁移应用场景："),
                "value": input("  预期价值：")
            }
            methods.append(method)
        data['methods'] = methods
        
        report = self._generate_step2_report(data)
        self._save_output(1, "跨领域知识扫描报告.md", report)
        
        self.project_data['steps'][1]['completed'] = True
        self.project_data['basic_info']['current_step'] = 2
        self._save_project_data()
        
        print("\n✅ 步骤2完成！下一步：共识假设挑战")

    def step3_consensus_challenge(self):
        """执行步骤3：共识假设挑战"""
        print("\n" + "="*50)
        print("🤔 Step 3: 共识假设挑战")
        print("="*50)
        
        data = {}
        consensus = []
        consensus_count = int(input("1. 请输入行业共识数量："))
        for i in range(consensus_count):
            print(f"\n共识 {i+1}:")
            con = {
                "content": input("  共识内容："),
                "reason": input("  形成原因：")
            }
            consensus.append(con)
        data['consensus'] = consensus
        
        anti_consensus = []
        anti_count = int(input("\n2. 请输入反共识假设数量："))
        for i in range(anti_count):
            print(f"\n反共识 {i+1}:")
            anti = {
                "hypothesis": input("  反共识假设："),
                "value": input("  价值大小（高/中/低）："),
                "feasibility": input("  可行性（高/中/低）："),
                "risk": input("  风险等级（高/中/低）："),
                "priority": input("  优先级（高/中/低）：")
            }
            anti_consensus.append(anti)
        data['anti_consensus'] = anti_consensus
        
        report = self._generate_step3_report(data)
        self._save_output(2, "共识假设挑战报告.md", report)
        
        self.project_data['steps'][2]['completed'] = True
        self.project_data['basic_info']['current_step'] = 3
        self._save_project_data()
        
        print("\n✅ 步骤3完成！下一步：多维方案碰撞")

    def show_project_status(self):
        """显示项目进度"""
        print("\n" + "="*50)
        print(f"📊 项目进度：{self.project_name}")
        print("="*50)
        
        completed = sum(1 for step in self.project_data['steps'] if step['completed'])
        total = len(self.project_data['steps'])
        progress = int(completed / total * 100)
        
        print(f"总进度：{completed}/{total} 步 ({progress}%)")
        print(f"当前步骤：Step {self.project_data['basic_info']['current_step'] + 1}: {self.project_data['steps'][self.project_data['basic_info']['current_step']]['name']}")
        print("\n各步骤状态：")
        for i, step in enumerate(self.project_data['steps'], 1):
            status = "✅ 已完成" if step['completed'] else "⏳ 未完成"
            print(f"Step {i}: {step['name']} {status}")
            if step['outputs']:
                for output in step['outputs']:
                    print(f"   ↳ {output}")

    def run(self):
        """运行助手"""
        print("🎉 欢迎使用FIA创新流程自动化助手！")
        print(f"当前项目：{self.project_name}")
        
        while True:
            print("\n" + "="*50)
            print("请选择操作：")
            print("1. 继续下一步")
            print("2. 查看项目进度")
            print("3. 跳转到指定步骤")
            print("4. 退出")
            
            choice = input("\n请输入选项：")
            
            if choice == '1':
                current_step = self.project_data['basic_info']['current_step']
                if current_step == 0:
                    self.step1_problem_definition()
                elif current_step == 1:
                    self.step2_knowledge_scan()
                elif current_step == 2:
                    self.step3_consensus_challenge()
                elif current_step < 10:
                    print(f"⚠️ Step {current_step + 1} 开发中，敬请期待...")
                else:
                    print("🎉 所有步骤已完成！")
            
            elif choice == '2':
                self.show_project_status()
            
            elif choice == '3':
                step = int(input("请输入要跳转到的步骤编号（1-10）：")) - 1
                if 0 <= step < 10:
                    self.project_data['basic_info']['current_step'] = step
                    self._save_project_data()
                    print(f"✅ 已跳转到 Step {step + 1}")
                else:
                    print("❌ 无效的步骤编号")
            
            elif choice == '4':
                print("👋 再见！")
                break
            
            else:
                print("❌ 无效选项，请重新输入")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='FIA创新流程自动化助手')
    parser.add_argument('--project', '-p', help='项目名称')
    args = parser.parse_args()
    
    assistant = FIAInnovationAssistant(args.project)
    assistant.run()
