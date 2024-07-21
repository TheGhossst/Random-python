import tkinter as tk
import random
import string

# Functions for printing upper and lower halves
def printUpperHalf(str):
    first = 0
    second = 0
    pos = 0
    output = ""

    for i in range(1, 5):
        first = str[pos]
        second = str[pos + 1]
        pos += 2

        output += " " * (4 - i) + first + "--" * (i - 1) + second + "\n"

    return output

def printLowerHalf(str):
    first = 0
    second = 0
    pos = 0
    output = ""

    for i in range(1, 5):
        first = str[pos]
        second = str[pos + 1]
        pos += 2

        output += " " * (i - 1) + first + "--" * (4 - i) + second + "\n"

    return output

# Function to print 'n' parts of DNA
def printDNA():
    output = ""
    n = 10  # Number of lobes hardcoded to 10
    for i in range(n):
        x = i % 6
        dna_str = ''.join(random.choices("1", k=8))

        if x % 2 == 0:
            output += printUpperHalf(dna_str)
        else:
            output += printLowerHalf(dna_str)

    return output

# Tkinter GUI
root = tk.Tk()
root.title("DNA Pattern")

# Text area for output``````````````````````````
output_text = tk.Text(root, height=20, width=40)
output_text.pack()

# Function to handle the printing
def print_dna():
    result = printDNA()
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Button to trigger printing
print_button = tk.Button(root, text="Print DNA Pattern", command=print_dna)
print_button.pack()

root.mainloop()