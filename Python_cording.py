'''
람다함수 : 1회용의 간단한 함수를 만드는 것
람다 표현식이라고 하며 이름이 없는 함수
익명 함수
'''
def add (x, y): # 이 함수와
    return x + y

lambda x, y : x + y # 이 함수는 같다

add = lambda x, y: x + y
print(add(1, 2))

print((lambda x, y: x + y)(1, 2))

'''
필터함수 : filter(적용시킬 함수, {반복 가능 객체})
'''
ages = [24, 16, 20, 54, 33]

def adult_func(n): #19 이상의 값이 들어오면 True
    if n >= 19: return True
    else: return False

print('성년 리스트 :')
for i in filter(adult_func, ages): # filter() 함수를 사용하여 i를 구함
    print(i, end=' ')
print('')
print('성년 리스트 :')
for i in filter(lambda x: x >= 19, ages): print(i, end=' ')
print('')
adult_age = list(filter(lambda x: x >= 19, ages))
print('성년 리스트 :', adult_age)

'''
맵 함수 : map(적용시킬 함수, 반복 가능 객체, ...)
'''
def square(x):
    return x ** 2

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_a = list(map(square, a))
print(square_a)

print(list(map(lambda x: x ** 2, a)))