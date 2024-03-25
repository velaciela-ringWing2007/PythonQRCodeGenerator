import tkinter as tk
from tkinter import scrolledtext
import qrcode
from PIL import Image, ImageTk


def create_qr_code():
    qr_text = text_area.get("1.0", "end-1c")  # テキストエリアからテキストを取得
    if qr_text.strip() == "":  # テキストが空かチェック
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white').convert('RGB')
    show_qr_code(img)


def show_qr_code(img):
    top = tk.Toplevel()
    top.title("QR Code")

    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(top, image=img)
    img_label.image = img  # レファレンスを保持
    img_label.pack()


def clear_text():
    text_area.delete("1.0", "end")


# GUIの作成
root = tk.Tk()
root.title("QR Code Generator")

# スクロール付きテキストエリア
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
text_area.pack(padx=10, pady=10)

# ボタン
create_button = tk.Button(root, text="QRコード作成", command=create_qr_code)
create_button.pack(side=tk.LEFT, padx=10, pady=10)

clear_button = tk.Button(root, text="クリア", command=clear_text)
clear_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
