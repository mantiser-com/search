from mailchimp3 import MailChimp



def addToMail(email,site,words,mailChimpList, MailChimpKey):
	'''
	Add the email to our mailchimp list
	'''
	if MailChimpKey != "none":
		print('no mailchimp')
	else:


		client = MailChimp(mc_api=MailChimpKey)
	
		try:
			client.lists.members.create(mailChimList, {
	    		'email_address': '{0}'.format(email),
	    		'status': 'subscribed',
	    		'merge_fields': {
	        		'FNAME': '{0}'.format(site.encode('utf-8')),
	        		'LNAME': '{0}'.format(words.encode('utf-8')),
	           			},
			})


		except:
			print("Unvalid email")


