K = int(input())  
room_numbers=input().split() 
room_count = {}
for i in room_numbers:
    if i in room_count:
        room_count[i]+=1
    else:
        room_count[i]=1
for i in room_count:
    if room_count[i]==1:
        print(i)
        break
