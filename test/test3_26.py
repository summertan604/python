i = 1
j = 1
tag = 0
result = "一千以内的质数为："
sum = 0
while i <= 1000:
    while j <= i:
        if i % j == 0 and j != 1 and j != i:
            tag = 1
            j += 1
            break
        j += 1
    if tag == 0 and i != 1:
        result += (str(i)+",")
        sum += 1
    i += 1
    j = 1
    tag = 0
print("1000以内的质数共有{}个".format(sum))
print(result)
