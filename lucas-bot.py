import praw
import pdb
import re
import os
import random

# Create the Reddit instance

reddit = praw.Reddit(
    client_id="id",
    client_secret="secret",
    password="password",
    username="username",
    user_agent="user_agent"
)

lucas_quotes = \
[
" I've calculated your chance of survival, but I don't think you'll like it. ",
" Do you want me to sit in a corner and rust or just fall apart where I'm standing?",
"Here I am, brain the size of a planet, and they tell me to take you up to the bridge. Call that job satisfaction? Cause I don't. ",
"Here I am, brain the size of a planet, and they ask me to pick up a piece of paper. ",
" It gives me a headache just trying to think down to your level. ",
" You think you've got problems. What are you supposed to do if you are a manically depressed robot? No, don't even bother answering. I'm 50,000 times more intelligent than you and even I don't know the answer.",
"Zaphod Beeblebrox: There's a whole new life stretching out in front of you. Marvin: Oh, not another one.",
"The first ten million years were the worst. And the second ten million... they were the worst too. The third ten million I didn't enjoy at all. After that, I went into a bit of a decline. ",
"Sorry, did I say something wrong? Pardon me for breathing which I never do anyway so I don't know why I bother to say it oh God I'm so depressed. ",
" I have a million ideas, but, they all point to certain death. ",
]

subreddit = reddit.subreddit('pythonforengineers')
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("comment_replied.txt", "r") as f:
            # Read the file into a list and remove any empty values
            comment_replied = f.read()
            comment_replied = comment_replied.split("\n")
            comment_replied = list(filter(None, comment_replied))

    for comment in subreddit.comments(limit=100):
        if comment.id not in comment_replied:
            if re.search("Lucas Help", comment.body, re.IGNORECASE):
                lucas_reply = "Lucas the robot says: " + random.choice(lucas_quotes)
                comment.reply(lucas_reply)
                comment_replied.append(comment.id)
            else:
                print("Nothing found")

# Write our updated list back to the file
with open("comment_replied.txt", "w") as f:
    for post_id in  comment_replied:
        f.write(post_id + "\n")