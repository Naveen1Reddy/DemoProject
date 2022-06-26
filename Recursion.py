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
    
    sub.append(arr[i])
    subsets(arr,i+1,out,sub)

    sub.pop()
    subsets(arr, i+1 ,out,sub)


arr = [1,2,3,1]
out = set()
sub = []
subsets(arr,0,out,sub)

print(out)

     