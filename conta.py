import qrcode


qrcode_conta = {
"gabriel_martins_da_silva": "00020101021126580014br.gov.bcb.pix01367baa29f3-7896-4265-8a6c-a628f1c7952b5204000053039865802BR5918GABRIEL M DA SILVA6009FORTALEZA62070503***630453F3",
"gabriel_martins_da_": "00020101021126580014br.gov.bcb.pix01367baa29f3-7896-4265-8a6c-a628f1c7952b5204000053039865802BR5918GABRIEL M DA SILVA6009FORTALEZA62070503***630453F3",
"gabriel_martins" : "00020101021126580014br.gov.bcb.pix01367baa29f3-7896-4265-8a6c-a628f1c7952b5204000053039865802BR5918GABRIEL M DA SILVA6009FORTALEZA62070503***630453F3"



}

for nomes in qrcode_conta:
    qrconta = qrcode_conta[nomes]
    imagen_qrcode = qrcode.make(qrconta)
    imagen_qrcode.save(f"pix{nomes}.png")


def format_cpf(event = None):
    
    text = entry.get().replace("/", "").replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue
        if index in [1, 3]: new_text += text[index] + "/"
        else: new_text += text[index]

    entry.delete(0, "end")
    entry.insert(0, new_text)


from tkinter import *
screen = Tk()

entry = Entry(screen, font = ("Arial", 20))
entry.bind("<KeyRelease>", format_cpf)
entry.pack()
screen.mainloop()