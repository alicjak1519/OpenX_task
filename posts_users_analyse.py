from utils import maximal_geo_dist
from utils import calc_dist


class PostsUsersAnalyser:

    def create_post_number_list(self, posts, users):
        user_posts_number = self._calc_posts_number(posts, users)
        return [f"{user_name} napisał(a) {number} postów" for (user_name, number) in user_posts_number]

    def _calc_posts_number(self, posts, users):
        users_and_posts = self._merge_users_and_posts(posts, users)
        user_posts = users_and_posts.groupby('name')
        return [(user_name, len(data)) if data.post_title.any() else (user_name, 0) for user_name, data in user_posts]

    def _merge_users_and_posts(self, posts, users):
        posts_to_join = posts.set_index('userId').add_prefix('post_')
        users_and_posts = users.join(posts_to_join, on=['id'])
        return users_and_posts

    def find_nonunique_titles(self, posts):
        titles_number = posts['title'].value_counts()
        return [title for title, amount in titles_number.items() if amount > 1]

    def find_neighbours(self, users):
        neighbours = []
        for index, user in users.iterrows():
            neighbour_dist = maximal_geo_dist()
            neighbour_name = 'No neighbours :( '
            for n_index, n_user in users.iterrows():
                dist = calc_dist(user, n_user)
                if (dist < neighbour_dist) and (n_user['id'] != user['id']):
                    neighbour_dist = dist
                    neighbour_name = n_user['name']
            neighbours.append((user['name'], neighbour_name))
        return neighbours
