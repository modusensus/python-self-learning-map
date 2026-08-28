# Python 安装指南

## 下载安装

- 官网下载：[python.org](https://www.python.org/downloads/)
- 推荐版本：Python 3.10+
- 安装时勾选 **"Add Python to PATH"**

## 验证安装

```bash
python --version
pip --version
```

## 虚拟环境

```bash
# 创建虚拟环境
python -m venv .venv

# 激活（Windows）
.venv\Scripts\activate

# 激活（macOS/Linux）
source .venv/bin/activate
```