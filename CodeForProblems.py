
# using all function 
print(all(i == i for i in range(1,10)))


# Operator overloading
class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print('Lets add')
        return self.num * n2.num

n1 = Number(10)
n2 = Number(11)
print(n1+n2)



# Implementing Linked List

class Node:
    def __init__(self,data,next,) -> None:
        self.data = data
        self.next = next
    
class LL:
    def __init__(self) -> None:
        self.head = None
    
    def Front(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def end(self,data):
        if self.head is None:
            self.headd = Node(data,None)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def print(self):
        if self.head is None:
            print("empty")

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)    

if __name__ == '__main__':
    l1= LL()
    l1.Front(10)
    l1.Front(12)
    l1.end(18)
    l1.print()

# Quick Sort 

def par(arr,low,high):
    i = low -1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def qck(arr,low,high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = par(arr,low,high)

        qck(arr,low,pi-1)
        qck(arr,pi+1,high)




l = [6,2,9,6,2,1,8,5,3]
a,b = l[0],l[1]

qck(l,0,8)
print(l)

#  Codechef - Hill sequence
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int,input().split()))
    dict1 = {}

    # storing values in dict1 as keys and their count as values
    for i in l1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    
    # checking any values has count >2 
    flag = False
    for i in l1 :
        if dict1[i] > 2:
            flag = True
            break
    
    # if Max elemnt occurs more than once output "-1"
    # if any values occues morethan twice also output '-1'
    if dict1[max(l1)] > 1 or flag :
        print(-1)
    else:
        # if l1 has no duplicates we just need to sort the list and copy the list to l2
        l2 = []
        if len(l1) == len(set(l1)):
            l1.sort()
            l2 = l1

        # if l1 has duplicates then we need to arrange them in hill manner
        else:
            l1.sort()
            max_ele = l1.pop(-1)
            l3 = []
            l4 = []
            for i in l1:
                if i not in l3:
                    l3.append(i)
                else:
                    l4.append(i)
            l4.reverse()

            l2 = l3 + [max_ele] + l4

            for i in l2:
                print(i,end = ' ')
            print()


# Merge Sort - Basic 
# sorting Two sorted lists into a single Sort List
l1 = [1,2,3,4,5]
l2 = [2,3,4,7,9]
l3 = []
s1,s2 = 0,0
while s1 < len(l1)-1:
    if l1[s1] <= l2[s2]:
        l3.append(l1[s1])
        s1 += 1
    else:
        l3.append(l2[s2])
        s2 += 1
l3 = l3 +l1[s1:] + l2[s2:]
print(l3)

# Binary Tree - Inorder Traversal
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None
    
tree = Node(1)
tree.left = Node(4)
tree.right = Node(5)
#tree.right =10

def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)

printInorder(tree)

# Happy Number
def happy(n):
    out = 0
    for i in str(n):
        out += int(i)**2
    return out

def happyno(n):
    s1 = n
    s2 = n
    while True :
        s1 = happy(s1)
        s2 = happy(happy(s2))
        if s1 == s2:
            break
    return (s1 == 1)

n = int(input('Enter a number : '))
print(happyno(n))

# Bin value to Decimal Equivalent ot 32bit reverse bin value

def bintobin(n):
    binval = bin(n)
    binval = binval[2:]
    length = len(binval)
    remaing = 32 - length
    newbin = '0'*remaing + binval
    multiplier = 1
    out = 0
    for i in newbin:
        out += int(i)*multiplier
        multiplier *= 2
    return out

print(bintobin(1))

# Longest Palindromic Subsequence in a Given string
# Function to pra subString str[low..high]
def printSubStr(str, low, high):
		print(str[low:high])

# This function prints the
# longest palindrome subString
# It also returns the length
# of the longest palindrome
def longestPalSubstr(str):
	
	# Get length of input String
	n = len(str)
	
	# All subStrings of length 1
	# are palindromes
	maxLength = 1
	start = 0
	
	# Nested loop to mark start
	# and end index
	for i in range(n):
		for j in range(i, n):
			flag = 1
			
			# Check palindrome
			for k in range(0, ((j - i) // 2) + 1):
				if (str[i + k] != str[j - k]):
					flag = 0

			# Palindrome
			if (flag > 0 and (j - i + 1) > maxLength):
				start = i
				maxLength = j - i + 1
				
	print("Longest palindrome subString is: ", end = "")
	printSubStr(str, start, start + maxLength)

	# Return length of LPS
	return maxLength

# Driver Code
if __name__ == '__main__':

	str = "asuszenbook"
	
	print("\nLength is: ", longestPalSubstr(str))


# hacker rank candies Problem
n = 10
l1 = [2,4,2,6,1,7,8,9,2,1]

ltr = [1]*n
rtl = [1]*n

for i in range(1,n):
    if l1[i] > l1[i-1]:
        ltr[i] = ltr[i-1]+1

for j in range(n-2,-1,-1):
    if l1[j] > l1[j+1]:
        rtl[j] = rtl[j]+1
out = 0
for i in range(n):
    out += max(ltr[i],rtl[i])
print(out)



# Swap Problem

def bintodec(s):
    out = 0
    s = s[::-1]
    for i in range(len(s)):
        if s[i] == '1':
            out += 2**i
    
    return out


swap_cost = 1
change_cost = 2
binarystring = '101010101'
binarystring = list(binarystring)
given_money = 7
current_binaryValue = bintodec(binarystring)

zero_pointer = len(binarystring) - 1
one_pointer = 0

while given_money >= swap_cost and zero_pointer > one_pointer :
    if binarystring[one_pointer] == '1':
        if binarystring[zero_pointer] == '0':
            binarystring[one_pointer],binarystring[zero_pointer] = binarystring[zero_pointer],binarystring[one_pointer]
            given_money -= swap_cost
            zero_pointer -= 1
            one_pointer += 1
        else:
            zero_pointer -= 1
    else:
        one_pointer += 1

for i in range(len(binarystring)):
    if binarystring[i] == '1' and given_money >= change_cost :
        binarystring[i] = '0'
        given_money -= change_cost
    
    if given_money < change_cost:
        break

Final_binary_Val = bintodec(binarystring)

print(current_binaryValue,Final_binary_Val)


"""
Ninja Control 

Given a 8*8 matrix where each block is a house so total 64 houses
Ninjas land on a particular block and can take control over all blocks -
  horizontal and Vertical to that Position .
  
When given a list of Positions find The total Blocks occupied by the Ninjas
 Ex : l1 = [[5, 5], [5, 3]]
"""

# CareFul With Matrix Creation using - [[0]*8]*8 this is Not Giving Correct Ans

mat = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
l1 = [[5, 5], [3, 3]]
count = 0
for i in l1:
    x, y = i[0], i[1]
    if mat[x][0] == 0:
        for j in range(8):
            if mat[x][j] == 0:
                count += 1
                mat[x][j] = 1

    if mat[0][y] == 0:
        for j in range(8):
            if mat[j][y] == 0:
                count += 1
                mat[j][y] = 1

print(count)

# Buy and Sell Stocks 3 - LeetCode . 123

def buysell(prices):
    min_price1 = min_price2 = 9999999999
    profit1 = profit2 = 0

    for i in range(len(prices)):
        min_price1 = min(prices[i], min_price1)
        profit1 = max(profit1,prices[i] - min_price1)

        min_price2 = min(min_price2 , prices[i] - profit1)
        profit2 = max(profit2,prices[i] - min_price2)
    
    return profit2


