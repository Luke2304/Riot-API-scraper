from RiotAPI import RiotAPI
import pandas as pd
import json
from helper import merge_two_dicts
from helper import participantIdentities
import constants as Consts

def main():
    api = RiotAPI('RGAPI-7937d1e9-ed86-4f57-bc41-da3f528e2674')
    r = api.get_match_id('2787975451')

    # Sub dictionaries that contain the information we want
    playerData = r['participantIdentities']
    matchData = r['participants']
    dataDF = participantIdentities(playerData, matchData)
    
    
    dataDF = dataDF[Consts.IDEAL_LIST_ORDER]

    dataDF.to_csv('match.csv', index=False)

if __name__ == '__main__':
    main()