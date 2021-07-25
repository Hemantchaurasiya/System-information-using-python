import platform,socket,psutil,re,uuid
from tkinter import *
def info():
    win = Tk()
    win.title("System Information")
    win.configure(background='#00ffbf')
    win.maxsize(width=900,height=400)
    win.minsize(width=900,height=400)

    uname = platform.uname()
    system = uname.system
    node = uname.node
    release = uname.release
    version = uname.version
    machine = uname.machine
    arch = platform.architecture()
    processor = uname.processor
    ip_address = socket.gethostbyname(socket.gethostname()) 
    mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"

    lavel1 = Label(win,text="SYSTEM INFORMATION ",bg='#00ff80',font=("Arial",15))
    lavel1.place(x=250,y=20)


    lavel1 = Label(win,text="OS Name",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=60)
    lavel1 = Label(win,text=""+system,bg='#ffbf00',font=("Arial",12),padx=200)
    lavel1.place(x=400,y=60)


    lavel1 = Label(win,text="Node",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=90)
    lavel1 = Label(win,text=node,bg='#ffbf00',font=("Arial",12),padx=157)
    lavel1.place(x=400,y=90)


    
    lavel1 = Label(win,text="Release",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=120)
    lavel1 = Label(win,text=release,bg='#ffbf00',font=("Arial",12),padx=225)
    lavel1.place(x=400,y=120)

    
    lavel1 = Label(win,text="Version",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=150)
    lavel1 = Label(win,text=version,bg='#ffbf00',font=("Arial",12),padx=194)
    lavel1.place(x=400,y=150)

    

    lavel1 = Label(win,text="Machine",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=180)
    lavel1 = Label(win,text=machine,bg='#ffbf00',font=("Arial",12),padx=207)
    lavel1.place(x=400,y=180)


    lavel1 = Label(win,text="Architecture",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=210)
    lavel1 = Label(win,text=arch,bg='#ffbf00',font=("Arial",12),padx=172)
    lavel1.place(x=400,y=210)

    
    lavel1 = Label(win,text="Processor",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=240)
    lavel1 = Label(win,text=processor,bg='#ffbf00',font=("Arial",12),padx=51)
    lavel1.place(x=400,y=240)

    
    lavel1 = Label(win,text="IP Address",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=270)
    lavel1 = Label(win,text=ip_address,bg='#ffbf00',font=("Arial",12),padx=175)
    lavel1.place(x=400,y=270)

    
    lavel1 = Label(win,text="Mac Address",bg='#00ffbf',font=("Arial",12))
    lavel1.place(x=150,y=300)
    lavel1 = Label(win,text=mac_address,bg='#ffbf00',font=("Arial",12),padx=175)
    lavel1.place(x=400,y=300)

    win.mainloop()
