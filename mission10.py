# cara untuk melakukan fungsi kalkulator amortisasi dalam python
def cicilan_bulanan_hutang_usaha(pokok_pinjaman, bunga_tahunan, lama_pinjaman):
    bunga_bulanan = bunga_tahunan / 12 / 100
    sisa_hutang = pokok_pinjaman

    # Menghitung cicilan tetap berdasarkan tenor lama_pinjaman
    cicilan = (
        pokok_pinjaman
        * bunga_bulanan
        / (1 - (1 + bunga_bulanan) ** -lama_pinjaman)
    )
    print(f"\n=== TENOR {lama_pinjaman} BULAN ===")
    print(f"total_hutang_usaha : Rp {pokok_pinjaman:,.2f}")
    print(f"cicilan / per bulan : Rp {cicilan:,.2f}\n")
    print("---RINCIAN HUTANG USAHA---")

    # loop untuk menghitung porsi pokok dan bunga setiap bulan
    for bulan in range(1, lama_pinjaman + 1):
        porsi_bunga = sisa_hutang * bunga_bulanan
        porsi_pokok = cicilan - porsi_bunga
        print(
            f"bulan ke-{bulan:02d} : bayar pokok = Rp {porsi_pokok:,.2f}, bunga = Rp {porsi_bunga:,.2f}"
        )
        sisa_hutang -= porsi_pokok

# tenor yang berbeda untuk simulasi cicilan bulanan hutang usaha
cicilan_bulanan_hutang_usaha(1000000, 5, 12)
cicilan_bulanan_hutang_usaha(1000000, 5, 24)
cicilan_bulanan_hutang_usaha(1000000, 5, 36)
cicilan_bulanan_hutang_usaha(1000000, 5, 60)
# selesai