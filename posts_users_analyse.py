class PostsUsersAnalyser:

    def __init__(self, posts=None, users=None):
        self.posts = posts
        self.users = users

    def create_post_number_list(self):
        user_posts_number = self._calc_posts_number()
        return [f"{user_name} napisał(a) {number} postów" for (user_name, number) in user_posts_number]

    def _calc_posts_number(self):
        users_and_posts = self._merge_users_and_posts()
        user_posts = users_and_posts.groupby('name')
        return [(user_name, len(data)) if data.post_title.any() else (user_name, 0) for user_name, data in user_posts]

    def _merge_users_and_posts(self):
        posts_to_join = self.posts.set_index('userId').add_prefix('post_')
        users_and_posts = self.users.join(posts_to_join, on=['id'])
        return users_and_posts

    def find_nonunique_titles(self):
        titles_number = self.posts['title'].value_counts()
        return [title for title, amount in titles_number.items() if amount > 1]

    def find_neighbours(self):
        neighbours = []
        for index, user in self.users.iterrows():
            neighbour_dist = self._maximal_geo_dist()
            neighbour_name = 'No neighbours :( '
            for n_index, n_user in self.users.iterrows():
                dist = self._calc_dist(user, n_user)
                if (dist < neighbour_dist) and (n_user['id'] != user['id']):
                    neighbour_dist = dist
                    neighbour_name = n_user['name']
            neighbours.append((user['name'], neighbour_name))
        return neighbours

    def _maximal_geo_dist(self):
        return (180 ** 2 + 360 ** 2) ** (1 / 2)

    def _calc_dist(self, user, n_user):
        lat = float(user['address']['geo']['lat'])
        lng = float(user['address']['geo']['lng'])
        n_lat = float(n_user['address']['geo']['lat'])
        n_lng = float(n_user['address']['geo']['lng'])
        return ((lat - n_lat) ** 2 + (lng - n_lng) ** 2) ** (1 / 2)
