import random


def generate_unionlotto(times):
    for i in range(0, times):
        for num in range(0, 6):
            print(random.randint(1, 33), end=' ')
        print(random.randint(1, 16))


def haomabaishitong(tel):
    print('test')


def tianqiyubao():
    print('test')


if __name__ == '__main__':
    while True:
        print("1-双色球随机选号")
        print("2-号码百事通")
        print("3-明日天气预报")
        print("0-结束程序")
        i = input("请输入功能编号：")
        if i == '1':
            n = int(input('您要生成几注双色球'))
            generate_unionlotto(n)
            continue
        elif i == '2':
            tel = input('请输入您要查询的电话号码')
            haomabaishitong(tel)
            continue
        elif i == '3':
            tianqiyubao()
        elif i == '0':
            print("谢谢使用，祝您生活愉快")
            break