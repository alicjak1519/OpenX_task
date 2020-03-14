import pandas as pd
import requests


class PostsUsersAnalysator():

    def __init__(self, posts=None, users=None):
        self.posts = posts
        self.users = users
        self.posts_and_users = merge_post_and_users(self.posts, self.users)

    def create_post_amount_list(self):
        string_list = []
        user_posts_amount = self.posts_and_users.groupby('user_name')
        for user_name, count in user_posts_amount:
            string_list.append(f"{user_name} napisał(a) {len(count)} postów")
        return string_list

    def find_nonunique_titles(self):
        titles_number = self.posts['title'].value_counts()
        nonunique_titles = [title for title, amount in titles_number.items() if amount > 1]
        return nonunique_titles

    def find_neighbours(self):
        neighbours = []
        for index, user in users.iterrows():
            nn_dist = (180 ** 2 + 360 ** 2) ** (1 / 2)
            for n_index, n_user in users.iterrows():
                dist = calc_dist(user, n_user)
                if (dist < nn_dist) and (dist > 0):
                    nn_dist = dist
                    nn_user = n_user
            neighbours.append((user['name'], nn_user['name']))
        return neighbours

def calc_dist(user, n_user):
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    n_lat = float(n_user['address']['geo']['lat'])
    n_lng = float(n_user['address']['geo']['lng'])
    return ((lat - n_lat) ** 2 + (lng - n_lng) ** 2) ** (1 / 2)


def merge_post_and_users(posts, users):
    users_to_join = users.set_index('id').add_prefix('user_')
    posts_and_users = posts.join(users_to_join, on=['userId'])
    return posts_and_users


def download_data(url):
    response = requests.get(url)
    return pd.read_json(response.text)


if __name__ == "__main__":
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    posts = download_data(posts_url)
    users = download_data(users_url)

    analysator = PostsUsersAnalysator(posts, users)
