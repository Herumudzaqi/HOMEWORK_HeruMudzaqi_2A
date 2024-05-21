stok = []
def tambah_data_barang ():
    nama_barang = str(input("masukan nama barang : ")).lower()
    jumlah_barang = int(input("masukan stok barang : "))

    stok_baru = {f"nama": nama_barang, "jumlah" : jumlah_barang }
    stok.append(stok_baru)
    print("\n")
    print("data berhasil ditambahkan")
    return "\n"

def edit_data ():
    index = int(input("masukan data index ke : "))
    nama_baru = str(input("masukan nama barang :"))
    jumlah_barang_baru = int(input("masukan stok :"))

    stok_baru = [("nama",nama_baru),("jumlah",jumlah_barang_baru) ]
    stok[index].update(stok_baru)
    print("\n")
    print("data telah diubah")
    return "\n"

def hapus_data_barang():
    delate = int(input("hapus data index ke : "))
    stok.pop(delate)
    print("\n")
    print("data berhasil dihapus")
    return "\n"

def tampil_data():
    print("====daftar barang============")
    for i in stok:
        print(f"{i['nama']} : {i['jumlah']}")
    return "\n"

def cari_data_barang():
    print("========hasil pencarian============")
    items = []
    cari = str(input("data yang akan dicari :")).lower()
    for i in stok :
        if cari in i["nama"] :
            items.append(i)
    if items :
        for item in items :  
            print(f"{item['nama']} : {item['jumlah']}")
    else : 
        print("tidak ada data dengan nama", cari)
    return "\n"

def jumlah_data():
    print("=========jumlah data==========")
    print(f"terdapat {len(stok)} data")
    return "\n"