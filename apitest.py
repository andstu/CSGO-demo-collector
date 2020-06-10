from steam.client import SteamClient
from csgo.client import CSGOClient
from csgo.features import Match

client = SteamClient()
cs = CSGOClient(client)

@client.on('logged_on')
def start_csgo():
    cs.launch()

@cs.on('ready')
def gc_ready():
    print('Ready')
    meme =  Match.request_recent_user_games(cs, account_id=71735956)
    print(meme)
    pass

client.cli_login()
client.run_forever()