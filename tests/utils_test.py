import unittest
import utils
import pandas as pd


class TestUtils(unittest.TestCase):

    def test_download_data(self):
        url = 'https://jsonplaceholder.typicode.com/posts'
        test_data_as_pd = pd.read_json('test_data/test_posts_download.json')
        test_data_downloaded = utils.download_data(url)
        self.assertTrue(test_data_as_pd.equals(test_data_downloaded))

    def test_calc_dist(self):
        test_users_neighbours = pd.read_json('test_data/test_users_neighbours.json')
        self.assertEqual(utils.calc_dist(test_users_neighbours.iloc[0], test_users_neighbours.iloc[1]), 5)


if __name__ == '__main__':
    unittest.main()
