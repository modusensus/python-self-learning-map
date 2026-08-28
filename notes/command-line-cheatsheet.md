# 命令行常用命令速查

> 搬运自 Obsidian 知识库 · 整理自与 DeepSeek 的对话（2026-08-26）
> "千百种命令"是错觉：内置命令就几十个，日常用到的不过 10 个

## 先厘清概念

- **CMD** 是 Windows 自带命令行解释器，脚本语言叫 Batch（批处理），语法古老，很少写复杂逻辑
- **PowerShell（pwsh）** 是更现代的命令行环境，脚本语言类似 C#，能调 .NET 类库
- 二者都是"命令行环境"，不是"编程语言"
- 你感觉命令多，是因为 Git、Node.js、Python 等工具往 PATH 里塞了可执行程序——那些是"你装的工具"，不是"必须会的命令"
- 在 WSL 里用 bash 的话，Windows 原生命令行完全可以绕过

## 🧭 文件与目录操作（先背熟）

| 用途     | CMD / pwsh              | bash / WSL                    |
| ------ | ----------------------- | ----------------------------- |
| 查看目录内容 | `dir`                   | `ls`（`ls -la` 看隐藏文件+详情）       |
| 进入文件夹  | `cd 文件夹名`               | 相同                            |
| 返回上级目录 | `cd ..`                 | 相同                            |
| 返回主目录  | `cd %USERPROFILE%`      | `cd ~`                        |
| 显示当前路径 | `pwd`                   | `pwd`                         |
| 创建文件夹  | `mkdir 文件夹名`            | `mkdir 文件夹名`（`-p a/b/c` 递归）   |
| 创建空文件  | `type nul > 文件名`        | `touch 文件名`                   |
| 复制文件   | `copy 源 目标`             | `cp 源 目标`（`-r` 递归复制文件夹）       |
| 复制文件夹  | `xcopy 源 目标 /E`         | `cp -r 源 目标`                  |
| 移动/重命名 | `move 源 目标`             | `mv 源 目标`                     |
| 删除文件   | `del 文件名`               | `rm 文件名`                      |
| 删除文件夹  | `rmdir /s 文件夹名`         | `rm -rf 文件夹名`（⚠️ 不可恢复）        |
| 查看文件内容 | `type 文件名`              | `cat 文件名`                     |
| 分页查看   | `more 文件名`              | `less 文件名`（q 退出）              |
| 查看末尾几行 | `more +10 文件名`（简陋）      | `tail -n 10 文件名`（`-f` 实时跟踪日志） |
| 搜索文件内容 | `findstr "关键词" 文件名`     | `grep "关键词" 文件名`（`-r` 递归）     |
| 统计行数   | `find /c /v "" 文件名`（简陋） | `wc -l 文件名`                   |

## 🌐 进程与服务

| 用途 | CMD / pwsh | bash / WSL |
|------|-----------|-----------|
| 查看进程 | `tasklist` | `ps aux`（`ps aux \| grep 关键词` 筛选） |
| 按名称结束进程 | `taskkill /IM 进程名 /F` | `pkill 进程名` |
| 按 PID 结束进程 | `taskkill /PID 1234 /F` | `kill -9 1234` |
| 查看端口占用 | `netstat -ano` | `netstat -tlnp` / `lsof -i :8080` |

## 📦 系统与环境信息

| 用途 | CMD / pwsh | bash / WSL |
|------|-----------|-----------|
| 环境变量 | `set` / `echo %PATH%` | `env` / `echo $PATH` |
| 当前用户 | `whoami` | `whoami` |
| 主机名 | `hostname` | `hostname` |
| 系统信息 | `systeminfo` | `uname -a` |
| 磁盘空间 | `wmic logicaldisk get size,freespace,caption` | `df -h` |

## 🧹 清理与常用操作

| 用途 | 命令 |
|------|------|
| 清屏 | `cls`（CMD/pwsh）/ `clear` 或 Ctrl+L（bash） |
| 命令历史 | `doskey /history` / `history` |
| 重复上一条 | `↑` 或 `!!` |
| 管道 | `命令A \| 命令B`（如 `ls \| grep ".txt"`） |
| 重定向 | `命令 > 文件`（覆盖）、`>> 文件`（追加） |
| 连续执行 | `命令A && 命令B`（前一个成功才执行下一个） |

## 🔥 网络相关

| 用途 | 命令 |
|------|------|
| 测连通性 | `ping 域名或IP` |
| 路由跟踪 | `tracert`（Windows）/ `traceroute`（Linux） |
| 本机网络配置 | `ipconfig` / `ifconfig` 或 `ip a` |
| DNS 解析 | `nslookup 域名` |
| 命令行下载 | `curl -O URL`（pwsh）/ `wget URL` 或 `curl -O URL`（WSL） |

## 🔧 已装工具的常用命令（这些必须记）

| 工具 | 常用命令 |
|------|---------|
| **Git** | `git status`、`git add .`、`git commit -m "..."`、`git push`、`git pull`、`git log --oneline` |
| **Node/npm** | `npm install`、`npm run 脚本名`、`npm publish`、`npx 命令` |
| **Python/pip** | `python 文件名.py`、`pip install 包名`、`pip list`、`python -m venv 环境名` |
| **WSL** | `wsl`（进入）、`wsl --list`（查看发行版）、`wsl --shutdown`（关停） |

## 🧠 三个救命指令

| 场景 | 命令 |
|------|------|
| 内置命令列表 | `help` |
| 某命令的用法 | `命令 /?`（CMD）/ `命令 --help` 或 `man 命令`（bash） |
| 模糊搜历史 | `Ctrl+R` + 关键词 |

## 💡 使用建议

- **别背，先用**：每次查表，查 10 次以上自然记住
- **重点 8 个**：`ls`/`cd`/`mkdir`/`rm`/`cp`/`mv`/`cat`/`grep`，占日常操作 80%
