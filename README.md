# I. Cách tải code
## 1. Tạo folder để lưu code sau đó mở Terminal cd vào folder vừa tạo
```
cd "Link folder của bạn"
```
## 2. Clone code về
```
git clone https://github.com/Annerose-Vajra/FindFriendPY.git
```
## 3. Vào file main.py và chạy code
# II. Chức năng của code
## 1. Khởi tạo và đọc dữ liệu (Dataloader)
### Chức năng:
 - Đọc dữ liệu từ các file text lưu trữ thông tin sinh viên, sở thích, thói quen và mối quan hệ bạn bè.

### Chi tiết:

 - load_students(filepath): đọc file student_info.txt, mỗi dòng chứa mã sinh viên (MSSV) và tên, tạo đối tượng Student lưu vào dict students với key là MSSV.

 - load_hobbies(filepath, students): đọc file hobbyc.txt, mỗi dòng chứa MSSV và một sở thích, thêm sở thích vào đối tượng Student tương ứng.

 - load_habits(filepath, students): tương tự nhưng với file habitc.txt lưu thói quen.

 - load_edges(filepath, graph): đọc file friends.txt, mỗi dòng chứa cặp MSSV biểu thị một cạnh trong đồ thị bạn bè, gọi graph.add_edge(u, v) để tạo quan hệ vô hướng.

## 2. Mô hình dữ liệu (Models)
### Student:

 - Lưu trữ thông tin cá nhân sinh viên: MSSV, tên, sở thích (set), thói quen (set).

 - Phương thức để thêm sở thích và thói quen.

## 3. Cấu trúc dữ liệu chính: Graph
### Graph:

 - Lưu trữ mạng xã hội dưới dạng đồ thị vô hướng.

 - Dùng dict với key là MSSV, value là danh sách các bạn trực tiếp (neighbors).

### Các phương thức:

 - add_edge(u, v): thêm quan hệ bạn bè 2 chiều giữa u và v.

 - neighbors(u): trả về danh sách bạn của u.

 - has_node(u): kiểm tra u có trong mạng không.

## 4. Thuật toán gợi ý bạn bè (Recommender)
### Ý tưởng:
Gợi ý những sinh viên chưa là bạn trực tiếp nhưng có mối quan hệ bạn chung, sở thích và thói quen tương đồng với user.

### Chi tiết:

- Lấy bạn trực tiếp của user.

- Lấy bạn của bạn (bạn cấp 2).

- Đếm số bạn chung với user.

- Đếm số sở thích chung giữa user và bạn cấp 2.

- Đếm số thói quen chung.

- Tính điểm tổng bằng cách kết hợp các yếu tố trên theo trọng số do bạn định nghĩa.

-  hóa điểm về thang 0-10 để dễ đánh giá.

- Sắp xếp theo điểm giảm dần và trả về top-k kết quả.

## 5. Giao diện và xử lý tương tác (Main)
Hiển thị menu với các lựa chọn: thêm bạn, xóa bạn, gợi ý bạn bè, xem danh sách sinh viên, thoát.

Khi người dùng chọn gợi ý bạn bè (option 3), yêu cầu nhập MSSV.

Kiểm tra MSSV hợp lệ, nếu không thông báo lỗi.

Gọi hàm gợi ý bạn bè, hiển thị kết quả kèm điểm tương thích.

Các lựa chọn thêm/xóa bạn hiện chưa hỗ trợ hoặc đang chờ phát triển.

Lựa chọn danh sách sinh viên gọi hàm list_users để hiển thị.


