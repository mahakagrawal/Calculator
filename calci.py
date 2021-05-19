from tkinter import *
import math
exp=""
def press(num):
    global exp
    exp=exp+str(num)
    eq.set(exp)
def equalpress():
    try:
        global exp
        t=str(eval(exp))
        eq.set(t)
        exp=""
    except:
        eq.set('error')
        exp=""    
def clear():
    global exp
    exp=""
    eq.set("")
def sin():
    global exp
    exp=math.sin(float(eq.get()))
    eq.set(exp)
def cos():
    global exp
    exp=math.cos(float(eq.get()))
    eq.set(exp)
def tan():
    global exp
    exp=math.tan(float(eq.get()))
    eq.set(exp)
def delete():
    global exp
    txt=eq.get()[:-1]
    eq.delete(0,END)
    eq.insert(0,txt)
    eq.set(exp)          
    
gui=Tk()
gui.configure(background='light green')
gui.title('Simple Calculator')
gui.geometry('545x410')
eq = StringVar()
exp_field=Entry(gui,textvariable=eq)
exp_field.grid(columnspan=5,ipadx=210,ipady=20)
eq.set("enter your expression")
b1=Button(gui,text='1',fg='white',bg='orange',command=lambda:press(1),height=4,width=14,relief='sunken',state='active',cursor='clock')
b2=Button(gui,text='2',fg='white',bg='orange',command=lambda:press(2),height=4,width=14,relief='sunken',state='active',cursor='dotbox')
b3=Button(gui,text='3',fg='white',bg='orange',command=lambda:press(3),height=4,width=14,relief='sunken',state='active',cursor='cross')
b4=Button(gui,text='4',fg='black',bg='white',command=lambda:press(4),height=4,width=14,relief='sunken',state='active',cursor='circle')
b5=Button(gui,text='5',fg='blue',bg='white',command=lambda:press(5),height=4,width=14,relief='sunken',state='active',cursor='exchange')
b6=Button(gui,text='6',fg='blue',bg='white',command=lambda:press(6),height=4,width=14,relief='sunken',state='active',cursor='fleur')
b7=Button(gui,text='7',fg='black',bg='white',command=lambda:press(7),height=4,width=14,relief='sunken',state='active',cursor='heart')
b8=Button(gui,text='8',fg='blue',bg='white',command=lambda:press(8),height=4,width=14,relief='sunken',state='active',cursor='man')
b9=Button(gui,text='9',fg='blue',bg='white',command=lambda:press(9),height=4,width=14,relief='sunken',state='active',cursor='mouse')
b0=Button(gui,text='0',fg='black',bg='white',command=lambda:press(0),height=4,width=14,relief='sunken',state='active',cursor='pirate')
plus=Button(gui,text='+',fg='white',bg='orange',command=lambda:press('+'),height=4,width=14,relief='sunken',state='active',cursor='shuttle')
minus=Button(gui,text='-',fg='blue',bg='white',command=lambda:press('-'),height=4,width=14,relief='sunken',state='active',cursor='sizing')
multiply=Button(gui,text='*',fg='blue',bg='white',command=lambda:press('*'),height=4,width=14,relief='sunken',state='active',cursor='spraycan')
divide=Button(gui,text='/',fg='blue',bg='white',command=lambda:press('/'),height=4,width=14,relief='sunken',state='active',cursor='target')
equal=Button(gui,text='=',fg='blue',bg='white',command=equalpress,height=4,width=14,relief='sunken',state='active',cursor='tcross')
mod=Button(gui,text='%',fg='white',bg='green',command=lambda:press('%'),height=4,width=14,relief='sunken',state='active',cursor='tcross')
power=Button(gui,text='^',fg='white',bg='green',command=lambda:press('**'),height=4,width=14,relief='sunken',state='active',cursor='tcross')
dot=Button(gui,text='.',fg='white',bg='green',command=lambda:press('.'),height=4,width=14,relief='sunken',state='active',cursor='tcross')
d=Button(gui,text='D',fg='white',bg='green',command=delete,height=4,width=14,relief='sunken',state='active',cursor='tcross')
clear=Button(gui,text='Clear',fg='blue',bg='white',command=clear,height=4,width=14,relief='sunken',state='active',cursor='star')
cos=Button(gui,text='Cos',fg='black',bg='white',command=cos,height=4,width=14,relief='sunken',state='active',cursor='star')
tan=Button(gui,text='Tan',fg='white',bg='green',command=tan,height=4,width=14,relief='sunken',state='active',cursor='star')
sin=Button(gui,text='Sin',fg='black',bg='white',command=sin,height=4,width=14,relief='sunken',state='active',cursor='star')
braces=Button(gui,text=')',fg='black',bg='white',command=lambda:press(')'),height=4,width=14,relief='sunken',state='active',cursor='star')
brace=Button(gui,text='(',fg='white',bg='orange',command=lambda:press('('),height=4,width=14,relief='sunken',state='active',cursor='star')
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
b0.grid(row=5,column=0)
plus.grid(row=2,column=3)
minus.grid(row=3,column=3)
multiply.grid(row=4,column=3)
divide.grid(row=5,column=3)
equal.grid(row=5,column=2)
clear.grid(row=5,column=1)
brace.grid(row=2,column=4)
braces.grid(row=3,column=4)
cos.grid(row=4,column=4)
sin.grid(row=5,column=4)
tan.grid(row=6,column=4)
mod.grid(row=6,column=1)
power.grid(row=6,column=2)
dot.grid(row=6,column=3)
d.grid(row=6,column=0)
