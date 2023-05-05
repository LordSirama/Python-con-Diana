from datetime  import datetime


franjas=[
  'true vampires',
  'early birds',
  'sunny warmers',
  'lunch workers',
  'sunset lovers',
  'prime timers'
]

def valor(dato):
  
  if datetime.strptime('00:00:00',"%H:%M:%S")<=dato<=datetime.strptime('03:59:59',"%H:%M:%S"):
    return 'true vampires'
  elif dato<=datetime.strptime('07:59:59',"%H:%M:%S"):
    return 'early birds'
  elif dato<=datetime.strptime('11:59:59',"%H:%M:%S"):
    return 'sunny warmers'
  elif dato<=datetime.strptime('15:59:59',"%H:%M:%S"):
    return 'lunch workers'
  elif dato<=datetime.strptime('19:59:59',"%H:%M:%S"):
    return 'sunset lovers'
  else:
    return 'prime timers'


b=int(input())
lis=[]
for i in range(b):
  d=datetime.strptime(input().split()[-1], "%H:%M:%S")
  lis.append(valor(d))

for i in franjas:
  print(i, lis.count(i))
  

# 7
# 2000-01-01 14:30:00
# 2000-01-02 03:59:59
# 2000-01-03 18:18:18
# 2000-01-04 20:20:20
# 2000-01-05 09:09:09
# 2000-01-06 22:22:22
# 2000-01-07 12:00:00

# true vampires 1
# early birds 0
# sunny warmers 1
# lunch workers 2
# sunset lovers 1
# prime timers 2