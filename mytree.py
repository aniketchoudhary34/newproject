#class node:
#    def __init__(self,data):
#        self.left=None
#        self.right=None
#        self.data=data
#    def show(self):
#        if self.left:
#            self.left.show()
#        print(self.data)
#        if self.right:
#            self.right.show()
#root=node(100)
#r_left=node(99)
#r_right=node(10)
#
#root.left=r_left
#root.right=r_right
#root.show()    
#



class treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=treenode(10)
node1=treenode(2)
node2=treenode(5)
root.left = node1
root.right=node2
node5=treenode(45)
node6=treenode(58)
node1.left=node5
node1.right=node6

print(root.data) 
print(root.left.data)
print(root.right.data)       
print(node1.left.data)
print(node1.right.data)