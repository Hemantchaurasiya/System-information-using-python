import system
import memory
import cpu
import battery

from tkinter import * 
from PIL import Image,ImageTk


win = Tk()
win.title("System Information")
win.configure(background='#00ffbf')
win.maxsize(width=900,height=400)
win.minsize(width=900,height=400)

def systemInfo():
    system.info()

def memoryInfo():
    memory.memInfo()

def CpuInfo():
    cpu.cpuInfo()

def BatteryInfo():
    battery.bettery_Info()


# img = Image.open(r"images\\background.jpg")
# img = img.resize((1530,790),Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(img)
# left_label = Label(win,image=photo)
# left_label.place(x=0,y=0,width=1530,height=790)

# system button
img1 = Image.open(r"images\\System.jpg")
img1 = img1.resize((500,250),Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(img1)
b1=Button(image=photo1,cursor="hand2",command=systemInfo)
b1.place(x=50,y=50,width=150,height=220)
b1_1=Button(text="System",cursor="hand2",command=systemInfo,font=("times new roman",15,"bold"),bg="LightGray",fg="black")
b1_1.place(x=50,y=250,width=150,height=40)

# system button
img2 = Image.open(r"images\\process.jpg")
img2 = img2.resize((500,250),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(img2)
b2=Button(image=photo2,cursor="hand2",command=CpuInfo)
b2.place(x=250,y=50,width=150,height=220)
b1_2=Button(text="Process",cursor="hand2",command=CpuInfo,font=("times new roman",15,"bold"),bg="LightGray",fg="black")
b1_2.place(x=250,y=250,width=150,height=40)

# memory button
img3 = Image.open(r"images\\memory.png")
img3 = img3.resize((500,250),Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(img3)
b3=Button(image=photo3,cursor="hand2",command=memoryInfo)
b3.place(x=450,y=50,width=150,height=220)
b1_3=Button(text="Memory",cursor="hand2",command=memoryInfo,font=("times new roman",15,"bold"),bg="LightGray",fg="black")
b1_3.place(x=450,y=250,width=150,height=40)


# battery button
img4 = Image.open(r"images\\battery.jpeg")
img4 = img4.resize((500,250),Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(img4)
b4=Button(image=photo4,cursor="hand2",command=BatteryInfo)
b4.place(x=650,y=50,width=150,height=220)
b1_4=Button(text="Battery",cursor="hand2",command=BatteryInfo,font=("times new roman",15,"bold"),bg="LightGray",fg="black")
b1_4.place(x=650,y=250,width=150,height=40)

win.mainloop()
