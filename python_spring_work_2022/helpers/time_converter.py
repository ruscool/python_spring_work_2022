# import bcrypt
#
# # password = userInput
# hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
# # save "hashAndSalt" in data base
#
# # To check:
# # password = userInput
# valid = bcrypt.checkpw(password.encode(), hashAndSalt)


# password = 'userInput'
# hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
# # save "hashAndSalt" in data base
# print(hashAndSalt,type(hashAndSalt))
# sd=hashAndSalt.decode('utf-8')
#
# print(sd,type(sd))
#
# h_new=sd.encode()
# # To check:
# print(h_new,type(h_new))
# # password =
# valid = bcrypt.checkpw(password.encode(), sd.encode())
# print(valid)

import datetime
import time

# s=datetime.datetime.now()
# print(s)
# ss=datetime.date.today()
# print(ss)
# print(time.gmtime(0))

print(time.ctime())  # 'Wed Apr 5 00:02:49 2017'

print('localtime', time.localtime())

a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
print(a)  # '2017-04-05-00.11.20'

a = time.ctime(time.time())
print('time.time', a)  # Wed Apr 5 00:13:47 2017
print('timestamp', datetime.datetime.fromtimestamp(0))
print('time.ctime', time.ctime())  # 'Wed Apr 5 00:02:49 2017'
a = datetime.datetime.fromtimestamp(0)
b = 6.933253049850464
# print(str(a-b))
print('ctime', time.ctime(6.933253049850464))  # 'Sun Nov 10 13:43:59 2013'
print('gmtime rr ', time.gmtime(6.933253049850464))
print('timedelta', datetime.timedelta(6.933253049850464))
print('time now', datetime.datetime.now())
now_time = datetime.datetime.now()
stime = datetime.datetime.now().timestamp()  # перевод в timestamp !!!
print('timestamp -', stime)
new_s = stime + 60
print('new_s=',datetime.datetime.fromtimestamp(new_s))
new_t = now_time.strftime('%d/%m/%Y %I:%M:%S')
print('format datetime', new_t)

vv = time.strftime("%M:%S", time.localtime())
print(vv)
time_1 = datetime.datetime.strptime(vv, "%M:%S")
time.sleep(2)
vv = time.strftime("%M:%S", time.localtime())
print(vv)

time_2 = datetime.datetime.strptime(vv, "%M:%S")
c = time_2 - time_1
print(c)
# bb=time.strptime(self.for_result[-1], "%M:%S")
t1 = datetime.date.today().isoformat()
print(t1)

t2 = datetime.datetime.now().strftime('%H:%M:%S')
print(t2)
# nn=time.strftime("%M:%S", time.localtime(6.933253049850464))
# print(nn)
print('localtime', time.localtime().tm_min)
