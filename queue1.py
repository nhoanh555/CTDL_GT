import queue as que #Sử dụng thư viện Queue 
q = que.Queue() #tạo Queue rỗng 

#Tạo hàm kiểm tra giá trị Queue có rỗng không, nếu không rỗng in ra giá trị còn lại 
def kiem_tra_rong(q):
    if q.empty():
        print("Queue rỗng")
    else:
        print("Queue không rỗng")
        q_list = list(q.queue)
        print("Các phần tử còn lại:", q_list)
    
#Tạo hàm kiểm tra giá trị Queue có đầy không (Giới hạn queue) (Trường hợp đặc biệt)
q1 = que.Queue(maxsize=3)
q1.put(1)
q1.put(2)
q1.put(3)
def kiem_tra_day(q):
    if q.full():
        print("Queue đã đầy")
    else:
        print("Queue chưa đầy")
    
#tạo hàm thêm nhiều giá trị vào Queue 
def them_phan_tu(q):
    n = int(input("Nhập số phần tử muốn thêm: "))
    for i in range (1,n+1):
        x = int(input("Nhập phần tử thứ " + str(i) + " muốn thêm: "))
        q.put(x) #Thêm 1 giá trị vào Queue

#Tạo hàm lấy phần tử đồng thời xóa nó khỏi Queue
def lay_phan_tu(q):
    #Đầu tiên, ta xác định nếu hàm Queue ta đã tạo có đủ số lượng phần tử cần lấy ra không (lấy ra quá nhiều sẽ lỗi)
    n = int(input("Nhập số lượng phần tử muốn lấy: "))
    if q.qsize() < n:
        print("Không đủ phần tử để lấy ra")
        return
    for i in range (1,n+1):
        print("Giá trị lấy ra:",q.get()) #Lấy phần tử trong Queue, đồng thời xóa phần tử đó khỏi hàng đợi
    return q
#Tạo hàm hiển thị Queue bằng cách chuyển Queue sang giá trị list 
def hien_thi_queue(q):
    q_list = list(q.queue)
    print("Các phần tử đã nhập:", q_list)

#Chương trình hoàn chỉnh
#Tạo giá trị Queue 4 rỗng
q4 = que.Queue() 
#Kiểm tra rỗng
kiem_tra_rong(q4)
#Nhập giá trị
them_phan_tu(q4)
#Hiển thị
hien_thi_queue(q4)
#Lấy và xóa bỏ phần tử
lay_phan_tu(q4)
#Kiểm tra rỗng lại lần nữa 
kiem_tra_rong(q4)
