import urllib
import urllib2
import simplejson

KEY = "AIzaSyBVRDTHiG1gdyVrELfwrNmQgfvRcHxXfJc&cx=017576662512468239146:omuauf_lfve"

query = urllib.urlencode({'q' : 'damon cortesi'})
url = 'https://googleapis.com/customsearch/v1?key=' + KEY + '&%s' \
  % (query)
search_results = urllib2.urlopen(url)
json = simplejson.loads(search_results.read())
results = json['responseData']['results']
for i in results:
  print i['title'] + ": " + i['url']
