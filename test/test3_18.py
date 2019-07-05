lst = [23, 45, 22, 44, 25, 66, 78]
lst1 = [lst[i] for i in range(0, len(lst)) if lst[i] % 2 != 0]
print(lst1)
lst1 = [lst[i]+5 for i in range(0, len(lst))]
print(lst1)