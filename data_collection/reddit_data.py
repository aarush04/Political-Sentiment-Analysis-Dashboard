#List of keywords
keywords =['Trump', 'Biden', 'Immigration', 'Unemployment', 'Democrat', 'Republican', 'Palestine', 'Israel']

#Reddit
import praw

client_id='ZxfoaYTfnB199pY_HjNZdg'
client_secret='yCv8xueSuWnauYa7yfuJYnPavaXUdA'
user_agent='Careless-Shirt753'
password='TheGuj123'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    password=password,
    username=user_agent
)

reddit_data={}
#subreddits=reddit.subreddit("news+worldnews+politics+PoliticalDiscussions+AmericanPolitics+uspolitics+worldevents")
subreddits=["news","worldnews","politics","PoliticalDiscussions","AmericanPolitics","uspolitics","worldevents"]
for keyword in keywords:
    titles=[]
    selftexts=[]
    comments=[]
    #posts
    for sub in subreddits:
        submissions = reddit.subreddit(sub).search(keyword, sort='top', limit=3,time_filter='week')
        print(sub)
        for submission in submissions:
            titles.append(submission.title)
            selftexts.append(submission.selftext)
            print(submission.title)
            #Comments
            submission.comments.replace_more(limit=10)
            for comment in submission.comments:
                print(comment.body)
                if keyword.lower() in comment.body.lower():
                    comments.append(comment.body)
    reddit_data[keyword]=[titles,selftexts,comments]

#How to access data dictionary:
##print(data['OpenAI'][0] yields titles, [1] yields selftext, [2] yields comments)






