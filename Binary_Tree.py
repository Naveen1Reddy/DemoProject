# Binary Tree

class Node:
    def __init__(self,x) -> None:
        self.left = None
        self.right = None
        self.data = x

def createbt():
    root = None
    val = int(input("Enter Data: "))
    if val == -1:
        return None
    root = Node(val)
    print(f'Enter value for left of {val} ')
    root.left = createbt()

    print(f'enter Value for Right of {val}')
    root.right = createbt()

    return root

