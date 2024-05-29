import pyperclip  # Библиотека для работы с буфером обмена
from tkinter import messagebox  # Модуль для отображения диалоговых окон
from tkinter import filedialog  # Модуль для работы с диалогами выбора файлов
from tkinter import *  # Основной модуль для работы с графическим интерфейсом
import keyboard  # Библиотека для работы с горячими клавишами

# Функция для смены темы оформления текстового поля
def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']

# Функция для смены шрифта текстового поля
def chenge_fonts(fontss):
     text_fild['font'] = fonts[fontss]['font']

# Функция для закрытия приложения с подтверждением
def notepad_exit():
     answer = messagebox.askyesno('ливаю', 'давай на уверенности или нет ?')
     if answer:
          window.destroy()

# Функция для открытия файла и загрузки его содержимого в текстовое поле
def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла',filetypes=(('Текстовые документы(*txt)','*txt'),('Все файлы','*.*')))
    if file_path:
        text_fild.delete('1.0',END)
        text_fild.insert('1.0', open(file_path,encoding='utf-8').read())

# Функция для сохранения содержимого текстового поля в файл
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы(*txt)','*txt'),('Все файлы','*.*')))
    if file_path:
        with open(file_path, 'w' , encoding='utf-8') as f:
            text = text_fild.get('1.0', END)
            f.write(text)

# Функция для вставки текста из буфера обмена в текстовое поле
def paste():
    clipboard_text = pyperclip.paste()
    if clipboard_text:
        text_fild.insert(INSERT, clipboard_text)

# Функция для копирования выделенного текста
def copy():
    text_fild.event_generate('<<Copy>>')

# Функция для вырезания выделенного текста
def cut():
    text_fild.event_generate('<<Cut>>')

# Функция для обработки нажатий клавиш (включая горячие клавиши)
def on_key_press(event):
    if keyboard.is_pressed('ctrl+v'):
        paste()
    elif keyboard.is_pressed('ctrl+c'):
        copy()
    elif keyboard.is_pressed('ctrl+x'):
        cut()

# Создание основного окна приложения
window = Tk()
window.title('text editor')
window.geometry('800x800')
window.iconbitmap('iconbitmap.ico')

# Создание главного меню
main_menu = Menu(window)

# Создание подменю "Файл"
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Кышь с пк', command=notepad_exit)
window.config(menu=file_menu)

# Создание подменю "Вид"
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Убогая', command=lambda: chenge_theme('ybogi'))
view_menu_sub.add_command(label='Скушная_т', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Скушная_с', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

# Добавление подменю шрифтов
font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Mister Brush', command=lambda: chenge_fonts('MB'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифты', menu=font_menu_sub)
window.config(menu=view_menu)

# Добавление подменю в главное меню
main_menu.add_cascade(label='Папки', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
window.config(menu=main_menu)

# Настройка рамки для текстового поля
f_text = Frame(window)
f_text.pack(fill=BOTH, expand=1)

# Словари для тем и шрифтов
view_colors = {
    'dark': {
        'text_bg': 'black',
        'text_fg': 'lime',
        'cursor': 'brown',
        'select_bg': '#B8D4D4'
    },
    'light': {
        'text_bg': 'white',
        'text_fg': 'black',
        'cursor': 'brown',
        'select_bg': '#B8D4D4'
    },
    'ybogi': {
        'text_bg': '#B8D4D4',
        'text_fg': '#000000',
        'cursor': 'brown',
        'select_bg': '#B8D4D4'
    }
}

fonts = {
   'Arial': {
    'font': 'Arial 13 bold'
},
'MB': {
    'font': ('Mister Brush', 14, 'bold')
},
'TNR': {
    'font': ('Times New Roman', 14, 'bold')
}
}

# Создание текстового поля
text_fild = Text(f_text, bg="#B8D4D4", fg="#000000", padx=10, pady=10, wrap=WORD, insertbackground='#F00018', selectbackground="#6BFFB8", font='Arial 13 bold')
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

# Создание полосы прокрутки для текстового поля
scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

# Привязка обработчика нажатий клавиш
window.bind('<KeyPress>', on_key_press)

# Запуск основного цикла обработки событий
window.mainloop()
