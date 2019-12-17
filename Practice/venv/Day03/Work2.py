# 请输入一个整数n，并按照顺序输出从1到n


def func():
    num = input("请输入一个整数：")
    count = 1
    while count <= int(num):
        print(count)
        count += 1


if __name__ == "__main__":
    func()