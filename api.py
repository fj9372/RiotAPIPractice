import operator
import time
import requests

def testMethod(name):
    api_key = ""
    user_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + '?api_key=' + api_key
    user = requests.get(user_url).json()

    riotID = user['id']                    
    riotAccountID = user['accountId']
    riotPuuID = user['puuid']
    riotName = user['name']
    iconID = user['profileIconId']
    level = user['summonerLevel']         

    matches_url = "https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/" + riotPuuID + '/ids?start=0&count=200&api_key=' + api_key
    
    
    matches = requests.get(matches_url).json()

    augment_dict = {}
    level = 0
    placement = 0
    players_eliminated = 0
    total_dmg = 0
    
    hello = 1
    for i in matches:
        time.sleep(1.5)
        tft_url = "https://americas.api.riotgames.com/tft/match/v1/matches/" + i + '?api_key=' + api_key
        match = requests.get(tft_url)
        print(match)
        match = match.json()
        print(match['metadata']['match_id'], hello)
        hello+=1
        participants = match['info']['participants']
        for participant in participants:
            if(participant['puuid'] == riotPuuID):
                for augment in participant['augments']:
                    if augment in augment_dict.keys():
                        augment_dict[augment] += 1
                    else:
                        augment_dict[augment] = 1
                level += participant['level']
                placement += participant['placement']
                players_eliminated += participant['players_eliminated']
                total_dmg += participant['total_damage_to_players']
    sort_augment = dict(sorted(augment_dict.items(), key = operator.itemgetter(1), reverse=True))
    print(list(sort_augment.keys())[0:3])
    print("Average Level: ", level/hello)
    print("Average Placement: ", placement/hello)
    print("Average Players Eliminated: ", players_eliminated/hello)
    print("Average Damage: ", total_dmg/hello)


