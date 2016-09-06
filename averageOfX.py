# averageOfX.py

n = input()
nlist = n.split()
l = 0
s = 0
for i in nlist:
    if int(i)>=0:
        s+=int(i)
        l+=1
    else:
        break;
print(s/l)
