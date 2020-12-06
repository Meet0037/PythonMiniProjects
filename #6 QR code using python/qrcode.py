import pyqrcode
from pyqrcode import QRCode
link = "https://github.com/Meet0037/PythonMiniProjects"
qr_url = pyqrcode.create(link)
qr_url.svg("pythonminiproject.svg",scale=20)
