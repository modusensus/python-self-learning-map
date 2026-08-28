# 多模型编排器（Model Orchestrator）

> DeepSeek 当老板（主模型）拆任务、派活、汇总；其他国产模型当工人执行子任务。

## 架构

```
你输入一个大任务
      ↓
DeepSeek（主模型）拆分成小任务  →  输出 JSON
      ↓
小任务1 → 工人模型 Kimi
小任务2 → 工人模型 通义千问     （轮流派活）
小任务3 → 工人模型 豆包
      ↓
DeepSeek（主模型）汇总成最终答案
```

## 项目结构

```
model-orchestrator/
├── .env.example       # API Key 模板（复制为 .env 后填 key）
├── config.py          # 模型注册表：每家模型的地址和名字
├── llm.py             # 通用调用函数：call_llm(模型名, 提示词)
├── orchestrator.py    # 编排器：拆任务 / 派活 / 汇总
├── main.py            # 入口：跑通整个流程
└── README.md          # 本文件
```

## 使用步骤

1. **安装依赖**

   ```bash
   pip install openai python-dotenv
   ```

2. **配置 API Key**

   ```bash
   cp .env.example .env
   ```

   然后编辑 `.env`，填入你自己的 key（.env 不会被提交到 GitHub）。

3. **先自测单个模型**（推荐，确认 key 没问题）

   ```bash
   python llm.py deepseek "你好"
   python llm.py kimi "你好"
   ```

4. **跑通整个编排**

   ```bash
   python main.py
   ```

## 关键知识点

- **OpenAI 兼容**：DeepSeek / Kimi / 通义 / 豆包 都用 OpenAI 格式，一套代码通吃
- **base_url 决定调谁**：同一个 `openai` 库，换 `base_url` 就换了模型
- **JSON 交互**：让模型输出 JSON，程序才能解析，这是 Agent 开发的常用套路
- **环境变量**：API Key 放 `.env`，用 `os.environ.get()` 读取，不写死在代码里
