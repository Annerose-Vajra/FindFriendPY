from dataloader import load_students, load_hobbies, load_habits, load_edges
from graph import Graph
from recommender import Recommender
from mostfriend import list_most_friends

def show_menu():
    print("=== MENU ===")
    print("1. Thêm bạn")
    print("2. Xóa bạn")
    print("3. Gợi ý bạn bè")
    print("4. Liệt kê danh sách toàn bộ người dùng")
    print("5. Danh sách người có nhiều bạn nhất")
    print("6. Thoát")
    

def list_users_with_friends(students, graph):

    print("\n=== Danh sách toàn bộ người dùng ===")
    print(f"{'MSSV':<10} {'Họ tên':<20} {'Bạn bè (MSSV)':<30}")
    print("-" * 60)

    for mssv, student in students.items():
        # Lấy danh sách bạn bè dưới dạng list chuỗi MSSV
        try:
            friends = list(graph.neighbors(mssv))
        except Exception:
            friends = []  # Nếu mssv không có trong graph, coi như chưa có bạn bè
        
        
        if friends:
            friend_list = ", ".join(sorted(friends))
        else:
            friend_list = "Chưa có bạn bè"  

        print(f"{mssv:<10} {student.name:<20} {friend_list:<30}")

    print()    

def main():
    students = load_students(r'D:\VSC\DSA\GroupProject\FindFriendPY\FindFriendPY-main\data\student_info.txt')
    load_hobbies(r'D:\VSC\DSA\GroupProject\FindFriendPY\FindFriendPY-main\data\hobbyc.txt', students)
    load_habits(r'D:\VSC\DSA\GroupProject\FindFriendPY\FindFriendPY-main\data\habitc.txt', students)

    graph = Graph()
    load_edges(r'D:\VSC\DSA\GroupProject\FindFriendPY\FindFriendPY-main\data\friends.txt', graph)

    recommender = Recommender(graph, students)

    while True:
        show_menu()
        choice = input("Chọn (1-6): ").strip()

        if choice == '1':
            user_id = input("Nhập MSSV của bạn: ").strip()
            if user_id not in students:
                print(f"[!] MSSV '{user_id}' không hợp lệ.")
                continue
            other = input("Nhập MSSV bạn muốn thêm: ").strip()

            if other not in students:
                print(f"[!] MSSV '{other}' không hợp lệ.")
            elif other == user_id:
                print("[!] Không thể thêm chính mình làm bạn.")
            else:
                # Kiểm tra xem đã là bạn chưa
                current_friends = graph.neighbors(user_id)
                if other in current_friends:
                    print(f"[!] {students[other].name} (MSSV {other}) đã là bạn của bạn rồi.")
                else:
                    graph.add_edge(user_id, other)
                    print(f"✔ Đã thêm bạn: {students[other].name} (MSSV {other})")

        elif choice == '2':
            user_id = input("Nhập MSSV của bạn: ").strip()
            if user_id not in students:
                print(f"[!] MSSV '{user_id}' không hợp lệ.")
                continue
            other = input("Nhập MSSV bạn muốn xóa: ").strip()
            if other in students:
                if other in graph.neighbors(user_id):
                    graph.remove_edge(user_id, other)
                    print(f"✔ Đã xóa bạn: {students[other].name} (MSSV {other})")
                else:
                    print(f"[!] {students[other].name} (MSSV {other}) hiện không phải là bạn của bạn.")
            else:
                print(f"[!] MSSV '{other}' không hợp lệ.")

        elif choice == '3':
            user_id = input("Nhập MSSV của bạn: ").strip()
            if user_id not in students:
                print(f"[!] MSSV '{user_id}' không hợp lệ.")
                continue
            recs = recommender.recommend_friends(user_id)
            print(f"\nGợi ý bạn bè cho {students[user_id].name} (MSSV {user_id}):")
            if not recs:
                print("Không có gợi ý mới.")
            else:
                for rid, score in recs:
                    name = students[rid].name if rid in students else rid
                    print(f"- {name} (MSSV {rid}) (Điểm: {score:.1f}/10)")

        elif choice == '4':
            # gọi hàm liệt kê từ listing.py
            list_users_with_friends(students, recommender.graph)

        elif choice == '6':
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        elif choice == '5':
            print(f"{list_most_friends(graph, students)}")

        else:
            print("[!] Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
