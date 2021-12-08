import sqlite3
from time import localtime,strftime
from os.path import exists
import creater

class consql():       
    def __init__(self,filename):
        self.filename=filename

    def con(self):
        self.db=sqlite3.connect(self.filename) 

    def inser(self,english,chinese,part_of_speech):
        timestr=strftime("%Y-%m-%d",localtime())
        exe=self.db.cursor()
        execu='insert into ENGLISH values(NULL,"'+english+'","'+chinese+'","'+part_of_speech+'",0,"'+timestr+'");'
        exe.execute(execu)
        self.db.commit()
        
    def ifexists(self):
        if exists(self.filename):
            pass
        else:
            print("数据库不存在")
            auto_create = creater.consql()
            auto_create.crea(self.filename)
            print("已自动创建")
            

if __name__ == "__main__":
    filename="asda.db"
    con=consql(filename)
    con.ifexists("/"+filename)
    english="english"
    chinese="中文"
    part_of_speech="n."
    con.con(filename)
    con.inser(english,chinese,part_of_speech)