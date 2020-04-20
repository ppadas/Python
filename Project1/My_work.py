from tkinter import *
from tkinter.ttk import Radiobutton
import datetime
import time
from tkinter import messagebox


def printRools():
    file = open("rools.txt", "r")
    rools = file.read()
    messagebox.showinfo('Правила', rools)

def getSymbol(text):
    for i in text:
        print(i)
        yield i

window = Tk()
window.geometry('1600x1000')
window.title("Мой клавиатурный тренажёр")
filenames = ['text.txt', 'bigText.txt', 'my.txt']

def clicked2():
    lbl = Label(window, text='New file:', font=("Arial Bold", 10))
    lbl.grid(column=3, row=5)
    entry = Entry(window, width=10)
    entry.grid(column=3, row=6)
    def clicked3():
        filenames[selected.get()] = entry.get()
        lbl.destroy()
        entry.destroy()
        button.destroy()
    button = Button(window, text="Ok", command=clicked3)
    button.grid(column=3, row=7)

def changeFile():
    rad1 = Radiobutton(window, text='-1', value=0, variable=selected)
    rad2 = Radiobutton(window, text='-2', value=1, variable=selected)
    rad3 = Radiobutton(window, text='-3', value=2, variable=selected)
    btn = Button(window, text="Выбрать", command=clicked2)
    rad1.grid(column=3, row=1)
    rad2.grid(column=3, row=2)
    rad3.grid(column=3, row=3)
    btn.grid(column=3, row=4)

def clicked():
    timeB = time.time()
    if selected.get() == 10:
        changeFile()
        return

    fileNow = filenames[selected.get()]
    with open(fileNow) as f:
        text_ = f.read()
    lbl = Label(window, text=text_, font=("Arial Bold", 12))
    lbl.grid(column=selected.get(), row=2)
    text = getSymbol(text_)
    letter = [next(text)]

    def check():
        textIn = text_
        textOut = entry.get()
        print(textIn)
        print(len(textOut))
        print(len(textIn))
        print(textOut)
        if len(textOut) + 1 == len(textIn):
            ##messagebox.showinfo('Результат', 'Все верно!\n Статистику и время можно посмотреть в файле ')
            lbl = Label(window, text='Все верно!\n Статистику и время можно посмотреть в файле ', font=("Arial Bold", 10))
            timeE = time.time()
            stat = open('stat.txt', 'a')
            stat.write("\n\n")
            stat.write(str(datetime.datetime.today()))
            stat.write("\n")
            stat.write("file:")
            stat.write(fileNow)
            stat.write("\nTime: ")
            stat.write(str(timeE - timeB))
            stat.write("sec")
            stat.write("\nStatistic:\n")
            for let, err in statistic.items():
                stat.write("<")
                stat.write(let)
                stat.write(">")
                stat.write(" - ")
                stat.write(str(err))
                stat.write(" ")
            stat.close()
            for i in list(statistic):
                del statistic[i]
        else:
            ##messagebox.showinfo('Результат', 'Нужно дописать текст')
            lbl = Label(window, text='Еще немного!', font=("Arial Bold", 10))
        lbl.grid(column=selected.get(), row=5)


    buttonOk = Button(window, text="Проверка", command=check)
    buttonOk.grid(column=selected.get(), row=4)
    entry = Entry(window, validate="key")
    entry.grid(column=selected.get(), row=3)
    entry.focus()

    def testVal(inStr):
        if inStr[len(inStr) - 1] != letter[0]:
            if letter[0] in statistic:
                a = statistic .get(letter[0])
                statistic .update({letter[0]: a+1})
            else:
                statistic .update({letter[0]: 1})
            return False
        letter.pop()
        letter.append(next(text))
        return True

    entry['validatecommand'] = (entry.register(testVal), '%P')

selected = IntVar()
rad1 = Radiobutton(window, text='Малая тренировка', value=0, variable=selected)
rad2 = Radiobutton(window, text='Большой текст', value=1, variable=selected)
rad3 = Radiobutton(window, text='Мой Файл', value=2, variable=selected)
rad4 = Radiobutton(window, text='Сменить файл', value=10, variable=selected)
btn = Button(window, text="Выбрать", command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)
btn.grid(column=4, row=0)
btn2 = Button(window, text="Правила", command=printRools)
btn2.grid(column=10, row=10)

statistic = {}

window.mainloop()
