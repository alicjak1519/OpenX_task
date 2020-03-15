from posts_users_analyse import PostsUsersAnalyser
from utils import download_data

if __name__ == "__main__":
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    posts = download_data(posts_url)
    users = download_data(users_url)

    analyser = PostsUsersAnalyser()

    posts_number = analyser.create_post_number_list(posts, users)
    nonunique_titles = analyser.find_nonunique_titles(posts)
    neighbours = analyser.find_neighbours(users)
