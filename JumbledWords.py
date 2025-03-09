import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]

num=random.randrange(0,len(words),1)



def reset():
    global answers,words,num
    num=random.randrange(0,len(words),1)
    mylbl.config(text=words[num])
    e.delete(0,END)

def default():
    global answers, words, num
    mylbl.config(text=words[num])
    
    

def Checkans():
    global answers,words,num
    var=e.get()
    if var.lower==answers[num]:
        messagebox.showinfo("yes","this is correct answer")
        reset()
    else:
        messagebox.showinfo("no"," this is wrong answer")
        e.delete(0,END)




root=Tk()
root.geometry("500x400+200+200")
root.title("JUmble words")
root.config(bg="black")


mylbl=Label(
    root,
    font=("Helvetica",20),
    text="your text here",
    bg="black",
    fg="white",
)
mylbl.pack(pady=40)


ans1=StringVar()
e=Entry(
    root,
    font=("Helvetica",18),
    textvariable=ans1
)
e.pack()


Checkbtn=Button(
    root,
    text="Check",
    font=("Times",12),
    width=10,
    command=Checkans,
            
)
Checkbtn.pack(pady=30)

Resetbtn=Button(
    root,
    text="Reset",
    font=("Times",12),
    width=10,
    command=reset        
)
Resetbtn.pack()

exitbtn=Button(
    root,
    text="EXit",
    font=("Times",12),
    command=root.quit
)
exitbtn.pack(pady=30)

default()

root.mainloop()