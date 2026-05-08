import tkinter as tk
from tkinter import messagebox

def kirim_formulir():
    nama = entry_nama.get()
    nim = entry_nim.get()

    barang_dipinjam = [barang for barang, var in barang_vars.items() if var.get()]

    # TO DO: Tampilkan Validasi input
    if not nama or not nim:
        messagebox.showerror("salah memasukkan data")
        return

    # TO DO: Tampilkan Validasi input
    if not barang_dipinjam:
        messagebox.showerror("Barang tidak tersedia")
        return

    # TO DO: Tampilkan ringkasan
    pesan = (
        f"Nama : {nama}\n"
        f"NIM : {nim}\n\n"
        f"Barang yang dipinjam:\n" + "\n".join(f"- {item}" for item in barang_dipinjam)
    )
    messagebox.showinfo("Peminjaman Berhasil", pesan)

root = tk.Tk()
root.title("Formulir Peminjaman Barang Elektronik")
root.geometry("400x450") # Untuk mengatur ukutan pada jendela GUI

# TO DO: Input Nama
tk.Label(root, text="Nama Mahasiswa:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 0))
entry_nama = tk.Entry(root, width=40)
entry_nama.pack(padx=20, pady=5)

# TO DO: Input NIM
tk.Label(root, text="NIM:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 0))
entry_nim = tk.Entry(root, width=40)
entry_nim.pack(padx=20, pady=5)

# TO DO: Pilihan Barang
tk.Label(root, text="Pilih Barang yang Ingin Dipinjam:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=(15, 5))
barang_list = ["Monitor", "Keyboard", "Multimeter", "Mouse", "Soulder"]
barang_vars = {}

for barang in barang_list:
    var = tk.BooleanVar()
    tk.Checkbutton(root, text=barang, variable=var).pack(anchor="w", padx=30)
    barang_vars[barang] = var

# TO DO: Tombol Kirim
tombol_kirim = tk.Button(root, text="Kirim", command=kirim_formulir, bg="#4CAF50", fg="white", width=15)
tombol_kirim.pack(pady=20)

root.mainloop()

