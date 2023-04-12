# DemoListTuple.py
device={'아이폰':5, '아이패드':10, '윈도우':20}
print(device)
device['갤럭시']=15
print(device['아이폰'])
del device['윈도우']
for item in device.items():
    print(item)

for k,v in device.items():
   print(k,v)

phone = {'kim':"1111", 'lee':'2222', 'park':'3333'}
p=phone
print(phone)
print(p)
print(id(phone), id(p))


