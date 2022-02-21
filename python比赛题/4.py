import random
a=[]
def asd():
        e=0
        c=200
        l=0
        y=0
        for b in range(0,100):
            d=random.randint(e,c)
            a.append(d)
            for x in range(0,100):
                if a[l]<d:
                    l=l+1
                    y=a[l]
        print(a)
        print("最大的数：" ,y)
asd()
