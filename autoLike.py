import tweepy
import traceback

CONSUMER_KEY = 'wlqpp2lv4wKRISFXuMxQh45i7'
CONSUMER_SECRET = 'qFDF0cIiIMvXzcrluqTI32oIk8Tr2xlyLBtP9i0cjriAl8AmnI'
ACCESS_TOKEN  = '911220352046395392-SyPkGbXJHCcqaYwI10lX1svjAfnIobQ'
ACCESS_SECRET = 'yZLqrvm5Y48aeqxILFIlzjR5XA5rHjlZPskLwzBgEWAGv'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

q = "紗倉まな"
count = 100
search_results = api.search(q=q, count=count)

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.user._json['id']
    tweet_id = result.id
    print(user_id)
    user = result.user.name
    print(user)
    tweet = result.text
    print(tweet)
    time = result.created_at
    print(time)
    try:
        api.create_favorite(tweet_id)
        print(user)
        print("をLikeしました")
        api.create_friendship(user_id)
        print("をFollowしました")
    except :
    #     # print '=== エラー内容 ==='
    #     # print 'type:' + str(type(e))
    #     # print 'args:' + str(e.args)
        # print("message:" + e.messages)
    #     # print 'e自身:' + str(e)
    #

        traceback.print_exc()
        print("もうすでにフォローしてます")
    print("######################")
