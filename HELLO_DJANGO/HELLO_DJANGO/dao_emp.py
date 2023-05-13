import pymysql
class DaoEmp:
    def __init__(self):
        
        self.con = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python',
                       db='python', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from emp"
        self.cur.execute(sql)
    
        list = self.cur.fetchall()
        return list
    

    def selectOne(self):
        sql = f"select * from emp where e_id=1"
        self.cur.execute(sql)
        
        list2 = self.cur.fetchone()
        return list2
        
    def __del__(self):
        self.cur.close()
        self.con.close()
        
    def insert(self,e_id,e_name,sex,addr):
        sql = f"insert into emp(e_id,e_name,sex,addr) values('{e_id}','{e_name}','{sex}','{addr}')"
        
        self.cur.execute(sql)
        
        cnt = self.cur.rowcount
        self.con.commit()
        return cnt
        
    def update(self,e_id,e_name,sex,addr):
        sql = f"update emp set e_name='{e_name}',sex='{sex}',addr='{addr}' where e_id='{e_id}'"
        
        self.cur.execute(sql)
        
        cnt2 = self.cur.rowcount
        self.con.commit()
        return cnt2
        
    def delete(self,e_id):
        sql = f"delete from emp where e_id='{e_id}'"
        
        self.cur.execute(sql)
        
        cnt2 = self.cur.rowcount
        self.con.commit()
        return cnt2
                                
if __name__ == '__main__':
    de = DaoEmp()
    cnt2 = de.delete("3")
    print("cnt2",cnt2)     