import sqlite3
import os
import Guest
from getpass import getpass


class getDB:
    def __init__(self):
        self.myDb= sqlite3.connect('F:/Kuliah/SEMESTER 3/Pemrograman Berorientasi Obyek I TM/Project/UAS-PBO-1/DB/DB FIX.sqlite')
        self.cursor = self.myDb.cursor()
    def hapusScrn(self):
        os.system('cls' if os.name == 'nt' else 'clear')
class MenuAwal(getDB):
    def startMenu(self):
        getDB().hapusScrn()
        pilihan = int(input('''
        Selamat datang di Toko Kelontong Jaya Baru
        1. Admin
        2. Member
        3. Pembeli
        '''))
        if pilihan == 1:
            MenuAwal().admin()
        elif pilihan == 2:
            tabel = str(input("tabel apa: "))
            Admin().deleteData(tabel)
        elif pilihan == 3:
            Guest.aGuest().menuguest()
    def admin(self):
        getDB().hapusScrn()
        pilihan = int(input('''
        Selamat datang di Admin
        1. Login Admin
        2. Daftar Admin
        '''))
        if pilihan == 1:
            MenuAwal().loginAdmin()
        elif pilihan == 2:
            MenuAwal().daftarAdmin()
        else:
            print("Inputan salah")
    def loginAdmin(self):
        getDB().hapusScrn()
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
            MenuAwal().loginAdmin()
    def daftarAdmin(self):
        userid= str(input("Masukkan username: "))
        password = getpass()
        query = "INSERT INTO admin (id_admin, password_admin) VALUES('{}', '{}');".format(userid, password)
        self.cursor.execute(query)
        self.myDb.commit()
        lanjut=str(input('Pendaftaran Admin Berhasil, lanjut login? (y/n)'))
        if lanjut.lower() == 'y':
            MenuAwal().loginAdmin()
        elif lanjut.lower() == 'n':
            MenuAwal().startMenu()
        # tabel = str(input("tabel apa: "))
        # Model().insertData(tabel)
class Admin(getDB):
    def menuAdmin(self):
        getDB().hapusScrn()
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
            Admin().deleteData('product')
        elif menuAdmin == 3:
            Admin().selectData()
        elif menuAdmin == 4:
            person().insertData()
        else:
            MenuAwal().startMenu()
    def insertData(self, tabel):
        self.tabel = tabel
        namaProduk = str(input("nama produk: "))
        hargaProduk = int(input("harga Produk: "))
        jumlahProduk = int(input('Jumlah produk: '))
        query = "INSERT INTO {} (namaProduct, hargaProduct, jumlahProduct) VALUES('{}', '{}', '{}');".format(tabel, namaProduk.lower(), hargaProduk, jumlahProduk)
        self.cursor.execute(query)
        self.myDb.commit()
        Admin().menuAdmin()
    def deleteData(self, tabel):
        self.tabel = tabel
        dataHapus = str(input('Data apa yang dihapus?: '))
        query = "DELETE FROM {} WHERE namaProduct = '{}'".format(tabel, dataHapus)
        self.cursor.execute(query)
        self.myDb.commit()
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
            print("Unutk produk ", search, " tidak ada")
            input('Ketik enter untuk kembali ke manu Admin')
            Admin().menuAdmin()

class person(getDB):
    def insertData(self):
        nama = str(input("Nama Anda: "))
        alamat = str(input("Alamat Anda: "))
        query = "INSERT INTO person (nama, alamat) VALUES('{}', '{}');".format(nama, alamat)
        self.cursor.execute(query)
        self.myDb.commit()
        Admin().menuAdmin()

stes=MenuAwal()
stes.startMenu()