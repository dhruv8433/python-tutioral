class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root=self.insertIntoTree(self.root,data)

    def insertIntoTree(self, root, data):
        if root is None:
         
            return Node(data)
        if data<root.data:
            root.left=self.insertIntoTree(root.left,data) 
            
        elif data>root.data:
            root.right=self.insertIntoTree(root.right,data)
        return root      

    def search(self, data):
        return self.findIntoTree(self.root, data)

    def findIntoTree(self,root, data):
        if root is None or root.data == data:
            return root
        
        if(root.data > data):
            return self.findIntoTree(root.left, data)    
        else:
            return self.findIntoTree(root.right, data)    

    
   
    def inorder(self): # left, root, right
       result = []
       self.rinorder( self.root, result)
       return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(self.root.left, result)
            result.append(root.data)
            self.rinorder(self.root.right, result)

    # def preorder(self): # root, left, right
    #     self.findRoot()
    #     self.findLeft() 
    #     self.findRight()

    # def postorder(self): # left, right, root
    #     self.findLeft() 
    #     self.findRight()
    #     self.findRoot()

bst = BinarySearchTree()
for i in [30, 23, 45, 12, 25, 35, 50]:
    bst.insert(i)
s=bst.search(25)
print(s.data if s else "Not Found")
print(bst.inorder())