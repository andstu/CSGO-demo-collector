from steam.client import SteamClient
from csgo.client import CSGOClient
from csgo.features import Match
import csgo.sharecode
import json
import urllib.request
import requests
import shutil

# site= "https://csgostats.gg/match"
# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#        'Accept-Encoding': 'none',
#        'Accept-Language': 'en-US,en;q=0.8',
#        'Connection': 'keep-alive'}

# req = urllib.request.Request(site, headers=hdr)

client = SteamClient()
cs = CSGOClient(client)

with open('./auth.json') as f:
  auth = json.load(f)

@client.on('logged_on')
def start_csgo():
    cs.launch()

@cs.on('ready')
def gc_ready():
    print('Ready')
    meme = csgo.sharecode.decode('CSGO-y7k25-vtEun-8NBMO-NmYLV-7FFdH')
    print(meme)
    cs.request_full_match_info(meme['matchid'], meme['outcomeid'], meme['token'])
    response, = cs.wait_event('full_match_info')
    site = response.matches[0].roundstatsall[-1].map
    file_name = f"{meme['matchid']}_{meme['outcomeid']}_{meme['token']}"
    print(site)
    print(file_name)
    with urllib.request.urlopen(site) as res, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(res, out_file)

    cs.exit()
    cs.emit('meme')


client.login(username=auth['usr'],password=auth['pass'])
cs.wait_event('meme')