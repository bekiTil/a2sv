# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        Q = deque()
        Q.append(root)
        
        while Q:
            currentElement = Q.popleft()
            if not currentElement:
                result.append("null")
                continue
            else:
                result.append(str(currentElement.val))
            Q.append(currentElement.left)
            Q.append(currentElement.right)
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        data = data.split(",")
        root = TreeNode(data[0])
        Q = deque()
        Q.append(root)
        dataIndex = 0
        
        while Q:
            currentElement = Q.popleft()
            if not currentElement:
                continue
            leftNode = None
            rightNode = None
            if data[dataIndex+1] != "null":
                leftNode = TreeNode(data[dataIndex+1])
            if data[dataIndex+2] != "null":
                rightNode = TreeNode(data[dataIndex+2])
            currentElement.left = leftNode
            currentElement.right = rightNode
            Q.append(leftNode)
            Q.append(rightNode)
            dataIndex += 2
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))