n=input()
row=list(map(int, input().split()))
row.sort()
for i in row:
    print(i, end=" ")
