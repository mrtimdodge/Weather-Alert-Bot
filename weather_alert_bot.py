# -*- coding: utf-8 -*-
"""
Created on Mon Mar  14

@author: DapperDodger
"""
import praw
import weatheralerts
import obot_weather as obot
alert_SAMECode = ""
alert_state = "AR"
alert_county = ""
subreddit = "DapperDodger"
app_ua = 'Weather-Alert-Bot is a Reddit bot intended to be used for location specific subreddits to provide weather alerts.'

r = obot.login()

    
if __name__=="__main__":
    nws = weatheralerts.WeatherAlerts(state=alert_state)
    for alert in nws.alerts:
        if alert.severity == 'Severe':
            text =  alert.title + " " + alert.areadesc
            r.submit(subreddit,"Severe Weather Alert",text)
        
    print "done"