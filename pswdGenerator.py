#Start

from tkinter import *

main_window = Tk()

#numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

#text input area
e = Entry(main_window, width= 50, borderwidth= 25).grid(row= 0, column= 0, columnspan= 3, padx= 30 )

list_of_numbers = []

#function to activate buttons
def number_input(number):
    current_value = e.get()
    e.delete(0, END)
    e.insert(str(current_value) + str(number))


def clear_value():
    list_of_numbers.clear()
    e.delete(0, END)

def sum_of_values():
    num1 = e.get()
    list_of_numbers.append(number)
    e.delete(0, END)

def equals():
    num1 = e.get()
    list_of_numbers.append(int(num1))
    e.delete(0, END)

    SUM = 0
    for values in list_of_numbers:
        SUM += int(values)

    e.insert(0, int(SUM))


#button
bttn9 = Button(main_window, text= "9", padx= 40, pady= 20, command= lambda : number_input(9) ).grid(row= 1, column= 0)
bttn8 = Button(main_window, text= "8", padx= 40, pady= 20, command= lambda : number_input(8) ).grid(row= 1, column= 1)
bttn7 = Button(main_window, text= "7", padx= 40, pady= 20, command= lambda : number_input(7) ).grid(row= 1, column= 2)

bttn6 = Button(main_window, text= "6", padx= 40, pady= 20, command= lambda : number_input(6) ).grid(row= 2, column= 0)
bttn5 = Button(main_window, text= "5", padx= 40, pady= 20, command= lambda : number_input(5) ).grid(row= 2, column= 1)
bttn4 = Button(main_window, text= "4", padx= 40, pady= 20, command= lambda : number_input(4) ).grid(row= 2, column= 2)

bttn3 = Button(main_window, text= "3", padx= 40, pady= 20, command= lambda : number_input(3) ).grid(row= 3, column= 0)
bttn2 = Button(main_window, text= "2", padx= 40, pady= 20, command= lambda : number_input(2) ).grid(row= 3, column= 1)
bttn1 = Button(main_window, text= "1", padx= 40, pady= 20, command= lambda : number_input(1) ).grid(row= 3, column= 2)

bttn0 = Button(main_window, text= "0", padx= 40, pady= 20, command= lambda : number_input() ).grid(row= 4, column= 0)

bttn_add = Button(main_window, text= "+", padx= 40, pady= 20, command= sum_of_values).grid(row= 4, column= 1)
bttn_clear = Button(main_window, text= "clr", padx= 40, pady= 20, command= clear_value).grid(row= 5, column= 1)
bttn_equals = Button(main_window, text= "=", padx= 40, pady= 20, command= equals).grid(row= 5, column= 2)

main_window.mainloop()

from tkinter import *
import pyperclip
import random
from password_strength import *
import math
from tkinter import messagebox

root = Tk()
root.geometry('350x350')
root.title('Python MiniProject')
# root.iconbitmap('bitmap.ico')

passstr = StringVar()
passlen_smallalpha = IntVar()
passlen_bigalpha = IntVar()
passlen_digits = IntVar()
passlen_specialcharac = IntVar()
passstr2 = StringVar()
passstr1 = StringVar()

passlen_smallalpha.set(0)
passlen_bigalpha.set(0)
passlen_digits.set(0)
passlen_specialcharac.set(0)


def generate():

    list1 = []
    small = passlen_smallalpha.get()
    big = passlen_bigalpha.get()
    digits = passlen_digits.get()
    special = passlen_specialcharac.get()

    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

    pass2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

    pass3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    pass4 = ['!', '@', '#', '$', '%', '&', '*']

    password = ""
    mylist = [pass1, pass2, pass3, pass4]
    k = 1

    while k == 1:
        random.shuffle(mylist)
        list1 = mylist
        for q in range(4):
            if list[q][1] == 'A' and big != 0:
                password = password + random.choice(pass2)
                big -= 1
            if list1[q][0] == 'a' and small != 0:
                password = password + random.choice(pass1)
                small -= 1
            if list[q][0] == '1' and digits != 0:
                password = password + random.choice(pass3)
                digits -= 1
            if list[q][0] == '!' and special != 0:
                password = password + random.choice(pass4)
                special -= 1
        if small == 0 and big == 0 and digits == 0 and special == 0:
            break

    passstr.set(password)


def copy_to_clipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)


def module_1():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    Label(f1, text="Password Generator ", font="calibre 20 bold").pack()

    Label(f1, text="Enter no. of small Alphabets").pack(pady=3)
    Entry(f1, textvariable=passlen_smallalpha).pack(pady=3)

    Label(f1, text="Enter no. of Big Alphabets").pack(pady=3)
    Entry(f1, textvariable=passlen_bigalpha).pack(pady=3)

    Label(f1, text="Enter no. of Digits").pack(pady=3)
    Entry(f1, textvariable=passlen_digits).pack(pady=3)

    Label(f1, text="Enter no. of Special Characters").pack(pady=3)
    Entry(f1, textvariable=passlen_specialcharac).pack(pady=3)

    Button(f1, text="Generate Password", command=generate).pack(pady=7)
    Entry(f1, textvariable=passstr).pack(pady=3)
    Button(f1, text="Copy to Clipboard", command=copy_to_clipboard).pack()
    Button(f1, text='->', command=home).place(x=0, y=0)


def strength_checker():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    if passstr2.get() == "":
        messagebox.showinfo("Error", "Password Can't Be Empty")
    else:
        result = PasswordStats(passstr.get())
        final = result.strength()
        label1 = Label(f1, text="")
        w = Canvas(f1, height=100, width=600)
        w.pack()
        label1.place(x=170, y=100)
        label1["text"] = str(math.ceil(final * 100)) + " %"
        if final >= 0.66:
            w.create_rectangle(70, 50, 280, 100, fill="#27cf54", outline="white")
        elif 0.10 < final < 0.40:
            w.create_rectangle(70, 50, 280, 100, fill="#f0f007", outline="white")
        elif final <= 0.10:
            w.create_rectangle(70, 50, 280, 100, fill="#27cf54", outline="white")
        b = Button(f1, text="->", command=module_2)
        b.place(x=0, y=0)


def module_2():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    head = Label(f1, text="Password Strength Calculator", font=("helvetica", 15, "bold"))
    head.pack(ipadx=5, ipady=5)
    entry = Entry(f1, textvariable=passstr2)
    entry.pack(ipadx=30, ipady=5)
    button = Button(f1, text="check", command=strength_checker)
    button.pack(ipadx=5, ipady=5)
    b = Button(f1, text="->", command=home)
    b.place(x=0, y=0)


def check_ch():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    string = passstr1.get()
    alphabets = digits = special = 0

    for i in range(len(string)):
        if string[i].isalpha():
            alphabets = alphabets + 1
        elif string[i].isdigit():
            digits = digits + 1
        else:
            special = special + 1
    b = Button(f1, text="->", command=module_3)
    b.place(x=0, y=0)
    l1 = Label(f1, text={" alphabets ", alphabets})
    l1.pack()
    l2 = Label(f1, text={" digits ", digits})
    l2.pack()
    l3 = Label(f1, text={" special symbol ", special})
    l3.pack()


def module_3():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    label = Label(f1, text=" Enter your Password ")
    label.pack()
    entry = Entry(f1, textvariable=passstr1)
    entry.pack()
    b = Button(f1, text="Check Character", command=check_ch)
    b.pack()
    b1 = Button(f1, text="->", command=home)
    b1.place(x=0, y=0)


def home():
    f1 = Frame()
    f1.place(x=0, y=0, width=350, height=350)
    label = Label(f1, text="Click On Button To Select A module")
    label.pack()
    button_1 = Button(f1, text="Random Password Generate", command=module_1)
    button_1.place(x=100, y=50)
    button_2 = Button(f1, text="Password Strength Check", command=module_2)
    button_2.place(x=107, y=100)
    button_3 = Button(f1, text="Character Type Check", command=module_3)
    button_3.place(x=117, y=150)


home()
root.mainloop()

