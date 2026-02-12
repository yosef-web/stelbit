x,y=map(int, input().split())
n=list(map(int, input().split()))
add=0
for i in n:
    if i<=y:
        add+=1
    else:
        add+=2
print(add)
