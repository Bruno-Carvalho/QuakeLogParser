import re

def get_log_as_list(logFile):
    with open(logFile, 'r') as log:
        logList = list(log)
        return logList

def get_match_list(log, indexes):
    match_list = []

    for i in range(len(indexes)):
        startIdx = indexes[i]
        endIdx = None
        if i == (len(indexes) - 1):
            endIdx = (len(log) - 1)
        else:
            endIdx = indexes[i+1]
        subList = log[startIdx:endIdx]
        match_list.append(subList)
    
    return match_list

def get_match_indexes(list):
    logIdx = []

    for line in range(len(list)):
        if 'InitGame:' in list[line]:
            logIdx.append(line)
    
    return logIdx

def get_match_info(gameTuple): 
    idx, match = gameTuple

    players = []
    totalKills = 0
    kills = dict()
    deaths = dict()
    game = idx + 1
    weapons = dict()

    for i in range(len(match)):
        line = match[i]
        lineLen = len(line.split())
        action = line.split()[1]

        match action:
            case "Kill:":
                killer = re.search('(?:Kill: \d+ \d+ \d+):(.+?)killed', line).group(1).lstrip().rstrip()
                killed = re.search('killed(.+?)by', line).group(1).lstrip().rstrip()
                totalKills += 1

                deaths[killed] = deaths[killed] + 1

                weapon = line.split()[(lineLen - 1)]
                if weapon not in weapons:
                    weapons[weapon] = 0

                weapons[weapon] = weapons[weapon] + 1

                if killer != '<world>' and killer != killed:
                    kills[killer] = kills[killer] + 1
                    

                elif killer == '<world>':
                    kills[killed] = kills[killed] - 1

            case "ClientUserinfoChanged:":
                playerName = line.split('\\')[1].rstrip()
                if playerName not in players:
                    players.append(playerName)
                    kills[playerName] = 0
                    deaths[playerName] = 0        

    return {
        "game": game,
        "totalKills": totalKills,
        "players": players,
        "kills": kills,
        "deaths": deaths,
        "weapons": weapons,
    }

serverlog = get_log_as_list('qgames.log') 

matchesIdexes = get_match_indexes(serverlog)

match_list = get_match_list(serverlog, matchesIdexes)

log_matches_data = list(map(get_match_info, enumerate(match_list)))

print(log_matches_data)