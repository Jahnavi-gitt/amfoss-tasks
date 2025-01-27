def countdfreq(S):
    freqs=[0]*10
    for char in S:
        if char.isdigit(): 
            digit=int(char)
            freqs[digit]+=1
    for freq in freqs:
        print(freq,end=" ")
S=input()
countdfreq(S)