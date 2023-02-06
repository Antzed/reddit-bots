import praw
import pdb
import re
import os

# Create the Reddit instance

reddit = praw.Reddit(
    client_id="id",
    client_secret="secret",
    password="password",
    username="username",
    user_agent="user_agent"
)


if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        # Read the file into a list and remove any empty values
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

        # Get the top 5 values from the subreddit pythonforengineers
        subreddit = reddit.subreddit('pythonforengineers')
        for submission in subreddit.new(limit=20):
            if submission.id not in posts_replied_to:
                if re.search("i love python", submission.title, re.IGNORECASE):
                    submission.reply("me bot says: I love Python too! I especially love praw")
                    print("Bot replying to : ", submission.title)
                    posts_replied_to.append(submission.id)
                elif re.search('python', submission.selftext, re.IGNORECASE):
                    submission.reply("you mentioned python, python very good!")
                    print("Bot replying to : ", submission.title)
                    posts_replied_to.append(submission.id)
                else:
                    print("Nothing found")

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")