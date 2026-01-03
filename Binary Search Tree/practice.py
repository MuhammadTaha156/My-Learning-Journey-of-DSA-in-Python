
class Node:
    def __init__(self,left=None,item=None,right=None):
        self.left=left
        self.item=item
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
        

    def insert(self,x):
        self.root=self.r_insert(self.root,x)
    
    def  r_insert(self,root,x):
        if root is None:
            return Node(None,x,None)
        if x<root.item:
            root.left=self.r_insert(root.left,x)
        elif x>root.item:
            root.right=self.r_insert(root.right,x)
        return root
    
    def search(self,x):
        return self.r_search(self.root,x)
    
    def r_search(self,root,x):
        if root is None or x==root.item:
            return root
        if x<root.item:
            return self.r_search(root.left,x)
        else:
            return self.r_search(root.right,x)
        

    def inOrder(self):
        result=[]
        self.r_inOrder(self.root,result)
        return result
    
    def r_inOrder(self,root,result):
        if root:
            self.r_inOrder(root.left,result)
            result.append(root.item)
            self.r_inOrder(root.right,result)

    def preOrder(self):
        result=[]
        self.r_preOrder(self.root,result)
        return result
    
    def r_preOrder(self,root,result):
        if root:
            result.append(root.item)
            self.r_preOrder(root.left,result)
            self.r_preOrder(root.right,result)

    def postOrder(self):
        result=[]
        self.r_postOrder(self.root,result)
        return result
    
    def r_postOrder(self,root,result):
        if root:
            self.r_postOrder(root.left,result)
            self.r_postOrder(root.right,result)
            result.append(root.item)


    



bt=BST()

print(bt.insert(50))
print(bt.root.item)
bt.insert(60)
bt.insert(30)
bt.insert(20)
bt.insert(35)
bt.insert(70)
bt.insert(65)
bt.insert(75)
print(bt.root.right.item)
print(bt.inOrder())
print(bt.preOrder())
print(bt.postOrder())

print(bt.search(75))
print(bt.search(30))

