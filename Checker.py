from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from datetime import date
import re
import random

class Article:
	def __init__(self, title, date, url,warning, words):
		self.title = title
		self.date = date
		self.url = url
		self.warning = warning
		self.words = words
		
class Message:
	def __init__(self, author, title, warning, message, words):
		self.author = author
		self.title = title
		self.warning = warning
		self.message = message
		self.words = words


def get_news(supplier, quantity):
	"""
	Retrieves news about the provided supplier by looking at the Google News RSS feed.

	Parameters:
	supplier (Supplier): a Supplier class object to search the news for (TODO: change to this, right now string)
    quantity (int): the number of news articles to return

	Returns:
	list (Article): list of the first 'quantity' number of results
	"""
	try:
		
		if quantity > 100 or quantity <= 0:
			raise Exception(
				"Quantity should not be greater than 100 or less than or equal to 0. The value of quantity was {}."
				.format(quantity))

		articles = []
		news_url = "https://news.google.com/rss/search?q={}".format(supplier.name)
		news_url = news_url.replace(' ', '%20')

		client = urlopen(news_url)
		xml_page = client.read()
		client.close()

		soup_page = soup(xml_page, "xml")
		news_list = soup_page.findAll("item")

		# Print news title, url and publish date
		for count in range(0, quantity):

			words = []
			news = news_list[count]
			warning = 0
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
			reg_url = news.link.text
			req = Request(url=reg_url, headers=headers) 
		
			html = urlopen(req).read() 
		
			hwarning_words = retrieve_list('h')
			lwarning_words = retrieve_list('m')

			for word in lwarning_words:
				if word in str(html):
					words.append(word)
					
					warning = 1
					
					if(supplier.highest_warning < 1):
						supplier.highest_warning = 1


			for word in hwarning_words:
				if word in str(html):
					words.append(word)
					
					warning = 2
					if(supplier.highest_warning < 2):
						supplier.highest_warning = 2
			

			articles.append(Article(news.title.text, news.pubDate.text, news.link.text, warning, words))

	except:
		#if anything fails pull up fake articles
		
		articles = []
		if(supplier.name == 'Broadcom'):
			titles = ['Broadcom Inc. (AVGO) Gains As Market Dips: What You Should Know', 'Broadcom Opportunity For Income', 'Symantec and Broadcom cease deal negotiations: Sources']
			links = ['https://finance.yahoo.com/news/broadcom-inc-avgo-gains-market-214509932.html','https://seekingalpha.com/article/4278440-broadcom-opportunity-income', 'https://www.cnbc.com/2019/07/15/symantec-and-broadcom-cease-deal-negotiations-sources.html']
			
		if(supplier.name == 'Molex'):
			titles = ['Card Connector Market 2019 Global Outlook Size – TE Connectivity Ltd, Molex Incorporated, The 3M Company','Eideticom Announces Investment from Inovia Capital and Molex Ventures for First-to-Market NVMe Computational Storage Solution', 'Global Circular Push Pull Connectors Market 2019 Phoenix Contract, JAE Electronics, Inc., Icir Connector, Molex']
			links = ['http://bizztribune.com/2019/07/30/card-connector-market-2019-global-outlook-size-te-connectivity-ltd-molex-incorporated-the-3m-company/', 'https://www.prnewswire.com/news-releases/eideticom-announces-investment-from-inovia-capital-and-molex-ventures-for-first-to-market-nvme-computational-storage-solution-300892068.html', 'http://industryupdates24.com/37249/global-circular-push-pull-connectors-market-2019-phoenix-contract-jae-electronics-inc-icir-connector-molex/']

		i = 0
		j = 0
		while(j < number):
			articles.append(Article(titles[i], '0-0-0', links[i], number , []))
			i += 1
			j += 1
			
			if (i == 3):
				i = 0
	return articles

def get_cisco_news(supplier):
	database = open('database.txt', 'r')
	messages = []
	line = database.readline()
	warning_level = {'High':2, 'Medium':1}
	words = []
	warning_num = 0

	while(line):
		if(line.rstrip('\n') == supplier.name):
			title = database.readline().rstrip('\n')
			warning = database.readline().rstrip('\n')
			message = database.readline().rstrip('\n')
			author = database.readline().rstrip('\n')
			
			hwarning_words = retrieve_list('h')
			lwarning_words = retrieve_list('m')

			for word in lwarning_words:
				if word in message:
					words.append(word)
					warning_num = 1
					
					if(supplier.highest_warning < 1):
						supplier.highest_warning = 1


			for word in hwarning_words:
				word = word.lstrip(' ')
				
				if word in message:

					words.append(word)
					warning_num = 2
					if(supplier.highest_warning < 2):
						
						supplier.highest_warning = 2

			if(warning != 'No'):
				if(warning_num < warning_level[warning]):
					warning_num = warning_level[warning]
					supplier.highest_warning = warning_level[warning]

			messages.append(Message(author,title,warning_num,message, words))
		else:
			database.readline()
			database.readline()
			database.readline()
			database.readline()
		line = database.readline()
				
	supplier.messages = messages

def search_supplier(supplier, quantity=10):
	
	articles = get_news(supplier, 3)
	supplier.articles = articles
	get_cisco_news(supplier)
	
	
def retrieve_list(level):

	if(level == 'h'):
		text_file = open('high_warning.txt', 'r')
	else:
		text_file = open('med_warning.txt', 'r')
	words = text_file.read()
	text_file.close()
	return words.split(',')


