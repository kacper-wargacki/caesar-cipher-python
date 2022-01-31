from tkinter import *
from tkinter import ttk

import cipher
import probability
import test


def main():
    test.checkEncryption()
    program = Tk()
    program.title('Szyfr Cezara')
    program.resizable(True, True)
    frame = ttk.Frame(program)
    program.geometry('700x500')
    ttk.Label(frame, text='Szyfr Cezara', style='Header.TLabel').grid(row=0, column=1)
    ttk.Label(frame, text='Podaj liczbę:', style='Header.TLabel').grid(row=1, column=0)
    ttk.Label(frame, text='Tekst:', style='Header.TLabel').grid(row=2, column=0)
    ttk.Label(frame, text='Wynik:', style='Header.TLabel').grid(row=3, column=0)
    ttk.Label(frame, text='Możliwe kombinacje:', style='Header.TLabel').grid(row=5, column=0)

    def encrypt():
        outputText.delete(0, END)
        outputText.insert(0, "")
        text = str(inputText.get())
        s = int(menu.get())
        encrypted_text = cipher.encrypt(text, s)
        result_text.set(encrypted_text)

    def decrypt():
        outputText.delete(0, END)
        outputText.insert(0, "")
        result_text.set('')
        decryptTextFrame.delete('1.0', END)
        text = str(inputText.get())
        decipheredText = cipher.decrypt(text)
        prob = probability.checkProbability(decipheredText)
        for text in decipheredText:
            decryptTextFrame.insert(END, text + '\n')
        decryptTextFrame.insert(END, f'Prawdopodobieństwo wynosi {round((prob / 26) * 100, 2)}% albo {prob}/26')

    result_text = StringVar()
    outputText = ttk.Entry(frame, width=100, textvariable=result_text, state='readonly')
    outputText.grid(row=3, column=1)

    menu = StringVar()
    Spinbox(frame, from_=1, to=999, textvariable=menu).grid(row=1, column=1)

    inputText = ttk.Entry(frame, width=100)
    inputText.grid(row=2, column=1)

    decryptTextFrame = Text(frame, wrap='none', height=20)
    decryptTextFrame.grid(row=5, column=1)
    decryptTextFrame.bind("<Key>", lambda e: 'break')
    vsb = ttk.Scrollbar(frame, command=decryptTextFrame.yview, orient="vertical")
    decryptTextFrame.configure(yscrollcommand=vsb.set)
    frame.grid_rowconfigure(5, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    vsb.grid(row=5, column=2, sticky="ns")
    decryptTextFrame.grid(row=5, column=1, sticky="nsew")

    ttk.Button(frame, width=10, text='Zaszyfruj', command=lambda: encrypt()).grid(row=4, column=1)
    ttk.Button(frame, width=10, text='Odszyfruj', command=lambda: decrypt()).grid(row=6, column=1)

    frame.pack()
    program.mainloop()


main()
