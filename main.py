from dataloader import load_students, load_hobbies, load_habits, load_edges
from graph import Graph
from recommender import Recommender

def main():
    students = load_students(r'data/student_info.txt')
    load_hobbies(r'data/hobbyc.txt', students)
    load_habits(r'data/habitc.txt', students)

    graph = Graph()
    load_edges(r'data/friends.txt', graph)

    recommender = Recommender(graph, students)

    user_id = input("Nhập mã số sinh viên để tìm bạn bè: ").strip()

    if user_id not in students:
        print(f"Mã số sinh viên '{user_id}' không hợp lệ.")
        return

    recs = recommender.recommend_friends(user_id)

    print(f"Gợi ý bạn bè cho {students[user_id].name} (MSSV {user_id}):")
    for rid, score in recs:
        if rid in students:
            print(f"- {students[rid].name} (MSSV {rid}) (Điểm: {score:.1f}/10)")
        else:
            print(f"- {rid} (Điểm: {score:.1f}/10)")


if __name__ == "__main__":
    main()
