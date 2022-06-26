def powset(arr ,i):

    if i >= len(arr): return [[]]

    temp = powset(arr,i+1)
    ans = [] + temp

    for i in temp:
        i.append(arr[i])
        ans.append(i)

    return ans

powset([1,2,3],0)