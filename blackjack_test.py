s = 0

for i in range(0,3):
  card = input()
  card = card.lower()
  if card == "a":
    val = 1
  elif card == "j" or card == "q" or card == "k":
    val = 10
  else:
    val = int(card)
  s = s + val

if s>21:
  print("bust")
elif s>=17:
  print("stand")
else:
  print("hit")
