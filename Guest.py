import Database
import sqlite3
import admin
import member

class aGuest(Database.getDB) :
    keranjang =[]
    harga =[]
    
    def cari(self):
        Database.getDB().hapusScrn()
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
                maunambah = input("Apakah Mau menambahkan lagi ? \n")
                if maunambah == "ya":
                    aGuest().cari()
                elif maunambah == "tidak":
                    

            elif nambah == 'tidak'.lower():
                aGuest().menuguest()

        except IndexError:
            print("Barang yang anda cari tidak ada di toko kami")
            aGuest().menuguest()

    def beli(self):
        Database.getDB().hapusScrn()
        total = sum(aGuest.harga)
        print("Isi keranjangmu adalah :\n")
        for x in aGuest.keranjang :
            print(x[0],"--------",x[1])
        print("Jadi total belanjaanmu adalah Rp.",total)
        konfirm = input("Apakah jadi untuk membeli barang tersebut?\n Ya/Tidak ").lower()
        

        if konfirm == "ya":
            if member.Member().is_member == True :
                totalfix = total - (total * 0,1)
                print("Selamat anda telah mendapatkan diskon 10% jadi total belanjaan anda sebesar ", totalfix)
                inputdata = "INSERT INTO keranjangbelanja ( totalHarga ) VALUES('{}');".format( totalfix )
                self.cursor.execute(inputdata)
                self.myDb.commit()
            elif member.Member.is_member == False :
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
        Database.getDB().hapusScrn()
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
            
            admin.Admin().daftarMember()
        elif menuGuest == 4 :
            exit(0)
        else:
            print("Masukkan Command dengan benar")
            aGuest().menuguest()

