
import tkinter as tk
from tkinter import *
import socket
import webbrowser

def helloWorld():
    print('helloWorld')
def findIP():
    print(socket.gethostbyname(socket.gethostname()))
def getIp():
    print('##')
## Create Buttons
def createBtnQuit(name1):
    root = tk.Tk()
    root.geometry('500x700')
    btn = tk.Button(root, text = name1, bd = '5', command = root.destroy)
    btn.pack(side = 'top')
    root.mainloop()
def createBtnFunc(cancel, Func):
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    btn = tk.Button(frame, text=cancel, fg="red",command=root.quit)
    btn.pack(side=tk.LEFT)
    slogan = tk.Button(frame,text=Func,command=helloWorld)
    slogan.pack(side=tk.RIGHT)
    root.mainloop()
def createBtnIp(mine, other):
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    slogan = tk.Button(frame,text=mine,command=findIP)
    slogan.pack(side=tk.LEFT)
    btn = tk.Button(frame, text=other, fg="red",command=getIp)
    btn.pack(side=tk.RIGHT)
    root.mainloop()
#createBtnQuit('Cancel ##')
#createBtnFunc('Quit', 'helloWorld')
#createBtnIp('myIp', 'otherIp')

## Create Webpage opener
def openWebpage(src):
    return webbrowser.open(str(src))
def openWebpageHttp(src):
    return webbrowser.open(('https://'+str(src)))
def openWebpageWWW(src):
    return webbrowser.open('https://www.'+str(src))
def openWebpages(pages, pages1, pages2):
    for src in pages:
        openWebpageHttp(src)
    for src in pages1:
        openWebpageWWW(src)
    for src in pages2:
        openWebpage(src)

intro = [
    'github.com/Laufer4u?tab=repositories',
    'drive.google.com/drive/my-drive',
    'mail.uoc.gr/imp/dynamic.php?page=mailbox#mbox:SU5CT1g',
    'mail.google.com/mail/u/0/#inbox']
second = [
    'google.com',
    'youtube.com',
    'facebook.com',
    'w3schools.com/js/default.asp',
    'w3schools.com/python/default.asp']
third = []
openWebpages(intro, second, third)

