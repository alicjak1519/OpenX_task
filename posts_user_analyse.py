import pandas as pd
import requests


class PostsUsersAnalysator():

    def __init__(self, posts=None, users=None):
        self.posts = posts
        self.users = users

def download_data(url):
    response = requests.get(url)
    return pd.read_json(response.text)


if __name__ == "__main__":
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    posts = download_data(posts_url)
    users = download_data(users_url)

    analysator = PostsUsersAnalysator(posts, users)
