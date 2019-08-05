CASM (Centralized Applicaiton for Supplier Monitoring)

CASM is a supplier monitoring tool created for Cisco's Supply Chain Case Competition. 

The description of the problem we were given for this competition is:
"
The Global Supplier Management (GSM) organization in Supply Chain 
is looking for a user-friendly and hands-off approach to proactively 
monitor supplier events/trends/news/updates. A solution is needed 
that will allow commodity managers to seamlessly keep up with the 
ins and outs of what's going on With thetr suppliers to help sense 
fluctuations in their businesses that may Impact Cisco in a meaningful way. 

The Project: This project will entail creating a solution that incorporates 
the latest news and events around a customizable set of suppliers that collates 
all relevant Information needed for comprehensive supplier management and alerts 
commodity managers if something Impactful may be happening "

We were only asked for a proof of concept, still we provided an almost fully functioning
tool.

We were only given a month and everything was coded by myself except lines 23-62 on Checker.py.
So I apologize for not following coding guidelines as I did not have much time.

This program consists of three features:

1. Adding Suppliers to dashboard:
	
	By clicking the add icon one may enter the name of a supplier to add to the dashboard
	or select browse and input a text file with a list of suppliers. After hitting ok CASM
	will look for top 3 news articles in google news regarding said suppliers, and also look
	for the supplier in the internal database explained in feature 3. These have
	a hyperlink attached so if clicked they open in an internet browser.

2. Customizable Alerts
	
	By clicking the gear icon, two lists of words will show up. When a high warning word is
	found in one of the supplier's articles, it will send an email to the address provided in
	the login screen, and display a red warning icon next to the article on the dashboard.
	The medium warning words will display a yellow warning icon on the dashboard.
	If the mouse pointer is placed over the warning icon, a message will show up showing
	which words were found in the article.
	Options for notifications are not functional, only supported option is email. They were
	placed for presentation purposes.

3. Local Article Database

	By clicking the third icon, a window will pop up where one is able to write an article
	about any supplier. These articles will show up under the google news articles in the dashboard.
	In theory, these articles should be stored in a server where all CASM instances would connect to,
	but currently it just stores it in a local text file.

4. Refresh
	
	The arrow icon searches all suppliers located in the dashboard again, through both google news
	and the internal database.

Any questions please email me at JuanGMendoza@utexas.edu