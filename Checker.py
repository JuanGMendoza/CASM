from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

class Article:
	def __init__(self, title, date, url):
		self.title = title
		self.date = date
		self.url = url

	def __str__(self):
		return "Title: {}\nDate: {}\nURL: {}\n\n".format(self.title, self.date, self.url)

	def __repr__(self):
		return "Title: {}\nDate: {}\nURL: {}\n\n".format(self.title, self.date, self.url)

def get_news(input, quantity=10):
	articles = []

	news_url = "https://news.google.com/rss/search?q={}".format(input)

	client = urlopen(news_url)
	xml_page = client.read()
	client.close()

	soup_page = soup(xml_page, "xml")
	news_list = soup_page.findAll("item")

	# Print news title, url and publish date
	for news in news_list:
		articles.append(Article(news.title.text, news.pubDate.text, news.link.text))

	return articles


def search_supplier(supplier):
	articles = get_news(supplier)

	for article in articles:
		print(article)

	return articles


if __name__ == '__main__':
	search_supplier("Apple")
