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

# Height Of A Binary Tree
def height(root):
    if root == None:
        return 0

    return max(height(root.left),height(root.right)) + 1


# Size Of A Binary Tree

def size(root):
    if root == None:
        return 0

    return size(root.left)+size(root.right) + 1

# Maximum Value In A Binary Tree

def max_val(root):
    if root == None:
        return 0
    
    return max(root.data,   max(  max_val(root.left),  max_val(root.right)  )   )

# Binary Tree Traversals 
# 1 - Pre Order Traversal

def preorder(root):
    if root:
        print(root.Data)

        preorder(root.left)
        
        preorder(root.right)


# 2 - in Order Traversal

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# 3 - Post Order Traversal

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
    
# 4 - Level Order Traversal

def LevelOrder(root):
    if root == None:
        return None
    
    queue = []
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp.data)

        if temp.left != None:
            queue.append(temp.left)
        if temp.right != None:
            queue.append(temp.right)
    
 



# Left View of A Binary Tree




# Right View Of A  Binary Tree





# Top View Of A Binary Tree 




# Bottom View Of A Binary Tree




# Flatten A Binary Tree into A Doubly Linked List