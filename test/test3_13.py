def seq(**dict1):
    return ("{name}隶属于{dept},电话:{tel},入职时间:{hiredate}".format_map(dict1))

dict1 = dict(name='技术部',hiredate='2017-9-23',tel='123456',dept='技术部')
print(seq(**dict1))