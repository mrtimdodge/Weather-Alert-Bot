# -*- coding: utf-8 -*-
"""
Created on Thurs Mar 31

@author: DapperDodger
"""

app_id = '6WMrw9ei1Q1ADQ'
app_secret = 'd5mViGqu0XzMtaQA8NnRVg7wFoo'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'Weather-Alert-Bot is a Reddit bot intended to be used for location specific subreddits to provide weather alerts.'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = '98nuXNOoTIxCpqaKIAR_9Tzvgk8'
app_refresh = '55060806-SmwaaEUE0BCmodM3NWYqp_uz5z8'

import praw
def login():
    r = praw.Reddit(user_agent=app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r

# -*- coding: utf-8 -*-

