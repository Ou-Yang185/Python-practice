import pymysql as pm
import string,random

field=string.ascii_letters+string.digits
db=pm.connect(host="127.0.0.1",user="root",password="123456",port=3306,database="activate_code",charset="utf8")      #均为默认，端口3306，host为127.0.0.1
cur=db.cursor()

def getRandom():
    return "".join(random.sample(str.upper(field),4))        #从字符串中随机选取n个不同的字符

def getcatenate(group):
    return "-".join([getRandom() for i in range(group)])      #每个激活码由几组字符串组成
                                                              #print("-".join([getRandom() for i in range(3)]))
                                                              #print("-".join([str(i) for i in range(10)]))
def generate(n):                                              #生成多少组激活码
    group=int(input("input number every activate code:"))
    return [getcatenate(group) for i in range(n)]

def make_insert(group,number):
    #create_db="CREATE DATABASE IF NOT EXISTS activate_code CHARACTER SET utf8 COLLATE utf8_general_ci"
    #cur.execute(create_db)
    #delete_and_build='DROP TABLE IF EXISTS code'
    create_tb='''CREATE TABLE code(                     
        id INT AUTO_INCREMENT NOT NULL,             
        code CHAR(40),
        primary key(id)
        );'''                                     #创建数据表格式
    #cur.execute(delete_and_build)               #可用于重复创建名字相同的表，如果表存在则删除，当创建好想要的表后，可将此句删除
    #cur.execute(create_tb)                      #创建表后，此句可删除
    for i in range(number):
        code="-".join([getRandom() for i in range(group)]) 
        sql="INSERT INTO code(id,code) VALUES ('%d','%s')" % (i,code)
        try:
            cur.execute(sql)
            db.commit(）
        except:
            db.rollback()

def select():
    select="select * from code"
    cur.execute(select)
    result=cur.fetchall()                       #获取所有结果，返回元组
    #db.close()                                 #选择性关闭数据库                                         
    print(result)
def clear_table():
    delete="delete from code"
    cur.execute(delete)
    print("delete successfully")
if __name__=="__main__":
    group=int(input("input number consist of each activate-code:"))    #例如：输入2 则为 "abucya-xsddaz",输入3 则为"dwedd-xscc-csddcd”
    number=int(input("input generate's number and insert into database directly:"))         #想要创建的激活码数目
    make_insert(group,number)
    select()                #查询整张表
    #clear_table()           #清空表
    select()







