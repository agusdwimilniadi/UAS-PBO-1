import sqlite3
class Model:
    #INSERT DATA
    def __init__(self):
        self.myDb= sqlite3.connect('F:/Kuliah/SEMESTER 3/Pemrograman Berorientasi Obyek I TM/Minggu 10/belajar sqite/pbo010.db')
        self.cursor = self.myDb.cursor()

    def insert(self,tabel, nama, email):
        self.tabel = tabel
        self.nama = nama
        self.email = email
        query = "INSERT INTO {} (nama, email) VALUES('{}', '{}');".format(nama, email)
        self.cursor.execute(query)
        self.myDb.commit()
    def selectData(self, tabel):
        self.tabel = tabel
        query = "SELECT * From {}".format(tabel)
        self.cursor.execute(query)
        hasilQuery = self.cursor.fetchall()
        self.myDb.commit()

        for hasil in hasilQuery:
            print(hasil)
persons=Model()
persons.selectData("person")

