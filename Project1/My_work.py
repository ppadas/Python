from tkinter import *
from tkinter.ttk import Radiobutton
import datetime
import time
from tkinter import messagebox
from collections import defaultdict


stat_template = '''

{today}
File: {file}
Time: {duration} seconds
Statistics:
{items}
'''

stat_item_template = '<{}> - {}\n'


def print_rools():
    file = open("rools.txt", "r")
    rools = file.read()
    messagebox.showinfo(titels[1], rools)


def get_symbol(text):
    for i in text:
        print(i)
        yield i


window = Tk()
window.geometry('800x500')
filenames = ['text.txt', 'bigText.txt', 'my.txt']
titles_file = open('titels.txt', 'r')
titles = titles_file.readlines()
titles_file.close()
for i in range(len(titles)):
    pair = titles[i].split("\n")
    titles[i] = pair[0]
window.title(titles[0])


def changeFile():
    rad1 = Radiobutton(window, text='-1', value=0, variable=selected)
    rad2 = Radiobutton(window, text='-2', value=1, variable=selected)
    rad3 = Radiobutton(window, text='-3', value=2, variable=selected)

    def clicked2():
        lbl = Label(window, text=titles[8], font=("Arial Bold", 10))
        lbl.grid(column=3, row=5)
        entry = Entry(window, width=10)
        entry.grid(column=3, row=6)

        def clicked3():
            file = open(entry.get(), "r")
            lines = file.readlines()
            if len(lines) > 1 or len(lines) == 0 or lines[0] == '':
                lbl_err = Label(window, text=titles[14] + ": " + entry.get(),
                                font=("Arial Bold", 10))
                lbl_err.grid(column=3, row=5)
            else:
                lbl_done = Label(window, text=titles[15] + ": " + entry.get(),
                                 font=("Arial Bold", 10))
                lbl_done.grid(column=3, row=5)
                filenames[selected.get()] = entry.get()
            lbl.destroy()
            entry.destroy()
            button.destroy()

        button = Button(window, text=titles[3], command=clicked3)
        button.grid(column=3, row=7)

    btn = Button(window, text=titles[2], command=clicked2)
    rad1.grid(column=3, row=1)
    rad2.grid(column=3, row=2)
    rad3.grid(column=3, row=3)
    btn.grid(column=3, row=4)


def clicked():
    time_begin = time.time()
    if selected.get() == 10:
        changeFile()
        return

    file_now = filenames[selected.get()]
    with open(file_now) as f:
        text_ = f.read()
    lbl = Label(window, text=text_, font=("Arial Bold", 12))
    lbl.grid(column=selected.get(), row=2)
    text = get_symbol(text_)
    letter = [next(text)]

    def check():
        text_in = text_
        text_out = entry.get()
        print(text_in)
        print(len(text_out))
        print(len(text_in))
        print(text_out)
        if len(text_out) + 1 == len(text_in):
            if len(statistic) == 0:
                lbl = Label(window, text=titles[13] + '\n' + titles[11],
                            font=("Arial Bold", 10))
            else:
                lbl = Label(window, text=titles[10] + '\n' + titles[11],
                            font=("Arial Bold", 10))
                time_end = time.time()
                items = ''.join(stat_item_template.format(let, err) for let,
                                err in statistic.items())
                stat = stat_template.format(today=datetime.datetime.today(),
                                            file=file_now,
                                            duration=str(time_end -
                                                         time_begin),
                                            items=items)
                print(items)
                with open('stat.txt', 'a') as stat_file:
                    stat_file.write(stat)
                for i in list(statistic):
                    del statistic[i]
        else:
            lbl = Label(window, text=titles[12], font=("Arial Bold", 10))
        lbl.grid(column=selected.get(), row=5)

    button_ok = Button(window, text=titles[9], command=check)
    button_ok.grid(column=selected.get(), row=4)
    entry = Entry(window, validate="key", width=50)
    entry.grid(column=selected.get(), row=3)
    entry.focus()

    def test_val(in_str):
        if in_str[-1] != letter[0]:
            statistic[letter[0]] += 1
            return False
        letter[0] = next(text)
        return True

    entry['validatecommand'] = (entry.register(test_val), '%P')

selected = IntVar()
rad1 = Radiobutton(window, text=titles[4], value=0, variable=selected)
rad2 = Radiobutton(window, text=titles[5], value=1, variable=selected)
rad3 = Radiobutton(window, text=titles[6], value=2, variable=selected)
rad4 = Radiobutton(window, text=titles[7], value=10, variable=selected)
btn = Button(window, text=titles[2], command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)
btn.grid(column=4, row=0)
btn2 = Button(window, text=titles[1], command=print_rools)
btn2.grid(column=10, row=10)

statistic = defaultdict(int)

window.mainloop()
