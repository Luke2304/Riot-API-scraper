# File for helper functions
import pandas as pd

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def participantIdentities(player, match):
    """Given player and match dictionaries, return a clean dataframe"""
    matchDF = pd.DataFrame()
    for i in range(0, 10):
        onePlayer = player[i]
        # Player data
        playerData = onePlayer['player']
        participantId = {'participantId': onePlayer['participantId']}
        bigDict = merge_two_dicts(participantId, playerData)
        # Match data
        smallDict = {'participantId': match[i]['participantId'],
                     'teamId': match[i]['teamId'],
                     'championId': match[i]['championId'],
                     'spell1Id': match[i]['spell1Id'],
                     'spell2Id':match[i]['spell2Id'],
                     'highestAchievedSeasonTier':match[i]['highestAchievedSeasonTier']
                    }
        statDict = match[i]['stats']
        matchDict = merge_two_dicts(statDict, smallDict)
        superDict = merge_two_dicts(matchDict, bigDict)
        playerDF = pd.DataFrame([superDict])
        matchDF = matchDF.append(playerDF, ignore_index=True)
    return matchDF