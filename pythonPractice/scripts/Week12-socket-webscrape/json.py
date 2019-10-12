import urllib.request
import json
url = 'https://data.cityofchicago.org/resource/tt4n-kn4t.json'
#url='http://maps.googleapis.com/maps/api/geocode/json?address=google'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()

print(r)
