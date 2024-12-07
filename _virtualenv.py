n = int(input())
arr=[]
for k in range(n):
    p = input()
    arr.append(p)

p = 0
count = 0

for i in range(n):
    for j in range(min(len(arr[i]), len(arr[i + 1]))):
        if arr[i][j] == arr[i+1][j]:
            count=count+1

for l in range(n):
    if count == len[arr[l]]:
        p = p+1

print(p)