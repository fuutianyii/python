import string,random
x=int(input())
s=''
for i  in range(0,x):
    s+=random.choice(string.ascii_letters+string.digits)
print(s)