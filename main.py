from posts_users_analyse import PostsUsersAnalyser
from utils import download_data

if __name__ == "__main__":
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    posts = download_data(posts_url)
    users = download_data(users_url)

    analysator = PostsUsersAnalyser()

    posts_number = analysator.create_post_number_list(posts, users)
    nonunique_titles = analysator.find_nonunique_titles(posts)
    neighbours = analysator.find_neighbours(users)
