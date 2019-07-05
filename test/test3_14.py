i = 1
sum = 0
while i <= 100:
    if (i % 3 == 0 or i % 7 == 0) and not(i % 3 == 0 and i % 7 == 0):
        print("满足条件的数字为："+str(i))
        sum = sum+1
    i = i+1
print("满足条件的个数为："+str(sum))
