def toVal(card):
    card = card.lower()
    if card == "a":
        val = 1
    elif card == "j" or card == "q" or card == "k":
        val = 10
    else:
        val = int(card)
    return val

a1 = input()
a2 = input()
b1 = input()
b2 = input()

if(a1 == a2 and b1 != b2):
    print("P1")
elif(a1 != a2 and b1 == b2):
    print("P2")
elif(a1 == a2 and b1 == b2):
    print("Draw")
else:
    a1 = int(toVal(a1))
    a2 = int(toVal(a2))
    b1 = int(toVal(b1))
    b2 = int(toVal(b2))
    sumA = (a1+a2)%10
    sumB = (b1+b2)%10
    if(sumA > sumB):
        print("P1")
    elif(sumA < sumB):
        print("P2")
    elif(sumA == sumB):
        print("Draw")
