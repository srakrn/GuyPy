length = int(input().strip())
arr = [""]*length

for i in range(0,length):
    arr[i] = input().strip()

c = 0
for i in range(0,len(arr)):
    checkupto = len(arr)-i
    for j in range(0,checkupto-1):
        if(len(arr[j])>len(arr[j+1])):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            c+=1
        elif(len(arr[j]) == len(arr[j+1]) and arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            c+=1

for i in arr:
    print(i)
print(c)
