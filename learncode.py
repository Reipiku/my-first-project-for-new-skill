margin_persen = 8
if margin_persen < 10:
    print("peringatan : margin tipis")
else:
    print("margin aman")

margin_persen = 12
if margin_persen == 15:
    print("margin aman")
else:
    print("margin tipis")

margin_keuntungan = 20
if margin_keuntungan >= 20:
    print("aku kaya")
else:
    print("aku miskin")
if margin_keuntungan <= 20:
    print("aku miskin")
else:
    print("aku kaya")

umur_pendafatar_SNBP = 20
tahun_kelulusan = 2024
if umur_pendafatar_SNBP >= 25 or tahun_kelulusan >= 2024:
    print("maaf, harus pake jalur mandiri")
elif umur_pendafatar_SNBP <= 25 and tahun_kelulusan <= 2025:
    print("selamat, anda bisa mendaftar SNBP")

daftar_transaksi = [5000, 12000, 75000, 20000, 30000]
total = 0
for transaksi in daftar_transaksi:
    total += transaksi
    print(total)

harga_buku_paket = [30000, 25000, 47000, 50000]
total_harga = 0
indeks = 0
panjang_daftar_harga = len(harga_buku_paket)
for harga in harga_buku_paket:
    if harga > 40000:
        total_harga += harga
        print(f"harga buku {harga} ditambahkan ke total, total sekarang: {total_harga}")
while indeks < panjang_daftar_harga:
   buku = harga_buku_paket[indeks]
   indeks += 1
   if buku > 40000:
      total_harga += buku
      print(f"uang Rp {buku} ditambahkan ke total, total sekarang: Rp{total_harga}")
      if total_harga > 100000:
         print("uang tidak cukup untuk membeli semua buku")
      break
indeks =+ 1

def hitung_pajak(harga, persen_pajak):
    return harga * persen_pajak / 100
def harga_final(harga, persen_pajak):
    pajak = hitung_pajak(harga, persen_pajak)
    diskon = harga * persen_pajak / 100
    return harga + pajak - diskon

print(harga_final(100000, 10))

def hitung_total_belanja(harga_barang, jumlah_barang, persen_diskon):
    return harga_barang * jumlah_barang - persen_diskon / 100
def uang_kembalian(uang_di_dompet, total_belanja):
    return uang_di_dompet - total_belanja
struk_belanja = hitung_total_belanja(30000, 2, 2000)
hitung_kembalian = uang_kembalian(100000, struk_belanja)
print(hitung_kembalian)

def cek_untung(modal, harga_jual):
    return modal * harga_jual / 100
def harga_barang(modal, cek_untung, harga_jual):
    cek_untung = modal - harga_jual
    harga_pasar = modal * harga_jual
    return harga_pasar + cek_untung
print(harga_barang(1000, 2000, 10))

transaksi = [ {"nama": "kopi", "harga": 18000, "qty": 3},
             {"nama": "roti", "harga": 12000, "qty": 2}
             ]
total_semua = 0
for item in transaksi:
    subtotal = item["harga"] * item["qty"]
    total_semua += subtotal
print(total_semua)

transaksi_jajan = []

transaksi_jajan.append({"nama": "martabak_keju", "harga": 25000, "qty": 1},)
transaksi_jajan.append({"nama": "mixue_eskrim", "harga": 14000, "qty": 1},)

total_semua = 0
total_terbesar = 0
for jajan in transaksi_jajan:
    subtotal = item["harga"] * item["qty"]
    total_semua += subtotal
    if subtotal > total_terbesar:
        total_terbesar = subtotal

print("total_jajan:", total_semua)
print("subtotal_terbesar:", total_terbesar) 

transaksi_saham = [
    ("BBCA", 10000, 200),
    ("MBG", 700, 300),
    ("BBCA", 10000, 200)
]
nama_saham, harga_lembar_saham, banyaknya_lembar = transaksi_saham[0]

total_investasi = harga_lembar_saham * banyaknya_lembar

print(f"jika saya membeli {nama_saham} sebanyak {banyaknya_lembar}lembar.")
print(f"total pembelian {total_investasi}")

set_saham = set(transaksi_saham)
print(set_saham)

nama_produk = "es_krim" 
harga = 14000
print(f"harga {nama_produk} : Rp{harga}")

nama_transaksi = "transfer_uang"
harga_satu_buku = 1540.345
jumlah_buku = 1
kalau_beli_dua = jumlah_buku + jumlah_buku
keperluan_transfer = "beli_buku"
pembelian_dua_buku = harga_satu_buku * kalau_beli_dua

transaksi_sebenarnya = (f"keperluan untuk pengerluaran {nama_transaksi}, nominal sebenarnya : {harga_satu_buku:.2f}, kalo beli dua nanti {pembelian_dua_buku:.2f}")
print(transaksi_sebenarnya)

nama_mesin_cuci = {'artis': 'rapi amat', 'influencer': 'widih salim'}
from collections import defaultdict
hitung = defaultdict(int)
for key in nama_mesin_cuci:
    hitung[key] += 1
    print(hitung[key])