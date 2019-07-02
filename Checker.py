from googlesearch import search_news, get_page
import re
import articleDateExtractor



class Article:

	def __init__(self):
		self.title = ''
		self.date = ''

def get_news(input, quantity=1):

	articles = []
	

	# for url in search_news(input, tld="co.in", num=10, stop=quantity, pause=2): 
	# 	print(url)
	# 	temp_article = Article()
	# 	date = '0-0-0'
	# 	content = str(get_page(url))
	# 	title = re.search('<title>(.+?)</title>', content)

	# 	if title:
	# 		date_time = articleDateExtractor.extractArticlePublishedDate(url) This is not working
	# 		if date_time:
	# 			temp_article.title = title
	# 			temp_article.date = date_time.date()
	# 			articles.append(temp_article)

	# 		else:
	# 			pass

	# 	else:
	# 		print("ERROR: No title found on website " + url)

	fake_article = Article()
	fake_article.date = '0-0-0'
	fake_article.title = 'test article'
	articles.append(fake_article)
	return articles

def search_supplier(supplier):
	supplier.articles = get_news(supplier.name)


