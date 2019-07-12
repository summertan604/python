from datetime import datetime,timedelta
import time
import os

data_time = datetime(2019, 10, 18, 8, 10)
time.sleep(2)
date_ = datetime(2019, 11, 11)
time_ = datetime.strptime("11:11","%H:%M")
print(data_time)
print(data_time.year)
print(data_time.time())

str_ = '2019-09-10'
str_date = datetime.strptime(str_,"%Y-%m-%d")
print(str_date)
print(datetime.now())
now_ = datetime.now()
now_befor = now_-timedelta(days=3, hours=36, minutes=12)
print(now_befor)
now_after = now_+timedelta(days=10)
print(now_after)

now_1=datetime.now()
now_2=datetime.today()
print(datetime.strftime(now_1,"%Y-%m-%d"))
print(now_1)
print(now_2)
print((str(now_1.year)+'{0}'+str(now_1.month)+'{0}'+str(now_1.day)).format('-'))