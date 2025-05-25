'''from tkinter import *

window = Tk()
window.geometry('400x200')
label = Label(window, text='헬로 파이썬')
label.pack()

window.mainloop()'''
from setuptools.config.expand import resolve_class

'''
from tkinter import *
window = Tk()

input_entry = Entry(window, width=50)
input_entry.pack()

button = Button(window, text='처리')
button.pack()
label = Label(window, text=' ')
label.pack()

window.mainloop()'''

'''계산기 만들기
from tkinter import *

window = Tk()
window.title('계산기')
window.geometry('400x200')

label = Label(window, text ='숫자 1').grid(column=0, row=0)
label = Label(window, text ='숫자 2').grid(column=0, row=1)
res_label = Label(window, text = '결과 :')
res_label.grid(column=0, row=2)

num1 = Entry(window, width=10)
num2 = Entry(window, width=10)
num1.grid(column=1, row=0)
num2.grid(column=1, row=1)

def add():
    answer = float(num1.get()) + float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text=res_text)

def subtrack():
    answer = float(num1.get()) - float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text=res_text)

def multiplication():
    answer = float(num1.get()) * float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text=res_text)

def division():
    answer = float(num1.get()) / float(num2.get())
    res_text = f'결과 = {answer}'
    res_label.configure(text=res_text)

btn_plus = Button(window, text='+', command=add)
btn_minus = Button(window, text='-' , command=subtrack)
btn_mult = Button(window, text='*' , command=multiplication)
btn_div = Button(window, text='/' , command=division)

btn_plus.grid(column=2, row=1)
btn_minus.grid(column=3, row=1) 
btn_mult.grid(column=4, row=1)
btn_div.grid(column=5, row=1)

window.mainloop() '''

