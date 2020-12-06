import sqlite3
con = sqlite3.connect('F:/Kuliah/SEMESTER 3/Pemrograman Berorientasi Obyek I TM/Project/UAS-PBO-1/DB/DB FIX.sqlite')
cursor = con.cursor()  
query = 'select * from admin;'
cursor.execute(query)
all_results = cursor.fetchall()
con.commit()
for result in all_results:
    print(result)
    
