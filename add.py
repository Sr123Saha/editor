from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


def chenge_fonts(fontss):
     text_fild['font'] = fonts[fontss]['font']


def notepad_exit():
     answer = messagebox.askyesno('ливаю', 'давай на уверенности или нет ?')
     if answer:
          window.destroy()

def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла',filetypes=(('Текстовые документы(*txt)','*txt'),('Все файлы','*.*')))
    if file_path:
        text_fild.delete('1.0',END)
        text_fild.insert('1.0', open(file_path,encoding='utf-8').read)


def seve_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы(*txt)','*txt'),('Все файлы','*.*')))
    f = open(file_path, 'W' , encoding='utf-8' )
    text =text_fild.get('1.0',END)
    f.write(text)
    f.close()


window = Tk()
window.title('text editor')
window.geometry('800x800')
window.iconbitmap('iconbitmap.ico')

main_menu = Menu(window)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть',command=open_file)
file_menu.add_separator()
file_menu.add_command(label='сохраняем',command=seve_file)
file_menu.add_separator()
file_menu.add_command(label='кышь с пк', command=notepad_exit)
window.config(menu=file_menu)

view_menu =Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='убогая',command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='скушная',command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема',menu=view_menu_sub)

font_menu_sub.add_command(label='Arial',command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Mister Brush',command=lambda: chenge_fonts('MB'))
font_menu_sub.add_command(label='Times New Roman',command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='шрифты',menu=font_menu_sub)
window.config(menu=view_menu)

main_menu.add_cascade(label='папки' , menu=file_menu)
main_menu.add_cascade(label='Вид' , menu=view_menu)
window.config(menu=main_menu)

window.config(menu=main_menu)

f_text = Frame(window)
f_text.pack(fill=BOTH ,expand=1)

view_colors = {
    'dark':{
        'text_bg': 'black',
        'text_fg': 'lime',
        'cursor':'brown',
        'select_bg': '#B8D4D4'   
        },
        'light':{
            'text_bg': 'white', 
            'text_fg': 'black', 
            'cursor':'brown',
            'select_bg': '#B8D4D4'  
        }

}

fonts = {
    'Arial':{
        'font': 'Arial 13 bold'
        },
        'MB':{
            'font': ('Mister Brush', 14, 'bold') 
        },
        'TNR':{
            'font': ('Times New Roman', 14, 'bold') 
            }

}


text_fild = Text(f_text,bg = "#B8D4D4",fg="#000000",padx=10,pady=10,wrap=WORD,insertbackground='#F00018',selectbackground="#6BFFB8",font='Arial 13 bold')
text_fild.pack(expand=1,fill=BOTH,side=LEFT)

scroll = Scrollbar(f_text,command=text_fild.yview)
scroll.pack(side=LEFT,fill=Y)
text_fild.config(yscrollcommand=scroll.set)

window.mainloop()
