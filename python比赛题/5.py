n=input()
c=len(n)
i=int(n)
s=0
while i>0:
    s+=(i%10)**c
    i=i//10
if s==int(n):
    print("是")
else:
    print("不是")