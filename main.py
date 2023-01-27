import tweepy
from keys import consumer_key,consumer_secret,access_token,access_token_secret
from mysql_connector import train_model,insert_data
from pandas_market_calendars import get_calendar
from datetime import datetime

def post_tweet():
    #set up tweets
    auth = tweepy.OAuth1UserHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    api = tweepy.API(auth)

    #check for business date
    nyse = get_calendar('NYSE')
    now = datetime.now()
    schedule = nyse.valid_days(start_date=now, end_date=now)

    #update the database with new data, default set to 1 previous day.
    insert_data(get_data)

    if schedule.empty:
        api.update_status(f'There is no SPY movement today on {str(datetime.today())[:11]}')
    else:
        api.update_status(f"the SPY stock today will go {train_model()}")
