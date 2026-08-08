"""用Python设计第一个游戏"""

counts = 4

while counts > 0:
    temp = input("不妨猜一桉桉现在心里想的是哪个数字：") 
    guess = int(temp)

    if guess == 9:
        print("你是桉桉心里的蛔虫吗？！")
        print("哼，猜中了也没奖励！")
        counts -= 4
    else:
        if guess < 9:
            print("小啦，再猜猜看呢？╰(￣ω￣ｏ)")
        else:
            print("大啦，再猜猜看呢？╭(￣▽￣)")
        counts -= 1

print ("游戏结束，不玩啦o(*￣▽￣*)ブ")        

