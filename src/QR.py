import qrcode

# URL de la página de FANUC M-20iA
url = "https://www.fanucamerica.com/products/robots/series/m-20/m-20ia"

# Crear código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,  # Ajusta el tamaño si es necesario
    border=1,
)
qr.add_data(url)
qr.make(fit=True)

# Imprimir QR en la terminal
qr.print_ascii()
