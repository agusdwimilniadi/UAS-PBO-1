import sqlite3
con = sqlite3.connect('F:/Kuliah/SEMESTER 3/Pemrograman Berorientasi Obyek I TM/Project/UAS-PBO-1/DB/DB FIX.sqlite')
cursor = con.cursor()  
query = 'select * from admin;'
# vaars= 'select id_admin from admin'
# passw= 'select password_admin from admin'
cursor.execute(query)
all_results = cursor.fetchall()
con.commit()
print(all_results[0][0])

if vars == 1 or vars == 2:
    print('sukses')
    
