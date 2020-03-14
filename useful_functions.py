import pandas as pd
import requests


def download_data(url):
    response = requests.get(url)
    return pd.read_json(response.text)
