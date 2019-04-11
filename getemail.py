from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import hashlib
import redis
from addMailchimp import addToMail 
from addMailchimp import testMailChimp
from sendToFirebase import *

r = redis.StrictRedis(host='redis', port=6379, db=0)


weGoodToGoMailchimp=True


def testMailchimpApi(mailchimplist,mailchimpkey):
    if testMailChimp(mailchimpkey,mailchimplist) == False:
        print("No access to mailchimp")
        weGoodToGoMailchimp=False



def writeEmailToFile(email,site,tags,user,botid,mailchimpkey,mailchimplist):
    '''
    Write the email to file
    '''
    print("Adidng email to file")
    f = open("out/"+botid+".csv", "a")
    f.write("{0},{1},{2} \n".format(email,site.encode('utf-8'),tags.encode('utf-8')))
    
    #Test if we hade a working mailchimp
    if weGoodToGoMailchimp: 
        addToMail(email,site,tags,mailchimplist,mailchimpkey)
    addEmailFirebase(email,user,site,tags,botid)
    f.close()


def haveSearched(url,user,words,botid):
    '''
    Check if we have scraped the search
    '''
    hash_url_d = hashlib.md5(str(botid+"-"+url).encode('utf-8'))
    hash_url =hash_url_d.hexdigest()
    from_cache = r.get(hash_url)
    print(from_cache)
    if from_cache == None:
        #We dont haveything in the cache :-( 
        r.set(hash_url,url)
        addUrlsFirebase(user,url,words,botid)
        return True
    else:
        print("Alreadyd scanned")
        return False


def extractEmail(emails,site,tags,user,botid,mailchimplist,mailchimpkey):
    '''
    Extract the email from the pages
    '''
    skipEnds=['jpg','png','gif']
    for email in emails:

        process_email=True
        for skip in skipEnds:
            if email.endswith(skip):
                process_email=False
        if process_email:


            hash_email_d = hashlib.md5(str(botid+"-"+email).encode('utf-8'))
            hash_email =hash_email_d.hexdigest()
            from_cache = r.get(hash_email)
            print(from_cache)
            if from_cache == None:
                #We dont haveything in the cache :-( 
                writeEmailToFile(email,site,tags,user,botid,mailchimpkey,mailchimplist)
                r.set(hash_email,email)





def getEmails(site,tags,user,botid,mailchimplist,mailchimpkey):
    #
    # Scrape the site and get all emails
    #
    # process urls one by one until we exhaust the queue


    # a queue of urls to be crawled
    new_urls = deque(site)
    
    # a set of urls that we have already crawled
    processed_urls = set()

    #Test if mailchimp api is good to go
    testMailchimpApi(mailchimplist,mailchimpkey)
    
    # a set of crawled emails
    emails = set()
    scanned_page_count=0
    while len(new_urls):
    
        # move next url from the queue to the set of processed urls
        url = new_urls.popleft()
        scanned_page_count+=1
        if scanned_page_count > 30:
            print("break to man pages scanned")
            break

        if haveSearched(url,user,tags,botid):

            processed_urls.add(url)
        
            # extract base url to resolve relative links
            parts = urlsplit(url)
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = url[:url.rfind('/')+1] if '/' in parts.path else url
        
            # get url's content
            print("Processing {}".format(url.encode('utf-8')))
            try:
                response = requests.get(url)
            except:
                # ignore pages with errors
                continue
        
            # extract all email addresses and add them into the resulting set
            new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
            #emails.update(new_emails)
            extractEmail(new_emails,url,tags,user,botid,mailchimpkey,mailchimplist)
        
            # create a beutiful soup for the html document
            soup = BeautifulSoup(response.text)
        
            # find and process all the anchors in the document
            for anchor in soup.find_all("a"):
                # extract link url from the anchor
                link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                if "#" in link or "@" in link:
                    pass
                else:
    
    
    
                    # resolve relative links
                    if link.startswith('/'):
                        link = base_url +"/"+ link
                    elif not link.startswith('https'):
                        link = path +"/"+ link
                    elif not link.startswith('http'):
                        link = path +"/"+ link
                    # add the new url to the queue if it was not enqueued nor processed yet
                    if not link in new_urls and not link in processed_urls:
                        new_urls.append(link)
    

