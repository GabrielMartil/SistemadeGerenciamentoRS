from biblioteca_tk import *
import funcao
import banco_dados
import parceiro
import csv
import pandas as pd



def tela_registro():
    
    registro = tk.Toplevel()
    aplicacao = jt_registro(registro)
class Funcs():
    def limpa_tela(self):
        self.entry_seg.delete(0, END)
        self.entry_cpf.delete(0, END)
        self.entry_tipo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_data.delete(0, END)
        self.entry_supr.delete(0, END)
        self.entry_parceiro.delete(0, END)
        self.entry_valor.delete(0, END)
        self.entry_obs.delete(0, END)
        self.entry_data_pg.delete(0, END)
    def limpa_tela2(self):
        self.entry_seg2.delete(0, END)
        self.entry_cpf2.delete(0, END)
        self.entry_tipo2.delete(0, END)
        self.entry_nome2.delete(0, END)
        self.entry_data2.delete(0, END)
        self.entry_supr2.delete(0, END)
        self.entry_parceiro2.delete(0, END)
        self.entry_valor2.delete(0, END)
        self.entry_obs2.delete(0, END)
        self.entry_data_pg2.delete(0, END)
    def variaveis(self):
        self.seg= self.entry_seg.get()
        self.cpf= self.entry_cpf.get()
        self.tipo= self.entry_tipo.get()
        self.nome= self.entry_nome.get()
        self.data= self.entry_data.get()
        self.supr=self.entry_supr.get()
        self.parceiro= self.entry_parceiro.get()
        self.valor= self.entry_valor.get()
        self.obs= self.entry_obs.get()
        self.data_pg = self.entry_data_pg.get()
    def buscar(self):
        self.variaveis()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d',sum(valor)) , obs , data_pg FROM base_dados GROUP BY seg WHERE DESC "
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
    def altera_dados(self):
        self.variaveis()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="UPDATE base_dados SET cpf= '"+self.cpf+"' , tipo1 = '"+self.tipo+"', nome = '"+self.nome+"', data = '"+self.data+"', supervisor = '"+self.supr+"', parceiro = '"+self.parceiro+"', valor = '"+self.valor+"', obs = '"+self.obs+"' , data_pg = '"+self.data_pg+"'  WHERE seg = '"+self.seg+"' "
        linhas = banco_dados.dml(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
    def deletar_cliente(self, event):
        try:
            itemSelecionados=self.listregist.selection()[0]
            self.listregist.delete(itemSelecionados)
            vquery="DELETE FROM base_dados WHERE seg='"+itemSelecionados+"'"
            linhas = banco_dados.dml(vquery)
            messagebox.showinfo(title="OK", message="Seguencia Deletada")
        except:
            messagebox.showinfo(title="ERRO", message="Selecione a Seguencia")
    def OuDoubleClick(self, event):
        self.limpa_tela()
        self.listregist.selection()

        for n in self.listregist.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.listregist.item(n, 'values')
            self.entry_seg.insert(END, col1)
            self.entry_cpf.insert(END, col2)
            self.entry_tipo.insert(END, col3)
            self.entry_nome.insert(END, col4)
            self.entry_data.insert(END, col5)
            self.entry_supr.insert(END, col6)
            self.entry_parceiro.insert(END, col7)
            self.entry_valor.insert(END, col8)
            self.entry_obs.insert(END, col9)
            self.entry_data_pg.insert(END, col10)
    def altocomplete(self):
        self.variaveis()
        self.listregist.delete(*self.listregist.get_children())
        vquery="SELECT cpf1 FROM contas_tb WHERE cpf1 LIKE '%"+self.cpf+"%'"
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            self.listregist.insert("", "end", values=i)
    def Treeview_colrs(self):
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg, cpf, tipo1, nome, data, supervisor, parceiro, printf('R$ %d,%d%d', sum(valor)), obs, MAX(data_pg) FROM base_dados GROUP BY seg ORDER BY seg DESC"
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
    def Busc_seg(self,event):
        self.variaveis()
        seg_01= self.entry_seg2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE seg = '{}'".format(seg_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_cpf(self,event):
        self.variaveis()
        cpf_01= self.entry_cpf2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE cpf = '{}'".format(cpf_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_tipo(self,event):
        self.variaveis()
        tipo_01= self.entry_tipo2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE tipo1 = '{}'".format(tipo_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_nome(self,event):
        self.variaveis()
        nome_01= self.entry_nome2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE nome = '{}'".format(nome_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_data(self,event):
        self.variaveis()
        data_01= self.entry_data2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE data = '{}'".format(data_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_supervisor(self,event):
        self.variaveis()
        super_01= self.entry_supr2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE supervisor = '{}'".format(super_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_parceiro(self,event):
        self.variaveis()
        parceiro_01= self.entry_parceiro2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE parceiro = '{}'".format(parceiro_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_valor(self,event):
        self.variaveis()
        valor_01= self.entry_valor2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE valor = '{}'".format(valor_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_obs(self,event):
        self.variaveis()
        obs_01= self.entry_obs2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE obs = '{}'".format(obs_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
    def Busc_data_pg(self,event):
        self.variaveis()
        data_01= self.entry_data_pg2.get()
        self.listregist.delete(*self.listregist.get_children())
        my_tag='normal'
        vquery="SELECT seg , cpf , tipo1, nome , data , supervisor , parceiro , printf('R$ %d,%d%d', valor) , obs , data_pg FROM base_dados WHERE data_pg = '{}'".format(data_01)
        linhas = banco_dados.dql(vquery)
        for i in linhas:
            if (my_tag =='gray'):
                my_tag = 'normal' 
            else: 
                my_tag ='gray' 
            self.listregist.insert("", 'end',iid=i[0], text=i[0],
                values =(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]),tags=(my_tag))
        self.limpa_tela2()
class jt_registro(Funcs):
    def __init__(self,registro):
        self.janela2 = (registro)
        self.tela()
        self.menu()
        self.frames()
        self.label()
        self.label02()
        self.TreeView()
        self.botao()
        self.imagem()
        registro.mainloop()
    def tela(self):
        self.janela2.title('REGISTROS')
        self.janela2.geometry("1135x700")
        self.janela2.minsize(1135,700)
        self.janela2.maxsize(1135,700)
        self.janela2.configure(bg = 'white')
        self.janela2.iconbitmap('imagens\logoicoo.ico')
        self.janela2.resizable(True, True)
    def dowlond(self):
        cols = ['SEQ','CPF','TIPO','DIARISTA','DATA','SUPERVISOR','PARCEIRO','VALOR', 'OBS', 'DATA PG'] # Your column headings here
        path = 'Diarias_pg/REGISTRO.csv'
        excel_name = 'Diarias_pg/REGISTRO.xlsx'
        lst = []
        
        with open(path, "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for i ,linha in enumerate(self.listregist.get_children()):
                row = self.listregist.item(linha,'values')
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
    def tela_parceiro(self):
        parceiro.tela_parceiro()
    def tela_diarista(self):
        parceiro.tela_diarista()
    def tela_pagamentos(self):
        parceiro.tela_pagamento()
    def frames(self):
        
        self.frame1 = Frame(self.janela2, bd = 2, bg = 'white')
        self.frame1.place(relx= 0 , rely=0.06, relwidth= 0.81,relheight= 0.93)

        self.frame2 = Frame(self.janela2, bd = 2, bg = 'white')
        self.frame2.place(relx= 0.815 , rely=0.06, relwidth= 0.177,relheight= 0.93)

        self.notebook=ttk.Notebook(self.frame2)
        self.notebook.place(relx= 0 , rely=0.10, relwidth= 0.98, relheight= 0.90)

        self.abas1 = Frame(self.notebook)
        self.notebook.add(self.abas1,text="ALTERAR")

        self.abas2 = Frame(self.notebook)
        self.notebook.add(self.abas2,text="BUSCAR")
    def gerando_arquivo1(self):
        funcao.Gerador_arquivo()
    def imagem(self):
        self.img2 = tk.PhotoImage(file="imagens/registro_nome.png")
        self.imga2 = customtkinter.CTkLabel(master=self.frame2,text="",image=self.img2)
        self.imga2.place(relx=0.02, rely=0.05, relwidth=0.95)

        self.img1 = tk.PhotoImage(file="imagens/nomers.png")
        self.imga1 = customtkinter.CTkLabel(master=self.janela2,text="",image=self.img1)
        self.imga1.place(relx=0.50, rely=0.004)
        """self.img2 = tk.PhotoImage(file="imagens/logo2.png")
        self.imga2 = customtkinter.CTkLabel(self.janela2, image=self.img2, bg = "#BEBEBE").place(relx=0.01, rely=0)"""
    def label(self):

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
        def format_data2(event = None):
            data = self.entry_data_pg.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_data_pg.delete(0, "end")
            self.entry_data_pg.insert(0, new_data)
        def salvarStringVar(event):
            tipo.set(tipo.get().upper())
            nome.set(nome.get().upper())
            super.set(super.get().upper())
            parc.set(parc.get().upper())
            obs.set(obs.get().upper())
            
        self.label_seg = customtkinter.CTkLabel(self.abas1, text="SEQ").place(relx=0.420 , rely=0)
        self.entry_seg = customtkinter.CTkEntry(self.abas1)
        self.entry_seg.place(relx=0.095 , rely=0.04, relwidth=0.80,relheight=0.045)
        
        self.label_cpf = customtkinter.CTkLabel(self.abas1, text="CPF").place(relx=0.420 , rely=0.087)
        self.entry_cpf = customtkinter.CTkEntry(self.abas1)
        self.entry_cpf.bind("<KeyRelease>", format_cpf)
        self.entry_cpf.place(relx=0.095 , rely=0.13, relwidth=0.80,relheight=0.045)
        
        self.label_tipo = customtkinter.CTkLabel(self.abas1, text="TIPO").place(relx=0.410 , rely=0.177)
        tipo = StringVar()
        self.entry_tipo = customtkinter.CTkEntry(self.abas1, textvariable= tipo)
        self.entry_tipo.bind("<KeyRelease>",salvarStringVar)
        self.entry_tipo.place(relx=0.095 , rely=0.22, relwidth=0.80,relheight=0.045)
        
        self.label_nome = customtkinter.CTkLabel(self.abas1, text="NOME COMPLETO").place(relx=0.220 , rely=0.267)
        nome = StringVar()
        self.entry_nome = customtkinter.CTkEntry(self.abas1, textvariable= nome)
        self.entry_nome.bind("<KeyRelease>",salvarStringVar)
        self.entry_nome.place(relx=0.095 , rely=0.31, relwidth=0.80,relheight=0.045)
        
        self.label_data =  customtkinter.CTkLabel(self.abas1, text="DATA").place(relx=0.410 , rely=0.357)
        self.entry_data =  customtkinter.CTkEntry(self.abas1)
        self.entry_data.bind('<KeyRelease>', format_data)
        self.entry_data.place(relx=0.095 , rely=0.40, relwidth=0.80,relheight=0.045)
        
        self.label_supr = customtkinter.CTkLabel(self.abas1, text="SUPERVISOR").place(relx=0.300 , rely=0.447)
        super = StringVar()
        self.entry_supr = customtkinter.CTkEntry(self.abas1, textvariable= super)
        self.entry_supr.bind("<KeyRelease>",salvarStringVar)
        self.entry_supr.place(relx=0.095 , rely=0.49, relwidth=0.80,relheight=0.045)
        
        self.label_parceiro = customtkinter.CTkLabel(self.abas1, text="PARCEIRO").place(relx=0.350 , rely=0.537)
        parc = StringVar()
        self.entry_parceiro = customtkinter.CTkEntry(self.abas1, textvariable= parc)
        self.entry_parceiro.bind("<KeyRelease>",salvarStringVar)
        self.entry_parceiro.place(relx=0.095 , rely=0.58, relwidth=0.80,relheight=0.045)
        
        self.label_valor =  customtkinter.CTkLabel(self.abas1, text="VALOR").place(relx=0.400 , rely=0.627)
        self.entry_valor =  customtkinter.CTkEntry(self.abas1)
        self.entry_valor.place(relx=0.095 , rely=0.67, relwidth=0.80,relheight=0.045)

        self.label_obs =  customtkinter.CTkLabel(self.abas1, text="OBSERVAÇÃO").place(relx=0.300 , rely=0.717)
        obs = StringVar()
        self.entry_obs =  customtkinter.CTkEntry(self.abas1, textvariable= obs)
        self.entry_obs.bind("<KeyRelease>",salvarStringVar)
        self.entry_obs.place(relx=0.095 , rely=0.76, relwidth=0.80,relheight=0.045)

        self.label_data_pg =  customtkinter.CTkLabel(self.abas1, text="DATA PG").place(relx=0.360 , rely=0.807)
        self.entry_data_pg =  customtkinter.CTkEntry(self.abas1)
        self.entry_data_pg.bind('<KeyRelease>', format_data2)
        self.entry_data_pg.place(relx=0.095 , rely=0.85, relwidth=0.80,relheight=0.045)
    def label02(self):

        def format_cpf(event = None):
    
            text = self.entry_cpf2.get().replace(".", "").replace("-", "")[:11]
            new_text = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(text)):
                
                if not text[index] in "0123456789": continue
                if index in [2, 5]: new_text += text[index] + "."
                elif index == 8: new_text += text[index] + "-"
                else: new_text += text[index]

            self.entry_cpf2.delete(0, "end")
            self.entry_cpf2.insert(0, new_text)
        def format_data(event = None):
            data = self.entry_data2.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_data2.delete(0, "end")
            self.entry_data2.insert(0, new_data) 
        def format_data2(event = None):
            data = self.entry_data_pg2.get().replace("/", "").replace("/", "")[:8]
            new_data = ""

            if event.keysym.lower() == "backspace": return
            
            for index in range(len(data)):
                
                if not data[index] in "0123456789": continue
                if index in [1, 3]: new_data += data[index] + "/"
                else: new_data += data[index]

            self.entry_data_pg2.delete(0, "end")
            self.entry_data_pg2.insert(0, new_data)
        def salvarStringVar(event):
            tipo2.set(tipo2.get().upper())
            nome2.set(nome2.get().upper())
            super2.set(super2.get().upper())
            parc2.set(parc2.get().upper())
            obs2.set(obs2.get().upper())

        self.label_seg2 = customtkinter.CTkLabel(self.abas2, text="SEQ").place(relx=0.420 , rely=0)
        self.entry_seg2 = customtkinter.CTkEntry(self.abas2)
        self.entry_seg2.bind("<Return>",self.Busc_seg)
        self.entry_seg2.place(relx=0.095 , rely=0.04, relwidth=0.80,relheight=0.045)
        
        self.label_cpf2 = customtkinter.CTkLabel(self.abas2, text="CPF").place(relx=0.420 , rely=0.087)
        self.entry_cpf2 = customtkinter.CTkEntry(self.abas2)
        self.entry_cpf2.bind("<Return>",self.Busc_cpf)
        self.entry_cpf2.bind("<KeyRelease>", format_cpf)
        self.entry_cpf2.place(relx=0.095 , rely=0.13, relwidth=0.80,relheight=0.045)
        
        self.label_tipo2 = customtkinter.CTkLabel(self.abas2, text="TIPO").place(relx=0.410 , rely=0.177)
        tipo2 = StringVar()
        self.entry_tipo2 = customtkinter.CTkEntry(self.abas2, textvariable= tipo2)
        self.entry_tipo2.bind("<KeyRelease>",salvarStringVar)
        self.entry_tipo2.bind("<Return>",self.Busc_tipo)
        self.entry_tipo2.place(relx=0.095 , rely=0.22, relwidth=0.80,relheight=0.045)
        
        self.label_nome2 = customtkinter.CTkLabel(self.abas2, text="NOME COMPLETO").place(relx=0.220 , rely=0.267)
        nome2 = StringVar()
        self.entry_nome2 = customtkinter.CTkEntry(self.abas2, textvariable= nome2)
        self.entry_nome2.bind("<KeyRelease>",salvarStringVar)
        self.entry_nome2.bind("<Return>",self.Busc_nome)
        self.entry_nome2.place(relx=0.095 , rely=0.31, relwidth=0.80,relheight=0.045)
        
        self.label_data2 =  customtkinter.CTkLabel(self.abas2, text="DATA").place(relx=0.410 , rely=0.357)
        self.entry_data2 =  customtkinter.CTkEntry(self.abas2)
        self.entry_data2.bind("<Return>",self.Busc_data)
        self.entry_data2.bind('<KeyRelease>', format_data)
        self.entry_data2.place(relx=0.095 , rely=0.40, relwidth=0.80,relheight=0.045)
        
        self.label_supr2 = customtkinter.CTkLabel(self.abas2, text="SUPERVISOR").place(relx=0.300 , rely=0.447)
        super2 = StringVar()
        self.entry_supr2 = customtkinter.CTkEntry(self.abas2, textvariable= super2)
        self.entry_supr2.bind("<KeyRelease>",salvarStringVar)
        self.entry_supr2.bind("<Return>",self.Busc_supervisor)
        self.entry_supr2.place(relx=0.095 , rely=0.49, relwidth=0.80,relheight=0.045)
        
        self.label_parceiro2 = customtkinter.CTkLabel(self.abas2, text="PARCEIRO").place(relx=0.350 , rely=0.537)
        parc2 = StringVar()
        self.entry_parceiro2 = customtkinter.CTkEntry(self.abas2, textvariable= parc2)
        self.entry_supr2.bind("<KeyRelease>",salvarStringVar)
        self.entry_parceiro2.bind("<Return>",self.Busc_parceiro)
        self.entry_parceiro2.place(relx=0.095 , rely=0.58, relwidth=0.80,relheight=0.045)
        
        self.label_valor2 =  customtkinter.CTkLabel(self.abas2, text="VALOR").place(relx=0.400 , rely=0.627)
        self.entry_valor2 =  customtkinter.CTkEntry(self.abas2)
        self.entry_valor2.bind("<Return>",self.Busc_valor)
        self.entry_valor2.place(relx=0.095 , rely=0.67, relwidth=0.80,relheight=0.045)

        self.label_obs2 =  customtkinter.CTkLabel(self.abas2, text="OBSERVAÇÃO").place(relx=0.300 , rely=0.717)
        obs2 = StringVar()
        self.entry_obs2 =  customtkinter.CTkEntry(self.abas2, textvariable= obs2)
        self.entry_obs2.bind("<KeyRelease>",salvarStringVar)
        self.entry_obs2.bind("<Return>",self.Busc_obs)
        self.entry_obs2.place(relx=0.095 , rely=0.76, relwidth=0.80,relheight=0.045)

        self.label_data_pg2 =  customtkinter.CTkLabel(self.abas2, text="DATA PG").place(relx=0.360 , rely=0.807)
        self.entry_data_pg2 =  customtkinter.CTkEntry(self.abas2)
        self.entry_data_pg2.bind("<Return>",self.Busc_data_pg)
        self.entry_data_pg2.bind('<KeyRelease>', format_data2)
        self.entry_data_pg2.place(relx=0.095 , rely=0.85, relwidth=0.80,relheight=0.045)
    def TreeView(self):
        column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10")
        self.listregist =ttk.Treeview(self.frame1, height=3,columns=column, show="headings")
        self.listregist.heading("#0", text="")
        self.listregist.heading("#1", text="SEQ")
        self.listregist.heading("#2", text="CPF")
        self.listregist.heading("#3", text="TIPO")
        self.listregist.heading("#4", text="DIARISTA")
        self.listregist.heading("#5", text="DATA")
        self.listregist.heading("#6", text="SUPERVISOR")
        self.listregist.heading("#7", text="PARCEIRO")
        self.listregist.heading("#8", text="VALOR")
        self.listregist.heading("#9", text="OBS")
        self.listregist.heading("#10", text="DATA PG")

        self.listregist.column("#0", width=1)
        self.listregist.column("#1", width=5)
        self.listregist.column("#2", width=60)
        self.listregist.column("#3", width=30)
        self.listregist.column("#4", width=150)
        self.listregist.column("#5", width=50)
        self.listregist.column("#6", width=50, anchor=tk.CENTER)
        self.listregist.column("#7", width=60)
        self.listregist.column("#8", width=40, anchor=tk.CENTER)
        self.listregist.column("#9", width=100)
        self.listregist.column("#10", width=40)

        self.listregist.tag_configure('gray', background='#D9EAF6')
        self.listregist.tag_configure('normal', background='white')

    

        self.listregist.place(relx=0.001,rely=0.005,relwidth=0.98,relheight=0.99)

        self.barra_rolagem=Scrollbar(self.frame1, orient="vertical")
        self.listregist.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.config(command=self.listregist.yview)
        self.barra_rolagem.place(relx=0.985, rely=0.005,relwidth=0.014, relheight=0.99)
        self.listregist.bind("<Double-1>", self.OuDoubleClick)
        self.listregist.bind("<Delete>",self.deletar_cliente)
        self.Treeview_colrs()
    def menu(self):
        menubar = Menu(self.janela2)
        self.janela2.config(menu=menubar)
                # create a menubar
        menubar = Menu(self.janela2)
        self.janela2.config(menu=menubar)
        # create the file_menu
        file_menu = Menu(
            menubar,
            tearoff=0
        )
        # add menu items to the File menu
        file_menu.add_command(label='Parceiros', command=self.tela_parceiro)
        file_menu.add_command(label='Diaristas', command=self.tela_diarista)
        file_menu.add_command(label='Pagamentos', command=self.tela_pagamentos)
        file_menu.add_separator()
        file_menu.add_command(label='Relatório', command=self.dowlond)
        # add the File menu to the menubar
        menubar.add_cascade(
            label="Menu",
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
    def botao(self):
        ##button aba1
        self.bto_alterdados2 = tk.PhotoImage(file="imagens/button_nm/AlterarDados.png")
        self.bto_alterdados = customtkinter.CTkButton(master=self.janela2,text="",image=self.bto_alterdados2, command=self.altera_dados)
        self.bto_alterdados.place(relx=0.17 , rely=0.01, relwidth=0.12, relheight=0.04)

        self.bto_limpa2 = tk.PhotoImage(file="imagens/button_nm/Limpar.png")
        self.bto_limpa = customtkinter.CTkButton(self.abas1,text="", image=self.bto_limpa2, command=self.limpa_tela)
        self.bto_limpa.place(relx=0.12 , rely=0.93, relwidth=0.75, relheight=0.055)

        self.bto_buscar2 = tk.PhotoImage(file="imagens/button_nm/BuscarDados.png")
        self.bto_buscar = customtkinter.CTkButton(master=self.janela2,text="" ,image=self.bto_buscar2, command=self.Treeview_colrs)
        self.bto_buscar.place(relx=0.03 , rely=0.01, relwidth=0.12, relheight=0.04)
       
    