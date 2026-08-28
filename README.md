# 🗺️ Tech Stack Map

> 个人技术栈搭建地图 —— 从 Python 数据分析，到前端、后端、GIS、AI Agent，一条一条学。

> 📌 **学习入口请看 [TECH-STACK-MAP.md](TECH-STACK-MAP.md)**（含每个技术的进度、笔记入口、实战项目清单）。

## Learning Goals

- Python programming
- Data analysis
- API integration
- AI Agent development
- Urban data applications

## 技术栈规划（Roadmap）

> 📌 **完整版请看 [TECH-STACK-MAP.md](TECH-STACK-MAP.md)** —— 含每个技术的学习进度、笔记入口、实战项目清单。
> 下面只是简版总览。GitHub 主页挂的是目标技术栈，不是当前水平，按顺序一条一条学，不贪多。

```
阶段一（现在）：Python + SQLite + 数据分析
    ├── Python 基础语法 ✅（已在进行）
    ├── 数据结构（列表/字典/元组/集合）
    ├── 文件读写 + CSV + 异常处理
    ├── SQLite（轻量数据库）
    └── 数据分析：NumPy + Pandas + Matplotlib
    → 毕业论文用得上，先搞定它

阶段二：前端三件套 + 设计
    ├── HTML5
    ├── CSS3
    ├── JavaScript
    └── Figma（设计稿）
    → 有博客基础，上手快

阶段三：后端
    ├── FastAPI（Python 后端）或 Node.js / NestJS
    └── 把前端后端串起来做网站

阶段四：GIS
    └── QGIS（配合城乡规划专业，做地理可视化）

阶段五：自动化 / AI 工具
    ├── n8n（自动化工作流）
    └── Dify（AI 应用）
    → 已经在用，持续深入即可
```

**难度梯度（从易到难）：**

```
HTML/CSS  <  Python  <  JavaScript  <  数据分析(NumPy/Pandas)  <  后端(FastAPI/Node/NestJS)
```

**心态提醒：** 技术栈挂主页是"远期蓝图"，不代表要一个月全学会。当下只专注阶段一（Python 数据分析），其他线等逐条推进。

## Progress

[x] Python basics（变量 / 字符串 / 条件 / 循环 / 函数 / 数字运算）

[-] 数据结构（列表 / 字典 / 元组 / 集合）

[ ] 数据分析（NumPy / Pandas / Matplotlib）

[ ] SQLite

[ ] 前端（HTML / CSS / JS）

[ ] 后端（FastAPI / Node.js / NestJS）

[ ] GIS（QGIS）

[ ] AI Agent / 自动化（n8n / Dify）

## Projects

| Project            | Description                 |
| ------------------ | --------------------------- |
| Daily Report Agent | AI information workflow     |
| Paper Assistant    | Academic research assistant |

## Structure

```
tech-stack-map/
├── TECH-STACK-MAP.md        # ⭐ 核心总地图（学习进度/笔记入口/项目清单）
├── environment/             # 环境配置（conda / docker / vscode / python安装）
├── notes/                   # 学习笔记（按主题分类）
│   ├── python/              #   Python 主题笔记
│   ├── learning-log.md      #   学习日志
│   └── errors.md            #   踩坑记录
├── stage-01-python-data/    # 阶段一：Python + SQLite + 数据分析（进行中）
│   ├── basics/              #   基础语法
│   ├── data-structures/     #   数据结构
│   ├── projects/            #   实战项目
│   ├── data-analysis/       #   数据分析
│   └── api-automation/      #   API 与自动化
├── stage-02-frontend/       # 阶段二：前端三件套 + 设计
├── stage-03-backend/        # 阶段三：后端
├── stage-04-gis/            # 阶段四：GIS（配合城乡规划专业）
├── stage-05-ai-tools/       # 阶段五：AI Agent + 自动化工具
├── requirements.txt         # 依赖清单
└── README.md                # 本文件（简版门面）
```
