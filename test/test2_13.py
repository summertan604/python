list=[]
for i in range(1,5):
    for j in range(1,5):
        if i==j:
            continue
        combine=str(i)+str(j)
        if combine not in list:
            list.append(combine)
print(list)
print(len(list))

phone = ''
if phone.strip():
    print('test'+phone.strip())