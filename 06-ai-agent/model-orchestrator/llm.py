# ============================================
# 通用模型调用函数
# 传入"模型名 + 提示词"，返回模型的回答文字
# 这是整个项目的地基：主模型和工人模型都走这一个函数
# ============================================

import os

from dotenv import load_dotenv
from openai import OpenAI

from config import MODELS

# 加载 .env 文件里的 API Key（第一次写 .env 后要重启终端）
load_dotenv()


def call_llm(model_key: str, prompt: str) -> str:
    """调用任意一个模型，返回它的回答。

    参数:
        model_key: 模型的名字，如 "deepseek" / "kimi" / "qwen" / "doubao"
        prompt:    你想问它的提示词
    返回:
        模型的回答文字
    """
    # 1. 从注册表拿出这个模型的配置
    cfg = MODELS[model_key]

    # 2. 从环境变量里拿 API Key（存在 .env 文件里）
    api_key = os.environ.get(cfg["env_key"])
    if not api_key:
        raise ValueError(f"找不到 {cfg['env_key']}，请检查 .env 文件是否配置")

    # 3. 创建客户端（⭐ 重点：只改 base_url 就能换一家模型）
    client = OpenAI(base_url=cfg["base_url"], api_key=api_key)

    # 4. 发请求，拿到回答
    resp = client.chat.completions.create(
        model=cfg["model"],
        messages=[{"role": "user", "content": prompt}],
    )

    return resp.choices[0].message.content


if __name__ == "__main__":
    # 自测：跑一下看看能不能通
    # 用法：python llm.py deepseek "你好"
    import sys

    model = sys.argv[1] if len(sys.argv) > 1 else "deepseek"
    prompt = sys.argv[2] if len(sys.argv) > 2 else "用一句话介绍你自己"
    print(f"调用模型: {model}")
    print(call_llm(model, prompt))
