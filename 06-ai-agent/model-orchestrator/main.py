# ============================================
# 入口程序：跑通整个"老板派活"流程
# 用法：python main.py
# ============================================

from orchestrator import aggregate, execute_subtasks, split_task


def main():
    print("=" * 45)
    print("多模型协作：DeepSeek 当老板，其他模型当工人")
    print("=" * 45)

    task = input("请输入你想完成的任务：\n> ")

    print("\n[1/3] DeepSeek 正在拆分任务...")
    subtasks = split_task(task)
    print(f"      拆成了 {len(subtasks)} 个小任务：")
    for i, s in enumerate(subtasks, 1):
        print(f"      {i}. {s}")

    print("\n[2/3] 工人模型开始干活...")
    results = execute_subtasks(subtasks)

    print("\n[3/3] DeepSeek 正在汇总结果...")
    final = aggregate(task, results)

    print("\n" + "=" * 45)
    print("【最终答案】")
    print(final)
    print("=" * 45)


if __name__ == "__main__":
    main()
