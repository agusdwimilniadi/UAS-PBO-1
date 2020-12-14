import sqlite3
import Database

is_member = False
class Member(Database.getDB):
    
    def menuMember(self):
        Database.getDB().hapusScrn()
        pilihan= str(input('''
                SELAMAT DATANG Member Toko Jaya Baru
        Masukkan Nomor Member anda : 
        '''))
        query = "SELECT nomor_member, nama from member where nomor_member = '{}'".format(pilihan)
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.myDb.commit()

        try:
            import Guest
            Database.getDB().hapusScrn()
            print("SELAMAT {} dengan ID Member : {} ANDA MENDAPATKAN DISKON Di Toko Kami".format(all_results[0][1], all_results[0][0]))
            is_member = True
            if is_member == True :
                print('asa')
            input('Ketik enter untuk melanjutkan')
            Guest.aGuest().menuguest()

        except IndexError:
            Database.getDB().hapusScrn()
            print("Untuk ID ", pilihan, " tidak ada")
            input('Ketik enter untuk memasukkan ID kembali')
            Member().menuMember()

