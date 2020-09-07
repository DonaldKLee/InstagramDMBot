# InstagramDMBot

A bot that can send messages for you to Instagram users. Ever wanted to send hundreds of the same text message to a friend or several friends efficiently? Well, now you can!  <-- Please make sure that they are ok with this first! Anything you do with this script is on you!

Note: This was a fun project for experimental and learning purposes. 
</br> Please do not use this for malicious behaviour, because YOU will be responsible! 

# Installation and Instructions
1. Download the code from this repository

2. install the following module
```
pip install selenium
```

3. Find the version of your Chrome browser in "Settings" --> "About Chrome". 

</br>Then [install a Webdriver for Chrome that supports your browser's version](https://sites.google.com/a/chromium.org/chromedriver/downloads)

4. Once your web driver has been installed, put it somewhere on your computer and copy and paste it's path (The path should start with C:\\, E:\\, etc.) onto line 31.

</br> Example:
```
PATH = "C:\Program Files (x86)\chromedriver.exe"  # Step 4 of the installations instructions 
```

### If you are stuck on step 3 or 4, watch this short [tutorial!](https://www.youtube.com/watch?v=Xjv1sY630Uc&feature=youtu.be&t=260)

5. Enter in your Instagram email, password, the recipient's username, the number of times you would like the message to send, and the message.

</br> This starts on line 23:
```
myemail = "myemail@gmail.com"                                # Enter in your email for Instagram inside the quotation marks
mypassword = "myInstagramPassword123"                        # Enter in your password for Instagram inside the quotation marks
friendusernames = ["@friend1", "@friend2", "@friend3"]       # Enter in the username of the recipient inside the quotation marks! To send this to mutiple users, seperate users by commas! Ex)  friendusernames = ["@friend1", "@friend2", "@friend3"]
numoftimes = "1"                                             # Enter in the number of times you would like to send the message to the recipient Ex) "2"

# The message being sent
message = "Hello, World!"
```

# How it works?
1. This script first opens up "https://www.instagram.com/". </br>
2. Logs in for you by automatically pasting in the login credentials that you filled in on "Step 5" of the "Installation and Instructions" process. </br>
3. Once logged in, the bot will press the "Direct message" button on Instagram. </br>
4. It will then click on the "New message" button and paste in the first username in the "friendusernames" list.  </br>
5. The bot will then click on "Next". </br>
6. Paste in the text in the "message" variable. </br>
7. Finally, the bot will virtually hit the ENTER/RETURN key on your computer and send the message!  </br>
8. If you have multiple recipients, the bot will repeat step 4 and onwards! 

## Libraries/Modules used:
**time** - A module that allowed us to add delays into the code. </br>
**Selenium** - A module used to automate web browsers.

# Terms of Service 
Please do **NOT** use this for spam, bullying, etc. 

</br> By using this script, YOU will take FULL responsibility for anything that happens to ANYONE you use this on and anything you do with this script!. 

</br> Additionally, using this script may involve a risk of you being banned and even other risks including but not limited to: being hacked, etc. Use this script at your own risk!

</br> These terms may be changed without notice.
