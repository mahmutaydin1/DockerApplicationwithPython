from Tkinter import *
from paramiko import *
from Tkinter import Listbox
import paramiko


sunucularhostname=[]
sunucularIP=[]
pencere=Tk()
pencere.title("Server Automation")
pencere.geometry("300x400")

header=Label(pencere,text="MANAGE YOUR SERVERS",font=("Open Sans",15,"bold"), fg="steelblue").place(x=10,y=20)

host=Label(pencere,text="Host IP:").place(x=10,y=50)
hostusername=Label(pencere,text="Username:").place(x=10,y=70)
hostpasswd=Label(pencere,text="Password:").place(x=10,y=90)

IP=StringVar()
Kullaniciadi=StringVar()
Pass=StringVar()
host_entry=Entry(pencere,textvariable=IP).place(x=100,y=50)
kullaniciadi_entry=Entry(pencere,textvariable=Kullaniciadi).place(x=100,y=70)
pass_entry=Entry(pencere,textvariable=Pass,show="*").place(x=100,y=90)

toplamsunucu=StringVar()

def SSH(*args):
    global y
    PORT=22
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(IP.get(), PORT, Kullaniciadi.get(),Pass.get())
    stdin,stdout,stderr=client.exec_command("hostname")
    output=stdout.readlines()
    sunucularhostname.append(output[0])

    if len(sunucularIP)==0:

        sunucularIP.append(IP.get())
    elif len(sunucularIP)!=0:
            if IP.get() in sunucularIP:
                pass
            else:
                sunucularIP.append(IP.get())


    print sunucularIP

    toplamsunucu.set(len(sunucularIP))



    #client.close()

toplam = Label(pencere, text="Total Servers:")
toplamsunucu.set(len(sunucularIP))
toplam.place(x=10, y=150)
sonuc=Label(pencere,textvariable=toplamsunucu)
sonuc.place(x=90,y=150)


connect=Button(pencere,text="Connect",command=SSH).place(x=130,y=120)




def foo():
    print "nice"


my_menu=Menu(pencere,tearoff=0)
pencere.config(menu=my_menu)

devices_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Devices',menu=devices_menu)
devices_menu.add_command(label="IPlist",command=foo)
devices_menu.add_separator()
devices_menu.add_command(label="Hostnamelist",command=foo)
edit_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Edit",menu=edit_menu)

pencere.bind('<Return>', SSH)



pencere.mainloop()

