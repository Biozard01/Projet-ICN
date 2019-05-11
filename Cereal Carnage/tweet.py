import tweepy

consumer_key = ""
consumer_secret = ""

access_token = "" 
access_token_secret = "" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

TWITTER_ACC = 'Cereal_Carnage'

BACKGROUND1 = "images/floor.png"
BACKGROUND2 = "images/dirt.png"
BACKGROUND3 = "images/snow.png"
BACKGROUND_CHOICE = "images/floortorch.png"

PLAYER_SKIN = "images/player.png"
ENNEMY0_SKIN = "images/eyeball.png"
ENNEMY1_SKIN = "images/turtle.png"
ENNEMY2_SKIN = "images/slime.png"
ENNEMY0_SKIN_CHOICE = "images/slime.png"

nbtweets = api.get_user(TWITTER_ACC).statuses_count
tweet = int(str(nbtweets)[:1])

if tweet <= 4:
    BACKGROUND_CHOICE = BACKGROUND1
    ENNEMY0_SKIN_CHOICE = ENNEMY0_SKIN
    
if tweet == 5:
    BACKGROUND_CHOICE = BACKGROUND2
    ENNEMY0_SKIN_CHOICE = ENNEMY1_SKIN

if tweet >= 6:
    BACKGROUND_CHOICE = BACKGROUND3
    ENNEMY0_SKIN_CHOICE = ENNEMY2_SKIN
