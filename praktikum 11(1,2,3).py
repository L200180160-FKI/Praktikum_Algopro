#kegiatan 1
from Tkinter import Tk, Label, Entry, Button
from tkMessageBox import showinfo

my_app = Tk(className='Aplikasi dengan beberapa widget')
L0 = Label(my_app, text="Data Diri", font=("Arial", 24))
L0.grid(row=0, column=0)
L1 = Label(my_app, text="Nama")
L1.grid(row=1, column=0)
E1 = Entry(my_app)
E1.grid(row=1, column=1)
L2 = Label(my_app, text="NIM")
L2.grid(row=2, column=0)
E2 = Entry(my_app)
E2.grid(row=2, column=1)
L3 = Label(my_app, text="Buku favorit")
L3.grid(row=3, column=0)
E3 = Entry(my_app)
E3.grid(row=3, column=1)
L4 = Label(my_app, text="Idola")
L4.grid(row=4, column=0)
E4 = Entry(my_app)
E4.grid(row=4, column=1)
L5 = Label(my_app, text="Motto")
L5.grid(row=5, column=0)
E5 = Entry(my_app)
E5.grid(row=5, column=1)


B=Button(my_app, text ="Tutup", command=my_app.quit)
B.grid(row=6, column=1)
my_app.mainloop()

#kegiatan 2
from Tkinter import Tk, Label, Button, StringVar, Entry
from tkMessageBox import showinfo

my_app=Tk(className='kalkulator')

L1=Label(my_app,text='Angka 1')
L1.grid(row=0,column=0)
str1=StringVar()
E1=Entry(my_app, textvariable=str1)
E1.grid(row=0,column=2,columnspan=3)
L2=Label(my_app, text='Angka 2')
L2.grid(row=1, column=0)
str2=StringVar()
E2=Entry(my_app, textvariable=str2)
E2.grid(row=1,column=2,columnspan=3)

def tambah():
         a=float(str1.get())
         b=float(str2.get())
         c=a+b
         hasil.config(text=c)
def kurang():
         a=float(str1.get())
         b=float(str2.get())
         c=a-b
         hasil.config(text=c)
def kali():
         a=float(str1.get())
         b=float(str2.get())
         c=a*b
         hasil.config(text=c)
def bagi():
         a=float(str1.get())
         b=float(str2.get())
         c=a/b
         hasil.config(text=c)

B1=Button(my_app,text='+',command=tambah)
B1.grid(row=2,column=0,pady=10)
B2=Button(my_app,text='-',command=kurang)
B2.grid(row=2,column=1)
B3=Button(my_app,text='x',command=kali)
B3.grid(row=2,column=2)
B4=Button(my_app,text=':',command=bagi)
B4.grid(row=2,column=3)

answer=Label(my_app, text='Hasil')
answer.grid(row=3,column=0,columnspan=2)
hasil=Label(my_app, text='0')
hasil.grid(row=3,column=2,columnspan=2)

my_app.mainloop()

#kegiatan 3
from Tkinter import Tk, Label, Entry, Button, StringVar, Canvas

my_app=Tk(className='Bangun Geometri Balok')

L1=Label(my_app,text='Panjang')
L1.grid(row=0,column=0)
str1=StringVar()
E1=Entry(my_app, textvariable=str1)
E1.grid(row=0,column=1,columnspan=3)
L2=Label(my_app, text='Lebar')
L2.grid(row=1, column=0)
str2=StringVar()
E2=Entry(my_app, textvariable=str2)
E2.grid(row=1,column=1,columnspan=3)
L3=Label(my_app, text='Tinggi')
L3.grid(row=2, column=0)
str3=StringVar()
E3=Entry(my_app, textvariable=str3)
E3.grid(row=2,column=1,columnspan=3)


def luas():
         x=float(str1.get())
         y=float(str2.get())
         z=float(str3.get())
         t=2*(x*y+y*z+z*x)
         L.config(text=t)

B=Button(my_app,text='Hitung Luas',command=luas)
B.grid(row=3,column=0)
L4=Label(my_app, text='Luas=')
L4.grid(row=3,column=1)
L=Label(my_app, text='0')
L.grid(row=3,column=2)

my_app.mainloop()

