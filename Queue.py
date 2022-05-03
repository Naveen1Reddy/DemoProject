class node:
    def __init__(self, data: int, next: int = None):
        self.data = data
        self.next = next


#Queue Using A linked List
class Q:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def add_ele(self,x):
        temp = node(x)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = self.tail.next
        
    
    def pop_ele(self):
        if self.head == None:
            return "Empty Queue"
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp
    
    def peek_ele(self):
        return self.head.data
            

# Queue Using a List
class Qu:
    def __init__(self) -> None:
        self.qu = []
    
    def add_ele(self,x):
        self.qu.append(x)
    
    def pop_ele(self):
        ans = self.qu[0]
        self.qu = self.qu[1:]

        return ans
    
    def peek_ele(self):
        return self.qu[0]

# queue Using Two Stacks 

from collections import deque


class Que:
    def __init__(self) -> None:
        self.s1 = deque()
        self.s2 = deque()

    def add_ele(self,x):
        self.s1.append(x)

    def pop_ele(self):
        if len(self.s1) < 1:
            return "Empty"
        else:
            while len(self.s1) > 0 :
                self.s2.append(self.s1.pop())

            ans = self.s2.pop()
            while len(self.s2) > 0:
                self.s1.append(self.s2.pop())
            
            return ans

        

    def peek_ele(self):
        if len(self.s1) < 1:
            return "Empty"
        else:
            while len(self.s1) > 0 :
                self.s2.append(self.s1.pop())

            ans = self.s2[-1]
            while len(self.s2) > 0:
                self.s1.append(self.s2.pop())
            return ans
