#阶层计算器

num = int(input("请输入数值(1-100):"))
if 1 <= num <= 100:
    total = 1
    i = 1
    while i <= num:
        total = total * i
        if i % 5 == 0:
            print("当前阶乘数为{},能被5整除，阶乘结果为{}".format(i, total))
        i = i + 1
    print(total)
else:
    print("输入内容无效，请重新输入")
