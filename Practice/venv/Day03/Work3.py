# 输入一个整数，并将其对应的星星数打印

def func():
    num = int(input("请输入一个整数："))
    while num:
        i = num - 1
        while i:
            print(' ', end = '')
            i = i - 1
        j = num
        while j:
            print('*', end = '')
            j = j - 1
        print()
        num = num - 1


if __name__ == "__main__":
    func()