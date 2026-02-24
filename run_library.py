from library import Book, Member, Staff, borrowTransaction

def jalankan_simulasi():
    print(" ======== SISTEM INFORMASI PERPUSTAKAAN UIN SUSKA ========")

   # Inisialisasi Objek
    buku1 = Book("Python for Data Science", "Jake Vanderplas", "978-1098121228")
    buku2 = Book("Struktur Data", "Bambang Hariyanto", "978-979-1153-34-8")

    print("\n" + "="*60)
    print(f"{'DAFTAR DATA BUKU':^60}")
    print("="*60)

    # Menampilkan Data Buku 1
    print(f"Judul    : {buku1.title}")
    print(f"Penulis  : {buku1.author}")
    print(f"ISBN     : {buku1.isbn}")
    print("-" * 60)

    # Menampilkan Data Buku 2
    print(f"Judul    : {buku2.title}")
    print(f"Penulis  : {buku2.author}")
    print(f"ISBN     : {buku2.isbn}")
    print("=" * 60)

    # Informasi Daftar Nama Anggota
    print("\n" + "="*60)
    print(f"{'INFORMASI ANGGOTA':^60}")
    print("="*60)

    # Inisialisasi Objek Member
    anggota = Member("putri indah", "12365478978")

    # Menampilkan Data dengan Format Rapi
    print(f"Nama Anggota : {anggota.name.title()}") # Menggunakan .title() agar jadi 'Putri Indah'
    print(f"ID Anggota   : {anggota.member}")
    print("-" * 60)

   # informasi Petugas Perpustakaan
    print("\n" + "="*60)
    print(f"{'PETUGAS PERPUSTAKAAN':^60}")
    print("="*60)

    # Inisialisasi Objek Staff
    petugas = Staff("Admin Perpus", "5001")

    # Menampilkan Data Petugas
    print(f"Nama Petugas : {petugas.name}")
    print(f"ID Petugas   : {petugas.staff_ic}")
    print("-" * 60)

    # Informasi Tambahan (Opsional)
    print("Status       : Sedang Bertugas")

   # --- SIMULASI PEMINJAMAN PERTAMA ---
    print("\n" + "="*60)
    print(f"{'PROSES PEMINJAMAN':^60}")
    print("="*60)

    # Membuat objek transaksi
    transaksi1 = borrowTransaction(buku1, anggota, petugas)

    if transaksi1.borrow_book():
        print(f"{anggota.name.title()} Berhasil Meminjam:")
        print(f"{buku1.title}")
        print(f"Oleh Petugas: {petugas.name}")
    else:
        print(f"Maaf, '{buku1.title}' sudah dipinjam orang lain.")
    print("-" * 60)


    # SIMULASI VALIDASI (Buku yang Sama)
    print(f"\n{'CEK VALIDASI: PINJAM BUKU YANG SAMA':^60}")
    print("-" * 60)

    # Mencoba meminjam kembali buku yang sudah dipinjam
    transaksi2 = borrowTransaction(buku1, anggota, petugas)

    if not transaksi2.borrow_book():
        print(f"Buku '{buku1.title}' SEDANG DIPINJAM.")
        print(f"Status: Tidak Tersedia / Harap Menunggu!")
    else:
        print(f"Putri Indah Buku berhasil dipinjam.")
    print("-" * 60)


    # --- SIMULASI PENGEMBALIAN ---
    print(f"\n{'PROSES PENGEMBALIAN':^60}")
    print("="*60)

    # Melakukan pengembalian
    transaksi1.return_book() 

    # Informasi status akhir
    print(f"Update: {buku1.title} sekarang tersedia kembali di rak.")
    print("=" * 60)

    # ringkasan aktivitas
    print("\n" + "="*60)
    print(f"{'RINGKASAN AKTIVITAS':^60}")
    print("="*60)
    print(f"Nama: {anggota.name}")
    print(f"total pinjaman: {len(anggota.borrowed_books)} buku")
    print("="*60 + "\n")

if __name__ =="__main__":
    jalankan_simulasi()