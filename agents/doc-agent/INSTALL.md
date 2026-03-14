# CalendarAgent 安装指南

支持两种安装方式：OpenClaw直接安装 和 Docker安装。

---

## 方式一：OpenClaw 直接安装（推荐）

### 前置要求

- 已安装 OpenClaw
- 有飞书应用配置（可选）

### 安装步骤

1. **克隆或下载项目**
```bash
git clone https://github.com/your-username/CalendarAgent.git
cd CalendarAgent
```

2. **复制到OpenClaw工作目录**
```bash
# 方式A：作为独立Agent使用
cp -r CalendarAgent ~/.openclaw/agents/CalendarAgent

# 方式B：在当前workspace中使用
cp -r CalendarAgent ~/.openclaw/workspace/CalendarAgent
```

3. **配置OpenClaw**
```bash
# 编辑 openclaw.json，添加CalendarAgent配置
openclaw config edit
```

4. **重启OpenClaw**
```bash
openclaw restart
```

5. **验证安装**
```bash
openclaw status
```

---

## 方式二：Docker 安装

### 前置要求

- 已安装 Docker
- 已安装 Docker Compose

### 安装步骤

1. **克隆或下载项目**
```bash
git clone https://github.com/your-username/CalendarAgent.git
cd CalendarAgent
```

2. **构建Docker镜像**
```bash
docker-compose build
```

3. **启动容器**
```bash
docker-compose up -d
```

4. **查看日志**
```bash
docker-compose logs -f
```

5. **验证安装**
```bash
docker-compose exec calendaragent openclaw status
```

### 常用Docker命令

```bash
# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 更新镜像并重启
docker-compose pull
docker-compose up -d

# 进入容器
docker-compose exec calendaragent sh
```

---

## 配置说明

### 环境变量

| 变量名 | 说明 | 默认值 |
|-------|------|-------|
| `OPENCLAW_WORKSPACE` | OpenClaw工作目录 | `/app/workspace` |
| `NODE_ENV` | 运行环境 | `production` |

### 数据持久化

Docker安装时，数据会保存在：
- `calendaragent-data` volume：持久化数据
- `./workspace`：工作目录挂载

---

## 卸载

### OpenClaw安装卸载
```bash
# 删除Agent目录
rm -rf ~/.openclaw/agents/CalendarAgent

# 重启OpenClaw
openclaw restart
```

### Docker安装卸载
```bash
# 停止并删除容器
docker-compose down -v

# 删除镜像
docker rmi calendaragent-calendaragent
```

---

## 故障排除

### OpenClaw安装问题
- 检查 `openclaw.json` 配置是否正确
- 查看日志：`openclaw logs`
- 确认权限：`chmod -R 755 ~/.openclaw/agents/CalendarAgent`

### Docker安装问题
- 检查Docker是否运行：`docker info`
- 查看容器日志：`docker-compose logs`
- 检查端口占用：`lsof -i :9999`

---

**技术支持**：如有问题，请提交Issue或联系维护者。
