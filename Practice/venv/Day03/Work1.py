# 完善第二个改进要求，并改进视频中小甲鱼的代码

import random


def func():
    times = 3
    secret = random.randint(1, 10)
    print("----------我爱鱼C工作室----------")
    # 这里先给guess赋值(赋一个绝对不等于secret的值)
    guess = 0
    print("不妨猜想一下小甲鱼现在心里想的是哪个数字：", end="")
    while (guess != secret) and (times > 0):
        temp = input()
        times = times - 1 # 用户每输入一次，可用机会就减1
        if guess == secret:
            print("卧槽，你是小甲鱼心里的蛔虫吗？！")
            print("猜中了也没有奖励")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了")
            if times > 0:
                print("再试一次吧：", end="")
            else:
                print("机会用光咯T_T")
    print("游戏结束，不玩啦~~~")


if __name__ == "__main__":
    func()