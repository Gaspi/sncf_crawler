

import sys, time, os, urllib, urllib2, re, csv
from bs4 import BeautifulSoup


def init_opener():
    proxy = urllib2.ProxyHandler({})
    #'http': 'http://127.0.0.1:8082', 'https': 'http://127.0.0.1:8082'})
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0)', 
               'Referer'   : 'http://www.voyages-sncf.com/'}
    opener = urllib2.build_opener(proxy, urllib2.HTTPCookieProcessor())
    opener.addheaders = headers.items()
    return opener

opener = init_opener()

search_url = 'http://www.voyages-sncf.com/weblogic/expressbooking/_SvExpressBooking?' \
             'bookingChoice=train&' \
             'origin_city=%(origin_city)s&' \
             'destination_city=%(destination_city)s&' \
             'outward_date=%(outward_date)s&' \
             'outward_time=%(outward_time)s&' \
             'nbPassenger=1&' \
             'PASSENGER_1_CARD=YOUNGS' \
             'classe=2&' \
             'train=Rechercher'


next_proposals_url = 'http://www.voyages-sncf.com/weblogic/proposals/nextTrains?hid=%s' \
                     '&rfrr=PropositionAller_body_Trains%%20suivants'

search_params = {'origin_city'     : 'Paris+(Toutes+gares+intramuros)',
                 'destination_city': 'Saint-Malo',
                 'outward_date'    : '31/07/2018',
                 'outward_time'    : 21 }

results = []

for k, v in search_params.items(): 
    search_params[k] = v and urllib2.quote(str(v), safe='') or ''
    

print search_url % search_params

html = opener.open(search_url % search_params).read()

proposals_url = re.search(r'<a href="([^"]+)" id="url_redirect_proposals"',
                          html, re.M).group(1)

time.sleep(5) # behave as a browser waiting to be redirected
prop = opener.open(proposals_url)

results.append(None)
end_of_day = True
last_hid = None

# get next trains
while not end_of_day:
    time.sleep(2)
    prop = opener.open(next_proposals_url % last_hid)
    results.append(None)
    end_of_day = True
    last_hid = None

