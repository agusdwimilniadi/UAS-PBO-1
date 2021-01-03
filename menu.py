import sqlite3
import os
import Database
import Guest
import member

class MenuAwal(Database.getDB):
    def startMenu(self):
        Database.getDB().hapusScrn()
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
            Guest.guestMenu().menuguest()
stes=MenuAwal()
stes.startMenu()