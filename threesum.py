from itertools import chain, combinations
n,m = input().split(" ")
m = int(m)
a = input().split(" ")
for i in range(0,len(a)):
	a[i] = int(a[i])
b = input().split(" ")
aset = set(a)
threeset = set([])
for z in chain.from_iterable(combinations(aset,r) for r in range(len(aset)+1)):
	if(len(z)==3):
		threeset.add(z)

for ans in b:
	hans = False
	for s in threeset:
		g = 0
		for v in s:
			g+=v
		if(v == int(ans)):
			hans = True
	if hans:
		print("YES")
	else:
		print("NO")
