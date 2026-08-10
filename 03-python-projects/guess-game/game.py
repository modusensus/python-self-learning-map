"""用Python设计第一个游戏"""
import random

counts = 4
answer = random.randint (1,10)

while counts > 0:
    temp = input("不妨猜一桉桉现在心里想的是哪个数字：") 
    guess = int(temp)

    if guess == answer:
        print ("你是桉桉心里的蛔虫吗？！")
        print ("哼，猜中了也没奖励！")
        break
    else:
        if guess < answer:
            print ("小啦，再猜猜看呢？╰(￣ω￣ｏ)")
        else:
            print ("大啦，再猜猜看呢？╭(￣▽￣)")
        counts -= 1

print ("游戏结束，不玩啦o(*￣▽￣*)ブ")        

