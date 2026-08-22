# ============================================
# 编排器：老板（DeepSeek）拆任务 → 工人模型干活 → 汇总
# 这是整个"模型编排"的核心逻辑
# ============================================

import json

from config import WORKERS
from llm import call_llm


def split_task(task: str) -> list[str]:
    """第一步：让主模型 DeepSeek 把大任务拆成几个小任务。

    技巧：我们要求 DeepSeek 返回 JSON 格式，程序才能方便地解析出任务列表。
    """
    prompt = f"""你是一个项目经理。请把下面这个任务拆分成最多 {len(WORKERS)} 个独立的小任务。
只输出 JSON，不要输出任何其他文字。格式如下：
{{"subtasks": ["小任务1", "小任务2", ...]}}

要拆分的任务：{task}"""

    text = call_llm("deepseek", prompt)

    # 清理：有的模型会把 JSON 包在 ```json ... ``` 里，需要去掉
    text = text.strip().removeprefix("```json").removesuffix("```").strip()

    data = json.loads(text)          # 把 JSON 文本转成 Python 字典
    return data["subtasks"]          # 取出小任务列表


def execute_subtasks(subtasks: list[str]) -> list[str]:
    """第二步：把每个小任务轮流派给工人模型，收集它们的回答。

    轮流派活的算法：i % len(WORKERS)
    - 第 1 个小任务 → 第 1 个工人
    - 第 2 个小任务 → 第 2 个工人
    - 第 3 个小任务 → 第 3 个工人
    - 第 4 个小任务 → 又回到第 1 个工人（取模）
    """
    results = []
    for i, subtask in enumerate(subtasks):
        worker = WORKERS[i % len(WORKERS)]
        print(f"  → 派给 [{worker}] 执行：{subtask}")
        answer = call_llm(worker, subtask)
        results.append(f"[{worker} 的回答]\n{answer}")
    return results


def aggregate(task: str, results: list[str]) -> str:
    """第三步：让主模型 DeepSeek 把各工人的成果汇总成最终答案。"""
    joined = "\n\n".join(results)
    prompt = f"""你是一个项目经理。下面是原任务和各员工的完成情况，请把它们汇总成一份完整、通顺的最终答案。

【原任务】{task}

【各员工成果】
{joined}"""
    return call_llm("deepseek", prompt)
