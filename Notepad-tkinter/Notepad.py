import os.path
from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename


if __name__ == '__main__':
    root=Tk()
    root.geometry("600x500")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("4.ico")

    #For text area of the Notepad
    textarea=Text(root,font="Roboto 13",padx=5,pady=5)
    file = None

    textarea.pack(fill=BOTH,expand=True)


    def newfile():
        global file
        root.title("Untitled-Notepad")
        file=None
        textarea.delete(1.0,END)

    def openfile():
        global file
        file= askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file= None
        else:
            root.title(os.path.basename(file)+ "-Notepad")
            textarea.delete(1.0,END)
            f=open(file,"r")
            textarea.insert(1.0,f.read())
            f.close()

    def savefile():
        global file
        if file==None:
            file= asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),
                                                            ("Text Documents","*.txt")])
            if file=="":
                file=None

            else:
                f=open(file,"w")
                f.write(textarea.get(1.0,END))
                f.close()

                root.title(os.path.basename(file) + "- Notepad")

        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

    def exitfile():
        root.destroy()

    def cut():
        textarea.event_generate(("<<Cut>>"))

    def copy():
        textarea.event_generate(("<<Copy>>"))

    def paste():
        textarea.event_generate(("<<Paste>>"))

    def about():
        msg.showinfo("Information","Notepad by Akshay Chaudhary")

    #For menu and menubar
    menubar=Menu(root)
    filemenu=Menu(menubar,tearoff=0)

    #To open different file
    filemenu.add_command(label="New",command=newfile)
    filemenu.add_command(label="Open",command=openfile)
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exitfile)
    menubar.add_cascade(label="File",menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit",menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    #For scrollbar
    scroll= Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)


    root.mainloop()




