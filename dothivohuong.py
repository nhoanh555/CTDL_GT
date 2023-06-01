import matplotlib.pyplot as plt
import networkx as nx

# Khởi tạo đồ thị
G = nx.Graph()

# Thêm các đỉnh vào đồ thị
dinh = [1, 2, 3, 4, 5]
G.add_nodes_from(dinh)

# Thêm các cạnh vào đồ thị
cung = [(1, 2), (1, 3), (2, 4), (4, 5), (3, 5)]
G.add_edges_from(cung)

# Vẽ đồ thị và hiển thị lên màn hình
nx.draw(G, with_labels=True)
plt.show()
