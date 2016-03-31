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
post_id = ""
subreddit = "DapperDodger"
app_ua = 'Weather-Alert-Bot is a Reddit bot intended to be used for location specific subreddits to provide weather alerts.'

r = obot.login()

    
if __name__=="__main__":
    nws = weatheralerts.WeatherAlerts(state=alert_state)
    for alert in nws.alerts:
        if alert.severity == 'Severe'and "Severe Weather Statement" not in alert.title:
            text =  alert.title + "\n\n Counties Affected: " + alert.areadesc
            if post_id and post_id != "":
                submiss = r.get_submission(submission_id=post_id)
                submiss.refresh()
                print submiss.selftext
                submiss.edit(submiss.selftext + "\n\n" + text + "\n\n" + "------------------------------------------------------")
            else:
                post_id = r.submit(subreddit,"Severe Weather Alert",text + "\n\n" + "------------------------------------------------------").id

        
    print "done"