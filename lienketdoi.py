#Tạo 1 lớp để tạo 1 nút trong danh sách được liên kết
class Node:
    def __init__ (self, data):
        self.item = data    #Biến item: lưu phần tử thực tế của Node
        self.next = None    #Biến next: lưu trữ địa chỉ đến nút tiếp theo
        self.prev = None    #Biến prev: lưu trữ địa chỉ đến nút trước đó trong danh sách được liên kết kép

#Tạo một lớp doublyLinkedList
#Chứa các hàm để chèn, xóa và hiển thị các phần tử của danh sách được liên kết kép
class doublyLinkedList:
    def __init__(self):
        self.start_node = None

#Chúng ta thêm các hàm sau vào lớp doublyLinkedList

    #1. Chèn các mục vào danh sách trống
    def InsertToEmptyList (self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")

    #2. Chèn các mục ở cuối
    def InsertToEnd (self, data):
        #Kiểm tra nếu danh sách trống
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        #Lặp lại cho đến khi gặp NULL tiếp theo
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    #3. Xóa các phần tử khỏi màn hình bắt đầu
    def DeleteAtStart (self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None;

    #4. Xóa các yếu tố từ cuối
    def delete_at_end (self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    #5. Đi qua danh sách được liên kết
    def Display (self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

#Tạo 1 danh sách liên kết đôi
NewDoublyLinkedList = doublyLinkedList()
#Chèn phần tử vào danh sách rỗng
NewDoublyLinkedList.InsertToEmptyList(10)
#Chèn phần tử vào cuối
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.InsertToEnd(50)
NewDoublyLinkedList.InsertToEnd(60)
#Hiển thị dữ liệu
NewDoublyLinkedList.Display()
#Xóa các phần tử từ đầu
NewDoublyLinkedList.DeleteAtStart()
#Xóa các phần tử từ cuối
NewDoublyLinkedList.DeleteAtStart()
#Hiển thị dữ liệu
NewDoublyLinkedList.Display

