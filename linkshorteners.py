# pip install pyshorteners
# MUST INSTALL THIS LIBRARY TO USE THIS CODE.


import pyshorteners

# create an instance of the Shortener class
shortener = pyshorteners.Shortener()

# get the short URL for a long URL
long_url = 'https://converterio.pythonanywhere.com/'
short_url = shortener.tinyurl.short(long_url)

# print the short URL
print(short_url)
