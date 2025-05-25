print('Hello Python!')

days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_set = set(days_list) #리스트를 집합으로 만들기
print(days_set)
fruits_tuple = ('apple', 'banana', 'orange', 'watermelon')
fruits_set = set(fruits_tuple) #튜플을 집합으로 만들기
print(fruits_set)
h_str = 'hello'
h_str = set(h_str) # 문자열을 집합으로 만들기
print(h_str) # 문자열 'l'의 중복을 허용하지 않음

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)} #
    return res

A = {1, 3}
B = {2, 4}
AxB = product_set(A, B)
print('A =', A)
print('B =', B)
print('A x B =', AxB)