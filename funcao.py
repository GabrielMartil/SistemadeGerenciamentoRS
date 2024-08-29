import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk


def Gerador_arquivo():
    gerador = tk.Toplevel()
    gerador.title('CADASTRO DE CONTA')
    gerador.geometry("600x305")
    gerador.configure(bg = '#BEBEBE')
    gerador.iconbitmap('imagens/logodajanela.ico')



    img = tk.PhotoImage(file="imagens/logo2cadastro.png")
    imgaa = tk.Label(gerador, image=img)
    imgaa.grid(row=1,column=0,padx = 0, pady= 0, sticky='nswe', columnspan = 6, rowspan=30)

    label_nome1 = tk.Label(gerador, text="DATA INICIAL").place(x=296, y=75)
    entry_nome1 = tk.Entry(gerador)
    entry_nome1.place(x=270, y=100)

    label_cpf1 = tk.Label(gerador, text="DATA FINAL").place(x=296, y=135)
    entry_cpf1 = tk.Entry(gerador)
    entry_cpf1.place(x=270, y=160)


    bto_excel= Button(gerador)
    botaoimg_1 = tk.PhotoImage(file="imagens/excellogo.png")
    bto_excel.config(image=botaoimg_1)
    bto_excel.imagem = botaoimg_1
    bto_excel.place(x=20, y=240)

    bto_pdf= Button(gerador)
    botaoimg_2 = tk.PhotoImage(file="imagens/pdflogo.png")
    bto_pdf.config(image=botaoimg_2)
    bto_pdf.imagem = botaoimg_2
    bto_pdf.place(x=20, y=180)

    gerador.mainloop()





