import requests
import gc

# https://developer.riotgames.com/apis

REGION = 'br1'
BASE_URL = 'https://{}.api.riotgames.com'.format(REGION)
API_KEY = 'RGAPI-706006aa-a279-4336-897b-c8c6b088091a'

class CHAMPION:
  # https://developer.riotgames.com/apis#champion-v3
  def CHAMPION_BY_NAME(region, name):
    URL = 'https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}'.format(region, name, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

class MATCH:
  # https://developer.riotgames.com/apis#match-v5
  def MATCH_BY_PUUID(region, puuid):
    URL = 'https://{}.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?start=0&count=20&api_key={}'.format(region, puuid, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

  def MATCH_BY_MATCHID(region, match_id):
    URL = 'https://{}.api.riotgames.com/lol/match/v5/matches/{}?api_key={}'.format(region, match_id, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

  def MATCH_BY_TIMELINE(region, match_id):
    URL = 'https://{}.api.riotgames.com/lol/match/v5/matches/{}/timeline?api_key={}'.format(region, match_id, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

class LEAGUE_EXP:
  # https://developer.riotgames.com/apis#league-exp-v4
  def LEAGUE_EXP_BY_ENTRIES(queue, tier, division, page):
    URL = BASE_URL + '/lol/league-exp/v4/entries/{}/{}/{}?page={}&api_key={}'.format(queue, tier, division, page, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

class LEAGUE:
  # https://developer.riotgames.com/apis#league-v4
  def LEAGUE_BY_SUMMONER_ID(summoner_id):
    URL = BASE_URL + '/lol/league/v4/entries/by-summoner/{}?api_key={}'.format(summoner_id, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

class SUMMONER:
  # https://developer.riotgames.com/apis#summoner-v4
  def SUMMONER_BY_SUMMONER_ID(summoner_id):
    URL = BASE_URL + '/lol/summoner/v4/summoners/{}?api_key={}'.format(summoner_id, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

class CHAMPION_MASTERY:
  # https://developer.riotgames.com/apis#champion-mastery-v4
  def CHAMPION_MASTERY_BY_SUMMONER_ID(summoner_id):
    URL = BASE_URL + '/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}'.format(summoner_id, API_KEY)
    get_response = requests.get(URL)
    return get_response.json()

# TESTS ENDPOINTS
# ===============

# champion_info = CHAMPION.CHAMPION_BY_NAME('br1', 'shapeshift')

# matches_info = MATCH.MATCH_BY_PUUID('americas', 'dZmlp3QUlexlZz0NwjOClDkzS6QOj92HvgkXChShQo-ITOoUCfWUmgLEo0iPUdR9k92z-aaykjjx2Q')
# matches_id_info = MATCH.MATCH_BY_MATCHID('americas', 'BR1_2572405937')
# matches_timeline_info = MATCH.MATCH_BY_MATCHID('americas', 'BR1_2572405937')

# league_exp = LEAGUE_EXP.LEAGUE_EXP_BY_ENTRIES('RANKED_SOLO_5x5', 'GRANDMASTER', 'I', page=2)

# league_summoner = LEAGUE.LEAGUE_BY_SUMMONER_ID('hRbL3c6345JmR0U8ueYyjlk9LauvopUFRy3bEgAieKz_DQ')

# summoner_info = SUMMONER.SUMMONER_BY_SUMMONER_ID('hRbL3c6345JmR0U8ueYyjlk9LauvopUFRy3bEgAieKz_DQ')

# champion_mastery_info = CHAMPION_MASTERY.CHAMPION_MASTERY_BY_SUMMONER_ID('hRbL3c6345JmR0U8ueYyjlk9LauvopUFRy3bEgAieKz_DQ')

# ===============

# Get summonerID by tier, queue, division
# -- Sample players in each divisions
league_exp = LEAGUE_EXP.LEAGUE_EXP_BY_ENTRIES('RANKED_SOLO_5x5', 'IRON', 'I', page=1)
league_exp = league_exp[:10]
league_exp_filtered = []

for league_exp_i in league_exp:
  league_exp_dict = {
    'summonerId': league_exp_i['summonerId'],
    'tier': league_exp_i['tier'],
    'rank': league_exp_i['rank']
  }
  league_exp_filtered.append(league_exp_dict)

gc.collect()
# Get PUUID by summonerID
# -- PUUID important for other information
# champion_mastery_info = CHAMPION_MASTERY.CHAMPION_MASTERY_BY_SUMMONER_ID('hRbL3c6345JmR0U8ueYyjlk9LauvopUFRy3bEgAieKz_DQ')

# Get matchID by PUUID
# matches_info = MATCH.MATCH_BY_PUUID('americas', 'dZmlp3QUlexlZz0NwjOClDkzS6QOj92HvgkXChShQo-ITOoUCfWUmgLEo0iPUdR9k92z-aaykjjx2Q')

# Get match info by matchID
# matches_id_info = MATCH.MATCH_BY_MATCHID('americas', 'BR1_2572405937')


print(league_exp_filtered)