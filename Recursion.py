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
print(ans)


def powset(arr ,i):

    if i >= len(arr): return [[]]

    temp = powset(arr,i+1)
    ans = [] + temp

    for x in temp:
        x.append(arr[i])
        ans.append(x)

    return ans

powset([1,2,3],0)