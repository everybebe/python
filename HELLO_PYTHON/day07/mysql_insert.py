# STEP 1
import pymysql
from numba.roc.hsadrv.devices import cus

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python',
                       db='python', charset='utf8') # 한글처리 (charset = 'utf8')

e_id ="3" 
e_name ="6" 
sex ="6" 
addr ="6" 
 


curs = con.cursor()
sql = f"UPDATE emp SET e_name='{e_name}' ,sex='{sex}',addr='{addr}' WHERE e_id='3'"

print("sql",sql)
curs.execute(sql)
print("cnt", curs.rowcount)

con.commit()

curs.close()
con.close()        
