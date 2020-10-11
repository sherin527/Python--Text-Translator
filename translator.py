from googletrans import Translator
from tkinter import *
root = Tk(className='Python Translator')
root.geometry('600x600')
root.configure(bg='light blue')

#variables

#option variable
optvar = StringVar()
text =StringVar()
OptionList = [
    'choose language',
    'hi',
    'af',
    'sq',
    'am',
    'ar',
    'hy',
    'az',
    'eu',
    'be',
    'bn',
    'bs',
    'ca',
    'ceb',
    'zh-cn',
    'zh-tw',
    'co',
    'en',
    'hr',
    'cs',
    'da',
    'nl',
    'en',
    'eo',
    'et',
    'tl',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'iw',
    'hi',
    'hmn',
    'hu',

]
optvar.set(OptionList[0])

adlbl = Label(root, text='ENTER YOUR TEXT HERE', font=('Times New Roman', 15), fg='purple')
adlbl.grid(row=0, column=0, sticky='n')

#get text from user
entr = Entry(font=('Times New Roman', 23), fg='red', width=40, textvariable=text)
entr.grid(row=1, column=0, sticky='n', pady=13)

lbl1 = Label(root, text=f'Choose The Language  To Translate ?', font=('Times New Roman', 15), fg='gray10')
lbl1.grid(row=2, column=0, sticky='n')

#option list
opt = OptionMenu(root, optvar, *OptionList)
opt.grid(row=3, column=0, pady=7)

def trans():
    ttext = text.get()
    optval = optvar.get()
    transolator = Translator()
    det = transolator.detect(ttext)
    #display detected language
    detlbl = Label(root, text=f'Detected Language Is : {det.lang}', font=('Times New Roman', 15), fg='gray20')
    detlbl.grid(row=5, column=0, sticky='n')

    #translate language
    translated = transolator.translate(ttext, dest=optval)
    print(translated)

    #display the translated text
    t = Text(root, height=20, width=70)
    t.grid(row=6, column=0, sticky='n')
    tr = translated.text
    t.insert(INSERT, tr)
    
#button
btn = Button(text='TRANSLATE', font=('Times New Roman', 20), fg='blue', command=trans)
btn.grid(row=4, column=0, sticky='n', pady=7)


root.mainloop()
