'''
구문오류 : 문법오류, 파싱오류 - print() 함수에서 따옴표를 빼먹는 등의 오류
예외 : 문법적으로는 문제가 없으나 실행 도중 만나게 되는 오류
'''
while True:
    try:
        a, b = 5, 1#input('두 수를 입력하세요 : ').split() # split은 입력 받은 값이 공백에 따라 분리된 원소로 받게 함
        result = int(a) / int(b)
        print(f'{a}/{b} = {result}')
        break
    except:
        print('수가 정확한지 확인하세요')

try:
    b = 2/0
    a = 1 + 'hundred'
except Exception as e: # 오류의 종류를 출력
    print('error :', e)

try:
    a = 1 + 'hundred' #먼저 발생하는 오류에 대해서
    b = 2/0

except ZeroDivisionError as e: print('0으로 나뉘는 오류')
except TypeError as e: print('지원되지 않는 연산자를 사용하는 오류') #출력값이 나옴

'''
try - except - else
예외가 발생하지 않은 경우 else문을 사용하여 결과값 출력
'''
try:
    a, b = input('두 수를 입력하세요 : ').split()
    result = int(a) / int(b)
except ZeroDivisionError: print('오류 : 0으로 나눔을 시도했습니다.')
except ValueError: print('오류 : 입력 값이 정수나 실수가 아닙니다.')
except SyntaxError: print('오류 : 10 2 와 같이 두 정수를 입력하세요.')
else: print(f'{a}/{b} = {result}')

'''
try - except - finally
예외 발생 여부와 상관없이 항상 출력됨
'''
def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError: print('0으로 나누는 오류 발생')
    else: print('결과 : ', result)
    finally: print('수행완료')

print('divide(100, 2) 함수호출 :')
divide(100, 2)
print('divide(100, 0) 함수호출 :')
divide(100, 0)