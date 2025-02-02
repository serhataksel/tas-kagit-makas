# Kelime Bulmaca Oyunu

## Proje Açıklaması
Kelime Bulmaca Oyunu, kullanıcıların rastgele seçilen bir kelimeyi tahmin etmeye çalıştığı eğlenceli bir oyundur. Kullanıcı, kelimedeki harfleri tahmin ederken, kalan hak sayısı da sınırlıdır. Oyuncu kelimeyi doğru tahmin ettiğinde oyunu kazanır, hakları bittiğinde ise kaybeder.

## Özellikler
- Rastgele kelime seçimi
- Harf tahmini
- Hatalı tahmin kontrolü
- Kazanma ve kaybetme durumu
- Geri bildirim mekanizması
- Kullanıcı dostu grafik arayüzü

## Gereksinimler
Bu oyunu çalıştırmak için aşağıdaki yazılımlara ihtiyaç vardır:
- Python 3.x
- Tkinter (Python ile birlikte gelir, ayrı bir yükleme gerektirmez)

## Kurulum
1. Python'u [Python resmi web sitesinden](https://www.python.org/downloads/) indirip yükleyin.
2. Aşağıdaki kodu bir Python dosyasına yapıştırın ve dosyayı `kelime_bulmaca.py` olarak kaydedin.

```python
import tkinter as tk
from tkinter import messagebox
import random

class KelimeBulmaca:
    def __init__(self, master):
        self.master = master
        self.master.title("Kelime Bulmaca Oyunu")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f0f0")

        self.kelimeler = ["programlama", "python", "tkinter", "yazılım", "bilgisayar", "geliştirme", "algoritma"]
        self.kelime = random.choice(self.kelimeler)
        self.tahminler = []
        self.kalan_hak = 6
        
        self.baslik_label = tk.Label(master, text="Kelimeyi Tahmin Et:", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.baslik_label.pack(pady=20)

        self.kelime_label = tk.Label(master, text=self.gizle_kelime(), font=("Helvetica", 24), bg="#f0f0f0")
        self.kelime_label.pack(pady=10)

        self.tahmin_entry = tk.Entry(master, font=("Helvetica", 16), justify='center')
        self.tahmin_entry.pack(pady=10)

        self.tahmin_button = tk.Button(master, text="Tahmin Et", command=self.tahmin_et, font=("Helvetica", 14), bg="#4CAF50", fg="white")
        self.tahmin_button.pack(pady=10)

        self.kalan_hak_label = tk.Label(master, text=f"Kalan Hak: {self.kalan_hak}", font=("Helvetica", 14), bg="#f0f0f0")
        self.kalan_hak_label.pack(pady=10)

    def gizle_kelime(self):
        gizli_kelime = ""
        for harf in self.kelime:
            if harf in self.tahminler:
                gizli_kelime += harf + " "
            else:
                gizli_kelime += "_ "
        return gizli_kelime.strip()

    def tahmin_et(self):
        tahmin = self.tahmin_entry.get().lower()
        self.tahmin_entry.delete(0, tk.END)

        if len(tahmin) != 1 or not tahmin.isalpha():
            messagebox.showerror("Hata", "Lütfen sadece bir harf girin.")
            return

        if tahmin in self.tahminler:
            messagebox.showinfo("Bilgi", "Bu
