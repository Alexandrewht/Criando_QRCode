import pyqrcode
from pathlib import Path

DIR = Path(__file__).parent

qr_url = 'https://github.com/Alexandrewht'
qr_code = pyqrcode.create(qr_url)
save_qrcode = DIR / 'qr_code_github.png'

qr_code.png(
    file = save_qrcode,
    scale = 10,
)
