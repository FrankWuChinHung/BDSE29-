import qrcode
from PIL import Image

# 定義網站URL
url = "https://8541-125-227-255-79.ngrok-free.app"

# 生成QR Code圖片
img = qrcode.make(url, box_size=10, border=2)

# 使用Pillow庫調整圖片大小
img = img.resize((300, 300), Image.ANTIALIAS)

# 儲存QR Code圖片
img.save("qrcode.png")

# 顯示QR Code圖片
img.show()
