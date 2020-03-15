import unittest
import pandas as pd
from posts_users_analyse import PostsUsersAnalyser

test_posts = pd.read_json('test_posts.json')
test_users = pd.read_json('test_users.json')


class TestPostsUsersAnalysator(unittest.TestCase):

    def test_create_posts_number_list(self):
        test_analyser = PostsUsersAnalyser(test_posts, test_users)
        self.assertEqual(len(test_analyser.create_post_number_list()), len(test_users))

    def test_calc_posts_number(self):
        test_analyser = PostsUsersAnalyser(test_posts, test_users)
        self.assertEqual(sum([pair[1] for pair in test_analyser._calc_posts_number()]), len(test_posts))

    def test_merge_users_and_posts(self):
        test_analyser = PostsUsersAnalyser(test_posts, test_users)
        self.assertGreaterEqual(len(test_analyser._merge_users_and_posts()), len(test_posts))

    def test_len_find_nonunique_titles(self):
        test_posts_nonunique_title = pd.read_json('test_posts_nonunique_title.json')
        test_analyser = PostsUsersAnalyser(test_posts_nonunique_title, test_users)
        self.assertEqual(len(test_analyser.find_nonunique_titles()), 1)

    def test_value_find_nonunique_titles(self):
        test_posts_nonunique_title = pd.read_json('test_posts_nonunique_title.json')
        test_analyser = PostsUsersAnalyser(test_posts_nonunique_title, test_users)
        self.assertEqual(test_analyser.find_nonunique_titles(), ["qui est esse"])

    def test_len_find_neighbours(self):
        test_analyser = PostsUsersAnalyser(test_posts, test_users)
        self.assertEqual(len(test_analyser.find_neighbours()), len(test_users))

    def test_value_find_neighbours(self):
        test_users_neighbours = pd.read_json('test_users_neighbours.json')
        test_analyser = PostsUsersAnalyser(test_posts, test_users_neighbours)
        self.assertEqual(test_analyser.find_neighbours()[0],
                         (test_users_neighbours.iloc[0]['name'], test_users_neighbours.iloc[1]['name']))

    def test_maximal_geo_dist(self):
        test_analyser = PostsUsersAnalyser(test_posts, test_users)
        self.assertEqual(test_analyser._maximal_geo_dist(), (180 ** 2 + 360 ** 2) ** (1 / 2))

    def test_calc_dist(self):
        test_users_neighbours = pd.read_json('test_users_neighbours.json')
        test_analyser = PostsUsersAnalyser(test_posts, test_users_neighbours)
        self.assertEqual(test_analyser._calc_dist(test_users_neighbours.iloc[0], test_users_neighbours.iloc[1]), 5)


if __name__ == '__main__':
    unittest.main()
