import psutil
from tkinter import *
#Function to get CPU information.
def cpuInfo():
    win = Tk()
    win.title("System Information")
    win.configure(background='#00ffbf')
    win.maxsize(width=900,height=400)
    win.minsize(width=900,height=400)
    psutil.cpu_count(logical=True)
    Physical_Core_Count = psutil.cpu_count(logical=False)

    #Getting the CPU Frequencies.
    fre=psutil.cpu_freq()
    Maximum_Frequency = fre.max #"Mhz"
    Minimum_Frequency = fre.min #"Mhz"
    Current_Frequency = fre.current #"Mhz"

    #cpu stats
    cpu_stats = psutil.cpu_stats()
    ctx_switches = cpu_stats.ctx_switches
    interrupts = cpu_stats.interrupts
    soft_interrupts = cpu_stats.soft_interrupts
    syscalls = cpu_stats.syscalls

    #Getting the CPU Usage.
    core = []
    for x, percentage_usage in enumerate(psutil.cpu_percent(percpu=True)):
        core.append(percentage_usage)
    Total_CPU_Usage = psutil.cpu_percent()

    lavel1 = Label(win,text="Frequency Information",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=150,y=20)

    lavel1 = Label(win,text="Maximum Frequency",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=60)
    lavel1 = Label(win,text=f'{Maximum_Frequency}Mhz',bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=60)


    lavel1 = Label(win,text="Minimum Frequency",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=90)
    lavel1 = Label(win,text=f'{Minimum_Frequency}Mhz',bg='#ffbf00',font=("Arial",12),padx=15)
    lavel1.place(x=400,y=90)


    
    lavel1 = Label(win,text="Current Frequency",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=120)
    lavel1 = Label(win,text=f'{Current_Frequency}Mhz',bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=120)

    lavel1 = Label(win,text="CPU",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=150,y=160)

    lavel1 = Label(win,text="CTX Switches",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=200)
    lavel1 = Label(win,text=ctx_switches,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=200)

    lavel1 = Label(win,text="Interrupts",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=230)
    lavel1 = Label(win,text=interrupts,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=230)

    lavel1 = Label(win,text="Soft Interrupts",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=260)
    lavel1 = Label(win,text=soft_interrupts,bg='#ffbf00',font=("Arial",12),padx=37)
    lavel1.place(x=400,y=260)

    lavel1 = Label(win,text="Syscalls",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=290)
    lavel1 = Label(win,text=syscalls,bg='#ffbf00',font=("Arial",12))
    lavel1.place(x=400,y=290)

    lavel1 = Label(win,text="CPU core Information",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=620,y=20)

    y_axis = 60
    for i in range(1,len(core)+1):
        lavel1 = Label(win,text=f'CORE{i}',bg='#00ffbf',font=("Arial",12))
        lavel1.place(x=650,y=y_axis)
        lavel1 = Label(win,text=f'{core[i-1]}%',bg='#ffbf00',font=("Arial",12))
        lavel1.place(x=750,y=y_axis)
        y_axis = y_axis+30