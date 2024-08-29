import customtkinter
import tkinter as tk
import tkinter
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
import lancamento



janela_login = customtkinter.CTk()
janela_login.geometry("600x305")
janela_login.iconbitmap('imagens\logoicoo.ico')
janela_login.title('LOGIN DE ACESSO')

usuario = "Gabriel Martins"
senha = "123456"

    
def open_lancamento():
    usuario1 = entry_usuario1.get()
    senha1 = entry_senha.get()
    if usuario == usuario1 and senha == senha1:
        janela_login.destroy()
        lancamento.openjanela()
        messagebox.showinfo(title="ERRO AO INSERIR", message="login efetuado com sucesso")
    else:
        messagebox.showinfo(title="ERRO AO INSERIR", message="Usuario/senha invalidos")
def submit():
    password=entry_senha.get()
    entry_senha.set("")
    
img = tk.PhotoImage(file="imagens/logo2cadastro.png")
imgaa = customtkinter.CTkLabel(master=janela_login, image=img)
imgaa.grid(row=0,column=0,padx = 0, pady= 0, sticky='nswe', columnspan = 7, rowspan=80)

label_usuario = customtkinter.CTkLabel(master=janela_login,text="USUÁRIO").grid(row=35,column=2,padx =0, pady= 0, sticky='nswe', columnspan = 1, rowspan=1)
entry_usuario1 = customtkinter.CTkEntry(master=janela_login, border_color='#030086')
entry_usuario1.grid(row=35,column=3,padx = 0, pady= 0, sticky='nswe', columnspan = 1)

label_senha = customtkinter.CTkLabel(master=janela_login,text="SENHA").grid(row=41,column=2,padx = 0, pady= 0, sticky='nswe', columnspan = 1)
entry_senha = customtkinter.CTkEntry(master=janela_login, border_color='#030086', show='*')
entry_senha.grid(row=41,column=3,padx = 0, pady= 0, sticky='nswe', columnspan = 1)

bto_gerar2 =ImageTk.PhotoImage(Image.open("imagens/button_nm/Apontar2.png"))
botao_de_login =customtkinter.CTkButton(master=janela_login, text="",image=bto_gerar2, command=open_lancamento)
botao_de_login.configure(image=bto_gerar2)
botao_de_login.grid(row=60,column=3,padx = 1, pady=1)

janela_login.mainloop()




    