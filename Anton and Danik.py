n=int(input())
word=input()
count_A=0
count_D=0
for i in word:
    if i=='A':
        count_A+=1
    elif i=='D':
        count_D+=1
if count_A>count_D:
    print("Anton")
elif count_A<count_D:
    print("Danik")
else:
    print("Friendship")
