from bs4 import BeautifulSoup

import datetime
rowdict = {}
rowdict['date'] = str(datetime.date.today())

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
base_url = br.open("http://www.isitwp.com/")
with open('websitesforwpcheck.txt') as f:
    for line in f:
        rowdict['website'] = str(line)
        br.select_form(nr=0)
        br["q"] = str(line)
        isitwp_response = br.submit()
        isitwp_response = isitwp_response.read()
        if "Good news everyone" in a:
            rowdict['iswordpresswebsite'] = "yes"
        else:
            rowdict['iswordpresswebsite'] = "no"
        print(rowdict,spread_sheet_id, worksheet_id)