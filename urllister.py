"""
URL Lister

"""
import urllib
from sgmllib import SGMLParser

class URLLister(SGMLParser):

    def reset(self):
        SGMLParser.reset()
        self.urls = []

    def start_a(self,attrs):
        # Attrs will be a list of tuples, [(attribute,value),(attribute,value),...]
        # 
        href = [v for k,v in attrs if k == 'href']
        if href:
            self.urls.extend(href)

usock = urllib.urlopen("http://diveintopython.org/") 
parser = URLLister(SGMLParser)
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls: print url


        
        
