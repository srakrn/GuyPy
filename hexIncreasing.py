list = "0123456789ABCDEF"

sequence = raw_input()
increasing = 0
decreasing = 0
unchanged = 0
for i in range(0,len(sequence)-1):
    before = list.index(sequence[i])
    after = list.index(sequence[i+1])
    if(before<after):
        increasing += 1
    elif(before>after):
        decreasing += 1
    else:
        unchanged += 1
if(increasing > 0 and decreasing == 0):
    print("Y")
else:
    print("N")
