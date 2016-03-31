# -*- coding: utf-8 -*-
"""
Created on Mon Mar  14

@author: DapperDodger
"""
import praw
import weatheralerts
import obot_weather as obot
import time
alert_SAMECode = ""
alert_state = "AR"
post_id = ""
subreddit = "DapperDodger"
app_ua = 'Weather-Alert-Bot is a Reddit bot intended to be used for location specific subreddits to provide weather alerts.'
current_day = time.localtime(time.time())[2]
r = obot.login()

    
if __name__=="__main__":
    while True:
        nws = weatheralerts.WeatherAlerts(state=alert_state)
        if post_id and post_id != "":
            submiss = r.get_submission(submission_id=post_id)
        for alert in nws.alerts:
            if alert.severity == 'Severe'and "Severe Weather Statement" not in alert.title:
                text =  alert.title + "\n\n Counties Affected: " + alert.areadesc
                if post_id and post_id != "" and current_day == time.localtime(time.time())[2]:
                    submiss = r.get_submission(submission_id=post_id)
                    submiss.refresh()
                    if alert.title not in submiss.selftext:
                        submiss.edit(submiss.selftext + "\n\n" + text + "\n\n" + "------------------------------------------------------")
                else:
                    post_id = r.submit(subreddit,"Severe Weather Alert",text + "\n\n" + "------------------------------------------------------").id
                    
        time.sleep(900)
    print "done"