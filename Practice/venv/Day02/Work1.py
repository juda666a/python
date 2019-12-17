#  还记得我们第一讲的动动手的题目吗？这一次要求使用变量，计算一年有多少秒？


def func():
    dayPerYear = 365
    hoursPerDay = 24
    minutesPerHour = 60
    secondsPerMinute = 60
    totalSecondCount = dayPerYear * hoursPerDay * minutesPerHour * secondsPerMinute
    print("一年共有：" + str(totalSecondCount) + "秒！")


if __name__ == "__main__":
    func()