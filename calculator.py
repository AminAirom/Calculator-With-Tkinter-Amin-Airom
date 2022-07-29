# ============================imports================================
import tkinter.messagebox
from tkinter import *

# ============================settings===============================
root = Tk()
root.title('Calculator')
root.geometry('400x200')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)
# =======================Variables===================================
num1 = StringVar()
num2 = StringVar()
res = StringVar()
# ===========================Frames==================================
Top_first = Frame(root, width=400, height=50, bg=color)
Top_first.pack(side='top')
Top_second = Frame(root, width=400, height=50, bg=color)
Top_second.pack(side='top')
Top_third = Frame(root, width=400, height=50, bg=color)
Top_third.pack(side='top')
Top_forth = Frame(root, width=400, height=50, bg=color)
Top_forth.pack(side='top')
Top_five = Frame(root, width=400, height=50, bg=color)
Top_five.pack(side='top')
# ===========================Buttons=================================
btn_plus = Button(Top_forth, text="+", width=10, highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_minus = Button(Top_forth, text="-", width=10, highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=5, pady=5)
btn_mul = Button(Top_forth, text="*", width=10, highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=5, pady=5)
btn_div = Button(Top_forth, text="/", width=10, highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=5, pady=5)
btn_clear = Button(Top_five, text="clear", width=10, highlightbackground=color, command=lambda: clear())
btn_clear.pack(side=LEFT, padx=5, pady=5)
btn_creator = Button(Top_five, text="creator", width=10, highlightbackground=color, command=lambda: creator())
btn_creator.pack(side=LEFT, padx=5, pady=5)
# ==========================Functions================================
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong !')
    elif ms == 'Division Error':
        tkinter.messagebox.showerror('Division Error', 'can not divide by 0 !')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == '0':
        errorMsg('Division Error')
    elif num2.get() != '0':
        try:
            value = float(num1.get()) / float(num2.get())
            res.set(value)
        except:
            errorMsg('error')


def clear():
    num1.set('')
    num2.set('')
    res.set('')


def creator():
    tkinter.messagebox.showinfo('creator', 'this calculator has been created by Amin Airom')


# =========================Labels and Entries========================
label_first_num = Label(Top_first, text='enter your first number :', bg=color)
label_first_num.pack(side=LEFT, padx=5, pady=5)
first_num = Entry(Top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)
label_second_num = Label(Top_second, text='enter your second number :', bg=color)
label_second_num.pack(side=LEFT, padx=5, pady=5)
second_num = Entry(Top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)
label_result = Label(Top_third, text='Result :', bg=color)
label_result.pack(side=LEFT, padx=5, pady=5)
result = Entry(Top_third, highlightbackground=color, textvariable=res)
result.pack(side=LEFT)
# ============================run====================================
root.mainloop()
