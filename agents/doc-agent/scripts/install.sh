#!/bin/bash

# CalendarAgent 安装脚本
# 用于在OpenClaw中安装CalendarAgent

set -e

echo "========================================="
echo "  CalendarAgent 安装脚本"
echo "========================================="
echo ""

# 检测OpenClaw安装
if ! command -v openclaw &> /dev/null; then
    echo "❌ 错误: 未检测到OpenClaw，请先安装OpenClaw"
    exit 1
fi

echo "✅ OpenClaw 已检测到"
echo ""

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "📂 项目目录: $PROJECT_DIR"
echo ""

# 询问安装方式
echo "请选择安装方式："
echo "1) OpenClaw Agent 安装（推荐）"
echo "2) OpenClaw Workspace 安装"
read -p "请输入选项 (1/2): " choice

case $choice in
    1)
        INSTALL_DIR="$HOME/.openclaw/agents/CalendarAgent"
        echo ""
        echo "📦 安装到: $INSTALL_DIR"
        ;;
    2)
        INSTALL_DIR="$HOME/.openclaw/workspace/CalendarAgent"
        echo ""
        echo "📦 安装到: $INSTALL_DIR"
        ;;
    *)
        echo "❌ 无效选项"
        exit 1
        ;;
esac

# 备份旧目录（如果存在）
if [ -d "$INSTALL_DIR" ]; then
    echo ""
    read -p "⚠️  目标目录已存在，是否备份？(y/n): " backup_choice
    if [ "$backup_choice" = "y" ]; then
        BACKUP_DIR="${INSTALL_DIR}.backup.$(date +%Y%m%d%H%M%S)"
        mv "$INSTALL_DIR" "$BACKUP_DIR"
        echo "✅ 已备份到: $BACKUP_DIR"
    else
        echo "❌ 安装取消"
        exit 1
    fi
fi

# 复制文件
echo ""
echo "📋 复制文件..."
cp -r "$PROJECT_DIR" "$INSTALL_DIR"

echo ""
echo "✅ 文件复制完成"
echo ""

# 询问是否重启OpenClaw
read -p "🔄 是否重启OpenClaw？(y/n): " restart_choice
if [ "$restart_choice" = "y" ]; then
    echo ""
    echo "🔄 重启OpenClaw..."
    openclaw restart
    echo "✅ OpenClaw 已重启"
fi

echo ""
echo "========================================="
echo "  ✅ CalendarAgent 安装完成！"
echo "========================================="
echo ""
echo "安装目录: $INSTALL_DIR"
echo ""
echo "下一步："
echo "1) 编辑 openclaw.json 配置CalendarAgent"
echo "2) 运行 'openclaw status' 验证安装"
echo ""
