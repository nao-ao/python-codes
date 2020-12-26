import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# 先ほど取得した各種キーを代入する

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 普通のツイート
api.update_status("Tweet from python")

# 画像付きツイート
api.update_with_media(status = 'image tweet from python', filename = 'sample.png')

# リプライツイート
# まずリプライを返したいユーザーのID(@のID)を代入
Account = 'samplemoviebot1'

# user_timelineで指定したユーザーのタイムラインのTweetを取得(最大20個まで)
tweets = api.user_timeline(Account, count=20, page=1)

# その一つ一つに対してリプライをする．
msg = 'reply from python'
for tweet in tweets:
  reply_text = "@"+str(tweet.user.screen_name) +" "+ msg
  api.update_status(status = reply_text, in_reply_to_status_id = tweet.id)
  # api.update_with_media('img.jpg', status = reply_text, in_reply_to_status_id = tweet.id)

# 画像付きリプライツイート
# まずリプライを返したいユーザーのID(@のID)を代入
Account = 'samplemoviebot1'

# user_timelineで指定したユーザーのタイムラインのTweetを取得(最大20個まで)
tweets = api.user_timeline(Account, count=20, page=1)

# その一つ一つに対してリプライをする．
msg = 'reply img from python'
for tweet in tweets:
  reply_text = "@"+str(tweet.user.screen_name) +" "+ msg
  api.update_with_media('sample.png', status = reply_text, in_reply_to_status_id = tweet.id)
