'''
객체 : 프로그램의 기본 구상 단위로, 데이터(속성)와 동작(메서드)을 포함합니다,
클래스 : 객체를 정의하는 틀로, 객체의 속성(데이터)과 동작(메서드)을 미리 설계합니다.
인스터스 : 클래스를 기반으로 생성된 실제 객체입니다.
프로그램을 실행하기 위해서는 객체가 필요하고 이러한 객체의 생성을 돕는 것이 클래스
'''
from multiprocessing.pool import worker


class GrandMother: # 클래스는 변수와 함수를 가지고 있다
    family = 'grandparents' # 속성 : 클래스 내부 변수와 변수값

    def print_self(self): # 메소드 : 클래스 내무 함수
        print(self)

lee = GrandMother() # 인스턴스

# 클래스 정의: 붕어빵 틀 만들기
class Bungeoppang:
    def __init__(self, filling):  # 생성자 (생성될 때 자동 실행)
        self.filling = filling    # 속재료 저장

    def describe(self):
        print(f"이 붕어빵은 {self.filling}이 들어 있어요.")

# 객체 생성 (붕어빵 만들기)
b1 = Bungeoppang("팥")
b2 = Bungeoppang("슈크림")

# 메서드 실행 (붕어빵 설명)
b1.describe()  # 출력: 이 붕어빵은 팥이 들어 있어요.
b2.describe()  # 출력: 이 붕어빵은 슈크림이 들어 있어요.

import datetime
print(datetime.datetime.now())

class Personalinfo: #class keyword로 클래스 정의 시작

    #Inutalizer, Instance aiiributes
    def __init__(self, name, age): #객체를 초기화하는 __init__() magic method
        self.name = name
        self.age = age

    #Instance method
    def getPersonalinfo(self): #메소드 정의
        return f'Name: {self.name}\nAge: {self.age}'

    #Istance method
    def ageGroup(self): #메소드 정의
        if self.age >= 30:
            return 'over 30'
        else:
            return 'under 30'

#create an instance object
personal_choi = Personalinfo('CK Choi', 25)#클래스이름() 생성자로 인스턴스 객체 생성
personal_Park = Personalinfo('Park', 41)
print(personal_choi.getPersonalinfo(), personal_choi.ageGroup())
print(personal_Park.getPersonalinfo(), personal_Park.ageGroup())

class Cat:
    def meow(self): # Cat 클래스의 메소드 추가
        print('meow')

    def walk(self):
        print('사뿐사뿐')

    def jelly(self):
        print('말랑쓰')

miyo = Cat()
mino = Cat()
miru = Cat()
miyo.meow() # Cat 클래스의 메소드 호출
mino.walk()
miru.jelly()

animals = ['lion', 'tiger', 'cat', 'dog']
print(type(animals))
print(id(animals))
t = 'tiger'
print(type(t))
print(id(t))

print(dir(int))
print(dir(list))
print(type(dir))

'''
객체 지향 프로그래밍 OOP : Object Oriented Programming
'''

class Cat:
    #생성자 또는 초기화 메소드
    def __init__(self, name, color): #self는 인스턴스 변수를 클래스 내부에 접근 시키기 위해 꼭 써야함
        self.name = name #name이라는 인스턴스 변수 생성
        self.color = color #color라는 인스턴스 변수 생성
    
    def meow(self): #고양이의 정보를 출력하는 메소드
        print(f'내 이름은 {self.name}, 색깔은 {self.color}, 야옹애옹')

miyo = Cat('미요', '회색')
mino = Cat('미노', '노란색')
miru = Cat('미루','카오스')

miyo.meow()
mino.meow()
miru.meow()

#__str__사용
class Cat:
    # 생성자 또는 초기화 메소드
    def __init__(self, name, color):  # self는 인스턴스 변수를 클래스 내부에 접근 시키기 위해 꼭 써야함
        self.name = name  # name이라는 인스턴스 변수 생성
        self.color = color  # color라는 인스턴스 변수 생성

    def __str__(self): #Cat 객체의 문자열 표현방식 __str__() 메소드
        return f'Cat(name = {self.name}, color = {self.color})'

    def meow(self): # 고양이의 정보를 출력하는 메소드
        print(f'내 이름은 {self.name}, 색깔은 {self.color}, 야옹애옹')

miyo = Cat('미요', '회색')
mino = Cat('미노', '노란색')
miru = Cat('미루', '카오스')

print(miyo) # miyo 인스턴스의 __srt__()메소드가 호출됨
print(mino) # mino 인스턴스의 __srt__()메소드가 호출됨
print(miru) # miru 인스턴스의 __srt__()메소드가 호출됨

print('===================캡슐화=======================')

'''
캡슐화 : 클래스 속성을 외부에서 접근할 때 오류를 줄이가 위해 상용한다.
'''
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): return f'Cat(name = {self.name}, age = {self.age})'

miyo = Cat('미요', 3)
print(miyo)
miyo.age = -5
print(miyo)

print('--------------------------')

class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self): #Cat의 문자열 표현방식
        return f'Cat(name = {self.__name}, age = {self.__age})'

    def set_age(self, age): #self.__age를 외부에서 자유롭게 접근하는 것을 제한하고 음수가 되지 않게 함
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

miyo = Cat('미요', 3)
print(miyo)
miyo.set_age(4)
miyo.set_age(-5)
print(miyo)

'''
객체의 아이덴티티(Identity operator) 연산
'''
list_a = [10, 20, 30]
list_b = [10, 20, 30]
if list_a is list_b: print('list_a is list_b') # 두 리스트 객체가 같은지 확인
else: print('list_a is not list_b')

'''
클래스의 상속
'''
print('--------------상속-------------')

class A: #부모 클래스
    PI = 3.14 #속성을 정함 : 클래스 변수

class B(A): #클래스 A를 부모로 가지는 자식 클래스 B
    pass

a = A() #A 클래스의 인스턴스 a 생성
b = B() #B 클래스의 인스턴스 b 생성
print(a.PI)
print(b.PI) #b는 부모 클래스의 속성과 메소드에 접근가능

class Person:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Manager(Person): #Person의 자식 클래스
    def __init__(self, name, position):
        Person.__init__(self, name) # 부모 클래스의 생성자 호출
        self.position = position #자식 클래스의 생성자 초기화
    def info(self):
        return f'관리직 : {self.name}, 직책 : {self.position}'

class Employee(Person): #Person의 자식 클래스
    def __init__(self, name, salary = 100):
        Person.__init__(self, name) # 부모 클래스의 생성자 호출
        self.salary = salary #자식 클래스의 생성자 초기화
    def get_salary(self):
        return f'종업원 : {self.get_name()}, 급여 : {self.salary}'

cto = Manager('박동민', '최고기술책임자(CTO)')
worker1 = Employee('박동윤', 320)
worker2 = Employee('홍승주', 250)

print(cto.info())
print(worker1.get_salary())
print(worker2.get_salary())