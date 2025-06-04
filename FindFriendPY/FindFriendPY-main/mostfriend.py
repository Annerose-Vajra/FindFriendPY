from dataloader import load_students, load_hobbies, load_habits, load_edges
from graph import Graph 

def bubble_sort(arr):
    n = len(arr)
    # Duyệt qua tất cả các phần tử trong danh sách
    for i in range(n):
        # Duyệt từ đầu đến cuối, hoán đổi nếu cần
        for j in range(0, n - i - 1):  # Mỗi lần duyệt giảm bớt phần tử đã sắp xếp
            if arr[j][1] < arr[j + 1][1]:  # So sánh theo số bạn (index 1)
                # Hoán đổi nếu cần
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def list_most_friends(graph, students):
    # Tính số lượng bạn của mỗi sinh viên
    friend_count = {}
    
    for student_id in students:
        friends = graph.neighbors(student_id)
        friend_count[student_id] = len(friends)
    friend_count_list = [(student_id, count) for student_id, count in friend_count.items()]
    # Sắp xếp danh sách sinh viên theo số bạn giảm dần
    sorted_friend_count = bubble_sort(friend_count_list)
    
    # In ra sinh viên có nhiều bạn nhất
    print("Danh sách sinh viên có nhiều bạn nhất:")
    for student_id, count in sorted_friend_count[:2]: # Lấy 2 sinh viên có nhiều bạn nhất
        print(f"{students[student_id].name} (MSSV {student_id}) - {count} bạn")
