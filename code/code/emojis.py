"""
Julia worked on this.
"""

import re

text = []
f=open('data.txt',"r")
for line in f:
	text.append(line)
# # with emoji

	emoji_pattern = re.compile("["
        	u"\U0001F600-\U0001F64F"  # emoticons
        	u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        	u"\U0001F680-\U0001F6FF"  # transport & map symbols
        	u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
	print(emoji_pattern.sub(r'', line)) # no emoji