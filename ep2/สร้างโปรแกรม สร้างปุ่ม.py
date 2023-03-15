import tkinter as tk

window = tk.Tk() #สร้างตัวแปรมารับหน้าชื่อวินโดว์
window.title('โปรแกรมความรู้')    #ชื่อแอพ
window.minsize(width=400,height=400)

title_label = tk.Label(master=window,text='Love')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text = 'Okay')
ok_button.pack()
