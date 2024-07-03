import pyqrcode

qr_url = 'https://github.com/Alexandrewht'
qr_code = pyqrcode.create(qr_url)

qr_code.png(
    file='qr_code.png',
    scale=8,
)