# MHOM SUKHUMBHAN MUNG

# Begins with input, then parse it into list.
inp = input().split(",")

# A variable to count flood occurrence
flooded = 0

# And check for objects with value less than 0 in inpList
for i in inp:
    if(int(i)<0):
        flooded += 1

# Print the results.
print(flooded)
