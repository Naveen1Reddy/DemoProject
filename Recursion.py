def powerset(arr , i , ans , subset):
    if i == len(arr):
        ans.append(list(subset))
        return

    subset.append(arr[i])
    powerset(arr ,i+1 ,ans , subset)

    subset.pop()
    powerset(arr,i+1, ans, subset)

arr = [1,2,3,4,5]
ans = []
subset = []
powerset(arr,0,ans,subset)
# print(ans)


def powset(arr ,i):

    if i >= len(arr): return [[]]

    temp = powset(arr,i+1)
    ans = [] + temp

    for x in temp:
        x.append(arr[i])
        ans.append(x)

    return ans

powset([1,2,3],0)


# Unique Subsets of Array which has Duplicate Elements

def subsets(arr , i ,out , sub):

    if i >= len(arr):
        ans = tuple(sub)
        if ans not in out:
            out.add(ans)
        
        return
    
    sub.append(arr[i])
    subsets(arr,i+1,out,sub)

    sub.pop()
    subsets(arr, i+1 ,out,sub)


arr = [1,2,3,1]
out = set()
sub = []
subsets(arr,0,out,sub)

# Not A good Apporach , Try using incrementing 'i ' unit we find next ele and i < len(arr)

# print(out)


"""
N Queen Problem
"""
def issafe(row,col,board):

    # check from curr to up
    i = row
    while (i >= 0):
        if board[i][col] == 1:
            return False
        i -= 1

    # check from curr to topLeft
    i = row
    j = col
    while (i >= 0) and (j >= 0):
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while (i >= 0) and (j < n):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def queen(row ,n ,ans ,board):
    if row == n:
        temp = [0]*n
        for x in range(n):
            for y in range(n):
                if board[x][y] == 1:
                    temp[y] = x+1

        ans.append(temp)
        return
    
    for i in range(n):

        if issafe(row,i,board):
            board[row][i] = 1
            queen(row+1 ,n, ans, board)

            board[row][i] = 0



n = 4
board = []
for i in range(n):
    board.append(list([0]*5))


row = 0
ans = []

queen(row ,n ,ans,board)

print(ans)

