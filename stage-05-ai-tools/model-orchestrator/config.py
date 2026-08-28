# ============================================
# 模型配置注册表
# ⭐ 关键知识：DeepSeek / Kimi / 通义 / 豆包 全都兼容 OpenAI 的 API 格式
#   所以它们都能用同一个 openai 库来调用，只需要改 base_url 和 model 名
# ============================================

MODELS = {
    # 主模型：负责拆任务、派活、汇总（你已有 key）
    "deepseek": {
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-chat",          # DeepSeek-V3 对话模型
        "env_key": "DEEPSEEK_API_KEY",     # 在 .env 里读取这个 key
        "role": "主模型（拆任务/派活/汇总）",
    },
    # 工人模型：Kimi（月之暗面）
    "kimi": {
        "base_url": "https://api.moonshot.cn/v1",
        "model": "moonshot-v1-8k",
        "env_key": "KIMI_API_KEY",
        "role": "工人模型",
    },
    # 工人模型：通义千问（阿里云）
    "qwen": {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-plus",
        "env_key": "QWEN_API_KEY",
        "role": "工人模型",
    },
    # 工人模型：豆包（字节跳动 / 火山方舟）
    "doubao": {
        "base_url": "https://ark.cn-beijing.volces.com/api/v3",
        "model": "doubao-1-5-pro-32k-250115",   # 注意：豆包的 model 通常填你的"推理接入点 ID"
        "env_key": "DOUBAO_API_KEY",
        "role": "工人模型",
    },
}

# 工人模型名单：编排时按顺序轮流派活
WORKERS = ["kimi", "qwen", "doubao"]
