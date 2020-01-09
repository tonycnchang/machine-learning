import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk

def w_section(b,h):
    if section_sharps.get() == "圆钢":
        Iz = np.pi*b**4/64
        w = 2*Iz/b
    elif section_sharps.get() == "矩形钢":
        Iz = b*h**3/12
        w = 2*Iz/h
    else:
        Iz = np.pi*(b**4-h**4)/64
        w = 2*Iz/b
    return w,Iz

def get_sharp(*args):
    print(section_sharps.get())
    if section_sharps.get() == "圆钢":
        section_dimension_label["text"] = "直径D"
    elif section_sharps.get() == "矩形钢":
        section_dimension_label["text"] = "宽b高h"
    else:
        section_dimension_label["text"] = "外径D内径d"
def get_parameters(*args):
    dimesion_list = list(map(eval,str.split(dimension_enter.get(),",")))
    if len(dimesion_list) == 1:
        dimesion_list.append(0)
    l_list = list(map(eval,str.split(length_enter.get(),",")))
    l_list = np.linspace(0,l_list[0],50)
    force = list(map(eval,str.split(force_enter.get(),",")))[0]
    E = list(map(eval,str.split(E_enter.get(),",")))[0]
    R = list(map(eval,str.split(R_enter.get(),",")))[0]
    w = w_section(dimesion_list[0],dimesion_list[1])
    y = np.zeros(50)
    y_r = []
    for i in range(len(l_list)):
        de = l_list[-1] - l_list[i]
        lengh = l_list[i] - l_list[0]
        m = force * de
        sigma = m/w[0]
        print(sigma)
        distance = -1*force*lengh**3/(3*E*w[1])
        print(distance)
        y_r.append(distance)
    plt.plot(l_list,y,"-b",lw=5)
    plt.scatter(l_list,y_r,c=y_r,cmap=plt.cm.Reds)
    plt.annotate(s="%dN"%force,xy=(l_list[-1],0),xytext=(l_list[-1],0.1),arrowprops={"shrink":0.05})
    plt.colorbar()         
    plt.show()

root = tk.Tk()
root.title("悬臂梁挠度")
root.geometry("300x400")

section_sharp_label = tk.Label(root,text="截面类型")
section_sharp_label.pack()

force_value = tk.StringVar(root,value="100")
force_label = tk.Label(root,text="载荷N")
force_enter = tk.Entry(root,textvariable=force_value)

section_dimension_value = tk.StringVar(root,value="50")
section_dimension_label = tk.Label(root,text="尺寸")
dimension_enter = tk.Entry(root,textvariable=section_dimension_value)

length_value = tk.StringVar(root,value="1000")
length_label = tk.Label(root,text="长度")
length_enter = tk.Entry(root,textvariable=length_value)

E_value = tk.StringVar(root,value="210000")
E_label = tk.Label(root,text="弹性模量")
E_enter = tk.Entry(root,textvariable=E_value)

R_value = tk.StringVar(root,value="0.3")
R_label = tk.Label(root,text="泊松比")
R_enter = tk.Entry(root,textvariable=R_value)

section_sharps_list = ["圆钢","矩形钢","圆管"]
name = tk.StringVar()
section_sharps = ttk.Combobox(root,textvariable=name)
section_sharps["values"] = section_sharps_list
section_sharps["state"] = "readonly"
section_sharps.current(0)
section_sharps.bind("<<ComboboxSelected>>",get_sharp)

calculate = Button(root,text="计算",command=get_parameters)

section_sharps.pack()
length_label.pack()
length_enter.pack()
section_dimension_label.pack()
dimension_enter.pack()
E_label.pack()
E_enter.pack()
R_label.pack()
R_enter.pack()
force_label.pack()
force_enter.pack()
calculate.pack()



#截面形状
##矩形
#b,h= 0.1,0.1 #b宽h高
#Iz = b*h**3/12
#w = 2*Iz/h
##圆
#d = 10 #直径
#Iz = np.pi*d**4/64
#w = 2*Iz/d
##圆环
#d,D = 0.002,0.03 #d内径D外径
#Iz = np.pi*(D**4-d**4)/64
#w = 2*Iz/D
#
#
#x = np.linspace(0,1,5)
#y = np.zeros(5)
#y_r = []
#f = 450
#
#E = 2.1e11
#ru = 0.3
#
#for i in range(len(x)):
#    de = x[-1] - x[i]
#    l = x[i] - x[0]
#    m = f * de
#    sigma = m/w
#    print(sigma)
#    tao = -3*f*l**3/E*Iz
#    print(tao)
#    y_r.append(tao)
#plt.plot(x,y,"-y")
#plt.scatter(x,y_r,c=x,cmap=plt.cm.Blues)          
#plt.show()
#
