from posts_users_analyse import PostsUsersAnalyser
from download_data import download_data

if __name__ == "__main__":
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    posts = download_data(posts_url)
    users = download_data(users_url)

    analysator = PostsUsersAnalyser(posts, users)

    posts_number = analysator.create_post_number_list()
    nonunique_titles = analysator.find_nonunique_titles()
    neighbours = analysator.find_neighbours()
