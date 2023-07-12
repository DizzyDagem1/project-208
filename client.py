#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
name = None 
listbox = None
textarea = None 
labelchat = None 
text_message = None 
filePathlabel = None

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
def connectToServer():
    global SERVER 
    global name 
    global sending_file 
    cname = name.get()
    SERVER.send(cname.encode())
    

def openmusicWindow():
    print("\n\t\t\t\t\t\tMusic Window")
    musicWindow = Tk()
    musicWindow.title("Music Window")
    musicWindow.geometry("600x500")
    global name 
    global listbox
    global textarea 
    global labelchat 
    global text_message
    global filePathLabel 
    musicLabel = Label(musicWindow,text="Choose your song:-",font=("Calibri",10))
    musicLabel.place(x=10,y=8)
    #name = Entry(musicWindow,width=30,font=("Calibri",10))
    #name.place(x=120,y=8)
    #name.focus()
    #connectServer = Button(musicWindow,text="Start Chatting",bd=1,font=("Calibri",10),command=connectToServer)
    #connectServer.place(x=350,y=6)
    #separator = ttk.Separator(musicWindow,orient="horizontal")
    #separator.place(x=0,y=35,relwidth=1,relheight=1)
    #labelusers = Label(musicWindow,text="Active Users",font=("Calibri",10))
    #labelusers.place(x=10,y=50)
    listbox = Listbox(musicWindow,height=5,width=67,activestyle="dotbox",font=("Calibri",10))
    listbox.place(x=10,y=70)
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview())
    playButton = Button(musicWindow,text="Play the Song",bd=1,font=("Calibri",10))
    playButton.place(x=282,y=160)
    stopButton = Button(musicWindow,text="Stop the Song",bd=1,font=("Calibri",10))
    stopButton.place(x=350,y=360)
    download = Button(musicWindow,text="Download the song",bd=1,font=("Calibri",10))
    download.place(x=435,y=160)
    labelchat = Label(musicWindow,text="",fg="blue",font=("Calibri",10))
    labelchat.place(x=10,y=180)
    #scrollbar2 = Scrollbar(textarea)
    #scrollbar2.place(relheight=1,relx=1)
    #scrollbar2.config(command=listbox.yview())
    attach = Button(musicWindow,text="Upload and Send",bd=1,font=("Calibri",10))
    attach.place(x=10,y=305)
    #text_message = Entry(musicWindow,width=43,font=("Calibri",12))
    #text_message.pack()
    #text_message.place(x=98,y=306)
    #send = Button(musicWindow,text="Send Message",bd=1,font=("Calibri",10))
    #send.place(x=450,y=305)
    #filePathlabel = Label(musicWindow,text="",fg="blue",font=("Calibri",10))
    #filePathlabel.place(x=10,y=330)
    musicWindow.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    openmusicWindow()

setup()


#-----------Bolierplate Code Start -----