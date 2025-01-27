def canplaceword(grid,word,row,col,direction):
    length=len(word)
    if direction=='horizontal':
        if col+length>10:
            return False
        for i in range(length):
            if grid[row][col+i] not in ('-',word[i]):
                return False
    elif direction=='vertical':
        if row+length>10:
            return False
        for i in range(length):
            if grid[row+i][col] not in ('-',word[i]):
                return False
    return True

def placeword(grid,word,row,col,direction):
    ogstate=[]
    if direction=='horizontal':
        for i in range(len(word)):
            ogstate.append(grid[row][col+i])
            grid[row][col+i]=word[i]
    elif direction=='vertical':
        for i in range(len(word)):
            ogstate.append(grid[row+i][col])
            grid[row+i][col]=word[i]
    return ogstate

def removeword(grid,ogstate,row,col,direction):
    if direction=='horizontal':
        for i in range(len(ogstate)):
            grid[row][col+i]=ogstate[i]
    elif direction=='vertical':
        for i in range(len(ogstate)):
            grid[row+i][col]=ogstate[i]

def solve(grid,words,index=0):
    if index == len(words):
        return True
    word=words[index]
    for row in range(10):
        for col in range(10):
            for direction in ['horizontal','vertical']:
                if canplaceword(grid,word,row,col,direction):
                    ogstate = placeword(grid,word,row,col,direction)
                    if solve(grid,words,index+1):
                        return True  
                    removeword(grid,ogstate,row,col,direction)
    return False

def crosswordpuzzle(grid,words):
    solve(grid,words)
    return grid
grid = [list(input().strip()) for _ in range(10)]
words=input().strip().split(';')
crosswordpuzzle(grid, words)
for row in grid:
    print("".join(row))
