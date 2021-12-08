import sqlite3

class consql():
    def crea(self,filename):
        db=sqlite3.connect(filename) 
        exe=db.cursor()
        exe.execute('create table ENGLISH(id integer primary key,english varchar(100),chinese varchar(100),Part_of_speech varchar(100),wrong_nums int(255),addtime varchar(100));')                  

if __name__ == '__main__':
    con = consql()
    filename=input("请输入数据库名：")
    con.crea(filename)
    print("创建成功")