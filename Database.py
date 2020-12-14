import sqlite3
import os
class getDB:
    def __init__(self):
        self.myDb= sqlite3.connect('DB/DB FIX.sqlite')
        self.cursor = self.myDb.cursor()
    def hapusScrn(self):
        os.system('cls' if os.name == 'nt' else 'clear')