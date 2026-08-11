import random  # 1. 导入 random 工具箱

# 2. 先随机一个数（练习 print 输出）
print(random.randint(1, 10))

# 3. 保存当前随机状态到 x
x = random.getstate()   # 📸 "随机到哪一步了"拍照存进 x
print(x)                # 打印状态（一堆内部数据，看不懂很正常）

# 4. 在保存状态之后，再随机一个数
print(random.randint(1, 10))   # ← 记下这个数字 B

# 5. 恢复之前保存的状态（时光倒流 ⏪）
random.setstate(x)

# 6. 恢复后再随机一个数
print(random.randint(1, 10))   # ← 应该和 B 一模一样！