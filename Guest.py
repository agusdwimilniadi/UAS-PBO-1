
import sqlite3

class aGuest :
    keranjang =[]
    harga =[]
    def __init__(self):
        self.myDb= sqlite3.connect('DB/DB FIX.sqlite')
        self.cursor = self.myDb.cursor()


    def cari(self):
        carian = input("Mau mencari barang apa : ")
        query = "SELECT namaProduct, hargaProduct from product where namaProduct = '{}'".format(carian.lower())
        self.cursor.execute(query)
        barang = self.cursor.fetchall()
        self.myDb.commit()
        try:
            print(barang[0][0]," dengan harga ",barang[0][1] ," Tersedia ditoko kami")
            nambah = input("Apakah  ingin ditambahkan dikeranjang ? \nya atau tidak ?").lower()
            if nambah == 'Ya'.lower():
                aGuest.keranjang.append(barang[0])
                aGuest.harga.append(barang[0][1])
                aGuest().cari()

            elif nambah == 'tidak'.lower():
                aGuest().menuguest()

        except IndexError:
            print("Barang yang anda cari tidak ada di toko kami")
            aGuest().menuguest()

    def beli(self):
        total = sum(aGuest.harga)
        print("Isi keranjangmu adalah :\n")
        for x in aGuest.keranjang :
            print(x[0],"--------",x[1])
        print("Jadi total belanjaanmu adalah Rp.",total)
        konfirm = input("Apakah jadi untuk membeli barang tersebut?\n Ya/Tidak ").lower()
        if konfirm == "ya":
            inputdata = "INSERT INTO keranjangbelanja ( totalHarga ) VALUES('{}');".format( total )
            self.cursor.execute(inputdata)
            self.myDb.commit()
            print("Terimakasih telah melakukan pembelian")
        elif konfirm == 'tidak':
            aGuest.keranjang.clear()
            aGuest.harga.clear()
            print("Isi keranjangmu sudah dihapus semua")
            aGuest().menuguest()
        else :
            print("Masukkan command dengan benar")
            aGuest().menuguest()



    def menuguest(self):
        menuGuest =int(input(''' 
            MENU Guest
            1. Mencari Barang
            2. Membeli Barang
            3. Daftar Member
            4. Exit

            Masukkan Pilihan Menu: 
             '''))
        if menuGuest == 1:
            aGuest().cari()
        elif menuGuest == 2 :
            aGuest().beli()
        elif menuGuest == 3 :
            from insert import person #biar bisa langsung menjalankan fungsi person insert data class person harus dibedakan file pythonnya kalau tidak nanti manggil 2 kali
            person().insertData()
        elif menuGuest == 4 :
            exit(0)
        else:
            print("Masukkan Command dengan benar")
            aGuest().menuguest()




