import tkinter as tk

from tkinter import *

window = tk.Tk()
window.geometry('400x600')
window.configure(bg = 'grey')

label = tk.Label(text = "Enter Line(s) to scan")
entry = tk.Text(height = 10, width = 40)
output = tk.Text(height = 10, width = 40)
label.pack(expand = True)
entry.pack(expand = False)

entry.insert(END, 'Enter lines to scan or macronize')

output.pack(expand = True)
output.insert(END, 'Scanned lines will show up here')

def scanoutput():
    import NewScanner as sc
    input = entry.get("1.0", "end-1c")
    outputtxt = ''.join(sc.reformat(sc.scanshort(sc.scanlong(sc.exception(sc.deletespaces(sc.elision(input)))))))
    output.delete('1.0',END)
    output.insert(END, outputtxt)
    output.insert(END, '\n Legend: +- = long, + = short')

def scanoutput2():
    from files import Dactylic as mn
    input = entry.get("1.0", 'end-1c')
    scanned = mn.syllabilize(input)
    output.delete('1.0', END)
    output.insert(END, scanned)
    output.insert(END,  '\n  Legend: - is long, + is short')

def macronize():
    from files import Macronizer as mac
    input = entry.get("1.0", 'end-1c')
    scanned = mac.macronize(input)
    output.delete('1.0', END)
    output.insert(END, scanned)


def textsave():
    pass


macronizebtn = tk.Button( text = "Macronize Line",  command = macronize).pack(expand = True)
scanbtn = tk.Button(text = "Scan Line in Dactylic Hexameter", command = scanoutput2).pack(expand = True)
addtxtbtn = tk.Button(text = "Save Line(s)", command = textsave).pack(expand = True)

window.mainloop()
