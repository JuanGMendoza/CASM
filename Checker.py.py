# import urllib
# import urllib.request
# import json
# url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
# query = input("Query:")
# query = urllib.parse.urlencode( {'q' : query } )
# response = urllib.request.urlopen (url + query ).read()
# data = json.loads ( response.decode() )
# results = data [ 'responseData' ] [ 'results' ]
# for result in results:
#     title = result['title']
#     url = result['url']
#     print ( title + '; ' + url )
from GoogleNews import GoogleNews
class GoogleNews_python:
   def __init__(self,name_search):
      self.name = name_search
   def GoogleNews(self):
      count = 0
      try :
         googlenews = GoogleNews()
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=10,pause=2):
         count += 1
         print (count)
         print(i + '\n')
if __name__=='__main__':
  googlenews = GoogleNews()
  gs = googlenews.search('chaun choung financial news')
  print(googlenews.gettext())