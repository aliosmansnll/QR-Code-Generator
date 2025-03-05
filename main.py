import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

# QR Kod oluşturma fonksiyonu
def generate_qr():
    text = entry.get()
    if text:
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="lightgrey")  # QR renkleri
        img = img.resize((200, 200))  # Boyutu büyüt
        img.save("temp_qr.png")  # Geçici olarak kaydet

        img = Image.open("temp_qr.png")
        img = ImageTk.PhotoImage(img)

        qr_label.config(image=img)
        qr_label.image = img

# QR Kodunu kaydetme fonksiyonu
def save_qr():
    text = entry.get()
    if text:
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            qr = qrcode.make(text)
            qr.save(filename)

# Tkinter arayüzü
root = tk.Tk()
root.title("QR Kod Oluşturucu")
width = 600
height = 600

# Ekran genişliği ve yüksekliği
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Ortalanmış X ve Y pozisyonlarını hesapla
x = (screen_width - width) // 2
y = (screen_height - height) // 2

# Pencerenin boyutunu ve başlangıç pozisyonunu ayarla
root.geometry(f"{width}x{height}+{x}+{y}")
root.configure(bg="lightgray")  # Arka plan rengi
root.config(padx=34,pady=50)
root.resizable(False, False)

# Giriş kutusu
entry = tk.Entry(root, width=40, font=("Arial", 14), bg="white", fg="black", bd=3)
entry.grid(row=0,column=1,columnspan=3,padx=10, pady=20, sticky="ew")


# Butonlar
generate_button = tk.Button(root, text="QR Kod Oluştur", font=("Arial", 12, "bold"),
                            bg="white", fg="black", padx=10, pady=5, command=generate_qr,width=20,height=1)
generate_button.grid(row=1,column=1,padx=20,pady=20)

save_button = tk.Button(root, text="Kaydet", font=("Arial", 12, "bold"),
                        bg="white", fg="black", padx=10, pady=5, command=save_qr,width=20,height=1)
save_button.grid(row=1,column=3,padx=20,pady=20)

# QR kod etiketi
qr_label = tk.Label(root,bg='lightgrey')
qr_label.grid(row=3,column=1,columnspan=3)

# Tkinter döngüsü
root.mainloop()