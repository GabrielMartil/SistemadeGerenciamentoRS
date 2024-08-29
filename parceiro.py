from biblioteca_tk import *
import banco_dados
import csv
import pandas as pd

def tela_parceiro():
    
    parceiro = tk.Toplevel()
    aplicacao = jt_parceiros(parceiro)
class Funcs():
    def variaveis(self):
        self.data_in = self.entry_in.get()
        self.data_fi = self.entry_fi.get()
    def select_lista(self):
        my_tag='normal'
        vquery="SELECT parceiro, tipo1, nome, data, count(nome),valor FROM base_dados GROUP BY seg, nome ORDER BY data"
        linhas = banco_dados.dql(vquery)
        for id in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end',text=id[0],
                values =(id[0],id[1],id[2],id[3],id[4],id[5]),tags=(my_tag))
    def gerar_excel(self):
        cols = ['PARCEIRO','TIPO','NOME','DATA','QUANT','VALOR'] # Your column headings here
        path = 'C:\\Users\\Gabriel Martins\\Dropbox\\PC (2)\\Desktop\\projeto01\\Diarias_pg\\relatorio.csv'
        excel_name = 'C:\\Users\\Gabriel Martins\\Dropbox\\PC (2)\\Desktop\\projeto01\\Diarias_pg\\relatorio.xlsx'
        lst = []
        
        with open(path, "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for i ,linha in enumerate(self.listacli.get_children()):
                row = self.listacli.item(linha,'values')
                lst.append(row)
            lst = list(map(list,lst))
            lst.insert(0,cols)
            for row in lst:
                csvwriter.writerow(row)
        writer = pd.ExcelWriter(excel_name)
        df = pd.read_csv(path, encoding= "ISO-8859-1")
        df.to_excel(writer,sheet_name="Relatorios")
        writer.save()
        messagebox.showinfo(title="SALVO", message="Arquivo Gerado")   
    def Filtrodata(self):
        self.variaveis()
        self.listacli.delete(*self.listacli.get_children())
        my_tag='normal'
        vquery="SELECT parceiro, nome, data, count(nome) from base_dados WHERE data BETWEEN '"+self.data_in+"' AND '"+self.data_fi+"' GROUP BY data, nome "
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end', text=i[0],
                values =(i[0],i[1],i[2],i[3]),tags=(my_tag))
class jt_parceiros(Funcs):
    def __init__(self,parceiro):
        self.janela4 = (parceiro)
        self.tela()
        self.frames()
        self.label()
        self.lista_colunas1()
        self.menu()
        self.butao()
        parceiro.mainloop()
    def tela(self):
        self.janela4.title('PARCEIRO')
        self.janela4.geometry("800x740")
        self.janela4.configure(bg = 'white')
        self.janela4.iconbitmap('imagens\logoicoo.ico')
        self.janela4.resizable(True, True)
    def frames(self):
        #frame das TreeView parceiro
        self.frame1 = Frame(self.janela4, bd = 2, bg = 'white')
        self.frame1.place(relx= 0 , rely=0, relwidth= 1,relheight= 0.99)
    def label(self):
        def format_data(event = None):
            data = self.entry_in.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_in.delete(0, "end")
            self.entry_in.insert(0, new_data)
        self.label_in = customtkinter.CTkLabel(self.janela4, text="DATA INICIAL").place(relx=0.05, rely=0.01)
        self.entry_in = customtkinter.CTkEntry(self.janela4)
        self.entry_in.bind("<KeyRelease>", format_data)
        self.entry_in.place(relx=0.18, rely=0.01, relwidth=0.10)

        def format_data_fi(event = None):
            data = self.entry_fi.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_fi.delete(0, "end")
            self.entry_fi.insert(0, new_data)
        self.label_fi = customtkinter.CTkLabel(self.janela4, text="DATA FINAL").place(relx=0.33, rely=0.01)
        self.entry_fi = customtkinter.CTkEntry(self.janela4)
        self.entry_fi.bind("<KeyRelease>", format_data_fi)
        self.entry_fi.place(relx=0.45, rely=0.01, relwidth=0.10)
    def lista_colunas1(self):#Treeview data a ser lançada
        column=("col1","col2","col3","col4","col5","col6")

        self.listacli =ttk.Treeview(self.frame1, height=3,columns=column, show="headings")
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="PARCEIRO")
        self.listacli.heading("#2", text="TIPO")
        self.listacli.heading("#3", text="NOME")
        self.listacli.heading("#4", text="DATA")
        self.listacli.heading("#5", text="QUANT")
        self.listacli.heading("#6", text="VALOR")
        
        self.listacli.column("#0", width=0)
        self.listacli.column("#1", width=60)
        self.listacli.column("#2", width=40)
        self.listacli.column("#3", width=15)
        self.listacli.column("#4", width=10, anchor="center")
        self.listacli.column("#5", width=10, anchor="center")
        self.listacli.column("#6", width=10, anchor="center")
        
        self.listacli.tag_configure('gray', background='#D9EAF6')
        self.listacli.tag_configure('normal', background='white')
        
        self.listacli.place(relx=0,rely=0.05,relwidth=0.973,relheight=0.958)

        self.barra_rolagem=Scrollbar(self.frame1, orient="vertical")
        self.listacli.configure(yscrollcommand=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listacli.yview)
        self.barra_rolagem.place(relx=0.978, rely=0.05,relwidth=0.02, relheight=0.956)
        self.select_lista()
    def menu(self):
        menubar = Menu(self.janela4)
        self.janela4.config(menu=menubar)
                # create a menubar
        menubar = Menu(self.janela4)
        self.janela4.config(menu=menubar)
        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )
        # add menu items to the File menu
        file_menu.add_command(label='EXCEL', command=self.gerar_excel)
        # add the File menu to the menubar
        menubar.add_cascade(
            label="Imprimir",
            menu=file_menu
        )    
    def butao(self):
        
        self.bto_filtro2 = tk.PhotoImage(file="imagens/button_nm/FILTRO.png")
        self.bto_filtro = customtkinter.CTkButton(self.janela4, text="", image=self.bto_filtro2,command=self.Filtrodata)
        self.bto_filtro.place(relx=0.80, rely=0.01, relwidth=0.15, relheight=0.03)

def tela_diarista():
    
    diarista = tk.Toplevel()
    aplicacao = jt_diarista(diarista)
class Funcs():
    def variaveis(self):
        self.data_in2 = self.entry_in2.get()
        self.data_fi2 = self.entry_fi2.get()
    def select_lista(self):
        my_tag='normal'
        vquery="SELECT tipo1, cpf, nome, count(nome), data, parceiro, valor FROM base_dados GROUP BY seg, nome ORDER BY nome "
        linhas = banco_dados.dql(vquery)
        for id in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end',text=id[0],
                values =(id[0],id[1],id[2],id[3],id[4],id[5],id[6]),tags=(my_tag))
    def gerar_excel(self):
        cols = ['TIPO','CPF','NOME','QUANT','DATA','PARCEIRO','VALOR'] # Your column headings here
        path = 'C:\\Users\\Gabriel Martins\\Dropbox\\PC (2)\\Desktop\\projeto01\\Diarias_pg\\geral.csv'
        excel_name = 'C:\\Users\\Gabriel Martins\\Dropbox\\PC (2)\\Desktop\\projeto01\\Diarias_pg\\geral.xlsx'
        lst = []
        
        with open(path, "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for i ,linha in enumerate(self.listacli.get_children()):
                row = self.listacli.item(linha,'values')
                lst.append(row)
            lst = list(map(list,lst))
            lst.insert(0,cols)
            for row in lst:
                csvwriter.writerow(row)
        writer = pd.ExcelWriter(excel_name)
        df = pd.read_csv(path, encoding= "ISO-8859-1")
        df.to_excel(writer,sheet_name="GERAL")
        writer.save()
        messagebox.showinfo(title="SALVO", message="Arquivo Gerado")   
    def Filtrodata1(self):
        self.variaveis()
        self.listacli.delete(*self.listacli.get_children())
        my_tag='normal'
        vquery="SELECT tipo1, cpf, nome, data, count(nome), valor FROM base_dados WHERE data BETWEEN '"+self.data_in2+"' AND '"+self.data_fi2+"'  GROUP BY data, nome"
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end', text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4]),tags=(my_tag))
class jt_diarista(Funcs):
    def __init__(self,diarista):
        self.janela5 = (diarista)
        self.tela()
        self.frames()
        self.label()
        self.lista_colunas1()
        self.menu()
        self.butao()
        diarista.mainloop()
    def tela(self):
        self.janela5.title('GERAL')
        self.janela5.geometry("800x740")
        self.janela5.configure(bg = 'white')
        self.janela5.iconbitmap('imagens\logoicoo.ico')
        self.janela5.resizable(True, True)
    def frames(self):
        #frame das TreeView parceiro
        self.frame1 = Frame(self.janela5, bd = 2, bg = 'white')
        self.frame1.place(relx= 0 , rely=0, relwidth= 1,relheight= 0.99)
    def label(self):
        self.label_in2 = customtkinter.CTkLabel(self.janela5, text="DATA INICIAL").place(relx=0.05, rely=0.01)
        self.entry_in2 = customtkinter.CTkEntry(self.janela5)
        self.entry_in2.place(relx=0.18, rely=0.01, relwidth=0.10)

        self.label_fi2 = customtkinter.CTkLabel(self.janela5, text="DATA FINAL").place(relx=0.33, rely=0.01)
        self.entry_fi2 = customtkinter.CTkEntry(self.janela5)
        self.entry_fi2.place(relx=0.45, rely=0.01, relwidth=0.10)
    def lista_colunas1(self):#Treeview data a ser lançada
        column=("col1","col2","col3","col4","col5","col6","col7")

        self.listacli =ttk.Treeview(self.frame1, height=3,columns=column, show="headings")
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="TIPO")
        self.listacli.heading("#2", text="CPF")
        self.listacli.heading("#3", text="NOME")
        self.listacli.heading("#4", text="QUANT")
        self.listacli.heading("#5", text="DATA")
        self.listacli.heading("#6", text="PARCEIRO")
        self.listacli.heading("#7", text="VALOR")
        
        self.listacli.column("#0", width=0)
        self.listacli.column("#1", width=60)
        self.listacli.column("#2", width=300)
        self.listacli.column("#3", width=15)
        self.listacli.column("#4", width=10)
        self.listacli.column("#5", width=10)
        self.listacli.column("#6", width=10)
        self.listacli.column("#7", width=10)
        
        self.listacli.tag_configure('gray', background='#D9EAF6')
        self.listacli.tag_configure('normal', background='white')
        
        self.listacli.place(relx=0,rely=0.05,relwidth=0.973,relheight=0.958)

        self.barra_rolagem=Scrollbar(self.frame1, orient="vertical")
        self.listacli.configure(yscrollcommand=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listacli.yview)
        self.barra_rolagem.place(relx=0.978, rely=0.05,relwidth=0.02, relheight=0.956)
        self.select_lista()
    def menu(self):
        menubar = Menu(self.janela5)
        self.janela5.config(menu=menubar)
                # create a menubar
        menubar = Menu(self.janela5)
        self.janela5.config(menu=menubar)
        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )
        # add menu items to the File menu
        file_menu.add_command(label='EXCEL', command=self.gerar_excel)
        # add the File menu to the menubar
        menubar.add_cascade(
            label="Imprimir",
            menu=file_menu
        )    
    def butao(self):

        self.bto_filtro2 = tk.PhotoImage(file="imagens/button_nm/FILTRO.png")
        self.bto_filtro = customtkinter.CTkButton(self.janela5, text="", image=self.bto_filtro2,command=self.Filtrodata1)
        self.bto_filtro.place(relx=0.80, rely=0.01, relwidth=0.15, relheight=0.03)

def tela_pagamento():
    
    pagamento = tk.Toplevel()
    aplicacao = jt_pagamentos(pagamento)
class Funcs():
    def variaveis(self):
        self.data_in3 = self.entry_in3.get()
        self.data_fi3 = self.entry_fi3.get()
    def select_lista(self):
        my_tag='normal'
        vquery="SELECT tipo1, parceiro, valor, nome, data_pg FROM base_dados GROUP BY seg, nome ORDER BY seg"
        linhas = banco_dados.dql(vquery)
        for id in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end',text=id[0],
                values =(id[0],id[1],id[2],id[3],id[4]),tags=(my_tag))
    def gerar_excel(self):
        cols = ['TIPO','PARCEIRO','VALOR','NOME','DATA'] # Your column headings here
        path = 'Diarias_pg\\RELATORIOpg.csv'
        excel_name = 'Diarias_pg\\RELATORIOpg.xlsx'
        lst = []
        
        with open(path, "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for i ,linha in enumerate(self.listacli.get_children()):
                row = self.listacli.item(linha,'values')
                lst.append(row)
            lst = list(map(list,lst))
            lst.insert(0,cols)
            for row in lst:
                csvwriter.writerow(row)
        writer = pd.ExcelWriter(excel_name)
        df = pd.read_csv(path, encoding= "ISO-8859-1")
        df.to_excel(writer,sheet_name="GERAL")
        writer.save()
        messagebox.showinfo(title="SALVO", message="Arquivo Gerado")   
    def Filtrodata1(self):
        self.variaveis()
        self.listacli.delete(*self.listacli.get_children())
        my_tag='normal'
        vquery="SELECT tipo1, cpf, nome, data, data_pg FROM base_dados WHERE data_pg BETWEEN '"+self.data_in3+"' AND '"+self.data_fi3+"'  GROUP BY data_pg, nome"
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end', text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4]),tags=(my_tag))
class jt_pagamentos(Funcs):
    def __init__(self,pagamento):
        self.janela5 = (pagamento)
        self.tela()
        self.frames()
        self.label()
        self.lista_colunas1()
        self.menu()
        self.butao()
        pagamento.mainloop()
    def tela(self):
        self.janela5.title('Relatorio')
        self.janela5.geometry("800x740")
        self.janela5.configure(bg = 'white')
        self.janela5.iconbitmap('imagens\logoicoo.ico')
        self.janela5.resizable(True, True)
    def frames(self):
        #frame das TreeView parceiro
        self.frame1 = Frame(self.janela5, bd = 2, bg = 'white')
        self.frame1.place(relx= 0 , rely=0, relwidth= 1,relheight= 0.99)
    def label(self):
        self.label_in3 = customtkinter.CTkLabel(self.janela5, text="DATA INICIAL").place(relx=0.05, rely=0.01)
        self.entry_in3 = customtkinter.CTkEntry(self.janela5)
        self.entry_in3.place(relx=0.18, rely=0.01, relwidth=0.10)

        self.label_fi3 = customtkinter.CTkLabel(self.janela5, text="DATA FINAL").place(relx=0.33, rely=0.01)
        self.entry_fi3 = customtkinter.CTkEntry(self.janela5)
        self.entry_fi3.place(relx=0.45, rely=0.01, relwidth=0.10)
    def lista_colunas1(self):#Treeview data a ser lançada
        column=("col1","col2","col3","col4","col5")

        self.listacli =ttk.Treeview(self.frame1, height=3,columns=column, show="headings")
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="TIPO")
        self.listacli.heading("#2", text="PARCEIRO")
        self.listacli.heading("#3", text="VALOR")
        self.listacli.heading("#4", text="NOME")
        self.listacli.heading("#5", text="DATA_PG")
        
        self.listacli.column("#0", width=0)
        self.listacli.column("#1", width=60)
        self.listacli.column("#2", width=10)
        self.listacli.column("#3", width=15)
        self.listacli.column("#4", width=100)
        self.listacli.column("#5", width=10)
        
        self.listacli.tag_configure('gray', background='#D9EAF6')
        self.listacli.tag_configure('normal', background='white')
        
        self.listacli.place(relx=0,rely=0.05,relwidth=0.973,relheight=0.958)

        self.barra_rolagem=Scrollbar(self.frame1, orient="vertical")
        self.listacli.configure(yscrollcommand=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listacli.yview)
        self.barra_rolagem.place(relx=0.978, rely=0.05,relwidth=0.02, relheight=0.956)
        self.select_lista()
    def menu(self):
        menubar = Menu(self.janela5)
        self.janela5.config(menu=menubar)
                # create a menubar
        menubar = Menu(self.janela5)
        self.janela5.config(menu=menubar)
        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )
        # add menu items to the File menu
        file_menu.add_command(label='EXCEL', command=self.gerar_excel)
        # add the File menu to the menubar
        menubar.add_cascade(
            label="Imprimir",
            menu=file_menu
        )    
    def butao(self):

        self.bto_filtro2 = tk.PhotoImage(file="imagens/button_nm/FILTRO.png")
        self.bto_filtro = customtkinter.CTkButton(self.janela5, text="", image=self.bto_filtro2,command=self.Filtrodata1)
        self.bto_filtro.place(relx=0.80, rely=0.01, relwidth=0.15, relheight=0.03)