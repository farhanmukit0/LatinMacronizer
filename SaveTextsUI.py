import pandas as pd
import tkinter as tk

from tkinter import *
import SecondaryUI

window2 = tk.Tk()
window2.configure(bg = 'grey')
window2.geometry('800x750')
#file = pd.read_csv('latintexts.csv')


texts = pd.DataFrame(list())

texts.insert(0, column='Text', value='')
texts.insert(1, column='Title',value='')
texts.insert(2, column='booknum', value='')
texts.insert(3, column='linenumst', value='')
texts.insert(4, column='linenumfi', value='')

showcase = tk.Text(window2, height = 10, width = 70)
showcasela = tk.Label(window2, text = 'Your Scanned/Macronized Text')
title = tk.Entry(window2,width = 20)
titlela = tk.Label(window2,text = 'Enter Title of the Latin Work')
booknum = tk.Entry(window2,width = 20)
booknumla = tk.Label(window2,text = 'Enter Book/Poem Number')
linenumst = tk.Entry(window2,width = 20)
linenumstla = tk.Label(window2,text = 'Enter Starting Line Number')
linenumfi = tk.Entry(window2,width = 20)
linenumfila = tk.Label(window2,text = 'Enter Final Line Number')

showcase.insert(END, SecondaryUI.output.get('1.0', 'end-1c'))

showcasela.pack(expand = True)
showcase.pack(expand = True)
titlela.pack(expand = True)
title.pack(expand = True)
booknumla.pack(expand = True)
booknum.pack(expand = True)
linenumstla.pack(expand = True)
linenumst.pack(expand = True)
linenumfila.pack(expand = True)
linenumfi.pack(expand = True)

def rowcounting():
    x = len(texts.index)-1
    x += 1
    return x

def insertxt():
    showcaseget = showcase.get('1.0',END)
    titleget = title.get()
    booknumget = booknum.get()
    linenumstget = linenumst.get()
    linenumfiget = linenumfi.get()
    rowcounter = rowcounting()
    texts.loc[rowcounter,'Text'] = showcaseget
    texts.loc[rowcounter, 'Title'] = titleget
    texts.loc[rowcounter, 'booknum'] = booknumget
    texts.loc[rowcounter, 'linenumst'] = linenumstget
    texts.loc[rowcounter, 'linenumfi'] = linenumfiget
    texts.to_csv('latintexts.csv')

def outputtxt():
    showcaseget = showcase.get('1.0', END)
    titleget = title.get()
    booknumget = booknum.get()
    linenumstget = linenumst.get()
    linenumfiget = linenumfi.get()
    rowcounter = rowcounting()
    for z in range(len(texts.index)-1):
        if texts['Title'][z] == titleget:
            if texts['booknum'][z] == booknumget:
                if texts['linenumst'][z] == linenumstget:
                    if texts['linenumfi'][z] == linenumfiget:
                        showcase.delete('1.0',END)
                        showcase.insert(END, texts['Text'][z])
        """else:
            showcase.delete('1.0', END)
            showcase.insert(END, 'Saved Entry Does Not Exist')"""

def showsaved():
    savedtexts.delete('1.0',END)
    for i in range(len(texts.index)):
        setdata = ['\n','TITLE:',texts['Title'][i],'BOOK#:',str(texts['booknum'][i]),'STARTING LINE:',str(texts['linenumst'][i]),'FINAL LINE:',str(texts['linenumfi'][i])]
        savedtexts.insert(END, ' '.join(setdata))

savebtn = tk.Button(window2, text='Save Lines', command= insertxt )
showbtn = tk.Button(window2, text='Show Text', command = outputtxt)
showsavesbtn = tk.Button(window2,text = 'Show List of Saved Texts',command = showsaved)
#changebtn = tk.Button(window2,text = 'change', command = savecsv())
savebtn.pack(expand = True)
showbtn.pack(expand = True)
showsavesbtn.pack(expand = True)
#changebtn.pack(expand = True)
savedtexts = tk.Text(window2,height = 10, width = 80)
savedtexts.pack(expand = True,pady = 20)
savedtexts.insert(END, 'Press Show Saves Button After Saving Texts')

window2.mainloop()

