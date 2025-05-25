'''
import turtle
turtle로 별 만들기
t = turtle.Turtle()
t.shape('turtle')
t.lt(35)
for _ in range(5):
    t.forward(100)
    t.lt(145)

turtle.done()
'''
'''
import turtle
t = turtle.Turtle()
n = 100
lenght = 5
for i in range(n):
    t.lt(360/n)
    t.forward(lenght)

turtle.done()
'''
'''
import turtle
t = turtle.Turtle()
t.circle(100)
'''
'''
겹침원 4개 만들기
import turtle
t = turtle.Turtle()
t.speed(100)
for j in range(4):
    t.setheading(j*90)
    for i in range(1, 11):
        t.circle(10*i)
turtle.done()
'''
'''
선에 색을 넣어서 도형 그리기
import turtle
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor('black')
colors = ['red', 'green', 'blue', 'orange']
for i in range(200):
    t.pencolor(colors[i%4]) #colors인데스가 1:4까지 나오게 표현
    t.forward(i)
    t.lt(93)
turtle.done()
'''
'''
turtle과 random모듈을 활용한 랜덤 순간이동 거북이 (랜덤플로팅)
import turtle
import random as rd

t = turtle.Turtle()
t.shape('circle')
t.speed(100)
d = 300
for _ in range(40):
    x = rd.randint(-d, d)
    y = rd.randint(-d, d)
    t.goto(x, y)

turtle.done()
'''