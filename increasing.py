# increasing.py

sequence = raw_input()
increasing = 0
decreasing = 0
unchanged = 0
for i in range(0,len(sequence)-1):
    before = int(sequence[i])
    after = int(sequence[i+1])
    if(before<after):
        increasing += 1
    elif(before>after):
        decreasing += 1
    else:
        unchanged += 1
if(increasing > 0 and decreasing == 0 and unchanged == 0):
    print("This is an increasing sequence")
else:
    print("This is not an increasing sequence")
