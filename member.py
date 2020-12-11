import sqlite3
class Member:
    def __init__(self):
        self.myDb= sqlite3.connect('F:/Kuliah/SEMESTER 3/Pemrograman Berorientasi Obyek I TM/Project/UAS-PBO-1/DB/DB FIX.sqlite')
        self.cursor = self.myDb.cursor()
    def memberMenu(self):
        pilihan= int(input('''
                SELAMAT DATANG Member Toko Jaya Baru
        Masukkan Nomor Member anda : 
        '''))

