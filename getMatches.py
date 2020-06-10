import urllib.request
from bs4 import BeautifulSoup

site= "https://csgostats.gg/match"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib.request.Request(site, headers=hdr)

try:
    page = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.fp.read())

soup = BeautifulSoup(page, "html.parser")
for icon in soup.find_all("span", class_="glyphicon glyphicon-play-circle"):
    matchURL = "https://csgostats.gg" + icon.find_parent("a").get('href')
    req = urllib.request.Request(matchURL, headers=hdr)
    try:
        matchPage = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.fp.read())
    soup = BeautifulSoup(matchPage, "html.parser")
    demoURL = "https://csgostats.gg" + soup.find("span", class_="glyphicon glyphicon-facetime-video").find_parent("a").get("href")
    req = urllib.request.Request(demoURL, headers=hdr)
    try:
        demoRes = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        demoRes = e.fp.read()
    print(demoRes)