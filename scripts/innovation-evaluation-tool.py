#!/usr/bin/env python3
"""
创新能力量化评估工具
功能：自动评估创新方案的五大维度得分，生成量化评估报告，支持多方案对比
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple

class InnovationEvaluationTool:
    def __init__(self):
        # 五大维度权重配置
        self.dimensions = {
            "创新性": {"weight": 0.3, "description": "反共识强度、方案独特性、认知突破程度"},
            "可行性": {"weight": 0.25, "description": "资源适配、技术可实现、风险可控"},
            "价值性": {"weight": 0.2, "description": "商业价值、社会价值、用户价值"},
            "可复制性": {"weight": 0.15, "description": "标准化程度、可推广范围、复用价值"},
            "可进化性": {"weight": 0.1, "description": "学习能力、迭代空间、持续优化潜力"}
        }
        
        # 评分标准
        self.scoring_criteria = {
            "创新性": [
                {"score": 0, "desc": "完全跟随行业常规做法，无任何创新"},
                {"score": 2, "desc": "局部微创新，对现有方案小幅优化"},
                {"score": 4, "desc": "跨领域方法迁移，有一定独特性"},
                {"score": 6, "desc": "打破部分行业共识，有明确差异化"},
                {"score": 8, "desc": "重大认知突破，反共识强度高"},
                {"score": 10, "desc": "颠覆性创新，重新定义行业规则"}
            ],
            "可行性": [
                {"score": 0, "desc": "完全不可行，技术/资源/风险存在致命问题"},
                {"score": 2, "desc": "可行性极低，需要突破多个重大瓶颈"},
                {"score": 4, "desc": "有一定可行性，但存在较多不确定性"},
                {"score": 6, "desc": "基本可行，核心瓶颈已解决，存在少量风险"},
                {"score": 8, "desc": "高度可行，技术成熟，资源可获得，风险可控"},
                {"score": 10, "desc": "完全可行，已通过验证，可立即落地"}
            ],
            "价值性": [
                {"score": 0, "desc": "无任何价值，甚至带来负面影响"},
                {"score": 2, "desc": "价值极低，投入产出比小于1"},
                {"score": 4, "desc": "有一定价值，投入产出比约1:1到1:3"},
                {"score": 6, "desc": "价值较高，投入产出比约1:3到1:10"},
                {"score": 8, "desc": "价值很高，投入产出比大于1:10，行业级价值"},
                {"score": 10, "desc": "价值极高，投入产出比大于1:100，社会级价值"}
            ],
            "可复制性": [
                {"score": 0, "desc": "完全不可复制，依赖特定资源/人/场景"},
                {"score": 2, "desc": "复制难度极大，需要定制化开发"},
                {"score": 4, "desc": "可复制，但需要较多适配工作"},
                {"score": 6, "desc": "复制性较好，标准化程度较高，少量适配即可推广"},
                {"score": 8, "desc": "复制性很强，高度标准化，可快速推广到多个场景"},
                {"score": 10, "desc": "完全标准化，开箱即用，可无限复制"}
            ],
            "可进化性": [
                {"score": 0, "desc": "完全固化，无任何迭代空间"},
                {"score": 2, "desc": "迭代空间极小，只能做局部微调"},
                {"score": 4, "desc": "有一定迭代空间，可优化部分功能"},
                {"score": 6, "desc": "迭代空间较大，可扩展功能和应用场景"},
                {"score": 8, "desc": "可进化性强，支持持续迭代和能力升级"},
                {"score": 10, "desc": "自进化系统，可自主学习优化，指数级成长"}
            ]
        }

    def _get_score_description(self, dimension: str, score: float) -> str:
        """获取得分对应的描述"""
        criteria = self.scoring_criteria[dimension]
        for i in range(len(criteria)-1):
            if criteria[i]['score'] <= score < criteria[i+1]['score']:
                return criteria[i]['desc']
        return criteria[-1]['desc']

    def calculate_creativity(self, scores: Dict[str, float], alpha: float = 0.4, beta: float = 0.3, gamma: float = 0.3, K: float = 8, E: float = 8) -> Tuple[float, float]:
        """
        计算单路径创造力C = (F^α · I^β · A^γ) · K · E
        :param scores: 各维度得分
        :param alpha: F权重
        :param beta: I权重
        :param gamma: A权重
        :param K: 知识广度得分(0-10)
        :param E: 实验验证能力得分(0-10)
        :return: (创造力得分, 综合得分)
        """
        F = scores['创新性'] / 10  # 归一化到0-1
        I = scores['可复制性'] / 10
        A = scores['创新性'] / 10
        
        creativity = (pow(F, alpha) * pow(I, beta) * pow(A, gamma)) * K * E
        
        # 综合得分（加权平均）
        total_score = sum(scores[dim] * self.dimensions[dim]['weight'] for dim in self.dimensions)
        
        return round(creativity, 2), round(total_score, 2)

    def evaluate_solution(self, solution_name: str, scores: Dict[str, float], K: float = 8, E: float = 8) -> Dict:
        """评估单个方案"""
        # 验证输入
        for dim in self.dimensions:
            if dim not in scores or scores[dim] < 0 or scores[dim] > 10:
                raise ValueError(f"维度{dim}的得分必须在0-10之间")
        
        creativity, total_score = self.calculate_creativity(scores, K=K, E=E)
        
        result = {
            "name": solution_name,
            "scores": scores,
            "creativity": creativity,
            "total_score": total_score,
            "level": self._get_level(total_score),
            "score_descriptions": {},
            "risk_warnings": []
        }
        
        # 添加得分描述
        for dim, score in scores.items():
            result['score_descriptions'][dim] = self._get_score_description(dim, score)
        
        # 风险预警
        for dim, score in scores.items():
            if score < 4:
                result['risk_warnings'].append(f"⚠️ {dim}得分过低（{score}/10）：{result['score_descriptions'][dim]}")
        
        return result

    def _get_level(self, total_score: float) -> str:
        """根据综合得分评定等级"""
        if total_score >= 9:
            return "S级（颠覆性创新）"
        elif total_score >= 8:
            return "A级（优秀创新）"
        elif total_score >= 7:
            return "B级（良好创新）"
        elif total_score >= 6:
            return "C级（一般创新）"
        elif total_score >= 5:
            return "D级（较差创新）"
        else:
            return "E级（不合格创新）"

    def compare_solutions(self, solutions: List[Dict]) -> List[Dict]:
        """多方案对比，按综合得分排序"""
        evaluated = []
        for sol in solutions:
            evaluated.append(self.evaluate_solution(sol['name'], sol['scores'], sol.get('K', 8), sol.get('E', 8)))
        
        # 按综合得分降序排序
        evaluated.sort(key=lambda x: x['total_score'], reverse=True)
        
        # 添加排名
        for i, sol in enumerate(evaluated, 1):
            sol['rank'] = i
        
        return evaluated

    def generate_evaluation_report(self, evaluation_result: Dict, output_path: str = None) -> str:
        """生成评估报告"""
        report = ["# 创新方案量化评估报告\n"]
        report.append(f"## 方案名称：{evaluation_result['name']}")
        report.append(f"## 评估时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        report.append("### 核心指标")
        report.append(f"- 综合得分：{evaluation_result['total_score']}/10")
        report.append(f"- 创造力指数：{evaluation_result['creativity']}")
        report.append(f"- 创新等级：{evaluation_result['level']}\n")
        
        report.append("### 各维度得分详情")
        report.append("| 维度 | 得分（10分制） | 权重 | 得分描述 |")
        report.append("|------|----------------|------|----------|")
        for dim, score in evaluation_result['scores'].items():
            weight = int(self.dimensions[dim]['weight'] * 100)
            desc = evaluation_result['score_descriptions'][dim]
            report.append(f"| {dim} | {score} | {weight}% | {desc} |")
        
        if evaluation_result['risk_warnings']:
            report.append("\n### ⚠️ 风险预警")
            for warning in evaluation_result['risk_warnings']:
                report.append(f"- {warning}")
        else:
            report.append("\n### ✅ 风险评估")
            report.append("- 无重大风险，方案可行性高")
        
        report.append("\n### 改进建议")
        for dim, score in evaluation_result['scores'].items():
            if score < 6:
                report.append(f"- 提升{dim}：建议针对{dim}维度进行优化，当前得分{score}，目标提升到6分以上")
            elif score < 8:
                report.append(f"- 优化{dim}：当前得分{score}，仍有提升空间")
        
        report_content = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"✅ 评估报告已保存到：{output_path}")
        
        return report_content

    def generate_comparison_report(self, comparison_result: List[Dict], output_path: str = None) -> str:
        """生成多方案对比报告"""
        report = ["# 创新方案多维度对比报告\n"]
        report.append(f"## 评估时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        report.append("### 方案排名")
        report.append("| 排名 | 方案名称 | 综合得分 | 创造力指数 | 创新等级 |")
        report.append("|------|----------|----------|------------|----------|")
        for sol in comparison_result:
            report.append(f"| {sol['rank']} | {sol['name']} | {sol['total_score']} | {sol['creativity']} | {sol['level']} |")
        
        report.append("\n### 各维度对比")
        dims = list(self.dimensions.keys())
        header = "| 方案名称 | " + " | ".join(dims) + " | 综合得分 | 排名 |"
        separator = "|----------|" + "|".join(["------------"] * len(dims)) + "|----------|------|"
        report.append(header)
        report.append(separator)
        for sol in comparison_result:
            scores = [str(sol['scores'][dim]) for dim in dims]
            report.append(f"| {sol['name']} | {' | '.join(scores)} | {sol['total_score']} | {sol['rank']} |")
        
        report.append("\n### 推荐方案")
        top_sol = comparison_result[0]
        report.append(f"推荐排名第一的方案：**{top_sol['name']}**")
        report.append(f"- 综合得分：{top_sol['total_score']}/10，等级：{top_sol['level']}")
        report.append(f"- 核心优势：创造力指数{top_sol['creativity']}，创新性和可行性平衡较好")
        
        if top_sol['risk_warnings']:
            report.append("\n注意事项：")
            for warning in top_sol['risk_warnings']:
                report.append(f"- {warning}")
        
        report_content = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"✅ 对比报告已保存到：{output_path}")
        
        return report_content

    def interactive_evaluation(self):
        """交互式评估单个方案"""
        print("🔍 创新方案量化评估工具")
        print("="*50)
        
        solution_name = input("请输入方案名称：")
        
        scores = {}
        print("\n请给各维度打分（0-10分）：")
        for dim, info in self.dimensions.items():
            while True:
                try:
                    score = float(input(f"{dim}（{info['description']}）："))
                    if 0 <= score <= 10:
                        scores[dim] = score
                        break
                    else:
                        print("❌ 得分必须在0-10之间，请重新输入")
                except ValueError:
                    print("❌ 请输入有效的数字")
        
        K = float(input("\n知识广度得分（0-10，默认8）：") or 8)
        E = float(input("实验验证能力得分（0-10，默认8）：") or 8)
        
        result = self.evaluate_solution(solution_name, scores, K, E)
        
        print("\n" + "="*50)
        print("📊 评估结果")
        print("="*50)
        print(f"方案名称：{result['name']}")
        print(f"综合得分：{result['total_score']}/10")
        print(f"创造力指数：{result['creativity']}")
        print(f"创新等级：{result['level']}")
        
        print("\n各维度得分：")
        for dim, score in result['scores'].items():
            print(f"  {dim}: {score}/10 - {result['score_descriptions'][dim]}")
        
        if result['risk_warnings']:
            print("\n⚠️ 风险预警：")
            for warning in result['risk_warnings']:
                print(f"  {warning}")
        
        save = input("\n是否保存报告？(y/n)：").lower() == 'y'
        if save:
            output_path = input("请输入报告保存路径（默认：./evaluation_report.md）：") or "./evaluation_report.md"
            self.generate_evaluation_report(result, output_path)

    def batch_evaluation(self, input_file: str, output_dir: str = "./"):
        """批量评估多个方案"""
        with open(input_file, 'r', encoding='utf-8') as f:
            solutions = json.load(f)
        
        os.makedirs(output_dir, exist_ok=True)
        results = []
        
        for sol in solutions:
            result = self.evaluate_solution(sol['name'], sol['scores'], sol.get('K', 8), sol.get('E', 8))
            results.append(result)
            report_path = f"{output_dir}/{sol['name'].replace(' ', '_')}_评估报告.md"
            self.generate_evaluation_report(result, report_path)
        
        # 生成对比报告
        comparison_result = self.compare_solutions(solutions)
        comparison_path = f"{output_dir}/多方案对比报告.md"
        self.generate_comparison_report(comparison_result, comparison_path)
        
        print(f"✅ 批量评估完成，共评估{len(solutions)}个方案，报告已保存到{output_dir}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='创新能力量化评估工具')
    parser.add_argument('--interactive', '-i', action='store_true', help='交互式评估单个方案')
    parser.add_argument('--batch', '-b', help='批量评估，输入JSON文件路径')
    parser.add_argument('--output', '-o', help='报告输出目录，默认当前目录', default='./')
    
    args = parser.parse_args()
    
    tool = InnovationEvaluationTool()
    
    if args.interactive:
        tool.interactive_evaluation()
    elif args.batch:
        tool.batch_evaluation(args.batch, args.output)
    else:
        parser.print_help()
