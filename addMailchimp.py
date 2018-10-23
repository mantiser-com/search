from mailchimp3 import MailChimp



def addToMail(email,site,words):
	'''
	Add the email to our mailchimp list
	'''
	client = MailChimp(mc_api='')
	
	try:
		client.lists.members.create('f1f0d85505', {
	    		'email_address': '{0}'.format(email),
	    		'status': 'subscribed',
	    		'merge_fields': {
	        		'FNAME': '{0}'.format(site.encode('utf-8')),
	        		'LNAME': '{0}'.format(words.encode('utf-8')),
	           			},
			})


	except:
		print("Unvalid email")


