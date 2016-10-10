# Use the creation of function, right?

def mvAvg(a):
	j = [0]*len(a)
	j[0] = (a[0]+a[1])/2
	for i in range(1,len(a)-1):
		j[i] = (a[i-1]+a[i]+a[i+1])/3
	j[len(a)-1] = (a[len(a)-2]+a[len(a)-1])/2
	return j

bullshit = input()
inp = input().split()
for i in range(0,len(inp)):
	inp[i] = int(inp[i])

ans = mvAvg(inp)
for i in ans:
	print(i)
