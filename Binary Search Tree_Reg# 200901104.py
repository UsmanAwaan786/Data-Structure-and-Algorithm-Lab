
# Name: Muhammad Usman       Reg # : 200901104
class B_S_T_Node:   #node class
	def __init__(self, val): # constructor
		self.left = None     #left of  node
		self.right = None    #right of  node
		self.val=val         # node value


def insert_search_tree(root, val): # BST insert function by comparing value of Root Node
	if root is None:
		return B_S_T_Node(val)
	else:
		if root.val == val:
			return root
		elif root.val < val:
			root.right = insert_search_tree(root.right, val)
		else:
			root.left = insert_search_tree(root.left, val)
	return root


def inorder(root):  #recursive inorder function
	if root:
		inorder(root.left)
		print(root.val,end=("-->"))
		inorder(root.right)
        
def preorder(root):  #recursive preorder function
	if root:
         print(root.val,end=("-->"))
         preorder(root.left)
         preorder(root.right)
         
         
def postorder(root): #recursive postorder function
	if root:
         postorder(root.left)
         postorder(root.right)
         print(root.val,end=("-->"))         


if __name__=="__main__": 
 
 root=B_S_T_Node(5)  #root node created with certain value
 

 
root = insert_search_tree(root, 12) 
root = insert_search_tree(root, 58)
root = insert_search_tree(root, 47)
root = insert_search_tree(root, 101)
root = insert_search_tree(root, 69)
root = insert_search_tree(root, 0)
print("our binary serach tree is in ¨Inoreder form¨: ",end=(" "))
inorder(root)
print("\n\nour binary serach tree is in ¨Preoreder form¨: ",end=(" "))
preorder(root)
print("\n\nour binary serach tree is in ¨Postoreder form¨: ",end=(" "))
postorder(root)
