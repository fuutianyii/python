import random
import string

w=open("rand.txt",'w')

for i in range(0,100):
    for v in range(0,20):
        w.write(random.choice(string.ascii_letters))

    w.write('\n')
