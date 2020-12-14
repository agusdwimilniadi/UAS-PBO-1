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
class MenuAwal:
    def startMenu(self):
        getDB().hapusScrn()
        pilihan = int(input('''
        Selamat datang di Toko Kelontong Jaya Baru
        1. Admin
        2. Member
        3. Pembeli
        '''))
        if pilihan == 1:
            HalamanAdmin().admin()
        elif pilihan == 2:
            Member().menuMember()
        elif pilihan == 3:
            Guest.aGuest().menuguest()
stes=MenuAwal()
stes.startMenu()