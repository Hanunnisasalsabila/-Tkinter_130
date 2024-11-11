import tkinter as tk
from tkinter import messagebox

#mengambil nilai dari setiap kotak
#lalu mengubahnya menjadi angka. nilai nya antara 0 sampai 100. 
#kalau misal ada nilai yang tidak valid seperti lebih dari 100 maka akan muncul pesan error
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0<= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
            messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")

#membuat jendela/tampilan utama, mengatur ukuran dan warna background nya, serta menuliskan judulnya
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

#Membuat judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Italic", 10, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)

#Membuat kotak input
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

#Membuat 10 kotak input untuk masing masing nilai disetiap mata pelajaran
#semua hasil input akan disimpan didalam entries buat memudahkan pengecekan di fungsi hasil prediksi nanti
entries = []
for i in range(10):
     label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", font=("Italic", 10, "bold"), bg="#f0f0f0")
     label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
     entry = tk.Entry(frame_input, width=10, font=("Italic", 10))
     entry.grid(row=i, column=1, padx=10, pady=5)
     entries.append(entry)

#Membuat tombol prediksi. ketika di klik, hasil prediksi akan muncul
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Italic", 10, "bold"), bg="#f0f0f0")
prediksi_button.pack(pady=30)

#menampilkan hasil prediksi. Kalau prediksinya berhasil,teks nya berubah tergantung hasil
hasil_label = tk.Label(root, text="", font=("Italic",10, "italic", "bold"), fg="red", bg="#f0f0f0")
hasil_label.pack(pady=20)

#Menjalankan Aplikasi
root.mainloop()