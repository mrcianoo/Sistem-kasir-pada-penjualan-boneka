def hitung_total_harga(jumlah_boneka):
    if 1 <= jumlah_boneka <= 12:
        harga_per_boneka = 20000
    elif 13 <= jumlah_boneka <= 24:
        harga_per_boneka = 19500
    elif 25 <= jumlah_boneka <= 50:
        harga_per_boneka = 18000
    elif jumlah_boneka > 50:
        harga_per_boneka = 17000
        
    total_harga = jumlah_boneka * harga_per_boneka
    return total_harga

def main():
    print("Sistem Kasir Perusahaan Boneka")
    jumlah_boneka = int(input("Masukkan jumlah boneka yang dibeli: "))
    if jumlah_boneka <= 0:
            print("Jumlah boneka harus lebih dari 0.")
    else:
        total_harga = hitung_total_harga(jumlah_boneka)
        print(f"Total harga untuk {jumlah_boneka} boneka adalah: Rp {total_harga}")
        
main()