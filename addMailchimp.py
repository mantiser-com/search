from mailchimp3 import MailChimp
import random
import string

def testMailChimp(mailchimpkey,mailchimplist):
	'''
	Test if we have a working mailchimp connection
	'''
	
	
	client = MailChimp(mc_api=mailchimpkey)

	randomEmail = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
	print(randomEmail)
	mailChimpGood = addToMail('test-api-{0}@mantiser.com'.format(randomEmail),"https://mantiser.com","test",mailchimpkey,mailchimplist)

	if mailChimpGood != False:
		deleteFromMailchimp(mailChimpGood,mailchimpkey,mailchimplist)
		print("mailchimp good")
		return True
	else:
		return False



def deleteFromMailchimp(userhash,mailchimpkey,mailchimplist):
	'''
	Delet the user from the list
	'''
	client = MailChimp(mc_api=mailchimpkey)

	try:
		client.lists.members.delete(list_id=mailchimplist, subscriber_hash=userhash)
	except:
		print('got error from mailchimp')




def addToMail(email,site,words,mailchimpkey,mailchimplist):
	'''
	Add the email to our mailchimp list
	'''
	client = MailChimp(mc_api=mailchimpkey)
	backFromMailchimp=""
	
	backFromMailchimp = client.lists.members.create(mailchimplist, {
	    'email_address': '{0}'.format(email),
	    'status': 'subscribed',
	    'merge_fields': {
	        'FNAME': '{0}'.format(site),
	        'LNAME': '{0}'.format(words),
	           },
	})
	return backFromMailchimp['id']
	#except:
	#	print(backFromMailchimp)
	#	print("Error update user")
	#	return False


