import unittest
import pandas as pd
from posts_users_analyse import PostsUsersAnalyser

test_analyser = PostsUsersAnalyser()


class TestPostsUsersAnalyser(unittest.TestCase):

    def test_create_posts_number_list(self):
        test_posts = pd.read_json('test_posts_posts_number.json')
        test_users = pd.read_json('test_users_posts_number.json')
        posts_number_list = test_analyser.create_post_number_list(test_posts, test_users)
        self.assertEqual(posts_number_list, ['Chelsey Dietrich napisał(a) 10 postów',
                                             'Clementina DuBuque napisał(a) 0 postów',
                                             'Clementine Bauch napisał(a) 10 postów',
                                             'Ervin Howell napisał(a) 10 postów',
                                             'Glenna Reichert napisał(a) 0 postów',
                                             'Kurtis Weissnat napisał(a) 0 postów',
                                             'Leanne Graham napisał(a) 10 postów',
                                             'Mrs. Dennis Schulist napisał(a) 0 postów',
                                             'Nicholas Runolfsdottir V napisał(a) 0 postów',
                                             'Patricia Lebsack napisał(a) 10 postów'])

    def test_find_nonunique_titles(self):
        test_posts_nonunique_title = pd.read_json('test_posts_nonunique_title.json')
        titles = test_analyser.find_nonunique_titles(test_posts_nonunique_title)
        self.assertEqual(titles, ["qui est esse"])

    def test_find_neighbours(self):
        test_users_neighbours = pd.read_json('test_users_neighbours.json')
        neighbours = test_analyser.find_neighbours(test_users_neighbours)
        self.assertEqual(neighbours, [('Leanne Graham', 'Ervin Howell'),
                                      ('Ervin Howell', 'Leanne Graham'),
                                      ('Clementine Bauch', 'Ervin Howell')])
    #
    # def test_maximal_geo_dist(self):
    #     test_analyser = PostsUsersAnalyser(test_posts, test_users)
    #     self.assertEqual(test_analyser._maximal_geo_dist(), (180 ** 2 + 360 ** 2) ** (1 / 2))
    #
    # def test_calc_dist(self):
    #     test_users_neighbours = pd.read_json('test_users_neighbours.json')
    #     test_analyser = PostsUsersAnalyser(test_posts, test_users_neighbours)
    #     self.assertEqual(test_analyser._calc_dist(test_users_neighbours.iloc[0], test_users_neighbours.iloc[1]), 5)


class TestUtils(unittest.TestCase):

    def test_maximal_geo_dist(self):
        self.assertEqual(utils.maximal_geo_dist(), (180 ** 2 + 360 ** 2) ** (1 / 2))


if __name__ == '__main__':
    unittest.main()
