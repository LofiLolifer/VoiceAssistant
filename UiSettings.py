from tkinter import *
from tkinter import filedialog

OptionList = [
    "Открыть в браузере",
    "Записать в файл",
    "Прочитать из файла",
    "Выключить компьютер",
]


def finder():
    c = (filedialog.askopenfiles())
    filename.set(str(c))


def button_setting():
    root1 = Tk()

    root1['bg'] = '#000'
    root1.title('Настройки')
    root1.wm_attributes("-alpha", 1)
    root1.geometry('500x400')

    frame = Frame(root1, bg="#000")
    frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.7)

    say_lb = Label(frame, text="Что вы говорите:", foreground="#86e7ff", bg="#000")
    say_lb.pack()
    global say_inp
    say_inp = Entry(frame, width=30)
    say_inp.pack()
    path_lb = Label(frame, text="Путь до файла/Ссылка:", foreground="#86e7ff", bg="#000")
    path_lb.pack()
    global path_inp
    global filename
    filename = StringVar()
    path_inp = Entry(frame, width=30, textvariable=filename)
    path_inp.pack()
    obz = Button(frame, text="Обзор", command=finder)
    obz.pack()

    variable = StringVar(frame)
    variable.set(OptionList[0])

    global opt
    opt = OptionMenu(frame, variable, *OptionList, command=zaplatka)
    opt.config(width=20, font=('Helvetica', 10))
    opt.pack()

    button_save = Button(frame, text="Сохранить", bg="#000", pady="12", padx="12", borderwidth=0, foreground="#86e7ff",
                         command=save)
    button_save.pack(side=BOTTOM)
    button_exit = Button(frame, text="Выход", bg="#000", pady="12", padx="12", borderwidth=0, foreground="#86e7ff",
                         command=root1.destroy)
    button_exit.pack(side=BOTTOM)


def zaplatka(name):
    global china
    china = OptionList.index(name)


def save():
    with open("Options.txt", "a") as file:
        file.write(say_inp.get() + " " + str(china) + " " + path_inp.get() + "\n")
        print("Задача добавлена в Options.txt")
