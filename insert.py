import sqlite3

class Model:
    #INSERT DATA
    def __init__(self):
        self.myDb= sqlite3.connect('F:/Kuliah/SEMESTER 3/Pemrograman Berorientasi Obyek I TM/Project/UAS-PBO-1/DB/DB FIX.sqlite')
        self.cursor = self.myDb.cursor()

    def insertData(self, tabel):
        self.tabel = tabel
        namaProduk = str(input("nama produk: "))
        hargaProduk = int(input("harga Produk: "))
        jumlahProduk = int(input('Jumlah produk: '))
        query = "INSERT INTO {} (namaProduct, hargaProduct, jumlahProduct) VALUES('{}', '{}', '{}');".format(tabel, namaProduk.lower(), hargaProduk, jumlahProduk)
        self.cursor.execute(query)
        self.myDb.commit()

    def deleteData(self, tabel):
        self.tabel = tabel
        dataHapus = str(input('Data apa yang dihapus?: '))
        query = "DELETE FROM {} WHERE namaProduct = '{}'".format(tabel, dataHapus)
        self.cursor.execute(query)
        self.myDb.commit()
    def selectData(self):
        search = str(input("Cek ketersediaan: "))
        query = "SELECT namaProduct from product where namaProduct = '{}'".format(search.lower())
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.myDb.commit()
        try:
            print('Untuk stok ', all_results[0][0], 'ada')
        except IndexError:
            print("tidak ada")

pilihan = int(input('''
    Selamat datang
    1. Admin
    2. Member
    3. Pembeli
'''))
if pilihan == 1:
    tabel = str(input("tabel apa: "))
    Model().insertData(tabel)
elif pilihan == 2:
    tabel = str(input("tabel apa: "))
    Model().deleteData(tabel)
elif pilihan == 3:
    Model().selectData()


