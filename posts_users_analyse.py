class PostsUsersAnalysator():

    def __init__(self, posts=None, users=None):
        self.posts = posts
        self.users = users

    def create_posts_number_list(self):
        posts_and_users = self._merge_post_and_users(self.posts, self.users)
        string_list = []
        user_posts_amount = posts_and_users.groupby('user_name')
        for user_name, count in user_posts_amount:
            string_list.append(f"{user_name} napisał(a) {len(count)} postów")
        return string_list

    def _merge_post_and_users(self, posts, users):
        users_to_join = users.set_index('id').add_prefix('user_')
        posts_and_users = posts.join(users_to_join, on=['userId'])
        return posts_and_users

    def find_nonunique_titles(self):
        titles_number = self.posts['title'].value_counts()
        nonunique_titles = [title for title, amount in titles_number.items() if amount > 1]
        return nonunique_titles

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
