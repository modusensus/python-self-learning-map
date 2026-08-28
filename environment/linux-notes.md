# 👑 Linux 用户与 root 权限

> 搬运自 Obsidian 知识库 · 整理自与 DeepSeek 的对话（2026-08-28）
> "我就是我云服务器的卡密" 😎

## root 是什么

**Linux 世界的"神"**——权限最高的超级管理员账户。类比：Windows 的 Administrator、Android 的"已 Root"、家里能开所有房间门的房东。

能做什么：读写任何文件、装删任何软件、改系统配置、管理所有用户、重启系统、**绕过所有权限检查**（系统先看"是不是 root"，是就直接放行）。

## 为什么平时不用 root？

- **开坦克买菜**：手滑敲错（如 `rm -rf /`）系统直接没，且没有任何确认提示
- **最佳实践**：平时用普通用户，需要系统级操作时 `sudo` 临时授权
- 好处：密码泄露破坏有限 + 操作有审计记录 + 行业标准（生产环境默认禁止 root 远程登录）

## 怎么判断我现在是谁？

| 方法 | 命令/标志 | 说明 |
|------|----------|------|
| 看提示符 | `#` vs `$` | `#` = root（"神之徽章"），`$` = 普通用户 |
| 直接问 | `whoami` | 打印当前用户名 |
| 看详情 | `id` | `uid=0(root)` 就是 root，root 的 uid 永远是 0 |

## 怎么切换身份？

| 命令 | 用途 | 要谁的密码 | 切到哪里 |
|------|------|-----------|---------|
| `su - 用户名` | 完全切换成另一个用户 | 目标用户密码 | 目标用户家目录 + 完整环境 |
| `sudo 命令` | 临时用 root 权限执行一条命令 | 当前用户密码 | 不切换环境 |
| `sudo -i` | 临时进入 root 环境 | 当前用户密码 | root 环境，`exit` 退回 |

> `su` 一定要带 `-`：不带的话只换身份不换环境变量和目录，容易出"命令找不到"的坑。

## 新建用户（root 的"造人"技能）

```bash
adduser deploy            # 创建用户，按提示设密码（信息可回车跳过）
usermod -aG sudo deploy   # 加入 sudo 组（CentOS 是 wheel 组）
# 验证：exit 后用 ssh deploy@公网IP 登录，跑 sudo apt update
```

用途：日常开发、专门建 `deploy` 用户跑服务（应用有漏洞也拿不到 root）、多人协作各用各的。

## pwd 显示 `/` 是为什么？

`/` 是文件系统的**根目录**（树根，所有目录从它长出），不是 root 的家目录。root 的家目录是 `/root`，普通用户在 `/home/deploy`。

## 相关笔记

- [docker-notes.md](docker-notes.md) — 在云服务器装 Docker Engine 时就会用到 root / sudo
- [../notes/command-line-cheatsheet.md](../notes/command-line-cheatsheet.md) — 常用命令行速查
