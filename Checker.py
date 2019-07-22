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


def get_news(supplier, quantity):
	"""
	Retrieves news about the provided supplier by looking at the Google News RSS feed.

	Parameters:
	supplier (Supplier): a Supplier class object to search the news for (TODO: change to this, right now string)
    quantity (int): the number of news articles to return

	Returns:
	list (Article): list of the first 'quantity' number of results
	"""
	if quantity > 100 or quantity <= 0:
		raise Exception(
			"Quantity should not be greater than 100 or less than or equal to 0. The value of quantity was {}."
			.format(quantity))

	articles = []

	news_url = "https://news.google.com/rss/search?q={}".format(supplier)

	news_url = news_url.replace(' ', '%20')

	client = urlopen(news_url)
	xml_page = client.read()
	client.close()

	soup_page = soup(xml_page, "xml")
	news_list = soup_page.findAll("item")

	# Print news title, url and publish date
	for count in range(0, quantity):
		news = news_list[count]
		articles.append(Article(news.title.text, news.pubDate.text, news.link.text))

	return articles


def search_supplier(supplier, quantity=10):
	articles = get_news(supplier, quantity)

	for article in articles:
		print(article)

	return articles


if __name__ == '__main__':
	search_supplier("Advanced Micro Devices")
