from biblioteca_tk import *
from tkinter.filedialog import askopenfilename
import banco_dados
import sqlite3
from sqlite3 import Error
image_data= b''

def tela_cadastro():

    cadastro = tk.Toplevel()
    cadast = Cadastro(cadastro)
class Funcs():
    def limpa_tela_semfoto(self):
        self.entry_tipo.delete(0, END)
        self.entry_nome1.delete(0, END)
        self.entry_cpf1.delete(0, END)
        self.entry_banco1.delete(0, END)
        self.entry_agencia1.delete(0, END)
        self.entry_conta1.delete(0, END)
        self.entry_pix1.delete(0, END)
        self.entry_supr.delete(0, END)
    def limpa_tela(self):
        global image_data
        self.entry_tipo.delete(0, END)
        self.entry_nome1.delete(0, END)
        self.entry_cpf1.delete(0, END)
        self.entry_banco1.delete(0, END)
        self.entry_agencia1.delete(0, END)
        self.entry_conta1.delete(0, END)
        self.entry_pix1.delete(0, END)
        self.entry_supr.delete(0, END)
        self.img_label.config(image=self.img_padao)
        image_data = b''
    def variaveis(self):
        self.tipo= self.entry_tipo.get()
        self.nome= self.entry_nome1.get()
        self.cpf= self.entry_cpf1.get()
        self.banco= self.entry_banco1.get()
        self.agencia= self.entry_agencia1.get()
        self.conta= self.entry_conta1.get()
        self.pix= self.entry_pix1.get()
        self.supr = self.entry_supr.get()
    def add_registro(self):
        con=sqlite3.connect('registro.db')
        cursor = con.cursor()
        self.variaveis()
        cursor.execute(f"INSERT INTO contas_tb (tipo, nome_completo, cpf1, banco, agencia, conta, pix, foto, supervisor1) VALUES ('{self.tipo}' , '{self.nome}' , '{self.cpf}', '{self.banco}', '{self.agencia}', '{self.conta}', '{self.pix}', ? , '{self.supr}')",[self.image_data])
        con.commit()
        con.close()
        self.limpa_tela()
        self.select_lista()
    def select_lista(self):
        self.listacli.delete(*self.listacli.get_children())
        my_tag='normal'
        vquery="SELECT tipo, nome_completo, cpf1, banco, agencia, conta, pix , foto FROM contas_tb order by nome_completo ASC"
        lista = banco_dados.dql(vquery)
        for i in lista:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end', text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6]),tags=(my_tag))
    def select_lista_semfoto(self):
        self.listacli.delete(*self.listacli.get_children())
        vquery="SELECT tipo, nome_completo, cpf1, banco, agencia, conta, pix FROM contas_tb order by nome_completo ASC"
        lista = banco_dados.dql(vquery)
        for i in lista:
            self.listacli.insert("", "end", values=i)
    def buscar(self, event):
        self.variaveis()
        nome_dados= self.entry_nome1.get()
        self.listacli.delete(*self.listacli.get_children())
        vquery="SELECT tipo , nome_completo , cpf1 , banco , agencia , conta , pix FROM contas_tb WHERE nome_completo = '{}'".format(nome_dados)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            self.listacli.insert("", "end", values=i)
    def buscartudo(self):
        my_tag='normal'
        self.listacli.delete(*self.listacli.get_children())
        vquery="SELECT tipo, nome_completo, cpf1, banco, agencia, conta, pix FROM contas_tb order by nome_completo ASC"
        lista = banco_dados.dql(vquery)
        for i in lista:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end', text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6]),tags=(my_tag))
    def altera_dados(self):
        con=sqlite3.connect('registro.db')
        cursor = con.cursor()
        self.variaveis()
        self.listacli.delete(*self.listacli.get_children())
        cursor.execute("UPDATE contas_tb SET tipo=?, nome_completo=?, cpf1=?, banco=?, agencia=?, conta=?, pix=?, foto=?, supervisor1=? WHERE nome_completo=?", (self.tipo, self.nome, self.cpf, self.banco, self.agencia, self.conta, self.pix, self.image_data, self.supr, self.nome))
        con.commit()
        con.close()
    def buscardados(self):
        self.variaveis()
        self.buscar()
        self.limpa_tela()
        global image_data,img
        image_data= b''
        seleciona = "SELECT foto FROM contas_tb WHERE LIKE nome_completo = '{}'".format(self.nome)
        lista = banco_dados.dql(seleciona)
        if lista[0] != b'':
            image_data = lista[0][0]
            img_data = lista[0][0]
              
            with open('.temp_pic', 'wb')as write_img:
                write_img.write(img_data)
                write_img.close()

            img = ImageTk.PhotoImage(Image.open('.temp_pic'))
            self.img_label.config(image=img)
    def OuDoubleClick(self,event):
        self.limpa_tela_semfoto()
        self.listacli.selection()
        
        for n in self.listacli.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listacli.item(n, 'values')
            self.entry_tipo.insert(END, col1)
            self.entry_nome1.insert(END, col2)
            self.entry_cpf1.insert(END, col3)
            self.entry_banco1.insert(END, col4)
            self.entry_agencia1.insert(END, col5)
            self.entry_conta1.insert(END, col6)
            self.entry_pix1.insert(END, col7)
    def ler_abrir_image(self):
        global image_data,img
        
        path = askopenfilename()
        if path:
            self.ler_image = open(path,"rb")
            self.image_data = self.ler_image.read()
            self.ler_image.close

            img = ImageTk.PhotoImage(Image.open(path))
            self.img_label.config(image=img)       
    def delete_image(self):
        global image_data
        image_data = b''
        self.img_label.config(image=self.img_padao)
    def deletar_cliente(self, event):
        try:
            itemSelecionados=self.listacli.selection()[0]
            self.listacli.delete(itemSelecionados)
            vquery="DELETE FROM contas_tb WHERE seg='"+itemSelecionados+"'"
            linhas = banco_dados.dml(vquery)
            messagebox.showinfo(title="OK", message="Seguencia Deletada")
        except:
            messagebox.showinfo(title="ERRO", message="Selecione a Seguencia")
    def Treeview_colrs(self):
        my_tag='normal'
        vquery="SELECT tipo, nome_completo, cpf1, banco, agencia, conta, pix FROM contas_tb order by nome_completo ASC"
        lista = banco_dados.dql(vquery)
        for i in lista:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listacli.insert("", 'end', text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6]),tags=(my_tag))
class Cadastro(Funcs):
    def __init__(self,cadastro):
        self.janela3 = cadastro
        self.tela_cadastro()
        self.frames()
        self.TreeView()
        self.label_01()
        self.imagem()
        self.imagem_perfil()
        self.botao()
        cadastro.mainloop()       
    def tela_cadastro(self):
        self.janela3.title('CADASTRO DE CONTA')
        self.janela3.geometry("1155x700")
        self.janela3.minsize(1155,700) 
        self.janela3.maxsize(1155,700) 
        self.janela3.configure(bg = 'white')
        self.janela3.resizable(True, True)
        self.janela3.iconbitmap('imagens\logoicoo.ico')
    def imagem(self):
        self.img1 = tk.PhotoImage(file="imagens/modelo010.png")
        self.imga1 = customtkinter.CTkLabel(self.janela3,text="", image=self.img1)
        self.imga1.place(relx=0, rely=0)

        self.img2 = tk.PhotoImage(file="imagens/cadastro.png")
        self.imga2 = customtkinter.CTkLabel(self.frame2,text="", image=self.img2)
        self.imga2.place(relx=0.095 , rely=0.01)
    def imagem_perfil(self):
        self.img_padao= tk.PhotoImage(file="imagens/perfil1.png")
        self.img_label= tk.Label(self.frame3,text="", image=self.img_padao, relief=tk.SOLID)
        self.img_label.pack()
    def frames(self):
        #frame das TreeView
        self.frame1 = Frame(self.janela3, bd = 2, bg = 'white')
        self.frame1.place(relx= 0 , rely=0.06, relwidth= 0.78,relheight= 0.938)
        #frame das entrys e label
        self.frame2 = Frame(self.janela3, bd = 2, bg = 'white')
        self.frame2.place(relx= 0.780, rely=0.06, relwidth= 0.22,relheight= 0.938)
        #frame da foto de perfil
        self.frame3 = Frame(self.frame2, bd = 2,
                            highlightbackground= 'white', highlightthickness=2 )
        self.frame3.place(relx=0.320 , rely=0.700, relwidth= 0.40,relheight= 0.19)
    def TreeView(self):#TreeView
        colmun = ("col1","col2","col3","col4","col5","col6","col7")
        self.listacli =ttk.Treeview(self.frame1, height=3,columns=colmun,show="headings")
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="TIPO")
        self.listacli.heading("#2", text="NOME COMPLETO")
        self.listacli.heading("#3", text="CPF")
        self.listacli.heading("#4", text="BANCO")
        self.listacli.heading("#5", text="AGENCIA")
        self.listacli.heading("#6", text="CONTA")
        self.listacli.heading("#7", text="PIX")
    
        self.listacli.column("#0", width=1)
        self.listacli.column("#1", width=65)
        self.listacli.column("#2", width=200)
        self.listacli.column("#3", width=100)
        self.listacli.column("#4", width=100)
        self.listacli.column("#5", width=60)
        self.listacli.column("#6", width=100)
        self.listacli.column("#7", width=250)
        
        self.listacli.tag_configure('gray', background='#D9EAF6')
        self.listacli.tag_configure('normal', background='white')

        self.listacli.place(relx=0,rely=0,relwidth=0.98,relheight=0.99)

        self.barra_rolagem=Scrollbar(self.frame1, orient="vertical")
        self.listacli.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listacli.yview)
        self.barra_rolagem.place(relx=0.984, rely=0.002,relwidth=0.015, relheight=0.986)
        self.listacli.bind("<Double-1>",self.OuDoubleClick)
        self.Treeview_colrs()
    def label_01(self):#label e Entry
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
        def salvarStringVar(event):
            t.set(t.get().upper())
            n.set(n.get().upper())
            b.set(b.get().upper())
            a.set(a.get().upper())
            c.set(c.get().upper())
            p.set(p.get().upper())
            s.set(s.get().upper())
        self.label_tipo = customtkinter.CTkLabel(self.frame2, text="TIPO").place(relx=0.420 , rely=0.06)
        t = StringVar()
        self.entry_tipo  = customtkinter.CTkEntry(self.frame2, textvariable= t)
        self.entry_tipo.bind("<KeyRelease>",salvarStringVar)
        self.entry_tipo.place(relx=0.095 , rely=0.10, relwidth=0.80,relheight=0.04)

        self.label_nome1 = customtkinter.CTkLabel(self.frame2, text="NOME").place(relx=0.410 , rely=0.14)
        n = StringVar()
        self.entry_nome1 = customtkinter.CTkEntry(self.frame2, textvariable= n)
        self.entry_nome1.bind("<Return>",self.buscar)
        self.entry_nome1.bind("<KeyRelease>",salvarStringVar)
        self.entry_nome1.place(relx=0.095 , rely=0.18, relwidth=0.80,relheight=0.04)
        
        self.label_cpf1 = customtkinter.CTkLabel(self.frame2, text="CPF").place(relx=0.420 , rely=0.22)
        self.entry_cpf1 = customtkinter.CTkEntry(self.frame2)
        self.entry_cpf1.bind("<KeyRelease>", format_cpf)
        self.entry_cpf1.place(relx=0.095 , rely=0.26, relwidth=0.80,relheight=0.04)

        self.label_banco1 = customtkinter.CTkLabel(self.frame2, text="BANCO").place(relx=0.390 , rely=0.30)
        b = StringVar()
        self.entry_banco1 = customtkinter.CTkEntry(self.frame2, textvariable = b)
        self.entry_banco1.bind("<KeyRelease>",salvarStringVar)
        self.entry_banco1.place(relx=0.095 , rely=0.34, relwidth=0.80,relheight=0.04)

        self.label_agencia1 = customtkinter.CTkLabel(self.frame2, text="AGENCIA").place(relx=0.370 , rely=0.38)
        a = StringVar()
        self.entry_agencia1 = customtkinter.CTkEntry(self.frame2, textvariable = a)
        self.entry_agencia1.bind("<KeyRelease>",salvarStringVar)
        self.entry_agencia1.place(relx=0.095 , rely=0.42, relwidth=0.80,relheight=0.04)

        self.label_conta1 = customtkinter.CTkLabel(self.frame2, text="CONTA").place(relx=0.400 , rely=0.46)
        c = StringVar()
        self.entry_conta1 = customtkinter.CTkEntry(self.frame2, textvariable = c)
        self.entry_conta1.bind("<KeyRelease>",salvarStringVar)
        self.entry_conta1.place(relx=0.095 , rely=0.50, relwidth=0.80,relheight=0.04)

        self.label_pix1 = customtkinter.CTkLabel(self.frame2, text="PIX").place(relx=0.430 , rely=0.54)
        p = StringVar()
        self.entry_pix1 = customtkinter.CTkEntry(self.frame2, textvariable= p)
        self.entry_pix1.bind("<KeyRelease>",salvarStringVar)
        self.entry_pix1.place(relx=0.095 , rely=0.58, relwidth=0.80,relheight=0.04)

        self.label_supr = customtkinter.CTkLabel(self.frame2, text="SUPERVISOR").place(relx=0.340 , rely=0.62)
        s = StringVar()
        self.entry_supr  = customtkinter.CTkEntry(self.frame2, textvariable = s)
        self.entry_supr.bind("<KeyRelease>",salvarStringVar)
        self.entry_supr.place(relx=0.095 , rely=0.66, relwidth=0.80,relheight=0.04) 
    def botao(self):
        self.bto_gerar2 = tk.PhotoImage(file="imagens/button_nm/Apontar.png")
        self.bto_gerar = customtkinter.CTkButton(self.janela3,text="",image=self.bto_gerar2, command=self.add_registro)
        self.bto_gerar.place(relx=0.01 , rely=0.01,relwidth= 0.12, relheight=0.04)

        self.bto_altera2 = tk.PhotoImage(file="imagens/button_nm/AlterarDados.png")
        self.bto_altera = customtkinter.CTkButton(self.janela3,text="",image=self.bto_altera2, command=self.altera_dados)
        self.bto_altera.place(relx=0.135 , rely=0.01,relwidth= 0.12, relheight=0.04)

        self.bto_buscar2 = tk.PhotoImage(file="imagens/button_nm/BuscarDados.png")
        self.bto_buscar = customtkinter.CTkButton(self.janela3,text="",image=self.bto_buscar2, command=self.buscartudo)
        self.bto_buscar.place(relx=0.26 , rely=0.01,relwidth= 0.12, relheight=0.04)

        self.bto_lixo2 = tk.PhotoImage(file="imagens/button_nm/limpar.png")
        self.bto_lixo = customtkinter.CTkButton(self.janela3,text="",image=self.bto_lixo2, command=self.limpa_tela)
        self.bto_lixo.place(relx=0.385, rely=0.01,relwidth= 0.12, relheight=0.04)

        self.bto_img = customtkinter.CTkButton(self.frame2,text="ABRIR FOTO", command=self.ler_abrir_image)
        self.bto_img.place(relx=0.300, rely=0.900,relwidth= 0.43, relheight=0.04)

        self.bto_img = customtkinter.CTkButton(self.frame2,text="FECHAR FOTO", command=self.delete_image)
        self.bto_img.place(relx=0.300 , rely=0.950,relwidth= 0.43, relheight=0.04)

