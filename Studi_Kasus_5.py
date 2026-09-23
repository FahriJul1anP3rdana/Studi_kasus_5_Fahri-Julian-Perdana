


def pemesanan_hotel(jenis_kamar, malam):
    if jenis_kamar == "standard":
        tarif = 200000 
    elif jenis_kamar == "deluxe":
        tarif = 350000 
    else:
        tarif = 0
    total_tarif = tarif * malam
    return total_tarif

    


while True:
    jenis_kamar = input("masukan kamar (standard/deluxe) : ")
    
    if jenis_kamar in ["standard", "deluxe"]:
        break
    elif jenis_kamar == "":
        print("koe ga boleh kosong!")
    else:
        print("inputan salah")

while True:
    tanggal_masuk = input("tanggal dia masuk :")
    if tanggal_masuk == "":
        print("jangan kosong")

    else:
        tanggal_masuk = int(tanggal_masuk)
        break

while True:
    tanggal_keluar = input("tanggal dia masuk :")
    if tanggal_keluar == "":
        print("jangan kosong")

    else:
        tanggal_keluar = int(tanggal_keluar)
        break


malam = tanggal_keluar - tanggal_masuk
biaya_pemesanan = pemesanan_hotel(jenis_kamar, malam)

print("jenis kamar :", jenis_kamar)
print("tanggal masuk: ",tanggal_masuk)
print("tanggal keluar: ",tanggal_keluar)
print("lama menginap: ",malam, "malam")
print("total biaya", biaya_pemesanan)



    
    