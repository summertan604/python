x=int(input("请输入需要打印的行数:"))
y = 0  #需要打印的空格数
z = 0  #需要打印的*号数
i = 1
while i <= x:
    z = 2*i-1
    y = x-i
    while y > 0:
        print(" ", end="")
        y -= 1
    while z > 0:
        print("*", end="")
        z -= 1
    print("\n")
    i += 1