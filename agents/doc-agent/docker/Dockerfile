# CalendarAgent Docker Image
# 日程管理专家智能助手

FROM node:20-alpine

# 设置工作目录
WORKDIR /app

# 安装OpenClaw
RUN npm install -g openclaw

# 复制项目文件
COPY . .

# 创建必要的目录
RUN mkdir -p /app/workspace/memory
RUN mkdir -p /app/workspace/sessions

# 设置环境变量
ENV OPENCLAW_WORKSPACE=/app/workspace
ENV NODE_ENV=production

# 暴露端口（如果需要）
EXPOSE 9999

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD openclaw status || exit 1

# 启动命令
CMD ["openclaw", "start"]
