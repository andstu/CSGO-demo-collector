from steam.client import SteamClient
from csgo.client import CSGOClient
from csgo.features import Match
import csgo.sharecode
from csgo.protobufs.cstrike15_gcmessages_pb2 import CMsgGCCStrike15_v2_MatchList
import json

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
    # meme = csgo.sharecode.decode('CSGO-y7k25-vtEun-8NBMO-NmYLV-7FFdH')
    # print(meme)
    # cs.request_full_match_info(meme['matchid'], meme['outcomeid'], meme['token'])
    # response, = cs.wait_event('full_match_info')
    #print(response)

    cs.request_player_profile(375771776)
    response, = cs.wait_event('player_profile')
    print(response)
    cs.exit()


client.cli_login(username=auth['usr'],password=auth['pass'])
client.run_forever()