from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()#นี่คือหน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทุกข้อมูล')#นี่คือชื่อโปรแกรม
GUI.geometry('500x400')#ขนาดหน้าจอโปแกรม

L1.Label(GUI,text='โปรอแกรมบันทึกความรู้',front=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

B1=ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=10)#ทำให้ปุ่มอยู่กลางจอ

###########
def Button2():  #Button2 เปลี่ยนชื่อได้
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1=Frame(GUI)#คล้ายกระดาน
FB1.place(x=200,y=200) #.place กำหนดโลเคชั่นว่าให้อยู่ตรงไหน
B2=ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
#B2.pack(ipadx=20,ipady=10)#ทำให้เกิดปุ่ม ขนากx,y
B2.pack(ipadx=20,ipady=10) 
#########
GUI.mainloop()
