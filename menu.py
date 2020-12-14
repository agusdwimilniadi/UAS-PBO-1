import sqlite3
import os
import Guest
import member



class getDB:
    def __init__(self):
        self.myDb= sqlite3.connect('DB/DB FIX.sqlite')
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
            import admin
            admin.HalamanAdmin().adminmenu()
        elif pilihan == 2:
            member.Member().menuMember()
        elif pilihan == 3:
            Guest.aGuest().menuguest()
stes=MenuAwal()
stes.startMenu()