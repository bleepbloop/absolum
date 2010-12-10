import urllib
import urllib2
import simplejson

KEY = \
"AIzaSyBVRDTHiG1gdyVrELfwrNmQgfvRcHxXfJc&cx=017576662512468239146:omuauf_lfve"

class CustomSearch(object):
    def __init__(self):
        self.key = KEY
        self.query = urllib.urlencode({'q' : 'damon cortesi'})
        self.url = 'https://googleapis.com/customsearch/v1?key=' + self.key + '&%s' % (self.query)

    def get_results(self):
        search_results = urllib2.urlopen(self.url)
        print search_results
        json = simplejson.loads(search_results.read())
        results = json['responseData']['results']
        for i in results:
            print i['title'] + ": " + i['url']
            
if __name__ == "__main__":
    cs = CustomSearch()
    cs.get_results()
