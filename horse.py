from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Добавление строки в текстовый блок
def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)

# Расположение лошадей на экране
def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)

# Чтение из файла оставшейся суммы
def loadMoney():
    try:
        f = open('money.dat', 'r')
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

# Запись суммы в файл
def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла, наш Ипподром закрывается!")
        quit(0)


root = Tk()

# Размеры окна программы
WIDTH = 1024
HEIGHT = 600

# Позиции лошадей
x01 = 20
x02 = 20
x03 = 20
x04 = 20

# Клички лошадей
nameHorse01 = "Ананас"
nameHorse02 = "Сталкер"
nameHorse03 = "Прожорливый"
nameHorse04 = "Копытце"

# Финансовые показатели
defaultMoney = 10000
money = 0
valuta = 'руб'

# Создаем главное окно
# Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Устанавливаем заголовок
root.title('ИППОДРОМ')

# Запрещаем изменение размеров
root.resizable(False, False)

# Устанавливаем ширину, высоту и позицию
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

road_image = PhotoImage(file="road.png") # Загружаем изображение фона
road = Label(root, image=road_image)# Устанавливаем в Label
road.place(x=0, y=17) # Выводим в окно

horse01_image = PhotoImage(file='horse01.png') # Загружаем изображение
horse01 = Label(root, image=horse01_image) # Устанавливаем в Label

horse02_image = PhotoImage(file='horse02.png')
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file='horse03.png')
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file='horse04.png')
horse04 = Label(root, image=horse04_image)

horsePlaceInWindow()

# Создаем кнопку и выводим ее на экран
startButton = Button(text="Старт", font='arial 20', width=61, background='#37AA37')
startButton.place(x=20, y=370)

# Создаем информационный чат виджетом Text
textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)

# Создаем и прикрепляем к тексту полосу прокрутки
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary["yscrollcommand"] = scroll.set

# Загружаем сумму средств игрока из файла
money = loadMoney()

if (money <= 0):
    messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
    quit(0)

# Формируем текстовую строку и выводим в нее оставшуюся сумму средств
labelAllMoney = Label(text=f'Осталось средств: {money} {valuta}.', font='Arial 12')
labelAllMoney.place(x=20, y=565)

# Выводим текстовые метки в левом нижнем углу окна
labelHorse01 = Label(text='Ставка на лошадь №1')
labelHorse01.place(x=20, y=450)

labelHorse02 = Label(text='Ставка на лошадь №2')
labelHorse02.place(x=20, y=480)

labelHorse03 = Label(text='Ставка на лошадь №3')
labelHorse03.place(x=20, y=510)

labelHorse04 = Label(text='Ставка на лошадь №4')
labelHorse04.place(x=20, y=540)

# Чекбоксы для лошадок
horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

# Выпадающий список
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

# Задаем атрибут "только для чтения""
stavka01["state"] = "readonly"
stavka01.place(x=280, y=450)
stavka02["state"] = "readonly"
stavka02.place(x=280, y=480)
stavka03["state"] = "readonly"
stavka03.place(x=280, y=510)
stavka04["state"] = "readonly"
stavka04.place(x=280, y=540)

root.mainloop()


