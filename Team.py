n=int(input())
count_1=0
count_2=0
total=0
check[]
for i in range(n):
    row=list(map(int, input().split()))
    for j in row:
        if j==1:
            count1+=1
        else:
            count0+=1
    if count1>=2:
        total+=1
    else:
        total+=0
    count1=0
print(total)
