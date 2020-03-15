import pandas as pd
import requests


def download_data(url):
    response = requests.get(url)
    return pd.read_json(response.text)


def calc_dist(user, n_user):
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    n_lat = float(n_user['address']['geo']['lat'])
    n_lng = float(n_user['address']['geo']['lng'])
    return ((lat - n_lat) ** 2 + (lng - n_lng) ** 2) ** (1 / 2)
