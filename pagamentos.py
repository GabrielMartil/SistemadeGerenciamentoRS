from biblioteca_tk import *
import banco_dados
import csv
import qrcode
import pandas as pd

def tela_pagamentos():
    
    pagamentos = tk.Toplevel()
    aplicacao = jt_pagamentos(pagamentos)
class Funcs():
    def limpa_tela(self):
        self.entry_nome1.delete(0, END)
        self.entry_cpf1.delete(0, END)
        self.entry_banco1.delete(0, END)
        self.entry_pix1.delete(0, END)
        self.entry_valor.delete(0, END)
        self.entry_pg.delete(0, END)
    def variaveis(self):
        self.nome= self.entry_nome1.get()
        self.cpf= self.entry_cpf1.get()
        self.banco= self.entry_banco1.get()
        self.pix= self.entry_pix1.get()
        self.valor= self.entry_valor.get()
        self.data_pg = self.entry_pg.get()
        self.inicial = self.entry_in.get()
        self.final = self.entry_fi.get()
        self.inicial1 = self.entry_in1.get()
        self.final1 = self.entry_fi1.get()
    def select_lista(self):
        my_tag='normal'
        vquery="""SELECT nome, cpf1 , banco , pix , printf('R$ %d,%d%d',sum(valor)) , data_pg from base_dados 
                INNER JOIN contas_tb on contas_tb.cpf1 = base_dados.cpf WHERE data_pg AND tipO1 = 'DIARISTA' GROUP BY nome"""
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli2.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5]),tags=(my_tag))     
    def OuDoubleClick(self,event):
        self.limpa_tela()
        self.listacli.selection()
        
        
        for n in self.listacli.selection():
            col1, col2, col3, col4, col5, col6 = self.listacli.item(n, 'values')
            self.entry_nome1.insert(END, col1)
            self.entry_cpf1.insert(END, col2)
            self.entry_banco1.insert(END, col3)
            self.entry_pix1.insert(END, col4)
            self.entry_valor.insert(END, col5)
            self.entry_pg.insert(END, col6)
        self.gerarQRcode()
    def OuDoubleClick1(self,event):
        self.limpa_tela()
        self.listacli2.selection()
        
        for n in self.listacli2.selection():
            col1, col2, col3, col4, col5, col6 = self.listacli2.item(n, 'values')
            self.entry_nome1.insert(END, col1)
            self.entry_cpf1.insert(END, col2)
            self.entry_banco1.insert(END, col3)
            self.entry_pix1.insert(END, col4)
            self.entry_valor.insert(END, col5)
            self.entry_pg.insert(END, col6)
    def gerar_excel1(self):
        cols = ['NOME','CPF','BANCO','AGENCIA','CONTA','PIX','VALOR','DATA PG'] # Your column headings here
        path = 'Diarias_pg/relatorio de Pagamentos.csv'
        excel_name = 'Diarias_pg/relatorio de Pagamentos.xlsx'
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
    def gerar_excel2(self):
        cols = ['NOME','CPF','BANCO','AGENCIA','CONTA','PIX','VALOR','DATA PG'] # Your column headings here
        path = 'Diarias_pg/relatorio de Pagamentos2.csv'
        excel_name = 'Diarias_pg/relatorio de Pagamentos2.xlsx'
        lst = []
        
        with open(path, "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for i ,linha in enumerate(self.listacli2.get_children()):
                row = self.listacli2.item(linha,'values')
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
    def Atualizar_datapg(self):
        self.variaveis()
        self.limpa_tela()
        self.listacli.delete(*self.listacli.get_children())
        vquery="UPDATE base_dados SET data_pg = '"+self.data_pg+"'  WHERE nome = '"+self.nome+"' AND data_pg IS NULL"
        linhas = banco_dados.dml(vquery)
        self.Treeview_colrs()
        self.select_lista()
    def Treeview_colrs(self):
        my_tag='normal'
        vquery="""SELECT nome, cpf1 , banco , pix , printf('R$ %d,%d%d',sum(valor)) , data_pg from base_dados 
                INNER JOIN contas_tb on contas_tb.cpf1 = base_dados.cpf WHERE data_pg IS NULL AND tipO1 = 'DIARISTA' GROUP BY nome"""
        linhas = banco_dados.dql(vquery)
        for id in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end',
                values =(id[0],id[1],id[2],id[3],id[4],id[5]),tags=(my_tag))
    def savetreeview(self):
        with open("new.csv", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')

            for row_id in self.listacli.get_children():
                row = self.listacli.item(row_id)['values']
                csvwriter.writerow(row)
                print(row)
                writer = pd.ExcelWriter("excel_name")
                df = pd.read_excel("new.csv")
                df.to_excel(writer,'sheetname')
                writer.save()
    def Filtrodata(self):
        self.variaveis()
        self.listacli.delete(*self.listacli.get_children())
        my_tag='normal'
        vquery="SELECT nome, cpf1 , banco , agencia , conta , pix , printf('R$ %d,%d%d',sum(valor)) , data_pg from base_dados INNER JOIN contas_tb on contas_tb.cpf1 = base_dados.cpf WHERE data_pg IS NULL AND tipO1 = 'DIARISTA' AND data BETWEEN '"+self.inicial+"' AND '"+self.final+"' GROUP BY nome"
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]),tags=(my_tag))
    def Filtrodata1(self):
        self.variaveis()
        self.listacli2.delete(*self.listacli2.get_children())
        my_tag='normal'
        vquery="SELECT nome, cpf1 , banco , agencia , conta , pix , printf('R$ %d,%d%d',sum(valor)) , data_pg from base_dados INNER JOIN contas_tb on contas_tb.cpf1 = base_dados.cpf WHERE data_pg AND tipO1 = 'DIARISTA' AND data_pg = '"+self.inicial1+"' GROUP BY nome"
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli2.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]),tags=(my_tag))
class jt_pagamentos(Funcs):
    def __init__(self,pagamentos):
        self.janela4 = (pagamentos)
        self.tela()
        self.frames()
        self.label()
        self.lista_colunas1()
        self.lista_colunas2()
        self.butao()
        self.Image()
        pagamentos.mainloop()
    def tela(self):
        self.janela4.title('PAGAMENTOS')
        self.janela4.geometry("1120x750")
        self.janela4.configure(bg = 'white')
        self.janela4.iconbitmap('imagens\logoicoo.ico')
        self.janela4.resizable(True, True)
    def frames(self):
        #frame das TreeView PAGAMENTOS
        self.frame1 = Frame(self.janela4, bd = 2, bg = 'white')
        self.frame1.place(relx= 0 , rely=0, relwidth= 0.788,relheight= 0.51)
        #frame das TreeView REGISTRO
        self.frame3 = Frame(self.janela4, bd = 2, bg = 'white')
        self.frame3.place(relx= 0 , rely=0.52, relwidth= 0.788,relheight= 0.476)
        #frame das label
        self.frame2 = Frame(self.janela4, bd = 2, bg = 'white')
        self.frame2.place(relx= 0.7901 , rely=0, relwidth= 0.205,relheight= 0.51)

        self.notebook=ttk.Notebook(self.janela4)
        self.notebook.place(relx= 0.7901 , rely=0.620, relwidth= 0.205, relheight= 0.25)

        self.abas1 = Frame(self.notebook)
        self.notebook.add(self.abas1,text="ABA1")

        self.abas2 = Frame(self.notebook)
        self.notebook.add(self.abas2,text="ABA2")

        #FRAME QRCODE
                # Frame para QR Code
        self.frame4 = Frame(self.janela4, bd=2, highlightbackground='white', highlightthickness=2)
        self.frame4.place(relx=0.8120, rely=0.370, relwidth=0.16, relheight=0.24)
        
        # Inicializar o Label (não mostrar ainda)
        self.img_label = tk.Label(self.frame4, relief=tk.SOLID)
        self.img_label.pack(expand=True, fill='both')

        self.img_padao = None
    def gerarQRcode(self):
        # Número que você deseja transformar em QR Code
        numero = self.entry_pix1.get()
        
        if not numero:
            print("Nenhum número foi inserido.")
            return
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(str(numero))
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        caminho_imagem = 'imagens/qrcode00.png'

        img.save(caminho_imagem)
        self.redimensionar_imagem(caminho_imagem)

    def redimensionar_imagem(self, caminho_imagem):
        img = Image.open(caminho_imagem)
        self.frame4.update_idletasks()
        frame_width = self.frame4.winfo_width()
        frame_height = self.frame4.winfo_height()

        img = img.resize((frame_width, frame_height), Image.ANTIALIAS)

        new_img_padao = ImageTk.PhotoImage(img)

        if self.img_padao:
            self.img_label.config(image='')
            self.img_label.image = None

        self.img_label.config(image=new_img_padao)
        self.img_label.image = new_img_padao
        
        self.img_padao = new_img_padao

    def lista_colunas1(self):#Treeview data a ser lançada
        column=("col1","col2","col3","col4","col5","col6")

        self.listacli =ttk.Treeview(self.frame1, height=3,columns=column, show="headings")
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="NOME")
        self.listacli.heading("#2", text="CPF")
        self.listacli.heading("#3", text="BANCO")
        self.listacli.heading("#4", text="PIX")
        self.listacli.heading("#5", text="VALOR")
        self.listacli.heading("#6", text="DATA PG")

        self.listacli.column("#0", width=0)
        self.listacli.column("#1", width=160)
        self.listacli.column("#2", width=60)
        self.listacli.column("#3", width=30)
        self.listacli.column("#4", width=160)
        self.listacli.column("#5", width=10)
        self.listacli.column("#6", width=20)
        
        self.listacli.tag_configure('gray', background='#D9EAF6')
        self.listacli.tag_configure('normal', background='white')
        
        self.listacli.place(relx=0,rely=0,relwidth=0.98,relheight=0.958)

        self.barra_rolagem=Scrollbar(self.frame1, orient="vertical")
        self.listacli.configure(yscrollcommand=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listacli.yview)
        self.barra_rolagem.place(relx=0.985, rely=0.005,relwidth=0.014, relheight=0.956)

        self.barra_rolagem1=Scrollbar(self.frame1, orient="horizontal")
        self.listacli.configure(xscrollcommand=self.barra_rolagem1.set)
        self.barra_rolagem1.config(command=self.listacli.xview)
        self.barra_rolagem1.place(relx=0.001, rely=0.966,relwidth=0.98, relheight=0.033)
        self.listacli.bind("<Double-1>",self.OuDoubleClick)
        self.Treeview_colrs()     
    def lista_colunas2(self):#Treeview data lançada

        column1=("col1","col2","col3","col4","col5","col6")
        self.listacli2 =ttk.Treeview(self.frame3, height=3,columns=column1, show="headings")
        self.listacli2.heading("#0", text="")
        self.listacli2.heading("#1", text="NOME")
        self.listacli2.heading("#2", text="CPF")
        self.listacli2.heading("#3", text="BANCO")
        self.listacli2.heading("#4", text="PIX")
        self.listacli2.heading("#5", text="VALOR")
        self.listacli2.heading("#6", text="DATA PG")

        self.listacli2.column("#0", width=0)
        self.listacli2.column("#1", width=160)
        self.listacli2.column("#2", width=60)
        self.listacli2.column("#3", width=30)
        self.listacli2.column("#4", width=160)
        self.listacli2.column("#5", width=10)
        self.listacli2.column("#6", width=20)
        
        self.listacli2.tag_configure('gray', background='#D9EAF6')
        self.listacli2.tag_configure('normal', background='white')

        self.listacli2.place(relx=0,rely=0,relwidth=0.98,relheight=0.955)

        self.barra_rolagem=Scrollbar(self.frame3, orient="vertical")
        self.listacli2.configure(yscrollcommand=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listacli2.yview)
        self.barra_rolagem.place(relx=0.985, rely=0.005,relwidth=0.014, relheight=0.955)

        self.barra_rolagem1=Scrollbar(self.frame3, orient="horizontal")
        self.listacli2.configure(xscrollcommand=self.barra_rolagem1.set)
        self.barra_rolagem1.config(command=self.listacli2.xview)
        self.barra_rolagem1.place(relx=0.001, rely=0.967,relwidth=0.98, relheight=0.033)
        self.listacli2.bind("<Double-1>",self.OuDoubleClick1)
        self.select_lista()
    def label(self):
        def format_cpf(event = None):
    
            text = self.entry_cpf1.get().replace(".", "").replace("-", "")[:11]
            new_text = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(text)):
                
                if not text[index] in "0123456789": continue
                if index in [2, 5]: new_text += text[index] + "."
                elif index == 8: new_text += text[index] + "-"
                else: new_text += text[index]

            self.entry_cpf1.delete(0, "end")
            self.entry_cpf1.insert(0, new_text)
        def format_data(event = None):
            data = self.entry_pg.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_pg.delete(0, "end")
            self.entry_pg.insert(0, new_data)
        def format_dataincial(event = None):
            data = self.entry_in.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_in.delete(0, "end")
            self.entry_in.insert(0, new_data)
        def format_datafinal(event = None):
            data = self.entry_fi.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_fi.delete(0, "end")
            self.entry_fi.insert(0, new_data)
        def format_dataincial1(event = None):
            data = self.entry_in1.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_in1.delete(0, "end")
            self.entry_in1.insert(0, new_data)
        def format_datafinal1(event = None):
            data = self.entry_fi1.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_fi1.delete(0, "end")
            self.entry_fi1.insert(0, new_data)
        self.label_nome1 = customtkinter.CTkLabel(self.frame2, text="NOME").place(x=90 , y=18)
        self.entry_nome1 = customtkinter.CTkEntry(self.frame2)
        self.entry_nome1.place(x=2 , y=38, relwidth=0.99, relheight=0.06)

        self.label_cpf1 = customtkinter.CTkLabel(self.frame2, text="CPF").place(x=100 , y=60)
        self.entry_cpf1 = customtkinter.CTkEntry(self.frame2)
        self.entry_cpf1.bind("<KeyRelease>", format_cpf)
        self.entry_cpf1.place(x=2 , y=80, relwidth=0.99, relheight=0.06)

        self.label_banco1 = customtkinter.CTkLabel(self.frame2, text="BANCO").place(x=90 , y=102)
        self.entry_banco1 = customtkinter.CTkEntry(self.frame2)
        self.entry_banco1.place(x=2 , y=122, relwidth=0.99, relheight=0.06)

        self.label_pix1 = customtkinter.CTkLabel(self.frame2, text="PIX").place(x=90 , y=144)
        self.entry_pix1 = customtkinter.CTkEntry(self.frame2)
        self.entry_pix1.place(x=2 , y=164, relwidth=0.99, relheight=0.06)

        self.label_valor = customtkinter.CTkLabel(self.frame2, text="VALOR").place(x=90 , y=186)
        self.entry_valor  = customtkinter.CTkEntry(self.frame2)
        self.entry_valor.place(x=2 , y=206, relwidth=0.99, relheight=0.06)

        self.label_pg = customtkinter.CTkLabel(self.frame2, text="DATA PG").place(x=85 , y=228)
        self.entry_pg = customtkinter.CTkEntry(self.frame2)
        self.entry_pg.bind('<KeyRelease>', format_data)
        self.entry_pg.place(x=2 , y=248, relwidth=0.99, relheight=0.06)

        self.label_in = customtkinter.CTkLabel(self.abas1, text="DATA INICIAL").place(relx=0.11, rely=0.05)
        self.entry_in = customtkinter.CTkEntry(self.abas1)
        self.entry_in.bind('<KeyRelease>', format_dataincial)
        self.entry_in.place(relx=0.10, rely=0.24, relwidth=0.35, relheight=0.20)

        self.label_fi = customtkinter.CTkLabel(self.abas1, text="DATA FINAL").place(relx=0.524, rely=0.05)
        self.entry_fi = customtkinter.CTkEntry(self.abas1)
        self.entry_fi.bind('<KeyRelease>', format_datafinal)
        self.entry_fi.place(relx=0.520, rely=0.24, relwidth=0.35, relheight=0.20)

        self.label_in1 = customtkinter.CTkLabel(self.abas2, text="DATA INICIAL").place(relx=0.11, rely=0.05)
        self.entry_in1 = customtkinter.CTkEntry(self.abas2)
        self.entry_in1.bind('<KeyRelease>', format_dataincial1)
        self.entry_in1.place(relx=0.10, rely=0.24, relwidth=0.35, relheight=0.20)

        self.label_fi1 = customtkinter.CTkLabel(self.abas2, text="DATA FINAL").place(relx=0.524, rely=0.05)
        self.entry_fi1 = customtkinter.CTkEntry(self.abas2)
        self.entry_fi1.bind('<KeyRelease>', format_datafinal1)
        self.entry_fi1.place(relx=0.520, rely=0.24, relwidth=0.35, relheight=0.20)
    def butao(self):
        self.bto_buscar2 = tk.PhotoImage(file="imagens/button_nm/pagamento.png")
        self.bto_buscar = customtkinter.CTkButton(self.janela4,text="",image=self.bto_buscar2, command=self.Atualizar_datapg)
        self.bto_buscar.place(relx=0.83, rely=0.880, relwidth=0.12, relheight=0.04)
        
        self.bto_apontar2 = tk.PhotoImage(file="imagens/button_nm/Relatorio.png")
        self.bto_apontar = customtkinter.CTkButton(self.abas1,text="",image=self.bto_apontar2, command=self.gerar_excel1)
        self.bto_apontar.place(relx=0.240, rely=0.78, relwidth=0.58, relheight=0.15)

        self.bto_apontar1 = tk.PhotoImage(file="imagens/button_nm/Relatorio.png")
        self.bto_apontar = customtkinter.CTkButton(self.abas2,text="",image=self.bto_apontar1, command=self.gerar_excel2)
        self.bto_apontar.place(relx=0.240, rely=0.78, relwidth=0.58, relheight=0.15)

        self.bto_filtro2 = tk.PhotoImage(file="imagens/button_nm/FILTRO.png")
        self.bto_filtro = customtkinter.CTkButton(self.abas1,text="", image=self.bto_filtro2, command=self.Filtrodata)
        self.bto_filtro.place(relx=0.240, rely=0.60, relwidth=0.58, relheight=0.15)

        self.bto_filtro3 = tk.PhotoImage(file="imagens/button_nm/FILTRO.png")
        self.bto_filtro1 = customtkinter.CTkButton(self.abas2,text="",image=self.bto_filtro2, command=self.Filtrodata1)
        self.bto_filtro1.place(relx=0.240, rely=0.60, relwidth=0.58, relheight=0.15)
    def Image(self):
        self.image01 = tk.PhotoImage(file="imagens/modelo01.png")
        self.image = customtkinter.CTkLabel(master=self.janela4,text="",image=self.image01)
        self.image.place(relx=0.7901 , rely=0.925)
        