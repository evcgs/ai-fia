# FIA-X 安装与使用指南（ai-fia）
## 🚀 快速开始
### 仓库信息
- **仓库名称**：ai-fia (AI First Innovation Framework)
- **定位**：AI驱动的通用创新方法论体系，国际化命名，易于全球传播
### 环境要求
- Python 3.8+
- 操作系统：macOS/Linux/Windows
- OpenClaw 2026.2.0+（可选，直接运行脚本不需要）
### 安装步骤
#### 方式1：OpenClaw 技能安装（推荐）
FIA-X 已经按照 OpenClaw 技能规范开发，可直接加载使用：
1. 确保技能目录位于 OpenClaw 工作区：
   ```bash
   # 默认路径已配置
   ls /Users/evcgs/.openclaw/workspace/skills/ai-fia
   ```
2. 重启 OpenClaw 网关，系统会自动识别加载 FIA-X 技能
3. 验证安装：
   ```bash
   openclaw skills list | grep fia-core
   # 输出包含 fia-core 说明安装成功
   ```
#### 方式2：独立运行（不需要 OpenClaw）
直接克隆或下载代码到本地即可使用：
```bash
# 进入项目目录
cd fia-core
# 验证运行
python scripts/fia-innovation-assistant.py --help
# 显示帮助信息说明安装成功
```
#### 方式3：安装包分发
```bash
# 打包成 .skill 安装包
openclaw skill package ai-fia --output ./dist
# 生成的 ai-fia.skill 可在其他 OpenClaw 环境安装
openclaw skill install ./dist/ai-fia.skill
```
---
## 🎯 使用方式
### 方式1：自然语言触发（OpenClaw 环境，最方便）
直接对话即可自动触发，不需要记忆任何命令：
#### 常用触发语示例：
```
# 启动完整创新流程
"帮我用FIA方法论做一个医疗AI创新项目"
"用FIA十步流程拆解这个创业项目"
"启动FIA创新流程助手，项目名称是新能源电池创新"
# 方案评估
"评估一下这个创新方案的得分"
"用FIA评估体系给这三个方案做个对比"
# 反共识挖掘
"挖掘医疗AI行业的反共识机会"
"分析新能源行业的主流共识和突破方向"
# 文档生成
"用FIA第一性原理模板拆解这个问题"
"生成一份FIA创新方案评估报告"
"参考反共识模板输出互联网行业机会清单"
```
#### 强制触发：
如果需要强制使用 FIA 技能，在对话开头加上前缀：
```
"使用FIA技能：帮我评估这个方案的创新性"
```
---
### 方式2：命令行触发（精准控制）
在终端直接运行脚本，适合自动化集成和批量处理：
#### 1. 创新流程助手
```bash
# 交互式引导完成十步创新流程
python scripts/fia-innovation-assistant.py --project "你的项目名称"
# 参数说明
--project, -p: 项目名称（可选，默认交互式输入）
```
#### 2. 创新方案评估工具
```bash
# 交互式评估单个方案
python scripts/innovation-evaluation-tool.py --interactive
# 批量评估多个方案
python scripts/innovation-evaluation-tool.py --batch solutions.json --output ./reports
# 参数说明
--interactive, -i: 交互式评估
--batch, -b: 批量评估，输入JSON文件路径
--output, -o: 报告输出目录
```
#### 3. 反共识机会挖掘工具
```bash
# 交互式挖掘反共识机会
python scripts/anti-consensus-mining-tool.py --interactive
# 批量挖掘
python scripts/anti-consensus-mining-tool.py --batch consensus.json --industry "医疗AI" --output ./reports
# 参数说明
--interactive, -i: 交互式挖掘
--batch, -b: 批量挖掘，输入共识JSON文件路径
--industry, -n: 目标行业名称
--output, -o: 报告输出目录
```
---
### 方式3：API 调用（二次开发）
所有工具都支持导入作为 Python 模块使用，适合集成到自己的系统中：
```python
# 导入评估工具
from scripts.innovation_evaluation_tool import InnovationEvaluationTool
# 初始化工具
evaluator = InnovationEvaluationTool()
# 评估方案
scores = {
    "创新性": 8.5,
    "可行性": 7.0,
    "价值性": 9.0,
    "可复制性": 6.5,
    "可进化性": 8.0
}
result = evaluator.evaluate_solution("新能源电池创新方案", scores)
# 输出结果
print(f"综合得分：{result['total_score']}")
print(f"创新等级：{result['level']}")
# 生成报告
evaluator.generate_evaluation_report(result, "./report.md")
```
---
## 📁 项目结构
```
ai-fia/
├── SKILL.md              # OpenClaw 技能元数据（必填）
├── readme.md             # 项目总览
├── install.md            # 本安装使用指南
├── extension-spec.md     # 行业扩展规范
├── scripts/              # 可执行工具脚本
│   ├── fia-innovation-assistant.py    # 创新流程助手
│   ├── innovation-evaluation-tool.py  # 方案评估工具
│   └── anti-consensus-mining-tool.py  # 反共识挖掘工具
└── references/           # 参考资源库
    ├── templates/        # 标准化模板
    │   ├── ten-steps-template.md
    │   ├── first-principle-template.md
    │   ├── interdisciplinary-template.md
    │   └── anti-consensus-template.md
    ├── case-library/     # 创新案例库
    │   ├── technology-innovation.md
    │   ├── product-innovation.md
    │   └── anti-consensus-innovation.md
    ├── industry-consensus-library/  # 行业共识库
    │   ├── medical-ai.md
    │   ├── new-energy.md
    │   └── internet.md
    └── thinking-models-library.md   # 跨学科思维模型库
```
---
## ✅ 功能验证
### 快速测试
运行以下命令验证所有功能正常：
```bash
# 进入项目目录
cd ai-fia
# 测试流程助手
python scripts/fia-innovation-assistant.py --help
# 测试评估工具
python scripts/innovation-evaluation-tool.py --help
# 测试反共识工具
python scripts/anti-consensus-mining-tool.py --help
```
### 完整流程测试
```bash
# 启动一个测试项目
python scripts/fia-innovation-assistant.py --project "测试项目"
# 按照引导完成第一步，确认可以正常生成报告
```
---
## 🔧 常见问题
### Q: 运行脚本提示权限不足？
A: 执行 `chmod +x scripts/*.py` 添加可执行权限
### Q: OpenClaw 无法识别技能？
A: 1. 确认技能目录位于 OpenClaw 工作区的 `skills/` 目录下
   2. 重启 OpenClaw 网关：`openclaw gateway restart`
   3. 检查 SKILL.md 文件格式是否正确
### Q: 生成的报告保存在哪里？
A: 默认保存在当前目录下的 `fia-projects/[项目名称]/` 目录中，可通过参数自定义输出路径
### Q: 如何扩展行业版本？
A: 参考 `EXTENSION_SPEC.md` 行业扩展规范，只需补充行业专属内容，不需要修改核心层代码
---
## 📞 技术支持
- 代码仓库：[内部 Git 地址]
- 文档中心：[内部文档地址]
- 问题反馈：提交 Issue 或联系维护团队
---
**版本**：v1.0  
**更新日期**：2026-03-14  
**维护人**：FIA-X 团队
