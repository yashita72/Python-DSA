

class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
    
    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)
          
    def preorder(root):
        if not root:
         return []
        return [root.val] + preorder(root.left) + preorder(root.right)    
    def postorder(root):
        if not root:
         return []
        return postorder(root.left) + postorder(root.right) + [root.val]
    def levelorder(root):
     if not root:
       return []
     queue=[root]
     result=[]
     while queue:
        current=queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
     return result