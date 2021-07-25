import psutil
from tkinter import *
#battery
def bettery_Info():
    win = Tk()
    win.title("System Information")
    win.configure(background='#00ffbf')
    win.maxsize(width=900,height=400)
    win.minsize(width=900,height=400)

    battery = psutil.sensors_battery()
    percent = battery.percent
    power_plug = battery.power_plugged
    left_time = battery.secsleft
    

    lavel1 = Label(win,text="Battery Information ",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=250,y=20)

    lavel1 = Label(win,text="Battery ",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=60)
    lavel1 = Label(win,text=f'{percent}%',bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=60)


    lavel1 = Label(win,text="Power Plug",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=90)
    lavel1 = Label(win,text=f'{power_plug}',bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=90)


    lavel1 = Label(win,text="Battery Time Left",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=120)
    lavel1 = Label(win,text=f'{left_time} Sec.',bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=120)

    win.mainloop()
