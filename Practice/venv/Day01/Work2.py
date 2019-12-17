# 编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”


def func():
    num = input("请输入1到100之间的数字：")
    if 0 <= int(num) <= 100:
        print("你妹好漂亮")
    else:
        print("你大爷好丑")


if __name__ == "__main__":
    func()