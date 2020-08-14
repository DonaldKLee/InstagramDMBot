# InstagramDMBot

Coming soon...

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
myemail = "example@gmail.com"             # Enter in your email, phone number, or username for Instagram inside the quotation marks
mypassword = "myInstagramPassword123"     # Enter in your password for Instagram inside the quotation marks
friendusername = "@myfriend"              # Enter in the username of the recipient inside the quotation marks
numoftimes = "1"                          # Enter in the number of times you would like to send the message to the recipient Ex) 1

# The message being sent
message = "Hello, World!"
```

# How it works?

# Tools
## Libraries/Modules used:
**time** - A module that allowed us to add delays into the code. </br>
**Selenium** - A module used to automate web browsers.

# Important 
Please do NOT use this for spam, bullying, etc. 

</br> By using this script, YOU will take FULL responsibility for anything that happens to ANYONE you use this on and anything you do with this script!. 

</br> Additionally, using this script may involve a risk of you being banned and even other risks including but not limited to: being hacked, etc. Use this script at your own risk!
