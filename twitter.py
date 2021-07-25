#!/usr/bin/python3
# -*- coding:utf-8 -*-
import tweepy
from config import *


def tweet(content):
    #tweet_content = "beep boop. this is a test. please ignore. have a nice day you're awesome <3"

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(token_key, token_secret)
    api = tweepy.API(auth)

    tweet = content
    print(tweet)

    api.update_status(tweet)

