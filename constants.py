
URL = {
    'base': 'https://{proxy}.api.riotgames.com/lol/{url}',
    'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
    'match_by_id': 'match/v{version}/matches/{match_id}'
}

API_VERSIONS = {
    'summoner': '3'
}

REGIONS = {
    'north_america': 'na1'
}

IDEAL_LIST_ORDER = ['participantId', 'summonerId','accountId', 'summonerName', 'profileIcon', 'teamId',
                    'championId', 'matchHistoryUri','currentAccountId','currentPlatformId',
                    'highestAchievedSeasonTier', 'win', 'champLevel', 'spell1Id', 'spell2Id',
                    'combatPlayerScore', 'kills', 'deaths', 'assists', 'doubleKills', 'tripleKills',
                    'quadraKills', 'pentaKills', 'killingSprees', 'largestCriticalStrike', 'largestKillingSpree',
                    'largestMultiKill', 'longestTimeSpentLiving','damageDealtToObjectives', 'damageDealtToTurrets',
                    'damageSelfMitigated', 'totalDamageDealt', 'totalDamageDealtToChampions','totalDamageTaken',
                    'trueDamageDealt', 'trueDamageDealtToChampions', 'trueDamageTaken', 'physicalDamageDealt',
                    'physicalDamageDealtToChampions', 'physicalDamageTaken', 'magicDamageDealt', 'magicDamageDealtToChampions',
                    'magicalDamageTaken', 'visionScore', 'sightWardsBoughtInGame', 'visionWardsBoughtInGame',
                    'wardsKilled', 'wardsPlaced','firstBloodAssist', 'firstBloodKill', 'firstTowerAssist',
                    'firstTowerKill', 'timeCCingOthers', 'totalHeal', 'totalTimeCrowdControlDealt',
                    'totalUnitsHealed', 'totalMinionsKilled', 'goldEarned', 'goldSpent', 'totalPlayerScore',
                    'totalScoreRank', 'objectivePlayerScore', 'turretKills', 'unrealKills', 'inhibitorKills',
                    'neutralMinionsKilled', 'neutralMinionsKilledEnemyJungle', 'neutralMinionsKilledTeamJungle',
                    'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'perk0', 'perk0Var1',
                    'perk0Var2', 'perk0Var3', 'perk1', 'perk1Var1', 'perk1Var2', 'perk1Var3', 'perk2',
                    'perk2Var1', 'perk2Var2', 'perk2Var3', 'perk3', 'perk3Var1', 'perk3Var2', 'perk3Var3',
                    'perk4', 'perk4Var1', 'perk4Var2', 'perk4Var3', 'perk5', 'perk5Var1', 'perk5Var2',
                    'perk5Var3', 'perkPrimaryStyle', 'perkSubStyle',  'platformId'
                    ]