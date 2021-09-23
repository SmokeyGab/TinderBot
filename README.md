# TinderBot

A tinder bot that swipes right for you every time.

# Usage

1.Download tinder_bot.py file
2.Download Chromedriver
3.Place Chromedriver in same folder as tinder_bot.py
4.Run tinder_bot.py
6.A Chrome browser should open
5.Either run TinderBot.login() or visit tinder.com manually in chrome instance
6.Login with your account credentials on tinder.com
7.In tinder_bot.py prompt type TinderBot.autoswipe() to start swiping

# Issues

Xpath has variable Id. To change the Xpath go to the button you want to click for example the "like" button on the tinder page. 
Right click on the like button and press "Inspect". In the html window that pops up find the button element a little up from where you landed and right click it.
Hover over the copy option and from the dropdown menu select copy xpath. Now take the copied xpath and insert it into the tinder_bot.py file under the "like" function.
Do the same for every function that clicks a button and you should be ready to go!
