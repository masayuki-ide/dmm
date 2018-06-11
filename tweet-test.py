import tweepy

#認証を行う
consumer_key = "TrWhvaA3Wtq9iZolfF7GOqCvr"
consumer_secret = "wxxxVs58dA04dY8x7Q9cIhfeEPHf7xMNgO9x7AfiSugk5omess"
access_token = "911220352046395392-2kqMRJfS1kjKUM35HyvaGNvVAiqdytO"
access_secret = "RyIZwMTjqZE4NxRcNETL34TyTwcqoJb96f9pUM46WcadT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# api.update_status("Hello World!!!")
q = "安室奈美恵"
count =10
search_result = api.search(q=q, count=count)

for result in search_result:
    username = result.user.json('screen_name')


print(username)
