from dataloader import load_students, load_hobbies, load_edges
from graph import Graph
from recommender import Recommender

def main():
    students = load_students(r'D:\VSC\DSA\FindFriendPY\data\student_info.txt')
    load_hobbies(r'D:\VSC\DSA\FindFriendPY\data\hobbyc.txt', students)
    graph = Graph()
    load_edges(r'D:\VSC\DSA\FindFriendPY\data\friends.txt', graph)

    recommender = Recommender(graph)

    user_id = input("Nhập mã số sinh viên để tìm bạn bè: ").strip()

    if user_id not in students:
        print(f"Mã số sinh viên '{user_id}' không hợp lệ.")
        return

    recs = recommender.recommend_friends(user_id)

    print(f"Gợi ý bạn bè cho {students[user_id].name} (MSSV {user_id}):")
    for rid in recs:
        if rid in students:
            print(f"- {students[rid].name} (MSSV {rid})")
        else:
            print(f"- {rid}")

if __name__ == "__main__":
    main()
