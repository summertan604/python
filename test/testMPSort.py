#冒泡排序
list = [5,98,2,65,21,36,23,9,78]

i = 0
while i < len(list):
    j = i+1
    temp = list[i]
    while j < len(list):
        if temp > list[j]:
            list[i] = list[j]
            list[j] = temp
            temp = list[i]
        j += 1
    i += 1
print(list)