from tkinter import * 

def frame(root,side):
    w = Frame(root)
    w.pack(side=side,expand=YES,fill=BOTH)
    return w

def button(root,side,text,command=None):
    btn = Button(root,text=text,command=command)
    btn.pack(side=side,expand=YES,fill=BOTH)
    return btn

def search(str,word):
    str = str.split(" ")
    found = False
    for i in str:
        if i== word:
            print(str.index(i))
            found = True
            break
    return str.index(i)

           

    

class seq(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        master.geometry("400x100")
        self.master.title("Sequential Search")

        
        display = StringVar()
        Entry(self,justify=CENTER,font="20",fg='green',width=40,relief=SUNKEN,textvariable=display).pack(expand=YES,fill=BOTH)

        word = StringVar()
        Entry(self,justify=CENTER,font="20",fg='green',width=40,relief=SUNKEN,textvariable=word).pack(expand=YES,fill=BOTH)

        result = StringVar()
        Label(self,font="20",fg='green',width=40,relief=SUNKEN,textvariable=result).pack(expand=YES,fill=BOTH)

        button(frame(self,TOP),RIGHT,"Submit",lambda w=word,d=display,r=result:r.set(search(d.get(),w.get())))
       


if __name__=="__main__":
    root= Tk()
    view = seq(root)
    view.pack()
    view.mainloop()