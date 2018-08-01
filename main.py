

import sys, time, os, urllib, urllib2, re, csv
from bs4 import BeautifulSoup


opener_headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0)',
                  'Host' : 'www.oui.sncf',
                  'Connection' : 'keep-alive',
                  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Referer'   : 'http://www.voyages-sncf.com/'}

def init_opener():
    proxy = urllib2.ProxyHandler({})
    #'http': 'http://127.0.0.1:8082', 'https': 'http://127.0.0.1:8082'})
    opener = urllib2.build_opener(proxy, urllib2.HTTPCookieProcessor())
    opener.addheaders = opener_headers.items()
    return opener

opener = init_opener()

base_url = 'http://www.oui.sncf/'

search_url = base_url + 'vsc/train-ticket/'

search_params = { '_LANG': 'fr',
                  'action:searchTravelLaunchTrain' : 'Rechercher',
                  'COMFORT_CLASS' : '2',
                  'DESTINATION_CITY' : 'Saint-Malo (Bretagne)',
                  'DESTINATION_CITY_RR_CODE' : 'FRXSB',
                  'INWARD_DATE' : '',
                  'INWARD_TIME' : '6',
                  'ORIGIN_CITY' : 'Paris (toutes gares intramuros)',
                  'ORIGIN_CITY_RR_CODE' : 'FRPAR',
                  'OUTWARD_DATE' : '01/08/2018',
                  'OUTWARD_SCHEDULE_TYPE' : 'DEPARTURE_FROM',
                  'OUTWARD_TIME' : '15',
                  'PASSENGER_1' : 'ADULT',
                  'PASSENGER_1_CARD' : 'YOUNG' }

for k, v in search_params.items(): 
    search_params[k] = v and urllib2.quote(str(v), safe='') or ''

search_full_url = search_url + "?" + ("&".join([k + '=' + v for k,v in search_params.items()]))


print search_full_url

response = opener.open(search_full_url)
print response.geturl()
print response.getcode()
html = response.read()

time.sleep(5) # behave as a browser waiting to be redirected


results = []

next_proposals_url = base_url + 'nextTrains?hid=%s'

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

