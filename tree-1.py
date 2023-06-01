import anytree as cay
from anytree import Node, RenderTree, NodeMixin

class Node:
    def __init__(self, ten):
        self.ten = ten
        self.children = []

    def them_cay(self, node):
        self.children.append(node)

def tao_cay():
    root_value = input("Giá trị gốc: ")
    root = Node(root_value)

    node_queue = [root]
    while len(node_queue) > 0:
        current_node = node_queue.pop(0)
        num_children = int(input(f"Nhập số lượng con của {current_node.ten}: "))
        for i in range(num_children):
            child_value = input(f"Nhập giá trị con thứ {i+1}: ")
            child_node = Node(child_value)
            current_node.them_cay(child_node)
            node_queue.append(child_node)

    return root
goc = tao_cay()
for pre, _, node in RenderTree(goc):
    print("%s%s" % (pre, node.ten))
