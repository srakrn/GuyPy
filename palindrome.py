# palindrome.py

txt = input() #อีเกรดเดอร์ควาย
txt = txt.strip()
l = len(txt)-1
status = "N"
for i in range(0,l+1):
    secondPart = txt[i:]
    firstPart = txt[0:i]
    joint = secondPart + firstPart
    for j in range(0,int(l/2)):
        if joint[j]==joint[l-j]:
            status = "Y"
print(status)
