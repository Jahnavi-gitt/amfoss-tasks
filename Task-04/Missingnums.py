n=int(input())
A=[int(x) for x in input().split()] 
m=int(input())
B=[int(x) for x in input().split()]
count_A={}
for num in A:
    if num in count_A:
        count_A[num]+=1
    else:
        count_A[num]=1
count_B={}
for num in B:
    if num in count_B:
        count_B[num]+=1
    else:
        count_B[num]=1
missingnums=[]
for num in count_B:
    if count_B[num]>count_A.get(num, 0):
        missingnums.append(num)
missingnums.sort()
print("Missing numbers are:")
print(" ".join(str(x) for x in missingnums))