import re
import pymysql #导入模块
db = pymysql.connect(
         host='192.168.1.10',
         port=3306,
         user='fty',
         passwd='toor',
         db='omelette',
         charset='utf8'
         )
cursor = db.cursor()





f=open("f:/desktop/input.txt",'rb')

while(data:=f.readline()):
    sql = f"select word_id from words  order by word_id desc limit 0,1"
    cursor.execute(sql)
    word_id = cursor.fetchone()
    word_id=int(word_id[0])+1
    uncn = re.compile(r'^([\(\)\u0061-\u007a,\u0020/.\']+) [\u4e00-\u9fa5]')
    en = "".join(uncn.findall(data.decode().lower()))
    en=en.replace("'","\\'")
    en=en.replace("\n","")
    ch=data.decode().replace(en,"").replace(" ","")
    ch=ch.replace("'","\\'")
    ch=ch.replace("\n","")
    print(en)
    print(ch)
    sql=f"INSERT INTO `words`(`word_id`, `english`, `chinese`, `posd`, `US`, `UK`, `exam_type`) VALUES ('{word_id}','{en}','{ch}','phrase','','','null')"
    print(sql)
    
    cursor.execute(sql)
    sql=f"INSERT INTO `word_family`(`row_num`, `word_id`, `books_id`, `self_defining`, `insert_date`) VALUES (NULL,'{word_id}','4','0','2023-06-11')"
    print(sql)
    cursor.execute(sql)
    
    sql = f"select word_num from word_books where books_id=4"
    cursor.execute(sql)
    word_num = cursor.fetchone()
    word_num=word_num[0]
    word_num=int(word_num)+1
    sql = f"update word_books set word_num = {word_num} where books_id=4"
    cursor.execute(sql)
    print(word_num)
    db.commit()