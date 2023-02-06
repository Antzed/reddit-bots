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

helplink = '''
General student service:\n
- https://www.washington.edu/students/servicesforstudents/

Courses/Professor info:\n
- https://uwgrades.com/

- https://www.washington.edu/cec/toc.html

- https://www.google.com/search?q=rate+my+professor+uw+%5Binsert+professor+name%5D&sxsrf=AJOqlzVwUt9A0OY5_KgZb7bdeYc_lw_RKg%3A1675667778386&ei=QqngY5GbF_aE0PEP8t2piAo&ved=0ahUKEwiRxMT1rID9AhV2AjQIHfJuCqEQ4dUDCBA&uact=5&oq=rate+my+professor+uw+%5Binsert+professor+name%5D&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABMgUIIRCrAjoICAAQogQQsAM6BAgjECc6BQgAEIAESgQIQRgBSgQIRhgAUNgGWJYaYLgkaAFwAHgAgAFQiAHVCpIBAjIymAEAoAEByAEFwAEB&sclient=gws-wiz-serp

UW student housing info:\n
- https://www.housingforhuskies.com/

UW on-campus food info:\n
- https://www.campusreel.org/colleges/university-of-washington-seattle-campus/dining_food/

UW on-campus job info:\n
- https://www.washington.edu/workstudy/find-a-job/
'''

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        # Read the file into a list and remove any empty values
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

        # Get the top 5 values from the subreddit pythonforengineers
        subreddit = reddit.subreddit('udub')
        for submission in subreddit.new(limit=50):
            if submission.id not in posts_replied_to:
                if re.search("\?", submission.title, re.IGNORECASE):
                    submission.reply("Hi! I am a bot! Your post is asking a question, so here are some usefuly links if you haven't found them yet!\n" + helplink)
                    print("Bot replying to : ", submission.title)
                    posts_replied_to.append(submission.id)
                else:
                    print("Nothing found")

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "w") as f:
            for post_id in posts_replied_to:
                f.write(post_id + "\n")