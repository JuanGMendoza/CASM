import smtplib, ssl

def send_email(recipient, suppliers):
	port = 465  # For SSL
	password = 'Cisco123'
	message = "Subject: Urgent News about " + str(suppliers) + '!'


	# Create a secure SSL context
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	    server.login("ciscoCasm@gmail.com", password)
	    server.sendmail('ciscoCasm@gmail.com', 'ciscoCasm@gmail.com', message)
	    

