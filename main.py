import time
from tkinter import *


def clicked1():
    btn2['relief'] = RAISED
    btn1['relief'] = GROOVE
    lbl.configure(text="")
    lbl2.configure(text="")
    lbl2.configure(text="Вами была выбрана книжная ориентация печати")


def clicked2():
    btn1['relief'] = RAISED
    btn2['relief'] = GROOVE
    lbl.configure(text="")
    lbl2.configure(text="")
    lbl2.configure(text="Вами была выбрана альбомная ориентация печати")


def clicked3():
    btn4['relief'] = RAISED
    btn3['relief'] = GROOVE
    lbl.configure(text="")
    lbl3.configure(text="")
    lbl3.configure(text="Режим автоматической двусторонней печати")


def clicked4():
    btn3['relief'] = RAISED
    btn4['relief'] = GROOVE
    lbl.configure(text="")
    lbl3.configure(text="")
    lbl3.configure(text="Режим односторонней печати")


def switchState():
    if btn1['state'] == DISABLED:
        btn1['state'] = NORMAL
        time.sleep(0.5)
        lbl.configure(text="Ready")
    else:
        btn1['state'] = DISABLED
        lbl.configure(text="")

    if btn2['state'] == DISABLED:
        btn2['state'] = NORMAL
    else:
        btn2['state'] = DISABLED
        lbl.configure(text="")

    if btn3['state'] == DISABLED:
        btn3['state'] = NORMAL
    else:
        btn3['state'] = DISABLED
        lbl.configure(text="")

    if btn4['state'] == DISABLED:
        btn4['state'] = NORMAL
    else:
        btn4['state'] = DISABLED
        lbl.configure(text="")

    if btn5['state'] == DISABLED:
        btn5['state'] = NORMAL
    else:
        btn5['state'] = DISABLED
        lbl.configure(text="")

    if spin['state'] == DISABLED:
        spin['state'] = NORMAL
    else:
        spin['state'] = DISABLED
        lbl.configure(text="")

    if btn6['state'] == DISABLED:
        btn6['state'] = NORMAL
    else:
        btn6['state'] = DISABLED
        lbl.configure(text="")


def get_kolvo_str():
    a = spin.get()
    global count
    count = a
    lbl5.configure(text="")
    lbl5.configure(text=f"Количество копий: {count} ")



def print1():
    i = 0
    while i < int(count):
        i = i+1
        print(f"Лист: {i}")
        time.sleep(0.5)


window = Tk()
window.title("МФУ Xerox B215")
window.geometry('550x350')

powerbutton = Button(window, text='Питание', command=switchState)


selected = IntVar()
btn1 = Button(window, text='Книжная', command=clicked1, state=DISABLED)
btn2 = Button(window, text='Альбомная', command=clicked2, state=DISABLED)
btn3 = Button(window, text='Двухстороняя печать', command=clicked3, state=DISABLED)
btn4 = Button(window, text='Односторонняя печать', command=clicked4, state=DISABLED)
btn5 = Button(window, text='Установить количество копий', command=get_kolvo_str, height=4, state=DISABLED)
btn6 = Button(window, text='Печать', command=print1, state=DISABLED)

spin = Spinbox(window, from_=0, to=100, width=5, state=DISABLED)
lbl = Label(window, font=("Arial Bold", 10))
lbl1 = Label(window, text="Введите количество страниц:")
lbl2 = Label(window)
lbl3 = Label(window)
lbl4 = Label(window)
lbl5 = Label(window)
powerbutton.grid(column=0, row=0)


btn1.grid(column=1, row=0)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn4.grid(column=2, row=0)
btn5.grid(column=4, row=1)
btn6.grid(column=2, row=3)
photo = PhotoImage(file = "123.png")
window.iconphoto(False, photo)


lbl.grid(column=0, row=1)
lbl1.grid(column=2, row=4)
lbl2.place(relx=.5, rely=.9, anchor="c", height=30, width=1300, bordermode=OUTSIDE)
lbl3.place(relx=.5, rely=.8, anchor="c", height=30, width=1300, bordermode=OUTSIDE)
lbl4.place(relx=.5, rely=.6, anchor="c", height=30, width=1300, bordermode=OUTSIDE)
lbl5.place(relx=.5, rely=.5, anchor="c", height=30, width=1300, bordermode=OUTSIDE)
spin.grid(column=3, row=4)

window.mainloop()
