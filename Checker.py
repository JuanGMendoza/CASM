#from googlesearch import search_news, get_page

#import re

#import articleDateExtractor

#import urllib.request





class Article:



	def __init__(self):

		self.title = ''

		self.date = ''

		self.url = ''



def get_news(input, quantity=10):



	articles = []

	



	# for url in search_news(input, tld="co.in", num=10, stop=quantity, pause=2): 

	# 	print(url)

	# 	temp_article = Article()

	# 	date = '0-0-0'

	# 	content = str(get_page(url))

	# 	title = re.search('<title>(.+?)</title>', content)

	# 	print(content)

	# 	if title:

	# 		#print(title)

	# 		#date_time = articleDateExtractor.extractArticlePublishedDate(url) #This is not working

	# 		if True:

	# 			temp_article.title = title

	# 			temp_article.date = date

	# 			articles.append(temp_article)



	# 		else:

	# 			pass



	# 	else:

	# 		print("ERROR: No title found on website " + url)

	fake_article = Article()
	fake_article2 = Article()

	

	fake_article.title = 'Heat Pipes Market: Industry Latest Trends & Global Outlook 2016-2024'
	fake_article.url = 'http://zmrindustryanalysis.com/7971/heat-pipes-market-industry-latest-trends-global-outlook-2016-2024/'
	
	articles.append(fake_article)
	fake_article2.title = "google"
	fake_article2.url = 'http://google.com'
	articles.append(fake_article2)
	
	return articles



def search_supplier(supplier):

	supplier.articles = get_news(supplier.name)
