# From now on, I am commenting in English.
# Let's start with the bubble sort

def bubblesort(arr):
    for i in range(0,len(arr)):
        # For the first loop, we're checking up to len(array) items
        # The second loop will be len(array)-1, etc,
        # That means, for the i th loop, we'll check for len(array)-i items in array
        checkupto = len(arr)-i
        for j in range(0,checkupto-1):
            # if array[j]>array[j+1] then switch
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# Length sort algrithm
def lengthsort(arr):
    for i in range(0,len(arr)):
        # For the first loop, we're checking up to len(array) items
        # The second loop will be len(array)-1, etc,
        # That means, for the i th loop, we'll check for len(array)-i items in array
        checkupto = len(arr)-i
        for j in range(0,checkupto-1):
            # if !!!!THE LENGTH!!!! of array[j]>array[j+1] then switch
            if(len(arr[j])>len(arr[j+1])):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# Now the input times, and FUCKING STRIP
length = int(input().strip())

# Declare empty array
array = [""]*length

# Prompts for n inputs
for i in range(0,length):
    array[i] = input().strip()

# And sort time, begins with alphabetical sort, then length sort.
# The partial part of alphabetical sort MUST be overridden by the length sort,
# means we should do the aplhabetical sort first.
array = bubblesort(array)
array = lengthsort(array)

# And print time.
for i in array:
    print(i)
