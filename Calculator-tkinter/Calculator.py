import math
from tkinter import *
import tkinter.messagebox as msg


class calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator by Akshay")
        self.geometry("400x600")
        self.wm_iconbitmap("calculator.ico")
        self.config(background="yellow")

        def click(event):
            text = event.widget.cget("text")

            if text == '=':
                if strvar.get().isdigit():
                    value= int(strvar.get())

                else:
                    try:
                        value = eval(screen.get())

                    except Exception as e:
                        value="Error"

                strvar.set(value)
                screen.update()

            elif text == 'C':
                strvar.set("")
                screen.update()

            elif text == "%":
                if strvar.get().isdigit():
                    value=int(strvar.get())/100
                    strvar.set(value)
                    screen.update()


            elif text=="log":
                if strvar.get().isdigit():
                    value=int(strvar.get())
                    strvar.set(math.log(value,10))
                    screen.update()

            elif text=="\u221A":
                if strvar.get().isdigit():
                    value=int(strvar.get())
                    strvar.set(math.sqrt(value))
                    screen.update()

            elif text=="ln":
                if strvar.get().isdigit():
                    value=int(strvar.get())
                    strvar.set(math.log(value))
                    screen.update()

            elif text=="<<":
                value= strvar.get()[:-1]
                strvar.set(value)
                screen.update()

            elif text=="+/-":
                if strvar.get()=='':
                    strvar.set("")
                    screen.update()
                else:
                    screen.insert(0,'-')

            else:
                strvar.set(strvar.get() + text)
                screen.update()

        #For display of the calculator
        strvar=StringVar()
        strvar.set("")
        screen=Entry(self,textvariable=strvar,font="Lato 25",bg="black",fg="white",justify=RIGHT)
        screen.pack(fill=BOTH,pady=15,padx=20,ipady=20)

        #Frame for each bottoms
        #For first row, second row and third row
        self.button1=[['7','8','9','/'],
                ['4','5','6','*'],
                ['1','2','3','-']]

        for row in self.button1:
            self.f0 = Frame(self,bg="yellow")
            self.f0.pack()
            for btn in row:
                b = Button(self.f0, text=f"{btn}", font="Lato 19", bg="black", fg="white", padx=19,pady=10)
                b.pack(side=LEFT, padx=5,pady=5)
                b.bind("<Button-1>", click)

        #For fourth row
        #['C','0','.','+']

        self.f0=Frame(self,bg="yellow")
        b=Button(self.f0,text="C",font="Lato 19",bg="black",fg="white", padx=19,pady=10)
        b.pack(side=LEFT, padx=8,pady=5)
        b.bind("<Button-1>",click)

        b=Button(self.f0,text="0",font="Lato 19",bg="black",fg="white", padx=19,pady=10)
        b.pack(side=LEFT, padx=3,pady=5)
        b.bind("<Button-1>", click)

        b=Button(self.f0,text=".",font="Lato 19",bg="black",fg="white", padx=20,pady=10)
        b.pack(side=LEFT, padx=5,pady=5)
        b.bind("<Button-1>", click)

        b=Button(self.f0,text="+",font="Lato 19",bg="black",fg="white", padx=18,pady=10)
        b.pack(side=LEFT, padx=6,pady=5)
        b.bind("<Button-1>", click)

        self.f0.pack()

        #for fifth row

        self.f0 = Frame(self, bg="yellow")
        b = Button(self.f0, text="log", font="Lato 19", bg="black", fg="white", padx=10, pady=10)
        b.pack(side=LEFT, padx=8, pady=5)
        b.bind("<Button-1>", click)

        b = Button(self.f0, text="ln", font="Lato 19", bg="black", fg="white", padx=16, pady=10)
        b.pack(side=LEFT, padx=3, pady=5)
        b.bind("<Button-1>", click)

        b = Button(self.f0, text="%", font="Lato 19", bg="black", fg="white", padx=14, pady=10)
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

        b = Button(self.f0, text="\u221A", font="Lato 19", bg="black", fg="white", padx=17, pady=10)
        b.pack(side=LEFT, padx=6, pady=5)
        b.bind("<Button-1>", click)

        self.f0.pack()


        # For last row
        # ['<<', '+/-', 'x**', '=']

        self.f0 = Frame(self,bg="yellow")
        b = Button(self.f0,text='<<',bg="black", fg="white", font="Lato 19", padx=12,pady=10)
        b.pack(side=LEFT, padx=5,pady=5)
        b.bind("<Button-1>", click)

        b = Button(self.f0, text="+/-", font="Lato 19", bg="black", fg="white", padx=10,pady=10)
        b.pack(side=LEFT, padx=5,pady=5)
        b.bind("<Button-1>", click)

        b = Button(self.f0, text="**", font="Lato 19", bg="black", fg="white", padx=16,pady=10)
        b.pack(side=LEFT, padx=5,pady=5)
        b.bind("<Button-1>", click)

        b = Button(self.f0, text="=", font="Lato 19", bg="black", fg="white", padx=19,pady=10)
        b.pack(side=LEFT, padx=4,pady=5)
        b.bind("<Button-1>", click)

        self.f0.pack()

        def close():
            message=msg.askokcancel("Message","Exit the Calculator?")
            if message:
                self.destroy()
            else:
                msg.showinfo("Information","Keep enjoying with the Calculation")

        def mhelp():
            msg.showinfo("Information","Calculator by Akshay Chaudhary")

        #For menu
        mymenu=Menu(self)
        m= Menu(mymenu,tearoff=0)
        m.add_command(label="Exit",command=close)
        mymenu.add_cascade(label="Exit",menu=m)

        h=Menu(mymenu,tearoff=0)
        h.add_command(label="Help",command=mhelp)
        mymenu.add_cascade(label="Help",menu=h)

        self.config(menu=mymenu)



if __name__ == '__main__':
    window=calculator()

    window.mainloop()