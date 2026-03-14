# GitHub 发布指南
## 🚀 一键发布到 GitHub
### 前置准备
1. 确保已经安装 Git 并配置好 GitHub 账号
2. 在 GitHub 上创建新的空仓库，命名为 `ai-fia`（Public 权限）
### 发布步骤
执行以下命令即可完成发布：
```bash
# 进入项目目录
cd /Users/evcgs/.openclaw/workspace/ai-fia-release
# 关联远程仓库（替换为你的 GitHub 仓库地址）
git remote add origin https://github.com/[your-github-username]/ai-fia.git
# 推送代码到 main 分支
git push -u origin main
# 打版本标签
git tag -a v1.0.0 -m "Release v1.0.0: Initial release of ai-fia framework"
git push origin v1.0.0
```
### 创建 GitHub Release
1. 进入你的 GitHub 仓库页面
2. 点击 "Releases" → "Draft a new release"
3. 选择标签 `v1.0.0`，填写发布标题：`v1.0.0 - FIA-X AI First Innovation Framework`
4. 复制以下发布说明：
```markdown
# FIA-X v1.0.0 正式发布
## 🎉 项目介绍
**ai-fia** (AI First Innovation Framework) 是一套以认知升级为核心、AI可执行为导向的通用创新方法论体系，核心主张是：
> 创造力不是灵光一现，而是**可量化、可执行、可进化的系统能力**
## ✨ 核心特性
### 1. 三大认知支柱
- **First-principle（第一性原理）**：穿透事物本质，摆脱路径依赖
- **Interdisciplinary（跨学科交叉）**：融合多元知识，创造新组合
- **Anti-consensus（反共识思维）**：突破群体认知，构建差异化壁垒
### 2. 十步创新流程
从问题拆解到持续进化的全闭环流程，覆盖创新全生命周期：
1. 问题本质拆解 → 2. 跨领域知识扫描 → 3. 共识假设挑战 → 4. 多维方案碰撞 → 5. 可行性快速验证
6. 方案迭代优化 → 7. 价值复盘沉淀 → 8. 场景适应调整 → 9. 协作执行落地 → 10. 学习进化循环
### 3. 核心工具集
- 🛠️ `fia-innovation-assistant.py`：交互式引导完成全流程创新，自动生成标准化报告
- 📊 `innovation-evaluation-tool.py`：五大维度量化评估创新方案，支持多方案对比排名
- 💡 `anti-consensus-mining-tool.py`：自动挖掘行业反共识机会，评估价值和可行性
### 4. 完整知识库
- 9个精选创新案例（技术/产品/反共识）
- 3大行业共识库（医疗AI/新能源/互联网，含39条主流共识+反共识方向）
- 6大类近100个跨学科思维模型
- 4份标准化创新模板
## 🚀 快速开始
### OpenClaw 环境（推荐）
1. 安装技能：`openclaw skill install ai-fia`
2. 自然语言触发："帮我用FIA方法论做一个创新项目"
### 独立运行
```bash
# 克隆仓库
git clone https://github.com/[your-github-username]/ai-fia.git
cd ai-fia
# 启动创新流程助手
python scripts/fia-innovation-assistant.py --project "你的项目名称"
```
## 📦 技能规格
- 兼容 OpenClaw 2026.2.0+
- 零依赖，纯 Python 开发，支持所有操作系统
- 完全符合 OpenClaw 技能规范，开箱即用
## 📄 许可证
MIT License - 详见 LICENSE 文件
```
5. 勾选 "Set as the latest release"，点击 "Publish release"
---
## ✅ 验证发布
发布完成后，其他人可以通过以下方式安装使用：
```bash
# OpenClaw 安装
openclaw skill install https://github.com/[your-github-username]/ai-fia/releases/download/v1.0.0/ai-fia.skill
# 或直接克隆使用
git clone https://github.com/[your-github-username]/ai-fia.git
```
---
## 📊 可选：生成安装包
如果需要生成 `.skill` 安装包用于 OpenClaw 分发：
```bash
openclaw skill package . --output ./dist
# 生成的 ai-fia.skill 文件可以直接上传到 GitHub Release 附件
```
