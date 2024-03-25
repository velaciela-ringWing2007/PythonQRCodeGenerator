import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import qrcode
from PIL import Image, ImageTk


def create_qr_code():
    qr_text = text_area.get("1.0", "end-1c")  # テキストエリアからテキストを取得
    if qr_text.strip() == "":  # テキストが空かチェック
        messagebox.showinfo("エラー", "テキストが入力されていません。")
        return

    global qr_img  # 後で保存機能で使うためにグローバル変数として保持
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')
    show_qr_code(qr_img)


def show_qr_code(img):
    top = tk.Toplevel()
    top.title("QR Code")

    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(top, image=img)
    img_label.image = img  # レファレンスを保持
    img_label.pack()


def clear_text():
    text_area.delete("1.0", "end")


def save_qr_code():
    if qr_img is None:
        messagebox.showinfo("エラー", "QRコードが生成されていません。")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNGファイル", "*.png")])
    if not file_path:
        return
    qr_img.save(file_path)
    messagebox.showinfo("保存完了", "QRコードを保存しました。")


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
clear_button.pack(side=tk.LEFT, padx=10, pady=10)

save_button = tk.Button(root, text="PNGとして保存", command=save_qr_code)
save_button.pack(side=tk.RIGHT, padx=10, pady=10)

qr_img = None  # QRコードのイメージを保持するための変数

root.mainloop()
