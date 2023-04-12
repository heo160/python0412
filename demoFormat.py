# demoFormat.py

url = 'http://credu.com/?page='+ str(1)
print(url)

for x in range(1,6):
    print(x,"*",x,"=", x*x)

for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(5))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15500000))
print("{0:e}".format(4/3))