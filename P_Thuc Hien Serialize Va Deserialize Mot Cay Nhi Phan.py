class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return 'None'
    return str(root.val) + ' ' + serialize(root.left) + ' ' + serialize(root.right)

def deserialize(s):
    def dfs():
        val = next(vals)
        if val == "None":
            return None
        node = Node(val)
        node.left = dfs()
        node.right = dfs()
        return node
    vals = iter(s.split())
    return dfs()

def print_tree(node):
    if node is None:
        return
    print(node.val)
    print_tree(node.left)
    print_tree(node.right)

# Tạo cây nhị phân
node = Node('root', Node('left', Node('left.left')), Node('right'))

# Serialize cây nhị phân
serialized_data = serialize(node)
print("Serialized data:", serialized_data)

# Deserialize chuỗi serialized và in ra cây nhị phân đã được deserialize
deserialized_node = deserialize(serialized_data)
print("Deserialized tree:")
print_tree(deserialized_node)
