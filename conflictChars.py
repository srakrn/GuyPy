strA = input().strip()
strB = input().strip()

# Sort by the alphabetical order
def alphasort(arr):
    # A string sorting by the priority of characters
    prio = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS"
    for i in range(0,len(arr)):
        # For the first loop, we're checking up to len(array) items
        # The second loop will be len(array)-1, etc,
        # That means, for the i th loop, we'll check for len(array)-i items in array
        checkupto = len(arr)-i
        for j in range(0,checkupto-1):
            # if you found that the arrangement is not in the same way as the `prio` string
            if(prio.index(arr[j])>prio.index(arr[j+1])):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# A list to keep record of strings found
charsFound = []

# We need to do two loops,
# The first loop will pick a char in strA,
for a in strA:
    # The second loop will loop through chars in strB,
    for b in strB:
        # check if those are matching, appending to a list.
        if(not(a in charsFound)):
            if(a==b):
                charsFound.append(a)

# Sort the list
charsFound = alphasort(charsFound)

# My idiot way to print the list of chars,
# Start by declaring a string with first answer
answerString = str(charsFound[0])
# and continuously append the next characters
for i in range(1,len(charsFound)):
    answerString += (" " + charsFound[i])

# And print
if(len(charsFound) == 0):
    print("NONE")
else:
    print(answerString)
