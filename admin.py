import sqlite3
import os
from getpass import getpass
import Database

class HalamanAdmin(Database.getDB):
    def adminmenu(self):
        Database.getDB().hapusScrn()
        pilihan = int(input('''
        Selamat datang di Admin
        1. Login Admin
        2. Daftar Admin
        3. Daftar Member
        '''))
        if pilihan == 1:
            HalamanAdmin().loginAdmin()
        elif pilihan == 2:
            HalamanAdmin().daftarAdmin()
        else:
            Admin().daftarMember()
    def loginAdmin(self):
        Database.getDB().hapusScrn()
        userid= str(input("Masukkan username: "))
        password = getpass()
        query = 'SELECT * from admin WHERE id_admin="{}" AND password_admin="{}"'.format(userid, password)
        self.cursor.execute(query)
        self.myDb.commit()
        if self.cursor.fetchone() is not None:
            print ("Login Berhasil, Selamat Datang ", userid, " di menu Admin.")
            input('Ketik Enter untuk Melanjutkan')
            Admin().menuAdmin()
        else:
            print ("Login failed")
            input('Klik Enter untuk masuk ke login ')
            HalamanAdmin().loginAdmin()
    def daftarAdmin(self):
        userid= str(input("Masukkan username: "))
        password = getpass()
        query = "INSERT INTO admin (id_admin, password_admin) VALUES('{}', '{}');".format(userid, password)
        self.cursor.execute(query)
        self.myDb.commit()
        lanjut=str(input('Pendaftaran Admin Berhasil, lanjut login? (y/n)'))
        if lanjut.lower() == 'y':
            HalamanAdmin().loginAdmin()
        elif lanjut.lower() == 'n':
            HalamanAdmin().adminmenu()
class Admin(Database.getDB):
    def menuAdmin(self):
        Database.getDB().hapusScrn()
        menuAdmin=int(input(''' 
            MENU ADMIN
        1. Tambah Barang di Toko
        2. Hapus Barang di Toko
        3. Cek Ketersediaan Barang
        4. Daftar Membership
        5. Logout
        
        Masukkan Pilihan Menu: 
        '''))
        if menuAdmin == 1:
            Admin().insertData('product')
        elif menuAdmin == 2:
            Admin().deleteData()
        elif menuAdmin == 3:
            Admin().selectData()
        elif menuAdmin == 4:
            Admin().daftarMember()
        else:
            HalamanAdmin().adminmenu()
    def insertData(self, tabel):
        self.tabel = tabel
        namaProduk = str(input("nama produk: "))
        hargaProduk = int(input("harga Produk: "))
        jumlahProduk = int(input('Jumlah produk: '))
        query = "INSERT INTO {} (namaProduct, hargaProduct, jumlahProduct) VALUES('{}', '{}', '{}');".format(tabel, namaProduk.lower(), hargaProduk, jumlahProduk)
        self.cursor.execute(query)
        self.myDb.commit()
        Admin().menuAdmin()
    def deleteData(self):
        dataHapus = str(input('Data apa yang dihapus?: '))
        query = "DELETE FROM Product WHERE namaProduct = '{}'".format(dataHapus)
        self.cursor.execute(query)
        self.myDb.commit()
        input("Data ", dataHapus, " berhasil dihapus")
        Admin().menuAdmin()
    def selectData(self):
        search = str(input("Cek ketersediaan: "))
        query = "SELECT namaProduct from product where namaProduct = '{}'".format(search.lower())
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.myDb.commit()
        try:
            print('Untuk stok ', all_results[0][0], 'ada')
            input('Ketik enter untuk kembali ke manu Admin')
            Admin().menuAdmin()
        except IndexError:
            print("Untuk produk ", search, " tidak ada")
            input('Ketik enter untuk kembali ke manu Admin')
            Admin().menuAdmin()
    def getNomorMember(self):
        query = "SELECT COUNT(id_member) FROM member"
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.myDb.commit()
        return (all_results[0][0]+1)
    def daftarMember(self):
        codeMember= 'TOKOJAYA00'
        nomorMember = str((Admin().getNomorMember()))
        nomorMemberFix= codeMember+nomorMember
        nama = str(input("Nama Member Baru: "))
        asalKota = str(input('Asal Kota Member Baru: '))
        query = "INSERT INTO member (nomor_member, nama, alamat) VALUES('{}', '{}', '{}');".format(nomorMemberFix, nama, asalKota)
        self.cursor.execute(query)
        self.myDb.commit()
        Database.getDB().hapusScrn()
        print('''
                DAFTAR MEMBERSHIP BERHASIL
            ID = {}
            Nama = {}

            nb: Masukkan nomor ID pada saat transaksi untuk mendapatkan diskon
        '''.format(nomorMemberFix, nama))
