# lớp node
class Node: 
   
    # chức năng khởi tao đối tượng node
    def __init__(self, data): 
        self.data = data  # gán dữ liệu 
        self.next = None  # khởi tạo
                          # tiếp theo là null null 
   
# lớp danh sách liên kết
class danhsachlienket: 
     
    # chức năng khởi tạo liên kết  
    # danh sách đối tượng 
    def __init__(self):  
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

# Tạo danh sách liên kết đơn mới
llist = LinkedList()

# Thêm phần tử vào đầu danh sách
llist.add_to_head(input("Phần tử đầu danh sách bạn chọn là: "))
llist.add_to_head(input("Phần tử đầu danh sách bạn chọn là: "))
llist.add_to_head(input("Phần tử đầu danh sách bạn chọn là: "))

# Thêm phần tử vào cuối danh sách
llist.add_to_tail(input("Phần tử cuối danh sách bạn chọn là: "))
llist.add_to_tail(input("Phần tử cuối danh sách bạn chọn là: "))
llist.add_to_tail(input("Phần tử cuối danh sách bạn chọn là: "))

# Xóa phần tử khỏi danh sách
llist.remove(input("Xóa phần tử: "))
# In kết quả
print("Kết quả sau khi thực hiện thao tác được trả về như sau:")
current = llist.head
while current is not None:
    print(current.data)
    current = current.next

# Kiểm tra phần tử có tồn tại trong danh sách hay không
if llist.search(input("Nhập phần tử cần kiểm tra: ")):
    print(f"Phần tử có tồn tại trong danh sách")
else:
    print("Phần tử không tồn tại trong danh sách")
