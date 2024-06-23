from tkinter import *


def function_button() -> None:
    val = input.get()
    label["text"] = val
    print("CLICKED")
    
def function_input() -> None:
    print("CIAOO")
    
    
window = Tk()
window.title("Hello")
window.minsize(500,300)
label = Label(master=window,text="Test LABEL")
label.pack()
label["text"] = "NEW"
button = Button(master=window,text = "HELLO",command= function_button)
button.pack()

input = Entry(width=50)
input.pack()


window.mainloop()









