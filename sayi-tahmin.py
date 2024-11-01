import random
import tkinter as tk
from tkinter import messagebox

class SayıTahminOyunu:
    def __init__(self, master):
        self.master = master
        self.master.title("Sayı Tahmin Oyunu")
        self.master.geometry("300x200")

        self.sayı = random.randint(1, 100)
        
        self.tahmin_label = tk.Label(master, text="1 ile 100 arasında bir sayı tahmin edin:")
        self.tahmin_label.pack(pady=10)

        self.tahmin_entry = tk.Entry(master)
        self.tahmin_entry.pack(pady=10)

        self.tahmin_button = tk.Button(master, text="Tahmin Et", command=self.tahmin_et)
        self.tahmin_button.pack(pady=10)

    def tahmin_et(self):
        try:
            tahmin = int(self.tahmin_entry.get())
            if tahmin < self.sayı:
                messagebox.showinfo("Sonuç", "Tahmininiz çok düşük!")
            elif tahmin > self.sayı:
                messagebox.showinfo("Sonuç", "Tahmininiz çok yüksek!")
            else:
                messagebox.showinfo("Sonuç", "Tebrikler! Doğru tahmin ettiniz.")
                self.sayı = random.randint(1, 100)  # Yeni bir sayı seç
        except ValueError:
            messagebox.showerror("Hata", "Lütfen bir sayı girin.")

root = tk.Tk()
oyun = SayıTahminOyunu(root)
root.mainloop()
