import random


def random_num(times):
    for i in range(0, times):
        for num in range(0, 6):
            print(random.randint(1, 33), end=' ')
        print(random.randint(1, 16))


print("1-双色球随机选号")
print("2-号码百事通")
print("3-明日天气预报")
print("0-结束程序")
i = input("请输入功能编号：")
if i =='1':
    n = int(input('您要生成几注双色球'))
    random_num(n)