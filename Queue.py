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

