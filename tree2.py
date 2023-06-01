from anytree import Node, RenderTree, PostOrderIter

class MyNode(Node):
    def __repr__(self):
        return self.name

def tao_cay():
    root_value = input("Giá trị gốc: ")
    root = MyNode(root_value)

    node_queue = [root]
    while len(node_queue) > 0:
        current_node = node_queue.pop(0)
        num_children = int(input(f"Nhập số lượng con của {current_node.name}: "))
        for i in range(num_children):
            child_value = input(f"Nhập giá trị con thứ {i+1}: ")
            child_node = MyNode(child_value, parent=current_node)
            node_queue.append(child_node)

    return root

goc = tao_cay()
for node in PostOrderIter(goc):
    depth = len(node.path) - 1
    prefix = "|   " * depth + "|-- "
    print(f"{prefix}{node}")
