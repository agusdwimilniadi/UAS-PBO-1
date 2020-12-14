import sqlite3
class Member(getDB):
    def menuMember(self):
        getDB().hapusScrn()
        pilihan= str(input('''
                SELAMAT DATANG Member Toko Jaya Baru
        Masukkan Nomor Member anda : 
        '''))
        query = "SELECT nomor_member, nama from member where nomor_member = '{}'".format(pilihan)
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.myDb.commit()

        try:
            getDB().hapusScrn()
            print("SELAMAT {} dengan ID Member : {} ANDA MENDAPATKAN DISKON Di Toko Kami".format(all_results[0][1], all_results[0][0]))
            input('Ketik enter untuk melanjutkan')
        except IndexError:
            getDB().hapusScrn()
            print("Untuk ID ", pilihan, " tidak ada")
            input('Ketik enter untuk memasukkan ID kembali')
            Member().menuMember()

