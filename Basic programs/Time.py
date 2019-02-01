import datetime
#perform operation on time

#current time
print(datetime.datetime.now())

#assign time
a=datetime.datetime(2019,2,1,12,38)
b=datetime.datetime(2019,1,1,11,32)

#diffrence between time (time delta)
c=a-b
print(c)
#c.total_seconds() for total seconds and c.days for days

#formating date
print(a.strftime('%Y-%m-%d_%H-%M-%S-%f'))

#adding time into time
after=a+datetime.timedelta(days=2)
print(after)


import time
#making delays on code, counting time of process

lst=[]
for i in range(5):
        lst.append(datetime.datetime.now())
        time.sleep(2)

for i in lst:
        print(i)
