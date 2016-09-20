import urllib.request
import json

# url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'

token = 'EAACEdEose0cBAMZBFccbMIEUhkL62eyJBiKX3tigjV13xHFlzSVq0YseXz2hjxTFwO6N8ACqO95rsQZBAfZBZCFOAgkNZBWJdVAZCii6ZBekLz2VW9nO2z03im8Cj4qWvHJ5ydNV8a7kI2LhLu9qLyzDoKWD7YWnYFNZBrSZAe64kTwZDZD'
url = 'https://graph.facebook.com/v2.3/me/groups?fields=id&access_token=' + token

resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

for id in data['data']:
    print(id['id'])
