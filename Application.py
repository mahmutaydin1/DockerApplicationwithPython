from Tkinter import *
from paramiko import *
from Tkinter import Listbox
import paramiko


sunucularIP=[]
sunucularhostname=[]

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




def SSH(*args):
    PORT=22
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(IP.get(), PORT, Kullaniciadi.get(),Pass.get())
    stdin,stdout,stderr=client.exec_command("hostname")
    output=stdout.readlines()
    print '\n'.join(output)
    #print output[0]
    sunucularIP.append(IP.get())
    sunucularhostname.append(output[0])
    print sunucularIP
    print sunucularhostname
    w = Listbox(pencere, cursor="")
    w.place(x=100, y=200)

    for i in sunucularIP:
        w.insert(END,i)


    #client.close()


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