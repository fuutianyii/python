import MySQLdb

db=MySQLdb.connect("172.16.1.131","fty","qwe","welcome")

dbcursor = db.cursor()

dbcursor.execute("delete from welcome where user='test'")

dbcursor.execute("flush privileges")

dbcursor.execute("insert into welcome value(0,'test','test')")

dbcursor.execute("flush privileges")

dbcursor.execute("update welcome set password='qwe' where user='test'")

dbcursor.execute("flush privileges")

dbcursor.execute("select * from welcome")

data= dbcursor.fetchone() #获取一行
while data: 
      print(data)  
      data = dbcursor.fetchone()
db.close()



