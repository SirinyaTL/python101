from tkinter import*
from tkinter import ttk
from tkinter import messagebox


GUI=Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')#ชื่อหน้าต่าง
GUI.geometry('400x400') #ขนาด

L1=Label(GUI,text='โปรแกรมบันทึกข้อมูล')
L1.place(x=130,y=20)  #ตำแหน่งตัวหนังสือ

#สร้างชื่อปุ่ม
#B1= Frame(GUI)
#B1.place(x=100, y=80)
#B2= ttk.Button(B1,text='วันนี้วันอะไร')
#B2.pack(ipadx=20,ipady=20)

#กดแล้วมีข้อความออกมา
def Button2():
    text= 'วันอังคาร'
    messagebox.showinfo(text)

B1= Frame(GUI)
B1.place(x=100, y=80)

B2= ttk.Button(B1,text='วันนี้วันอะไร',command=Button2)
B2.pack(ipadx=20,ipady=20)

#วิชาที่เรียน
def Button3():
    text= 'คณิต,ไทย'
    messagebox.showinfo('วิชาที่เรียนวันนี้',text)
    
B2= Frame(GUI)
B2.place(x=100, y=180)
B3= ttk.Button(B1,text='เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

#เวลลาเลิกเรียน
def Button4():
    text= '15.00 น.'
    messagebox.showinfo('เวลาเลิกเรียน',text)

B3= Frame(GUI)
B3.place(x=100,y=250)
B4= ttk.Button(B1,text='เลิกเรียนกี่โมง',command=Button4)
B4.pack(ipadx=20,ipady=20)


#โปรแกรมพิเศษ
def Button5():
    text= 'ดูหนัง'
    messagebox.showinfo('โปรแกรมพิเศษ',text)

B4= Frame(GUI)
B4.place(x=100,y=350)
B5= ttk.Button(B1,text='มีโปรแกรมพิเศษไหม?',command=Button5)
B5.pack(ipadx=20,ipady=20)




