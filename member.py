import sqlite3
import Database
import Guest

class Member(Database.getDB):
    keranjang =[]
    harga =[]
    def menuMember(self):
        Database.getDB().hapusScrn()
        pilihan= str(input('''
                SELAMAT DATANG Member Toko Jaya Baru
        Masukkan Nomor Member anda : 
        '''))
        query = "SELECT nomor_member, nama from member where nomor_member = '{}'".format(pilihan.upper())
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.myDb.commit()

        try:
            import Guest
            Database.getDB().hapusScrn()
            print("SELAMAT {} dengan ID Member : {} ANDA MENDAPATKAN DISKON Di Toko Kami".format(all_results[0][1], all_results[0][0]))
            input('Ketik enter untuk melanjutkan')
            Member().transaksiMember()

        except IndexError:
            Database.getDB().hapusScrn()
            print("Untuk ID ", pilihan, " tidak ada")
            input('Ketik enter untuk memasukkan ID kembali')
            Member().menuMember()
    def transaksiMember(self):
        Database.getDB().hapusScrn()
        menuGuest =int(input(''' 
            MENU Member
            1. Mencari Barang
            2. Membeli Barang
            3. Exit

            Masukkan Pilihan Menu: 
             '''))
        if menuGuest == 1:
            Member().cari()
        elif menuGuest == 2 :
            Member().beli()
        elif menuGuest == 3 :
            exit(0)
        else:
            print("Masukkan Command dengan benar")
            Member().menuMember()
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
                Member().keranjang.append(barang[0])
                Member().harga.append(barang[0][1])
                maunambah = input("Apakah Mau menambahkan lagi ? \n")
                if maunambah == "ya":
                    Member().cari()
                elif maunambah == "tidak".lower() :
                    Member().transaksiMember()
            elif nambah == 'tidak'.lower():
                Member().transaksiMember()

        except IndexError:
            print("Barang yang anda cari tidak ada di toko kami")
            Member().menuMember()

    def beli(self):
        Database.getDB().hapusScrn()
        total = sum(Member.harga)
        print("Isi keranjangmu adalah :\n")
        for x in Member.keranjang :
            print(x[0],"--------",x[1])
        print("Jadi total belanjaanmu adalah Rp.",total ," dan mendapat diskon 10% menjadi Rp.", round(total-(total*10/100)))
        konfirm = input("Apakah jadi untuk membeli barang tersebut?\n Ya/Tidak ").lower()
        

        if konfirm == "ya":
            inputdata = "INSERT INTO keranjangbelanja ( totalHarga ) VALUES('{}');".format( total )
            self.cursor.execute(inputdata)
            self.myDb.commit()
            input("Terimakasih telah melakukan pembelian")
            import menu
            menu.MenuAwal().startMenu()
        elif konfirm == 'tidak':
            Member().keranjang.clear()
            Member().harga.clear()
            print("Isi keranjangmu sudah dihapus semua")
            Member().menuMember()
        else :
            print("Masukkan command dengan benar")
            Member().menuMember()

