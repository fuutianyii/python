import MySQLdb
connect=MySQLdb.connect('192.168.99.55','fty','qwe','student')
c=connect.cursor()
#c.execute('''insert into student values('fty',7)''')
#c.execute('''select * from student''')
#print(c.fetchall())
#c.execute('''desc student''')
#print(c.fetchall())
connect.close()