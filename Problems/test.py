from tkinter import *

def check_result():
    input_value = input_box.get()
    if input_value == "1":
        result_label.config(text="You gey")
    elif input_value == "2":
        result_label.config(text="Rhon gey")
    else:
        result_label.config(text="Invalid input")

def clear():
    input_box.delete(0, END)
    result_label.config(text="")

window = Tk()
window.title("Your Mom")

window.geometry("480x320")

yd = Label(window, text = "Your Dad")
yd.pack()

input_box = Entry(window)
input_box.pack()

check_button = Button(window, text="Check", command=check_result)
check_button.pack()

clear_button = Button(window,text = "Clear", command = clear)
clear_button.pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()