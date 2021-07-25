import psutil
from tkinter import *
import shutil
def size(byte):
  #this the function to convert bytes into more suitable reading format.
  #Suffixes for the size
  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024

def memInfo():
    win = Tk()
    win.title("System Information")
    win.configure(background='#00ffbf')
    win.maxsize(width=900,height=400)
    win.minsize(width=900,height=400)
    
    mem = psutil.virtual_memory()
    total_momory = size(mem.total)
    available_momory = size(mem.free)
    used_momory = size(mem.used)
    Percentage = mem.percent

    #Getting the Swap Memory Data.
    sw_mem = psutil.swap_memory()
    sw_total_momory = size(sw_mem.total)
    sw_available_momory = size(sw_mem.free)
    sw_used_momory = size(sw_mem.used)
    sw_Percentage = sw_mem.percent

    c = shutil.disk_usage('C:')
    c_total = size(c.total)
    c_used = size(c.used)
    c_free = size(c.free)
    

    lavel1 = Label(win,text="RAM Information:",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=100,y=20)

    lavel1 = Label(win,text="Total RAM :",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=100,y=60)
    lavel1 = Label(win,text=total_momory,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=210,y=60)


    lavel1 = Label(win,text="Used RAM : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=100,y=90)
    lavel1 = Label(win,text=used_momory,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=210,y=90)


    
    lavel1 = Label(win,text="Free RAM : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=100,y=120)
    lavel1 = Label(win,text=available_momory,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=210,y=120)

    
    lavel1 = Label(win,text="Used RAM : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=100,y=150)
    lavel1 = Label(win,text=f'{Percentage}%',bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=210,y=150)

    lavel1 = Label(win,text="Total RAM :",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=450,y=20)

    lavel1 = Label(win,text="Total Swaped Memory : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=450,y=60)
    lavel1 = Label(win,text=sw_total_momory,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=700,y=60)


    lavel1 = Label(win,text="Used Swaped Memory : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=450,y=90)
    lavel1 = Label(win,text=sw_used_momory,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=700,y=90)

    
    lavel1 = Label(win,text="Free Swaped Memory : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=450,y=120)
    lavel1 = Label(win,text=sw_available_momory,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=700,y=120)

    
    lavel1 = Label(win,text="Used Swaped Memory : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=450,y=150)
    lavel1 = Label(win,text=f'{sw_Percentage}%',bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=700,y=150)

    lavel1 = Label(win,text="C Drive Size :",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=100,y=190)

    lavel1 = Label(win,text="Total Disk Memory : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=100,y=230)
    lavel1 = Label(win,text=c_total,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=300,y=230)

    lavel1 = Label(win,text="Used Disk Memory : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=100,y=260)
    lavel1 = Label(win,text=c_used,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=300,y=260)

    lavel1 = Label(win,text="Free Disk Memory : ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=100,y=290)
    lavel1 = Label(win,text=c_free,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=300,y=290)
    win.mainloop()