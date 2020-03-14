import pandas as pd
import requests


def download_data(url):
    response = requests.get(url)
    return pd.read_json(response.text)


if __name__ == "__main__":
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    posts = download_data(posts_url)
    users = download_data(users_url)
