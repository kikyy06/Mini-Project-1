def hitung_gaji():
    jam_kerja = int(input("masukkan jam kerja: "))
    tarif_kerja = int(input("masukkan tarif kerja: "))

    gaji = jam_kerja * tarif_kerja
    print("Gaji anda adalah:" , gaji)

    if jam_kerja > 160:
        bonus = 0.10 * gaji + gaji
        print("ini adalah gaji ditambah bonus anda",bonus)
    else:
        print("anda tidak mendapatkan bonus")

while True:
    hitung_gaji()
    print()
    ulang = input("Apakah anda ingin menghitung ulang gaji? (Y/T): ")
    if ulang == "t":
        break
print("Terimakasih")
