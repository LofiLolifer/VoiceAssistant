import main
from tkinter import *
import UiSettings



#Функции
def default_window_minimize():
    root2 = Tk()
    root2['bg'] = '#000'
    root2.title('Minimize')
    root2.wm_attributes("-alpha", 1)
    root2.geometry('200x200')

    root2.resizable(width=False, height=False)
    frame1 = Frame(root2, bg="#000")
    frame1.place(relx=0, rely=0.4, relwidth=1, relheight=0.7)
    butt = Button(frame1, text="Слушай меня", bg="#000", command=minimize_button_click, pady="12", padx="12",
                  borderwidth=0, foreground="#86e7ff", font=50)
    butt.pack()

def btn_click():
    output.config(text="Слушаю...")
    root.update()
    query1 = main.listen_me()
    todo = main.china_clicker(query1)
    message(query1, todo)

def minimize_button_click():
    query2 = main.listen_me()
    main.china_clicker(query2)



def message(query1, todo):
    if todo != "":
        output.config(text="Услышал\n" + query1 + "\n" + todo)
    else:
        output.config(text="Услышал\n" + query1)


root = Tk()

#Окно
root.image = PhotoImage(file="C:/Users/feede/PycharmProjects/pythonProject5/BG.png")
bg_logo = Label(root, image=root.image)
bg_logo.grid(row=0, column=0)

root['bg'] = '#000'
root.title('Ботяра')
root.wm_attributes("-alpha", 1)
root.geometry('750x800')

root.resizable(width=False, height=False)

frame = Frame(root, bg="#000")
frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.7)

#Картинка кнопки
img = PhotoImage(file=r"C:/Users/feede/PycharmProjects/pythonProject5/loop.png")
imgBtn = img.subsample(5, 5)

btn = Button(frame, image=imgBtn, bg="#000", command=btn_click, pady="12", padx="12", borderwidth=0)
btn.pack()

#Вывод состояния
output = Label(frame, text="Не слушаю", bg="#000", font=40, foreground="#86e7ff")
output.pack(side=BOTTOM)

# Кнопки панели


btn_settings = Button(frame, font=50, text="Настройки", bg="#000", foreground="#86e7ff", borderwidth=0,
                      command=UiSettings.button_setting)



btn_settings.pack(side=TOP)

btn_minimize = Button(frame, font=50, text="Уменьшить", bg="#000", foreground="#86e7ff", borderwidth=0,
                      command=default_window_minimize)
btn_minimize.pack(side=TOP)

root.mainloop()
