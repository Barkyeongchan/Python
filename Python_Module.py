#모듈 = 파이썬 함수나 변수, 클래스 들을 모아놓은 스크립트 파일 / import 모듈 이름
import datetime
print(datetime.datetime.now()) # 모듈이름.클래스이름.메소드이름
today = datetime.date.today()

print(today)

print(dir(datetime)) #모듈이 가진 클래스 목록 출력

import datetime as dt #as를 사용하여 모듈의 별칭을 정함
start_time = dt.datetime.now()
print(start_time.replace(month = 12, day = 25)) #replace 메소드를 통해 month와 day의 값을 변화 / 지속X
print(start_time)

from datetime import datetime # from을 사용하여 특정 클래스를 선택해 import함
start_time = datetime.now()
print(start_time.replace(month = 12, day = 25))

#크리스마스까지 남은 시간 구하기
import datetime as dt

today = dt.date.today()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}일 입니다')

xMas = dt.datetime(2025, 12, 25)
gap = xMas - dt.datetime.now()

print(f'크리스마스까지는 {gap.days}일 {gap.seconds // 3600}시간 남았습니다')

import time # time모듈과 .sleep메소드를 활용한 지연 노출방법
print('바로 출력되는 구문.')
time.sleep(1)
print('1초 뒤에 출력되는 구문.')

import time
start_time = time.time()
print(1+2+3+4+5+6+7+8+9+10)
end_time = time.time()
gap = end_time - start_time
print('1에서 10까지의 합을 구하고 출력하는 시간:{:7.4f}초'.format(gap))

#math모듈을 import
import math
print(dir(math))

#난수모듈 random
import random as rd
print(rd.random())
print(rd.randrange(5))
print(rd.randint(1, 5))

a = range(0, 101, 5)
print('0에서 100사이의 임의의 정수 3개', rd.sample(a, 3))
print(rd.randrange(0,101,5))

#조건문을 사용한 위와 동일인 코드
ok = [i for i in range(0, 101, 5)]
random_3 = rd.sample(a, 3)
print(random_3)

def pseudo_rand(x):
    a = 1103515245
    b = 12345
    m = 2 ** 31
    new_x = (a * x + b) % m
    return new_x

seed = int(input()) # 초기값을 임의로 설정
x = pseudo_rand(seed) # seed를 입력으로 하여 새로운 x를 만듬
print(x)
x = pseudo_rand(x) # x를 입력하여 새로운 x를 만듬
print(x)

#seed를 현재시간으로 하는 코드
import datetime as dt
def pseudo_rand(x):
    a = 1103515245
    b = 12345
    m = 2 ** 31
    new_x = (a * x + b) % m
    return new_x

seed = dt.datetime.now(). timestamp() # 초기값을 현재시간으로 사용 / timestamp를 사용해 부동소수점으로 받음
x = pseudo_rand(int(seed)) # seed를 정수값으로 받기위해 int를 사용
print(x)
x = pseudo_rand(x) # x를 입력하여 새로운 x를 만듬
print(x)

#로또번호 추첨기
import random as rd
lotto_list = list(range(1, 46))
rd.shuffle(lotto_list)
lotto_list = lotto_list[:6]
lotto_list.sort()
print('이번 주의 추천 로또 번호 :', lotto_list)

import sys
sys.prefix