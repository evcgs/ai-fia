#!/usr/bin/env python3
"""
反共识机会挖掘工具
功能：自动分析行业共识，生成反共识机会清单，评估可行性和价值
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple
import re

class AntiConsensusMiningTool:
    def __init__(self):
        # 内置行业共识库（可扩展）
        self.builtin_consensus = {
            "医疗大模型": [
                {
                    "content": "医疗大模型要做通用大模型，覆盖所有科室和疾病",
                    "reason": "通用大模型在其他领域的成功经验，资本偏好大而全的故事",
                    "tags": ["技术路线", "产品定位"]
                },
                {
                    "content": "模型参数越大效果越好，需要千亿级参数",
                    "reason": "大模型的scaling law经验，越大越能吸引眼球",
                    "tags": ["技术路线", "性能优化"]
                },
                {
                    "content": "医疗AI的终极目标是替代医生，实现全自动诊断",
                    "reason": "科技宣传的误导，对医疗行业责任体系不了解",
                    "tags": ["产品定位", "价值主张"]
                },
                {
                    "content": "先做通用技术平台，再找落地场景",
                    "reason": "技术导向思维，先有技术再找应用",
                    "tags": ["落地路径", "战略选择"]
                }
            ],
            "新能源汽车": [
                {
                    "content": "续航里程越长越好，用户愿意为长续航支付溢价",
                    "reason": "早期电动车续航短，用户有里程焦虑",
                    "tags": ["产品设计", "用户需求"]
                },
                {
                    "content": "新能源车企必须自建工厂才能保证质量",
                    "reason": "传统车企的经验，自建工厂可控性强",
                    "tags": ["运营模式", "供应链"]
                },
                {
                    "content": "全自动驾驶是电动车的核心竞争力",
                    "reason": "科技公司宣传，资本故事需要",
                    "tags": ["技术路线", "价值主张"]
                },
                {
                    "content": "换电模式比充电模式体验更好",
                    "reason": "换电速度快，解决补能焦虑",
                    "tags": ["运营模式", "用户体验"]
                }
            ],
            "互联网": [
                {
                    "content": "流量是互联网产品的核心，用户量越大价值越高",
                    "reason": "互联网上半场的经验，流量变现模式",
                    "tags": ["产品逻辑", "商业模式"]
                },
                {
                    "content": "免费模式是互联网产品的标配，先烧钱再盈利",
                    "reason": "互联网平台的成功路径，通过免费获取用户",
                    "tags": ["商业模式", "运营策略"]
                },
                {
                    "content": "算法推荐是内容平台的最优解",
                    "reason": "算法推荐提升用户停留时长，广告收入更高",
                    "tags": ["产品设计", "技术路线"]
                },
                {
                    "content": "To C产品比To B产品天花板更高",
                    "reason": "To C产品用户基数大，估值更高",
                    "tags": ["战略选择", "商业模式"]
                }
            ]
        }
        
        # 反共识评估维度
        self.evaluation_dimensions = [
            {"name": "价值潜力", "weight": 0.3, "description": "反共识如果成立带来的价值大小"},
            {"name": "可行性", "weight": 0.3, "description": "反共识成立的概率和实现难度"},
            {"name": "竞争壁垒", "weight": 0.2, "description": "反共识带来的差异化和壁垒高低"},
            {"name": "风险程度", "weight": 0.2, "description": "反共识失败带来的损失和风险"}
        ]

    def extract_consensus_from_text(self, text: str) -> List[Dict]:
        """从文本中提取行业共识"""
        # 匹配共识模式："大家都认为..."、"行业普遍认为..."、"共识是..."等
        patterns = [
            r'(大家普遍认为|行业共识是|普遍认为|大家都觉得|通常认为|主流观点是)([^。！\n]+)',
            r'(要想成功|必须|应该|一定要)([^。！\n]+)'
        ]
        
        consensus_list = []
        for pattern in patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                consensus = {
                    "content": match[1].strip(),
                    "reason": "从文本提取",
                    "source": "文本输入",
                    "tags": []
                }
                if consensus['content'] and len(consensus['content']) > 10:
                    consensus_list.append(consensus)
        
        return consensus_list

    def generate_anti_consensus(self, consensus: Dict) -> List[Dict]:
        """针对单个共识生成反共识假设"""
        content = consensus['content']
        anti_hypotheses = []
        
        # 反共识生成策略
        strategies = [
            # 策略1：完全反向
            ("反向假设", lambda x: f"{x}是错误的，恰恰相反，"),
            # 策略2：边界限定
            ("边界限定", lambda x: f"{x}只在特定条件下成立，实际上更应该"),
            # 策略3：因果倒置
            ("因果倒置", lambda x: f"不是因为{x}，而是因为"),
            # 策略4：场景替换
            ("场景替换", lambda x: f"在XX场景下，{x}不成立，应该"),
            # 策略5：升级替代
            ("升级替代", lambda x: f"{x}是旧有思路，更好的方法是")
        ]
        
        for strategy_name, strategy_func in strategies:
            hypothesis = strategy_func(content)
            anti_hypotheses.append({
                "hypothesis": hypothesis,
                "generation_strategy": strategy_name,
                "original_consensus": content,
                "score": 0,
                "evaluation": {}
            })
        
        return anti_hypotheses

    def evaluate_anti_consensus(self, anti_consensus: Dict) -> Dict:
        """评估反共识机会的价值和可行性"""
        print(f"\n评估反共识：{anti_consensus['hypothesis']}")
        print("请从以下维度打分（0-10分）：")
        
        scores = {}
        total_score = 0
        for dim in self.evaluation_dimensions:
            while True:
                try:
                    score = float(input(f"  {dim['name']}（{dim['description']}）："))
                    if 0 <= score <= 10:
                        scores[dim['name']] = score
                        total_score += score * dim['weight']
                        break
                    else:
                        print("  ❌ 得分必须在0-10之间，请重新输入")
                except ValueError:
                    print("  ❌ 请输入有效的数字")
        
        total_score = round(total_score, 2)
        
        # 优先级评定
        if total_score >= 8:
            priority = "极高"
            recommendation = "强烈推荐投入，重点布局"
        elif total_score >= 6:
            priority = "高"
            recommendation = "值得投入，积极探索"
        elif total_score >= 4:
            priority = "中"
            recommendation = "可小范围试点，观察效果"
        else:
            priority = "低"
            recommendation = "风险较高，建议谨慎投入"
        
        return {
            **anti_consensus,
            "scores": scores,
            "total_score": total_score,
            "priority": priority,
            "recommendation": recommendation,
            "evaluation_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def match_success_cases(self, anti_consensus: Dict) -> List[Dict]:
        """匹配相似的反共识成功案例"""
        # 内置案例库
        case_library = [
            {
                "name": "蔚来代工模式",
                "original_consensus": "车企必须自建工厂才能保证质量",
                "anti_consensus": "新能源车企不需要自建工厂，代工模式更高效",
                "result": "蔚来通过江淮代工快速实现量产，降低了初期投入和风险",
                "industry": "新能源汽车"
            },
            {
                "name": "特斯拉软件付费",
                "original_consensus": "汽车是一次性买卖，后续没有收入",
                "anti_consensus": "汽车可以通过软件订阅实现持续收入",
                "result": "特斯拉Autopilot软件付费收入超过10亿美元/年，利润率极高",
                "industry": "新能源汽车"
            },
            {
                "name": "拼多多反向电商",
                "original_consensus": "电商应该人找货，搜索是核心",
                "anti_consensus": "电商可以货找人，推荐模式效率更高",
                "result": "拼多多通过社交推荐和拼团模式，3年时间突破万亿GMV",
                "industry": "互联网"
            },
            {
                "name": "推想医疗专科AI",
                "original_consensus": "医疗AI要做通用大模型，覆盖所有科室",
                "anti_consensus": "医疗AI应该聚焦专科专病，做深做透才有价值",
                "result": "推想医疗聚焦肺部影像AI，成为国内首个获得NMPA三类证的医疗AI产品，落地3000多家医院",
                "industry": "医疗大模型"
            }
        ]
        
        matching_cases = []
        for case in case_library:
            # 简单的关键词匹配
            if any(keyword in anti_consensus['hypothesis'] for keyword in case['anti_consensus'].split()):
                matching_cases.append(case)
            elif anti_consensus.get('original_consensus') and case['original_consensus'] in anti_consensus['original_consensus']:
                matching_cases.append(case)
        
        return matching_cases

    def generate_opportunity_report(self, anti_consensus_list: List[Dict], industry: str, output_path: str = None) -> str:
        """生成反共识机会报告"""
        report = ["# 反共识机会挖掘报告\n"]
        report.append(f"## 行业：{industry}")
        report.append(f"## 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # 按优先级排序
        anti_consensus_list.sort(key=lambda x: x['total_score'], reverse=True)
        
        report.append("### 机会总览")
        report.append(f"共挖掘到 {len(anti_consensus_list)} 个反共识机会：")
        report.append("| 优先级 | 数量 |")
        report.append("|--------|------|")
        for priority in ["极高", "高", "中", "低"]:
            count = sum(1 for ac in anti_consensus_list if ac['priority'] == priority)
            report.append(f"| {priority} | {count} |")
        
        report.append("\n### 高价值机会详情")
        for i, ac in enumerate([ac for ac in anti_consensus_list if ac['priority'] in ["极高", "高"]], 1):
            report.append(f"#### 机会 {i}：{ac['priority']}优先级")
            report.append(f"**反共识假设**：{ac['hypothesis']}")
            report.append(f"**原始共识**：{ac['original_consensus']}")
            report.append(f"**生成策略**：{ac['generation_strategy']}")
            report.append(f"**综合得分**：{ac['total_score']}/10")
            report.append(f"**建议**：{ac['recommendation']}\n")
            
            report.append("**各维度得分**：")
            report.append("| 维度 | 得分 | 权重 |")
            report.append("|------|------|------|")
            for dim in self.evaluation_dimensions:
                report.append(f"| {dim['name']} | {ac['scores'][dim['name']]} | {int(dim['weight']*100)}% |")
            
            # 匹配案例
            cases = self.match_success_cases(ac)
            if cases:
                report.append("\n**相似成功案例**：")
                for case in cases:
                    report.append(f"- [{case['name']}] {case['result']}")
            
            report.append("\n---\n")
        
        # 所有机会列表
        report.append("### 全部机会清单")
        report.append("| 优先级 | 综合得分 | 反共识假设 | 建议 |")
        report.append("|--------|----------|------------|------|")
        for ac in anti_consensus_list:
            report.append(f"| {ac['priority']} | {ac['total_score']} | {ac['hypothesis'][:50]}... | {ac['recommendation']} |")
        
        report_content = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"✅ 反共识机会报告已保存到：{output_path}")
        
        return report_content

    def interactive_mining(self):
        """交互式反共识挖掘"""
        print("🔍 反共识机会挖掘工具")
        print("="*50)
        
        industry = input("请输入目标行业：")
        
        # 选择共识来源
        print("\n请选择共识来源：")
        print("1. 使用内置行业共识库")
        print("2. 从文本输入提取共识")
        choice = input("请输入选项：")
        
        consensus_list = []
        if choice == '1':
            if industry in self.builtin_consensus:
                consensus_list = self.builtin_consensus[industry]
                print(f"\n✅ 加载内置{industry}行业共识{len(consensus_list)}条")
            else:
                print(f"⚠️ 内置库中没有{industry}行业的共识，请选择文本输入")
                choice = '2'
        
        if choice == '2':
            print("\n请输入包含行业共识的文本（输入空行结束）：")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            text = "\n".join(lines)
            consensus_list = self.extract_consensus_from_text(text)
            print(f"\n✅ 从文本中提取到{len(consensus_list)}条共识")
        
        if not consensus_list:
            print("❌ 没有获取到任何共识，退出")
            return
        
        # 生成反共识
        all_anti_consensus = []
        for i, consensus in enumerate(consensus_list, 1):
            print(f"\n📝 处理共识 {i}/{len(consensus_list)}：{consensus['content']}")
            anti_list = self.generate_anti_consensus(consensus)
            
            # 筛选有价值的反共识
            for j, anti in enumerate(anti_list, 1):
                print(f"\n反共识假设 {j}：{anti['hypothesis']}")
                use = input("是否评估这个反共识？(y/n，默认y)：").lower()
                if use == 'n':
                    continue
                
                evaluated = self.evaluate_anti_consensus(anti)
                all_anti_consensus.append(evaluated)
        
        if not all_anti_consensus:
            print("❌ 没有选择任何反共识，退出")
            return
        
        # 生成报告
        print("\n" + "="*50)
        print("📊 挖掘完成")
        print(f"共生成{len(all_anti_consensus)}个反共识机会")
        
        save = input("\n是否保存报告？(y/n)：").lower() == 'y'
        if save:
            output_path = input("请输入报告保存路径（默认：./anti_consensus_report.md）：") or "./anti_consensus_report.md"
            self.generate_opportunity_report(all_anti_consensus, industry, output_path)
        
        # 显示高优先级机会
        high_priority = [ac for ac in all_anti_consensus if ac['priority'] in ["极高", "高"]]
        if high_priority:
            print("\n🌟 高价值反共识机会：")
            for i, ac in enumerate(high_priority, 1):
                print(f"{i}. [{ac['priority']} {ac['total_score']}分] {ac['hypothesis']}")
                print(f"   建议：{ac['recommendation']}")

    def batch_mining(self, industry: str, consensus_file: str, output_dir: str = "./"):
        """批量挖掘反共识机会"""
        with open(consensus_file, 'r', encoding='utf-8') as f:
            consensus_list = json.load(f)
        
        os.makedirs(output_dir, exist_ok=True)
        
        all_anti_consensus = []
        for consensus in consensus_list:
            anti_list = self.generate_anti_consensus(consensus)
            for anti in anti_list:
                # 批量模式下默认自动评估（可扩展为AI自动评分）
                anti['scores'] = {dim['name']: 5 for dim in self.evaluation_dimensions}
                anti['total_score'] = 5
                anti['priority'] = "中"
                anti['recommendation'] = "待人工评估"
                all_anti_consensus.append(anti)
        
        report_path = f"{output_dir}/{industry}_反共识机会报告.md"
        self.generate_opportunity_report(all_anti_consensus, industry, report_path)
        
        print(f"✅ 批量挖掘完成，共生成{len(all_anti_consensus)}个反共识机会，报告已保存到{report_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='反共识机会挖掘工具')
    parser.add_argument('--interactive', '-i', action='store_true', help='交互式挖掘反共识机会')
    parser.add_argument('--batch', '-b', help='批量挖掘，输入共识JSON文件路径')
    parser.add_argument('--industry', '-n', help='目标行业名称')
    parser.add_argument('--output', '-o', help='报告输出目录，默认当前目录', default='./')
    
    args = parser.parse_args()
    
    tool = AntiConsensusMiningTool()
    
    if args.interactive:
        tool.interactive_mining()
    elif args.batch and args.industry:
        tool.batch_mining(args.industry, args.batch, args.output)
    else:
        parser.print_help()
