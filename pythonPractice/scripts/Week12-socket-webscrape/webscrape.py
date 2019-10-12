import re
from urllib.request import Request, urlopen

#url = "https://finance.google.com/finance?q=NASDAQ:AAPL&output=json"
url = "https://www.google.com/finance/getprices?q=.NSEI&x=NSE&i=600&p=1d&f=d,o,h,l,c,v";
htmlfile = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
html = htmlfile.read()
text = html.decode()
#print(text)
# get rid of the headers
content = text.split("\n",8)[8]; #skip 8 lines - store rest into list

# get data into list
data = []

# go over each line
for line in content.split("\n"):
	# check if it is an empty line
	if line != "":
		# get rid of line number, put the rest into list,
		#then add it into data
		data.append(line.split(",")[1:])

# print the data
print(data)

# print the first line
print(data[0])

# print the last line
print(data[len(data)-1])
