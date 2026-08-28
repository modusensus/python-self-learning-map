# 技术术语速查表（小白版）

> 搬运自 Obsidian 知识库 · 整理自与 DeepSeek 的对话（2026年5月起持续更新）
> 按分类整理，每个术语都注明了"为什么你需要知道"

---

## 🌐 网络基础

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **HTTP** | 浏览器和服务器之间的"通信语言"，不加密 | 你调 API 时看到的 `http://` 开头 |
| **HTTPS** | 加密版 HTTP，别人偷听不到内容 | GitHub 推送、DeepSeek API 都用它 |
| **URL** | 网址，告诉你东西在互联网上的哪个位置 | `https://github.com/你的仓库` 就是 URL |
| **API** | 两个软件之间的"传话人" | 你调 DeepSeek API 让 AI 干活，就是它在传话 |
| **代理（Proxy）** | 帮你转发网络请求的"中间人" | Git 报错 `port 443` 时，就是代理没配好 |

## 🔐 安全与认证

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **SSH** | 加密的远程操作通道，不用反复输密码 | 配了 SSH 后 `git push` 不用输密码 |
| **SSH 密钥** | 一把"数字钥匙"，分公钥和私钥 | 公钥贴 GitHub，私钥自己留 |
| **Token** | 一次性/定期更换的"临时密码" | DeepSeek API Key、GitHub PAT |

## 📦 版本管理 & 编程基础

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **Git** | 你电脑上的"时光机"，记录每次改动 | `git add`、`git commit`、`git push` |
| **GitHub** | 存放 Git 仓库的"云盘" | 你的作品集展示厅 |
| **Markdown** | 用 `#`、`*`、`[]()` 表示格式的文本语法 | 本笔记就是 Markdown |
| **JSON** | 用 `{}` 和 `[]` 存数据的格式 | n8n 导出的工作流就是 JSON |
| **命令行/终端** | 黑窗口，用键盘输入指令指挥电脑 | Git Bash、CMD、PowerShell |

## 🛠️ 常用工具

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **n8n** | 可视化自动化工具，把各种 App 串起来干活 | 新闻推送、考研日报都是它搭的 |
| **Docker** | 把软件装进"隔离盒子"里运行 | Dify、n8n 都用 Docker 装 |
| **Dify** | AI 应用开发平台，能做知识库问答 | 你的考研助手就是 Dify 搭的 |
| **Agent** | 能自主使用工具的 AI | Dify 里的 Agent 可以搜知识库、联网查资料 |
| **RAG** | 让 AI 从你给的资料里找答案 | Dify 知识库的核心技术 |

## 🐍 Python 办公自动化（2026 新增）

| 术语 | 人话解释 | 安装 |
|------|---------|------|
| **Pandas** | Excel 数据处理之王，3 行代码合并 100 个表 | `pip install pandas openpyxl` |
| **OpenPyXL** | Excel 格式美化——字体/颜色/边框/冻结窗格 | （同上） |
| **Python-Docx** | Word 批量生成——占位符替换、证书/合同模板填充 | `pip install python-docx` |
| **Smtplib** | Python 内置邮件库，工资条/日报群发 | 内置库，无需安装 |
| **Schedule** | 定时任务调度器，每日自动跑脚本 | `pip install schedule` |
| **PyInstaller** | 把 Python 脚本打包成 exe，分发给不会代码的同事 | `pip install pyinstaller` |

## 🌐 网站开发（2026-08 新增）

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **Node.js** | JavaScript 的"本地运行环境"，相当于 Python 解释器 | 跑 Astro、npm、n8n 都靠它，你电脑里已经装了 |
| **npm** | Node.js 的"应用商店"，安装和管理 JS 库 | `npm install`、`npm run dev` 都是它 |
| **npx** | npm 自带工具，临时运行某个包、不留痕迹 | `npx astro add` 就是它，用完就走 |
| **NestJS** | Node.js 上的大型后端框架（TypeScript 首选） | 对应 Python 的 Django/FastAPI |
| **FastAPI** | Python 的后端框架，简单 + 自动生成 API 文档 | 以后把 GIS/数据处理能力做成 API 用它 |
| **Astro** | 前端框架，专做博客等内容型网站（岛屿架构、静态生成） | 你的博客就是它搭的 |
| **Conda** | Python 的包管理 + 环境管理 | ≈ npm + nvm 的结合体 |

## 🐙 Git 与开源（2026-08 新增）

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **Commit** | 一次"存盘点"，把暂存区生成历史快照 | `git commit -m "..."` 是你每天按的保存键 |
| **分支（Branch）** | 代码的"平行宇宙"，试验新功能不碰主线 | `git switch` 切换、`git merge` 合并 |
| **PR（Pull Request）** | GitHub 上"请求把我的改动合并进去"的机制 | 开源协作核心：先 push，再 `gh pr create` |
| **gh** | GitHub 官方命令行工具，在终端操作 GitHub 事务 | PR、Issue、建仓库都不用开浏览器 |
| **CI/CD** | 提交代码自动体检（CI）/ 自动上线（CD） | GitHub Actions，Push 之后机器替你跑测试 |
| **Release / Tag** | Tag 给版本"贴里程碑"，Release 是打包下载页 | npm 插件的标准发布流程 |
| **License** | 开源协议，规定别人怎么用你的代码 | 建仓库时选 MIT 最省心 |
| **代码覆盖率** | 测试"跑过了多少行代码"的比例 | Codecov 徽章，93% 就是"随便改"的底气 |

## 🤖 AI 与大模型（2026-08 新增）

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **LangChain** | LLM 应用的"乐高脚手架"，把模型+数据+工具编排起来 | 实现 RAG 和 Agent 的主流框架 |
| **LangGraph** | LangChain 的底层编排引擎，用图/状态机建复杂 Agent | 循环、多 Agent 协作靠它 |
| **LlamaIndex** | 专注"数据+检索"的框架，RAG 天然脚手架 | 与 LangChain 常混用：它管检索，LangChain 管编排 |
| **向量数据库** | 存"文本向量"的库，支持语义相似度搜索 | RAG 检索的地基（Milvus、Chroma 等） |
| **Embedding** | 把文本转成高维向量，语义相近向量距离近 | RAG 建索引的第一步 |
| **Agentic RAG** | Agent 自己决定何时检索、检索几次 | RAG 的进化方向 |
| **幻觉（Hallucination）** | 模型一本正经编造不存在的内容 | RAG 靠"先查资料再回答"来压制它 |

## ☁️ 服务器与 Linux（2026-08 新增）

| 术语 | 人话解释 | 为什么你需要知道 |
|------|---------|----------------|
| **栈（Stack）** | 内存里的"叠盘子"，存局部变量，后进先出、快而小 | 递归太深会"栈溢出" |
| **堆（Heap）** | 内存里的"仓库货架"，存对象实体，慢而大 | Python/JS 的对象都在这 |
| **内网穿透** | 把本地电脑的服务暴露到公网（隧道技术） | cpolar/frp/ngrok，你 Minecraft 联机用过 |
| **公网 IP** | 给外人访问的"门牌号" | 云服务器自带，家宽一般没有 |
| **弹性公网 IP** | 可解绑换绑、关机不变的公网 IP | 想要固定 IP 就转弹性 |
| **安全组** | 云厂商的防火墙，"入方向"放行才能访问 | 服务在跑但外网不通，九成是它没放行 |
| **root** | Linux 的"神"，权限最高的账户 | 提示符 `#` = root，`$` = 普通用户 |
| **sudo** | 临时用 root 权限执行一条命令 | 平时普通用户，需要时 sudo |
| **apt** | Ubuntu 的软件管家（命令行应用商店） | `apt install` 装一切，自动解决依赖 |
| **systemctl** | 系统服务管家：启动/停止/重启/自启 | `systemctl status nginx` 查服务状态 |
| **Nginx** | Web 服务器/反向代理，处理 HTTP 请求 | 托管网站、转发 FastAPI 都要它 |
| **虚拟化** | 把物理服务器切成多台虚拟机 | 你的 2核4GiB 就是"切"出来的 |

## 🔄 易混概念

| 易混组合 | 一句话区别 |
|---------|-----------|
| HTTP vs HTTPS | S = 安全（加密） |
| Git vs GitHub | Git 是工具（本地），GitHub 是网站（云端） |
| URL vs API | URL 是"地址"，API 是"用这个地址能干的事" |
| 镜像 vs 容器 | 镜像 = 安装包（静态），容器 = 运行的程序（动态） |
| RAG vs Agent | RAG 让 AI 从资料里找，Agent 让 AI 主动干活 |
| Pandas vs OpenPyXL | Pandas 处理数据，OpenPyXL 美化格式——搭配使用 |
| Node.js vs npm | Node.js 是运行环境（操作系统），npm 是包管理器（应用商店） |
| npm vs npx | npm 永久安装，npx 临时执行（网页 vs 无痕网页） |
| git vs gh | git 管代码本身，gh 管 GitHub 事务（PR/Issue/仓库） |
| git pull vs git fetch | pull = fetch（只下载）+ merge（合并） |
| git reset vs git revert | reset 改历史（高危），revert 新增反向提交（安全） |
| CI vs CD | CI 检查"代码对不对"，CD 解决"怎么上线" |
| TCP vs UDP | TCP 打电话（可靠有序），UDP 发广播（快但可能丢） |
| LangChain vs LlamaIndex | LangChain 管编排，LlamaIndex 管检索，常混用 |
| LangChain vs LangGraph | LangChain 组件库，LangGraph 底层图编排引擎 |
| RAG vs 微调 | RAG 外挂知识库（实时、可溯源），微调改模型权重（贵、黑盒） |
| 栈 vs 堆 | 栈 = 叠盘子（快、小、自动），堆 = 仓库货架（慢、大、手动/GC） |
| 虚拟机 vs 容器 | 虚拟机 = 砌墙隔房间（重），容器 = 拉帘子（轻） |
| cpolar vs frp | cpolar = 租精装房（开箱即用），frp = 自己建房（自主可控） |
| frp vs Nginx | frp 打通网络（隧道），Nginx 响应请求（Web 服务） |
| root vs sudo | root 是账户，sudo 是"临时借用 root 权限"的命令 |
| su vs sudo | su 完全切换用户（要对方密码），sudo 单条命令临时提权（要自己密码） |
| 公网 IP vs 内网 IP | 门牌号（对外）vs 房间号（对内通信） |
| 安全组 vs ufw | 云厂商防火墙（控制台配）vs 系统内防火墙（命令配） |
| apt vs apt-get | apt 是改良版，输出友好有进度条；apt-get 更老更底层 |
| 动态代码 vs 前端动效 | 后端逻辑（服务器跑）vs 前端交互（浏览器跑） |
