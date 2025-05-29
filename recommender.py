class Recommender:
    def __init__(self, graph, students):
        self.graph = graph
        self.students = students

    def recommend_friends(self, user_id, max_results=3, w_mutual=0.3, w_hobby=0.5, w_habit=0.2):
        if not self.graph.has_node(user_id):
            return []

        friends = set(self.graph.neighbors(user_id))
        user = self.students.get(user_id)
        if not user:
            return []

        mutual_counts = {}
        hobby_counts = {}
        habit_counts = {}

        for friend in friends:
            foafs = set(self.graph.neighbors(friend))
            for foaf in foafs:
                if foaf == user_id or foaf in friends:
                    continue

                mutual_counts[foaf] = mutual_counts.get(foaf, 0) + 1
                foaf_hobbies = self.students[foaf].hobbies if foaf in self.students else set()
                hobby_counts[foaf] = len(user.hobbies.intersection(foaf_hobbies))
                foaf_habits = self.students[foaf].habits if foaf in self.students else set()
                habit_counts[foaf] = len(user.habits.intersection(foaf_habits))

        scores = {}
        max_score = 0
        for uid in mutual_counts:
            score = (w_mutual * mutual_counts.get(uid, 0)
                     + w_hobby * hobby_counts.get(uid, 0)
                     + w_habit * habit_counts.get(uid, 0))
            scores[uid] = score
            if score > max_score:
                max_score = score

        # Chuẩn hóa điểm về thang 0-10
        recommendations = []
        for uid, score in scores.items():
            normalized_score = (score / max_score) * 10 if max_score > 0 else 0
            recommendations.append((uid, normalized_score))

        recommendations.sort(key=lambda x: x[1], reverse=True)

        return recommendations[:max_results]
