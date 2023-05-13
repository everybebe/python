# STEP 1
import pymysql
from numba.roc.hsadrv.devices import cus

# STEP 2: MySQL Connection 연결
con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python',
                       db='python', charset='utf8') # 한글처리 (charset = 'utf8')

e_id ="3" 

curs = con.cursor()
sql = f"delete from emp where e_id='{e_id}'"

print("sql",sql)
curs.execute(sql)
print("cnt", curs.rowcount)

con.commit()

curs.close()
con.close()        
