import qrcode

# Formato padrão de um QR code PIX para pagamento
pix_payload = "00020126360014BR.GOV.BCB.PIX01163208924399954016BRL5802.005802.00.0000000000000006304BR5925DAVISON DO NASCIMENTO DIN6008Fortaleza61080540900062070503***6304F9F2"

# Cria o objeto QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adiciona os dados ao QR code
qr.add_data(pix_payload)
qr.make(fit=True)

# Cria uma imagem do QR code
img = qr.make_image(fill='black', back_color='white')

# Salva a imagem
img.save("pix_qr_code.png")
