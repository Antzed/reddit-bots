import praw


reddit = praw.Reddit(
    client_id="id",
    client_secret="secret",
    password="password",
    username="username",
    user_agent="user_agent"
)
subreddit = reddit.subreddit("learnpython")
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

