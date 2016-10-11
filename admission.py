n = int(input())
dict = {}
def cs(l):
	s = ""
	for i in l:
		s += i+", "
	return s[:-2]
for i in range(0,n):
	id,a,b,c,d = input().split(",")
	dict.setdefault(a,[]).append(id)
	dict.setdefault(b,[]).append(id)
	dict.setdefault(c,[]).append(id)
	dict.setdefault(d,[]).append(id)
list = input().split(",")
for i in list:
	print("{} -> {}".format(i,cs(dict[i])))
