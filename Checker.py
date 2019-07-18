from googlesearch import search_news, get_page
import re
import articleDateExtractor
import urllib.request

class Article:

	def __init__(self):
		self.title = ''
		self.date = ''
		self.url = ''


	def __str__(self):
		return "Title: {}, Date: {}".format(self.title, self.date)

	def __repr__(self):
		return "Title: {}, Date: {}".format(self.title, self.date)

def get_news(input, quantity=10):
	articles = []

	for url in search_news(input, tld="co.in", num=10, stop=quantity, pause=2): 
		print(url)
		temp_article = Article()
		date = '0-0-0'
		content = str(get_page(url))
		title = re.search('<title>(.+?)</title>', content)

		if title:
			date_time = articleDateExtractor.extractArticlePublishedDate(url)
			if date_time:
				temp_article.title = title
				temp_article.date = date_time.date()
				articles.append(temp_article)

			else:
				pass

		else:
			print("ERROR: No title found on website " + url)

	print("\n\n\n")

	for article in articles:
		print(article)
		print("\n")

	# fake_article = Article()
	# fake_article.date = '0-0-0'
	# fake_article.title = 'test article'
	# articles.append(fake_article)
	# return articles

	return articles


def search_supplier(supplier):

	supplier.articles = get_news(supplier.name)

#if __name__ == '__main__':
#	get_news('Foxconn', 10)
