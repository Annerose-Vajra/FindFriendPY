class Recommender:
    def __init__(self, graph):
        self.graph = graph

    def recommend_friends(self, user_id, max_results=5):
        if not self.graph.has_node(user_id):
            return []

        friends = self.graph.neighbors(user_id)
        mutual_counts = {}

        for friend in friends:
            friends_of_friend = self.graph.neighbors(friend)
            for foaf in friends_of_friend:
                if foaf != user_id and foaf not in friends:
                    mutual_counts[foaf] = mutual_counts.get(foaf, 0) + 1

        sorted_recs = sorted(mutual_counts.items(), key=lambda x: x[1], reverse=True)
        return [rec[0] for rec in sorted_recs[:max_results]]
