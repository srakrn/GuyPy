# averageOfX.py

n = 0
nlist = []
while n>=0:
    n = int(input())
    nlist.append(n)
sum = 0
for i in nlist:
  sum+=i
print(sum/len(nlist))
