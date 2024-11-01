import random
import tkinter as tk
from tkinter import messagebox

# Olası seçenekler
SECENEKLER = ['Taş', 'Kağıt', 'Makas']

def bilgisayar_secimi():
    return random.choice(SECENEKLER)

def oyunu_oyna(oyuncu_secimi):
    bilgisayar_secimi_ = bilgisayar_secimi()
    if oyuncu_secimi == bilgisayar_secimi_:
        sonuc = f"Berabere! Her ikisi de {oyuncu_secimi} seçti."
    elif (oyuncu_secimi == 'Taş' and bilgisayar_secimi_ == 'Makas') or \
         (oyuncu_secimi == 'Makas' and bilgisayar_secimi_ == 'Kağıt') or \
         (oyuncu_secimi == 'Kağıt' and bilgisayar_secimi_ == 'Taş'):
        sonuc = f"Sen kazandın! {oyuncu_secimi}, {bilgisayar_secimi_}'yı yener."
    else:
        sonuc = f"Bilgisayar kazandı! {bilgisayar_secimi_}, {oyuncu_secimi}'yi yener."
    
    # Sonucu göster
    messagebox.showinfo("Sonuç", sonuc)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Taş, Kağıt, Makas Oyunu")
root.geometry("400x300")
root.configure(bg="#4a4a4a")

# Başlık etiketi
baslik_etiketi = tk.Label(root, text="Taş, Kağıt, Makas", font=("Helvetica", 16, "bold"), bg="#4a4a4a", fg="white")
baslik_etiketi.pack(pady=20)

# Bilgilendirici etiket
bilgi_etiketi = tk.Label(root, text="Hamleni seç:", font=("Helvetica", 12), bg="#4a4a4a", fg="white")
bilgi_etiketi.pack(pady=10)

# Butonlar için bir çerçeve oluştur
buton_cerceve = tk.Frame(root, bg="#4a4a4a")
buton_cerceve.pack(pady=20)

# Butonları oluştur ve çerçeveye ekle
tas_buton = tk.Button(buton_cerceve, text="Taş", font=("Helvetica", 12), width=10, command=lambda: oyunu_oyna("Taş"))
tas_buton.grid(row=0, column=0, padx=10)

kagit_buton = tk.Button(buton_cerceve, text="Kağıt", font=("Helvetica", 12), width=10, command=lambda: oyunu_oyna("Kağıt"))
kagit_buton.grid(row=0, column=1, padx=10)

makas_buton = tk.Button(buton_cerceve, text="Makas", font=("Helvetica", 12), width=10, command=lambda: oyunu_oyna("Makas"))
makas_buton.grid(row=0, column=2, padx=10)

# Pencereyi başlat
root.mainloop()
