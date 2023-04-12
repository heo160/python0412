# # ifelse.py

# score = int(input('점수 입력:'))

# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score < 90:
#     grade = 'B'
# elif 70 <= score < 80:
#     grade = 'C'
# else:
#     gfade = 'D'

#print("등급: ", grade)


print('-----------수열')
print(list(range(10)))
print(list(range(1,32)))

lst = list(range(1,11))
print([i**2 for i in lst if i>5])
tp = ('apple', 'orange', 'kiwi')
print([v.upper() for v in tp])

print(-------------------'필터링')

def getBiggerThan20(i):
    return i>20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)