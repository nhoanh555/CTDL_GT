# định nghĩa 1 lớp (Class) Node để biểu diễn 1 nút(Node) trong danh sách liên kết đơn 
class Node:
    # hàm khởi tạo init của lớp Node nhận vào tham số data 
    def __init__(self, data):
        # lưu trữ giá trị của data vào biến self.data của nút(Node) hiện tại 
        self.data = data
        # ban đầu gía trị của self.next sẽ được gán bằng None nghĩa là ở nút hiện tại cũng là nút cuối cùng của danh sách
        # sau khi có 1 nút mới được thêm vào danh sách thì nút trước nó sẽ thay đổi để trỏ đến nút mới và tham chiếu "next" của nút mới cũng được thiết lập thành None
        # các nút trong danh sách được kết nối với nhau thông qua các tham chiếu "next" của chúng
        self.next = None
# định nghĩa 1 lớp (Stack) với 2 phương thức là khởi tạo và 1 thuộc tính là "top"
class Stack:
    # hàm khởi tạo init của lớp Stack
    def __init__(self):
        # thuộc tính top được khởi tạo bằng giá trị None đại diện cho trạng thái ban đầu của Stack là rỗng
        self.top = None
   
    # hàm kiểm tra xem ngăn xếp có trống hay không
    def is_empty(self):
        # self.top là phần tử đầu tiên của stack, nếu nó không tồn tại thì ngăn xếp đang rỗng
        # nếu self.top là "None" tức không có phần tử nào trong Stack thì hàm trả giá trị True , ngược lại False
        if self.top is None:
            return True
        return False
   
    # hàm thêm phần tử mới vào đỉnh của ngăn xếp, trong đó x là giá trị của phần tử mới 
    def push(self, x):
        new_node = Node(x)  
    # kiểm tra xem nút mới có được khởi tạo thành công hay không (không bị None) 
    #  nếu nút mới không bị None(khởi tạo thành công) thì thực hiện các bước tiếp theo để thêm nó vào danh sách   
        if new_node is not None:
            # kiểm tra xem danh sách có bị rỗng hay không ("top" = "None")
            # nếu rỗng thì gán "new _node" cho "top" để khởi tạo danh sách 
            if self.is_empty():
                self.top = new_node
            # nếu không rỗng thì đặt"new_node.next" bằng"top" để nối new_node với phần tử đầu tiên ở hiện tại
            # rồi gán "top" cho "new_node" để cập nhật phần tử đầu tiên của danh sách
            else:
                new_node.next = self.top
                self.top = new_node
   
    # hàm dùng để loại bỏ phần tử đầu tiên khỏi Stack và trả về giá trị của phần tử đó 
    def pop(self):
        # kiểm tra xem danh sách có trống không, nếu không thì tiếp tục, ngược lại thì nó sẽ trả giá trị None
        if not self.is_empty():
            # gán giá trị biến p cho phần tử trên cùng của Stack, nghĩa là phần tử sẽ bị loại bỏ 
            p = self.top
            # đoạn code có nhiệm vụ thay đổi từ node đầu tiên sang node tiếp theo trong danh sách liên kết
            self.top = p.next
            # lưu trữ giá trị của Node hiện tại ( nút đầu tiên của Stack) vào biến x
            x = p.data
            # xóa nút đầu tiên ra khỏi danh sách 
            del p
            # trả về giá trị của nút vừa bị xóa
            return x
    
    # hàm nhập vào số n từ bàn phím và thêm vào đầu của danh sách 
    def input(self, n):
        # sử dụng vòng lặp để lặp qua từng giá trị "i" trong khoảng từ 0 đến n - 1
        for i in range(n):
            # yêu cầu người dùng nhập giá trị số từ bàn phím
            x = int(input("NHAP SO THU " + str(i) + ": "))
            # sau khi đã nhập xong, sử dụng phương thức "push" để thêm giá trị vừa nhập đó vào đầu của ngăn xếp
            self.push(x)
    
    # hàm dùng để in ra các phần tử trong ngăn, bắt đầu từ phần tử đầu tiên đến phần tử cuối cùng 
    def output(self):
        # tạo biến "p" để duyệt qua các phần tử đã có. lúc đầu "p" được gán bằng giá trị của phần tử đầu tiên 
        p = self.top
        # vòng lặp sẽ tiếp tục chạy cho đến khi biến "p" trỏ đến "None",tức là đã duyệt hết các phần tử trong ngăn
        while p is not None:
            # in ra giá trị của phần tử hiện tại mà biến "p" đang trỏ tới
            print(p.data)
            # di chuyển biến "p" đến phần tử tiếp theo trong ngăn
            p = p.next

# khởi tạo đối tượng Stack mới và gán vào biến "s"
s = Stack()
# nhập vào số phần tử cần thêm vào 
n = int(input("nhập n "))
# gọi phương thức input của "s" để thêm "n" phần tử vào
s.input(n)
# in ra màn hình
print("danh sách các phần tử vừa được nhập vào STACK")
# gọi phương thức output của "s" để in ra các phần tử trong Stack
s.output()

# yêu cầu người dùng nhập vào phần tử họ cần 
x = int(input("nhập phần tử muốn thêm vào"))
# thêm phần tử vừa mới được nhập vào vào Stack
s.push(x)
# in ra màn hình
print("STACK sau khi được thêm phần tử", x)
# câu lệnh dùng để in ra các phần tử trong Stack bắt đầu từ phần tử đầu tiên và kết thúc với phần tử cuối cùng
s.output()

# câu lệnh dùng để lấy ra phần tử trên đỉnh của Stack và đồng thời cũng xóa phần tử đó khỏi Stack "s" gán cho "p"
p = s.pop()
# in ra màn hình
print("phần tử được lấy ra và xóa đi là ", p)
print("STACK sau khi đã lấy đi phần tử")
# câu lệnh dùng để in ra các phần tử trong Stack bắt đầu từ phần tử đầu tiên và kết thúc với phần tử cuối cùng
s.output()
