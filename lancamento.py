import sqlite3
from sqlite3 import Error

import banco_dados
from biblioteca_tk import *


def openjanela():
    
    janela = tk.Tk()
    aplicacao = Aplicacao(janela)

class Funcs():
    def limpa_tela(self):
        self.entry_seg.delete(0, END)
        self.entry_cpf.delete(0, END)
        self.entry_tipo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_data.delete(0, END)
        self.entry_supr.delete(0, END)
        self.entry_parceiro1.delete(0, END)
        self.entry_valor.delete(0, END)
        self.entry_obs.delete(0, END)
    def variaveis(self):
        self.seg= self.entry_seg.get()
        self.cpf= self.entry_cpf.get()
        self.tipo= self.entry_tipo.get()
        self.nome= self.entry_nome.get()
        self.data= self.entry_data.get()
        self.supr= self.entry_supr.get()
        self.parceiro= self.entry_parceiro1.get()
        self.valor= self.entry_valor.get()
        self.obs= self.entry_obs.get()
    def add_registro(self):
        self.variaveis()
        my_tag1 ='gray'
        seleciona = "SELECT cpf1 FROM contas_tb WHERE cpf1 = '{}'".format(self.cpf)
        lista = banco_dados.dql(seleciona)    
        while True:
            for self.cpf in lista:
                self.variaveis()
                self.listacli.insert("", "end",values=(self.seg,self.cpf,self.tipo,self.nome,self.data,self.supr,self.parceiro,self.valor,self.obs),tags=(my_tag1))
                vquery = "INSERT INTO base_dados (cpf , tipo1, nome , data , supervisor , parceiro , valor, obs) VALUES ('"+self.cpf+"' , '"+self.tipo+"', '"+self.nome+"', '"+self.data+"', '"+self.supr+"','"+self.parceiro+"', '"+self.valor+"', '"+self.obs+"')"
                banco_dados.dml(vquery)
                self.limpa_tela()
                return
            else:
                messagebox.showinfo(title="ERRO AO INSERIR", message="CAMPOS VAZIOS")
                break
    def buscardados(self,event):
        
        self.variaveis()
        self.entry_cpf.delete(0, END)
        self.entry_tipo.delete(0, END)
        self.entry_supr.delete(0, END)
        nome_dados= self.entry_nome.get()
        
        if self.nome == "":
                
            messagebox.showinfo(title="ERRO DE NOME", message="NOME COMPLETO NÃO INFORMADO")
            return 
        try:       
            seleciona = "SELECT cpf1 , tipo , supervisor1 FROM contas_tb WHERE nome_completo = '{}'".format(nome_dados)
            lista = banco_dados.dql(seleciona)
            self.entry_cpf.insert(END, lista[0][0])
            self.entry_tipo.insert(END, lista[0][1])
            self.entry_supr.insert(END, lista[0][2])
        except:
            messagebox.showinfo(title="ERRO DE CADASTRO", message="COLABORADOR NÃO CADASTRADO")
            return                       
    def OuDoubleClick(self, event):
        self.limpa_tela()
        self.listacli.selection()

        for n in self.listacli.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listacli.item(n, 'values')
            self.entry_seg.insert(END, col1)
            self.entry_cpf.insert(END, col2)
            self.entry_tipo.insert(END, col3)
            self.entry_nome.insert(END, col4)
            self.entry_data.insert(END, col5)
            self.entry_supr.insert(END, col6)
            self.entry_parceiro1.insert(END, col7)
            self.entry_valor.insert(END, col8)
            self.entry_obs.insert(END, col9)
    def deletar_cliente(self, event):
        try:
            #itemSelecionados=self.listacli.selection()
            #self.listacli.delete(itemSelecionados)
            for item in self.listacli.get_children():
                self.listacli.delete(item)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione a Seguencia")
    def Treeview_colrs(self):
        self.variaveis()
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor, parceiro , printf('R$ %d,%d%d',sum(valor)) , obs FROM base_dados GROUP BY seg"
        lista = banco_dados.dql(vquery)
        for i in lista:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end', text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]),tags=(my_tag))    
class Aplicacao(Funcs):
    def __init__(self,janela):
        self.janela1 = janela
        self.tela()
        self.frames()
        self.lista_frame1()
        self.Treeview()
        self.botao()
        self.imagem()
        self.menu()
        janela.resizable(0, 0.6)
        style = ttk.Style()
        style.configure("Treeview",
            background="#D3D3D3",#D3D3D3
            foreground="black",
            rowheight=25,
            fieldbackfround="#D3D3D3"
            )
        style.map("Treeview", background = [("selected","#254360")])
    def tela(self):
        self.janela1.title('RECORDS SERVICE')
        self.janela1.configure(bg = 'white')
        self.janela1.iconbitmap('imagens\logoicoo.ico')
        self.janela1.resizable(True, True)
        self.janela1.state('zoomed')
    def frames(self):
        self.frame1 = Frame(self.janela1, bd = 2, bg = '#BEBEBE',
                            highlightbackground= '#030086', highlightthickness=2 )
        self.frame1.place(relx= 0.148 , rely=0.17, relwidth= 0.85,relheight= 0.82)

        self.frame3 = Frame(self.janela1, bd = 2, bg="white")
        self.frame3.place(relx= 0.005 , rely=0.10, relwidth= 0.140,relheight= 0.89)

        self.notebook=ttk.Notebook(self.frame3)
        self.notebook.place(relx= 0.005 , rely=0.08, relwidth= 0.99, relheight= 0.92)
        self.abas1 = Frame(self.notebook)
        self.notebook.add(self.abas1,text="LANÇAR")      
    def banco_de_dados(self):
        registro.tela_registro()
    def cadastro_de_conta(self):
        cadastro.tela_cadastro()
    def janela_pagamentos(self):
        pagamentos.tela_pagamentos()       
    def imagem(self):
        self.img1 = ImageTk.PhotoImage(file="imagens/APONTAMENTO1.png")
        self.imga1 = tk.Label(master=self.janela1, image=self.img1, bg="white").place(relx=0, rely=0)#(relx=0.37, rely=0.02)
        
        self.img2 = ImageTk.PhotoImage(file="imagens/lancamento1A.png")
        self.imga2 = tk.Label(self.frame3, image=self.img2, bg="white").place(relx=0.001, rely=0.02, relwidth=0.95) 

    def lista_frame1(self):#FRAME PARA LANÇAR

        def format_cpf(event = None):
            
            text = self.entry_cpf.get().replace(".", "").replace("-", "")[:11]
            new_text = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(text)):
                
                if not text[index] in "0123456789": continue
                if index in [2, 5]: new_text += text[index] + "."
                elif index == 8: new_text += text[index] + "-"
                else: new_text += text[index]

            self.entry_cpf.delete(0, "end")
            self.entry_cpf.insert(0, new_text) 
        def format_data(event = None):
    
            data = self.entry_data.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_data.delete(0, "end")
            self.entry_data.insert(0, new_data)
        def salvarStringVar(event):
            n.set(n.get().upper())
            p.set(p.get().upper())
            o.set(o.get().upper())
            
        self.label_seg = customtkinter.CTkLabel(self.abas1, text="SEQ").place(relx=0.420 , rely=0.04)
        self.entry_seg = customtkinter.CTkEntry(self.abas1, border_color='#030086')
        self.entry_seg.place(relx=0.095 , rely=0.08, relwidth=0.80)

        self.label_cpf = customtkinter.CTkLabel(self.abas1, text="CPF").place(relx=0.420 , rely=0.12)
        self.entry_cpf = customtkinter.CTkEntry(self.abas1, border_color='#030086')
        self.entry_cpf.bind("<KeyRelease>", format_cpf)
        self.entry_cpf.place(relx=0.095 , rely=0.16, relwidth=0.80)

        self.label_tipo = customtkinter.CTkLabel(self.abas1, text="TIPO").place(relx=0.410 , rely=0.20)
        self.entry_tipo = customtkinter.CTkEntry(self.abas1, border_color='#030086')
        self.entry_tipo.place(relx=0.095 , rely=0.24, relwidth=0.80)

        self.label_nome = customtkinter.CTkLabel(self.abas1, text="NOME COMPLETO").place(relx=0.290 , rely=0.28)
        n = StringVar()
        self.entry_nome = customtkinter.CTkEntry(self.abas1, textvariable= n, border_color='#030086')
        self.entry_nome.bind("<Return>",self.buscardados)
        self.entry_nome.bind("<KeyRelease>",salvarStringVar)
        self.entry_nome.place(relx=0.095 , rely=0.32, relwidth=0.80)

        self.label_data =  customtkinter.CTkLabel(self.abas1, text="DATA").place(relx=0.410 , rely=0.36)
        self.entry_data =  customtkinter.CTkEntry(self.abas1, border_color='#030086')
        self.entry_data.bind('<KeyRelease>', format_data)
        self.entry_data.place(relx=0.095 , rely=0.40, relwidth=0.80)

        self.label_supr =  customtkinter.CTkLabel(self.abas1, text="SUPERVISOR").place(relx=0.320 , rely=0.44)
        self.entry_supr =  customtkinter.CTkEntry(self.abas1, border_color='#030086')
        self.entry_supr.place(relx=0.095 , rely=0.48, relwidth=0.80)

        self.label_parceiro1 =  customtkinter.CTkLabel(self.abas1, text="PARCEIRO").place(relx=0.350 , rely=0.52)
        p = StringVar()
        self.entry_parceiro1 =  customtkinter.CTkEntry(self.abas1, textvariable=p, border_color='#030086')
        self.entry_parceiro1.bind("<KeyRelease>",salvarStringVar)
        self.entry_parceiro1.place(relx=0.095 , rely=0.56, relwidth=0.80)

        self.label_valor = customtkinter.CTkLabel(self.abas1, text="VALOR").place(relx=0.400 , rely=0.60)
        self.entry_valor = customtkinter.CTkEntry(self.abas1, border_color='#030086')
        self.entry_valor.place(relx=0.095 , rely=0.64, relwidth=0.80)

        self.label_obs =  customtkinter.CTkLabel(self.abas1, text="OBSERVAÇÃO").place(relx=0.300 , rely=0.68)
        o = StringVar()
        self.entry_obs =  customtkinter.CTkEntry(self.abas1, textvariable=o, border_color='#030086')
        self.entry_obs.bind("<KeyRelease>",salvarStringVar)
        self.entry_obs.place(relx=0.095 , rely=0.72, relwidth=0.80)
    def Treeview(self):
        self.colum=("col1","col2","col3","col4","col5","col6","col7","col8","col9")
        self.listacli =ttk.Treeview(self.frame1, height=3,columns=self.colum, show='headings')
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="SEQ")
        self.listacli.heading("#2", text="CPF")
        self.listacli.heading("#3", text="TIPO")
        self.listacli.heading("#4", text="DIARISTA")
        self.listacli.heading("#5", text="DATA")
        self.listacli.heading("#6", text="SUPERVISOR")
        self.listacli.heading("#7", text="PARCEIRO")
        self.listacli.heading("#8", text="VALOR")
        self.listacli.heading("#9", text="OBS")

        self.listacli.column("#0", width=1)
        self.listacli.column("#1", width=10)
        self.listacli.column("#2", width=80)
        self.listacli.column("#3", width=40)
        self.listacli.column("#4", width=250)
        self.listacli.column("#5", width=60)
        self.listacli.column("#6", width=100, anchor=tk.CENTER)
        self.listacli.column("#7", width=30)
        self.listacli.column("#8", width=80, anchor=tk.CENTER)
        self.listacli.column("#9", width=200)

        self.listacli.tag_configure('gray', background='#D9EAF6')
        self.listacli.tag_configure('normal', background='white')
        self.listacli.place(relx=0,rely=0.0,relwidth=0.987,relheight=0.999)
        
        self.barra_rolagem=Scrollbar(self.frame1, orient="vertical")
        self.listacli.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listacli.yview)
        self.barra_rolagem.place(relx=0.988, rely=0.005,relwidth=0.01, relheight=0.99)
        self.listacli.bind("<Double-1>",self.OuDoubleClick)
        self.listacli.bind("<Delete>",self.deletar_cliente)
    def menu(self):
        menubar = Menu(self.janela1)
        self.janela1.config(menu=menubar)
                # create a menubar
        menubar = Menu(self.janela1)
        self.janela1.config(menu=menubar)
        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )
        # add menu items to the File menu
        file_menu.add_command(label='Registro', command=self.banco_de_dados)
        file_menu.add_command(label='Cadastro', command=self.cadastro_de_conta)
        file_menu.add_command(label='Pagamentos',command=self.janela_pagamentos)
        file_menu.add_separator()
        # add the File menu to the menubar
        menubar.add_cascade(
            label="Janelas",
            menu=file_menu
        )
        # create the Help menu
        help_menu = Menu(
            menubar,
            tearoff=0
        )
        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')

        # add the Help menu to the menubar
        menubar.add_cascade(
            label="Help",
            menu=help_menu
        )
    def botao(self): # ESSES SÃO OS BOTOES QUE ESTÃO DENTRO DA JANELA


        self.bto_gerar2 = tk.PhotoImage(file="imagens/button_nm/Apontar2.png")#FF7A00
        self.bto_gerar = customtkinter.CTkButton(master=self.abas1, text="" ,image=self.bto_gerar2, command=self.add_registro)
        self.bto_gerar.place(relx=0.20 , rely=0.78, relwidth=0.60)

        self.bto_limpar2 = tk.PhotoImage(file="imagens/button_nm/Limpar.png")
        self.bto_limpar = customtkinter.CTkButton(master=self.abas1,text="" ,image=self.bto_limpar2, command=self.limpa_tela)
        self.bto_limpar.place(relx=0.20 , rely=0.84, relwidth=0.60)

    

    

