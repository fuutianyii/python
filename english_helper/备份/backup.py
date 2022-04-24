import os
files=os.listdir()
for file in files:
    if (os.path.isfile(file)) & (file!="backup.py"):
        r=open(file,"rb")
        w=open("备份/"+file,"wb")
        w.write(r.read())
        r.close()
        w.close()
        print("backup"+" "+file+" susccess")