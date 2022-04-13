import pymysql
db = pymysql.connect("192.168.99.155","fty","qwe","welcome" )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT * from welcome")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone() 
while data:
    print(data)
    data = cursor.fetchone()
# 关闭数据库连接
db.close()


import MySQLdb
db = MySQLdb.connect("192.168.99.155","fty","qwe","welcome")
cursor = db.cursor()#MySQLdb.cursors.DictCursor
cursor.execute("select * from welcome")
# db.commit() # 提交数据
while data:
    print(data)
    data = cursor.fetchone()
# cursor.owncount() #影响了多少航
db.close()
