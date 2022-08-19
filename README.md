# Quake Log Parser

This script extracts information of each game that is logged in the given file, given the log follows the Quake 3 Arena server log files patterns. It collects the following data:
- The _'id'_ of each game initialized _(max. 2147483647)_
- Number of total kills for each game *_(including world deaths)_
- Players that connected to each game
- Kills scoreboard for each mach _*(players lose 1 kill score once the die to the game environment, such as falling from a high distance)_
- Death scoreboard for each mach
- The amount of times that a weapon was used to kill a player in each match

**In order to run the script correctly, the log file must be located at the same folder as the .py script, and must be named "serverlog.log"**
<br/>
<br/>

The raw output will return one array containing the information for all games initialized logged in the given file, and should look like this:

```
[{'game': 1, 'totalKills': 0, 'players': ['Isgalamido'], 'kills': {'Isgalamido': 0}, 'deaths': {'Isgalamido': 0}, 'weapons': {}}, {'game': 2, 'totalKills': 11, 'players': ['Isgalamido', 'Dono da Bola', 'Mocinha'], 'kills': {'Isgalamido': -7, 'Dono da Bola': 0, 'Mocinha': 0}, 'deaths': {'Isgalamido': 10, 'Dono da Bola': 0, 'Mocinha': 1}, 'weapons': {'MOD_TRIGGER_HURT': 7, 'MOD_ROCKET_SPLASH': 3, 'MOD_FALLING': 1}}, {'game': 3, 'totalKills': 4, 'players': ['Dono da Bola', 'Mocinha', 'Isgalamido', 'Zeh'], 'kills': {'Dono da Bola': -1, 'Mocinha': 0, 'Isgalamido': 1, 'Zeh': -2}, 'deaths': {'Dono da Bola': 1, 'Mocinha': 1, 'Isgalamido': 0, 'Zeh': 2}, 'weapons': {'MOD_ROCKET': 1, 'MOD_TRIGGER_HURT': 2, 'MOD_FALLING': 1}}, {'game': 4, 'totalKills': 105, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Assasinu Credi'], 'kills': {'Dono da Bola': 9, 'Isgalamido': 19, 'Zeh': 20, 'Assasinu Credi': 12}, 'deaths': {'Dono da Bola': 31, 'Isgalamido': 23, 'Zeh': 27, 'Assasinu Credi': 24}, 'weapons': {'MOD_TRIGGER_HURT': 9, 'MOD_FALLING': 11, 'MOD_ROCKET': 20, 'MOD_RAILGUN': 8, 'MOD_ROCKET_SPLASH': 51, 'MOD_MACHINEGUN': 4, 'MOD_SHOTGUN': 2}}, {'game': 5, 'totalKills': 14, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Assasinu Credi'], 'kills': {'Dono da Bola': 0, 'Isgalamido': 2, 'Zeh': 1, 'Assasinu Credi': -1}, 'deaths': {'Dono da Bola': 1, 'Isgalamido': 0, 'Zeh': 5, 'Assasinu Credi': 8}, 'weapons': {'MOD_ROCKET': 4, 'MOD_ROCKET_SPLASH': 4, 'MOD_TRIGGER_HURT': 5, 'MOD_RAILGUN': 1}}, {'game': 6, 'totalKills': 29, 'players': ['Fasano Again', 'Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'UnnamedPlayer', 'Maluquinho', 'Assasinu Credi', 'Mal'], 'kills': {'Fasano Again': 0, 'Oootsimo': 8, 'Isgalamido': 3, 'Zeh': 7, 'Dono da Bola': 2, 'UnnamedPlayer': 0, 'Maluquinho': 0, 'Assasinu Credi': 1, 'Mal': 0}, 'deaths': {'Fasano Again': 0, 'Oootsimo': 2, 'Isgalamido': 7, 'Zeh': 8, 'Dono da Bola': 5, 'UnnamedPlayer': 1, 'Maluquinho': 1, 'Assasinu Credi': 3, 'Mal': 2}, 'weapons': {'MOD_ROCKET': 5, 'MOD_RAILGUN': 2, 'MOD_SHOTGUN': 4, 'MOD_ROCKET_SPLASH': 13, 'MOD_TRIGGER_HURT': 3, 'MOD_FALLING': 1, 'MOD_MACHINEGUN': 1}}, {'game': 7, 'totalKills': 130, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi', 'Chessus!', 'Chessus'], 'kills': {'Oootsimo': 20, 'Isgalamido': 14, 'Zeh': 8, 'Dono da Bola': 10, 'Mal': -3, 'Assasinu Credi': 19, 'Chessus!': 0, 'Chessus': 0}, 'deaths': {'Oootsimo': 19, 'Isgalamido': 15, 'Zeh': 21, 'Dono da Bola': 26, 'Mal': 28, 'Assasinu Credi': 19, 'Chessus!': 0, 'Chessus': 2}, 'weapons': {'MOD_FALLING': 7, 'MOD_TRIGGER_HURT': 20, 'MOD_ROCKET_SPLASH': 49, 'MOD_ROCKET': 29, 'MOD_SHOTGUN': 7, 'MOD_RAILGUN': 9, 'MOD_MACHINEGUN': 9}}, {'game': 8, 'totalKills': 89, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi'], 'kills': {'Oootsimo': 15, 'Isgalamido': 20, 'Zeh': 12, 'Dono da Bola': 1, 'Mal': -3, 'Assasinu Credi': 9}, 'deaths': {'Oootsimo': 14, 'Isgalamido': 11, 'Zeh': 11, 'Dono da Bola': 16, 'Mal': 20, 'Assasinu Credi': 17}, 'weapons': {'MOD_TRIGGER_HURT': 9, 'MOD_ROCKET': 18, 'MOD_ROCKET_SPLASH': 39, 'MOD_FALLING': 6, 'MOD_RAILGUN': 12, 'MOD_MACHINEGUN': 4, 'MOD_SHOTGUN': 1}}, {'game': 9, 'totalKills': 67, 'players': ['Oootsimo', 'Isgalamido', 'Zeh', 'Dono da Bola', 'Mal', 'Assasinu Credi', 'Chessus!', 'Chessus'], 'kills': {'Oootsimo': 8, 'Isgalamido': 1, 'Zeh': 12, 'Dono da Bola': 1, 'Mal': 2, 'Assasinu Credi': 7, 'Chessus!': 0, 'Chessus': 8}, 'deaths': {'Oootsimo': 12, 'Isgalamido': 3, 'Zeh': 15, 'Dono da Bola': 5, 'Mal': 15, 'Assasinu Credi': 14, 'Chessus!': 0, 'Chessus': 3}, 'weapons': {'MOD_TRIGGER_HURT': 8, 'MOD_ROCKET_SPLASH': 25, 'MOD_SHOTGUN': 1, 'MOD_ROCKET': 17, 'MOD_MACHINEGUN': 3, 'MOD_FALLING': 3, 'MOD_RAILGUN': 10}}, {'game': 10, 'totalKills': 60, 'players': ['Oootsimo', 'Dono da Bola', 'Zeh', 'Chessus', 'Mal', 'Assasinu Credi', 'Isgalamido'], 'kills': {'Oootsimo': -1, 'Dono da Bola': 3, 'Zeh': 7, 'Chessus': 5, 'Mal': 1, 'Assasinu Credi': 3, 'Isgalamido': 5}, 'deaths': {'Oootsimo': 8, 'Dono da Bola': 3, 'Zeh': 5, 'Chessus': 9, 'Mal': 14, 'Assasinu Credi': 8, 'Isgalamido': 13}, 'weapons': {'MOD_TELEFRAG': 25, 'MOD_TRIGGER_HURT': 17, 'MOD_ROCKET': 4, 'MOD_ROCKET_SPLASH': 1, 'MOD_RAILGUN': 7, 'MOD_BFG_SPLASH': 2, 'MOD_BFG': 2, 'MOD_MACHINEGUN': 1, 'MOD_CRUSH': 1}}, {'game': 11, 'totalKills': 20, 'players': ['Dono da Bola', 'Isgalamido', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'UnnamedPlayer', 'Mal'], 'kills': {'Dono da Bola': -2, 'Isgalamido': 4, 'Zeh': 0, 'Oootsimo': 4, 'Chessus': 0, 'Assasinu Credi': -3, 'UnnamedPlayer': 0, 'Mal': 0}, 'deaths': {'Dono da Bola': 5, 'Isgalamido': 4, 'Zeh': 2, 'Oootsimo': 1, 'Chessus': 3, 'Assasinu Credi': 4, 'UnnamedPlayer': 0, 'Mal': 1}, 'weapons': {'MOD_TRIGGER_HURT': 7, 'MOD_CRUSH': 1, 'MOD_ROCKET_SPLASH': 4, 'MOD_BFG_SPLASH': 3, 'MOD_MACHINEGUN': 1, 'MOD_RAILGUN': 4}}, {'game': 12, 'totalKills': 160, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Isgalamido': 24, 'Dono da Bola': 3, 'Zeh': 11, 'Oootsimo': 12, 'Chessus': 12, 'Assasinu Credi': 18, 'Mal': -7}, 'deaths': {'Isgalamido': 21, 'Dono da Bola': 31, 'Zeh': 16, 'Oootsimo': 23, 'Chessus': 24, 'Assasinu Credi': 19, 'Mal': 26}, 'weapons': {'MOD_TRIGGER_HURT': 37, 'MOD_RAILGUN': 38, 'MOD_ROCKET_SPLASH': 35, 'MOD_BFG_SPLASH': 8, 'MOD_ROCKET': 25, 'MOD_MACHINEGUN': 7, 'MOD_BFG': 8, 'MOD_FALLING': 2}}, {'game': 13, 'totalKills': 6, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Isgalamido': -1, 'Dono da Bola': -1, 'Zeh': 2, 'Oootsimo': 1, 'Chessus': 0, 'Assasinu Credi': 0, 'Mal': 0}, 'deaths': {'Isgalamido': 1, 'Dono da Bola': 2, 'Zeh': 0, 'Oootsimo': 1, 'Chessus': 0, 'Assasinu Credi': 2, 'Mal': 0}, 'weapons': {'MOD_TRIGGER_HURT': 2, 'MOD_ROCKET': 1, 'MOD_ROCKET_SPLASH': 1, 'MOD_BFG_SPLASH': 1, 'MOD_BFG': 1}}, {'game': 14, 'totalKills': 122, 'players': ['Isgalamido', 'Dono da Bola', 'Zeh', 'Oootsimo', 'Chessus', 'Assasinu Credi', 'Mal'], 'kills': {'Isgalamido': 22, 'Dono da Bola': 1, 'Zeh': 4, 'Oootsimo': 9, 'Chessus': 7, 'Assasinu Credi': 3, 'Mal': -5}, 'deaths': {'Isgalamido': 12, 'Dono da Bola': 25, 'Zeh': 21, 'Oootsimo': 11, 'Chessus': 14, 'Assasinu Credi': 19, 'Mal': 20}, 'weapons': {'MOD_RAILGUN': 20, 'MOD_TRIGGER_HURT': 31, 'MOD_ROCKET': 23, 'MOD_ROCKET_SPLASH': 24, 'MOD_MACHINEGUN': 4, 'MOD_BFG_SPLASH': 10, 'MOD_FALLING': 5, 'MOD_BFG': 5}}, {'game': 15, 'totalKills': 3, 'players': ['Zeh', 'Assasinu Credi', 'Dono da Bola', 'Fasano Again', 'Isgalamido', 'Oootsimo'], 'kills': {'Zeh': -3, 'Assasinu Credi': 0, 'Dono da Bola': 0, 'Fasano Again': 0, 'Isgalamido': 0, 'Oootsimo': 0}, 'deaths': {'Zeh': 3, 'Assasinu Credi': 0, 'Dono da Bola': 0, 'Fasano Again': 0, 'Isgalamido': 0, 'Oootsimo': 0}, 'weapons': {'MOD_TRIGGER_HURT': 3}}, {'game': 16, 'totalKills': 0, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh'], 'kills': {'Dono da Bola': 0, 'Oootsimo': 0, 'Isgalamido': 0, 'Assasinu Credi': 0, 'Zeh': 0}, 'deaths': {'Dono da Bola': 0, 'Oootsimo': 0, 'Isgalamido': 0, 'Assasinu Credi': 0, 'Zeh': 0}, 'weapons': {}}, {'game': 17, 'totalKills': 13, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh', 'UnnamedPlayer', 'Mal'], 'kills': {'Dono da Bola': -2, 'Oootsimo': 0, 'Isgalamido': 0, 'Assasinu Credi': -3, 'Zeh': 0, 'UnnamedPlayer': 0, 'Mal': -1}, 'deaths': {'Dono da Bola': 2, 'Oootsimo': 3, 'Isgalamido': 1, 'Assasinu Credi': 4, 'Zeh': 2, 'UnnamedPlayer': 0, 'Mal': 1}, 'weapons': {'MOD_FALLING': 3, 'MOD_TRIGGER_HURT': 6, 'MOD_RAILGUN': 2, 'MOD_ROCKET_SPLASH': 2}}, {'game': 18, 'totalKills': 7, 'players': ['Dono da Bola', 'Oootsimo', 'Isgalamido', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Dono da Bola': -1, 'Oootsimo': 0, 'Isgalamido': 1, 'Assasinu Credi': 2, 'Zeh': 2, 'Mal': -1}, 'deaths': {'Dono da Bola': 1, 'Oootsimo': 1, 'Isgalamido': 1, 'Assasinu Credi': 1, 'Zeh': 1, 'Mal': 2}, 'weapons': {'MOD_ROCKET_SPLASH': 4, 'MOD_ROCKET': 1, 'MOD_FALLING': 1, 'MOD_TRIGGER_HURT': 1}}, {'game': 19, 'totalKills': 95, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Isgalamido': 13, 'Oootsimo': 10, 'Dono da Bola': 12, 'Assasinu Credi': 8, 'Zeh': 20, 'Mal': 2}, 'deaths': {'Isgalamido': 12, 'Oootsimo': 14, 'Dono da Bola': 15, 'Assasinu Credi': 17, 'Zeh': 18, 'Mal': 19}, 'weapons': {'MOD_TRIGGER_HURT': 12, 'MOD_ROCKET': 27, 'MOD_ROCKET_SPLASH': 32, 'MOD_SHOTGUN': 6, 'MOD_RAILGUN': 10, 'MOD_MACHINEGUN': 7, 'MOD_FALLING': 1}}, {'game': 20, 'totalKills': 3, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Isgalamido': 0, 'Oootsimo': 1, 'Dono da Bola': 1, 'Assasinu Credi': 0, 'Zeh': 0, 'Mal': 0}, 'deaths': {'Isgalamido': 0, 'Oootsimo': 0, 'Dono da Bola': 1, 'Assasinu Credi': 1, 'Zeh': 1, 'Mal': 0}, 'weapons': {'MOD_ROCKET_SPLASH': 2, 'MOD_ROCKET': 1}}, {'game': 21, 'totalKills': 131, 'players': ['Isgalamido', 'Oootsimo', 'Dono da Bola', 'Assasinu Credi', 'Zeh', 'Mal'], 'kills': {'Isgalamido': 17, 'Oootsimo': 21, 'Dono da Bola': 12, 'Assasinu Credi': 16, 'Zeh': 19, 'Mal': 6}, 'deaths': {'Isgalamido': 19, 'Oootsimo': 18, 'Dono da Bola': 19, 'Assasinu Credi': 30, 'Zeh': 15, 'Mal': 30}, 'weapons': {'MOD_ROCKET': 37, 'MOD_TRIGGER_HURT': 14, 'MOD_RAILGUN': 9, 'MOD_ROCKET_SPLASH': 60, 'MOD_MACHINEGUN': 4, 'MOD_SHOTGUN': 4, 'MOD_FALLING': 3}}]
      
```

<br/>
And should look like this if formatted to a JSON file for example:
<br/>
      
```json
[
{
"game":1,
"totalKills":0,
"players":[
   "Isgalamido"
],
"kills":{
   "Isgalamido":0
},
"deaths":{
   "Isgalamido":0
},
"weapons":{

}
},
{
"game":2,
"totalKills":11,
"players":[
   "Isgalamido",
   "Dono da Bola",
   "Mocinha"
],
"kills":{
   "Isgalamido":-7,
   "Dono da Bola":0,
   "Mocinha":0
},
"deaths":{
   "Isgalamido":10,
   "Dono da Bola":0,
   "Mocinha":1
},
"weapons":{
   "MOD_TRIGGER_HURT":7,
   "MOD_ROCKET_SPLASH":3,
   "MOD_FALLING":1
}
},
{
"game":3,
"totalKills":4,
"players":[
   "Dono da Bola",
   "Mocinha",
   "Isgalamido",
   "Zeh"
],
"kills":{
   "Dono da Bola":-1,
   "Mocinha":0,
   "Isgalamido":1,
   "Zeh":-2
},
"deaths":{
   "Dono da Bola":1,
   "Mocinha":1,
   "Isgalamido":0,
   "Zeh":2
},
"weapons":{
   "MOD_ROCKET":1,
   "MOD_TRIGGER_HURT":2,
   "MOD_FALLING":1
}
},
{
"game":4,
"totalKills":105,
"players":[
   "Dono da Bola",
   "Isgalamido",
   "Zeh",
   "Assasinu Credi"
],
"kills":{
   "Dono da Bola":9,
   "Isgalamido":19,
   "Zeh":20,
   "Assasinu Credi":12
},
"deaths":{
   "Dono da Bola":31,
   "Isgalamido":23,
   "Zeh":27,
   "Assasinu Credi":24
},
"weapons":{
   "MOD_TRIGGER_HURT":9,
   "MOD_FALLING":11,
   "MOD_ROCKET":20,
   "MOD_RAILGUN":8,
   "MOD_ROCKET_SPLASH":51,
   "MOD_MACHINEGUN":4,
   "MOD_SHOTGUN":2
}
},
{
"game":5,
"totalKills":14,
"players":[
   "Dono da Bola",
   "Isgalamido",
   "Zeh",
   "Assasinu Credi"
],
"kills":{
   "Dono da Bola":0,
   "Isgalamido":2,
   "Zeh":1,
   "Assasinu Credi":-1
},
"deaths":{
   "Dono da Bola":1,
   "Isgalamido":0,
   "Zeh":5,
   "Assasinu Credi":8
},
"weapons":{
   "MOD_ROCKET":4,
   "MOD_ROCKET_SPLASH":4,
   "MOD_TRIGGER_HURT":5,
   "MOD_RAILGUN":1
}
},
{
"game":6,
"totalKills":29,
"players":[
   "Fasano Again",
   "Oootsimo",
   "Isgalamido",
   "Zeh",
   "Dono da Bola",
   "UnnamedPlayer",
   "Maluquinho",
   "Assasinu Credi",
   "Mal"
],
"kills":{
   "Fasano Again":0,
   "Oootsimo":8,
   "Isgalamido":3,
   "Zeh":7,
   "Dono da Bola":2,
   "UnnamedPlayer":0,
   "Maluquinho":0,
   "Assasinu Credi":1,
   "Mal":0
},
"deaths":{
   "Fasano Again":0,
   "Oootsimo":2,
   "Isgalamido":7,
   "Zeh":8,
   "Dono da Bola":5,
   "UnnamedPlayer":1,
   "Maluquinho":1,
   "Assasinu Credi":3,
   "Mal":2
},
"weapons":{
   "MOD_ROCKET":5,
   "MOD_RAILGUN":2,
   "MOD_SHOTGUN":4,
   "MOD_ROCKET_SPLASH":13,
   "MOD_TRIGGER_HURT":3,
   "MOD_FALLING":1,
   "MOD_MACHINEGUN":1
}
},
{
"game":7,
"totalKills":130,
"players":[
   "Oootsimo",
   "Isgalamido",
   "Zeh",
   "Dono da Bola",
   "Mal",
   "Assasinu Credi",
   "Chessus!",
   "Chessus"
],
"kills":{
   "Oootsimo":20,
   "Isgalamido":14,
   "Zeh":8,
   "Dono da Bola":10,
   "Mal":-3,
   "Assasinu Credi":19,
   "Chessus!":0,
   "Chessus":0
},
"deaths":{
   "Oootsimo":19,
   "Isgalamido":15,
   "Zeh":21,
   "Dono da Bola":26,
   "Mal":28,
   "Assasinu Credi":19,
   "Chessus!":0,
   "Chessus":2
},
"weapons":{
   "MOD_FALLING":7,
   "MOD_TRIGGER_HURT":20,
   "MOD_ROCKET_SPLASH":49,
   "MOD_ROCKET":29,
   "MOD_SHOTGUN":7,
   "MOD_RAILGUN":9,
   "MOD_MACHINEGUN":9
}
},
{
"game":8,
"totalKills":89,
"players":[
   "Oootsimo",
   "Isgalamido",
   "Zeh",
   "Dono da Bola",
   "Mal",
   "Assasinu Credi"
],
"kills":{
   "Oootsimo":15,
   "Isgalamido":20,
   "Zeh":12,
   "Dono da Bola":1,
   "Mal":-3,
   "Assasinu Credi":9
},
"deaths":{
   "Oootsimo":14,
   "Isgalamido":11,
   "Zeh":11,
   "Dono da Bola":16,
   "Mal":20,
   "Assasinu Credi":17
},
"weapons":{
   "MOD_TRIGGER_HURT":9,
   "MOD_ROCKET":18,
   "MOD_ROCKET_SPLASH":39,
   "MOD_FALLING":6,
   "MOD_RAILGUN":12,
   "MOD_MACHINEGUN":4,
   "MOD_SHOTGUN":1
}
},
{
"game":9,
"totalKills":67,
"players":[
   "Oootsimo",
   "Isgalamido",
   "Zeh",
   "Dono da Bola",
   "Mal",
   "Assasinu Credi",
   "Chessus!",
   "Chessus"
],
"kills":{
   "Oootsimo":8,
   "Isgalamido":1,
   "Zeh":12,
   "Dono da Bola":1,
   "Mal":2,
   "Assasinu Credi":7,
   "Chessus!":0,
   "Chessus":8
},
"deaths":{
   "Oootsimo":12,
   "Isgalamido":3,
   "Zeh":15,
   "Dono da Bola":5,
   "Mal":15,
   "Assasinu Credi":14,
   "Chessus!":0,
   "Chessus":3
},
"weapons":{
   "MOD_TRIGGER_HURT":8,
   "MOD_ROCKET_SPLASH":25,
   "MOD_SHOTGUN":1,
   "MOD_ROCKET":17,
   "MOD_MACHINEGUN":3,
   "MOD_FALLING":3,
   "MOD_RAILGUN":10
}
},
{
"game":10,
"totalKills":60,
"players":[
   "Oootsimo",
   "Dono da Bola",
   "Zeh",
   "Chessus",
   "Mal",
   "Assasinu Credi",
   "Isgalamido"
],
"kills":{
   "Oootsimo":-1,
   "Dono da Bola":3,
   "Zeh":7,
   "Chessus":5,
   "Mal":1,
   "Assasinu Credi":3,
   "Isgalamido":5
},
"deaths":{
   "Oootsimo":8,
   "Dono da Bola":3,
   "Zeh":5,
   "Chessus":9,
   "Mal":14,
   "Assasinu Credi":8,
   "Isgalamido":13
},
"weapons":{
   "MOD_TELEFRAG":25,
   "MOD_TRIGGER_HURT":17,
   "MOD_ROCKET":4,
   "MOD_ROCKET_SPLASH":1,
   "MOD_RAILGUN":7,
   "MOD_BFG_SPLASH":2,
   "MOD_BFG":2,
   "MOD_MACHINEGUN":1,
   "MOD_CRUSH":1
}
},
{
"game":11,
"totalKills":20,
"players":[
   "Dono da Bola",
   "Isgalamido",
   "Zeh",
   "Oootsimo",
   "Chessus",
   "Assasinu Credi",
   "UnnamedPlayer",
   "Mal"
],
"kills":{
   "Dono da Bola":-2,
   "Isgalamido":4,
   "Zeh":0,
   "Oootsimo":4,
   "Chessus":0,
   "Assasinu Credi":-3,
   "UnnamedPlayer":0,
   "Mal":0
},
"deaths":{
   "Dono da Bola":5,
   "Isgalamido":4,
   "Zeh":2,
   "Oootsimo":1,
   "Chessus":3,
   "Assasinu Credi":4,
   "UnnamedPlayer":0,
   "Mal":1
},
"weapons":{
   "MOD_TRIGGER_HURT":7,
   "MOD_CRUSH":1,
   "MOD_ROCKET_SPLASH":4,
   "MOD_BFG_SPLASH":3,
   "MOD_MACHINEGUN":1,
   "MOD_RAILGUN":4
}
},
{
"game":12,
"totalKills":160,
"players":[
   "Isgalamido",
   "Dono da Bola",
   "Zeh",
   "Oootsimo",
   "Chessus",
   "Assasinu Credi",
   "Mal"
],
"kills":{
   "Isgalamido":24,
   "Dono da Bola":3,
   "Zeh":11,
   "Oootsimo":12,
   "Chessus":12,
   "Assasinu Credi":18,
   "Mal":-7
},
"deaths":{
   "Isgalamido":21,
   "Dono da Bola":31,
   "Zeh":16,
   "Oootsimo":23,
   "Chessus":24,
   "Assasinu Credi":19,
   "Mal":26
},
"weapons":{
   "MOD_TRIGGER_HURT":37,
   "MOD_RAILGUN":38,
   "MOD_ROCKET_SPLASH":35,
   "MOD_BFG_SPLASH":8,
   "MOD_ROCKET":25,
   "MOD_MACHINEGUN":7,
   "MOD_BFG":8,
   "MOD_FALLING":2
}
},
{
"game":13,
"totalKills":6,
"players":[
   "Isgalamido",
   "Dono da Bola",
   "Zeh",
   "Oootsimo",
   "Chessus",
   "Assasinu Credi",
   "Mal"
],
"kills":{
   "Isgalamido":-1,
   "Dono da Bola":-1,
   "Zeh":2,
   "Oootsimo":1,
   "Chessus":0,
   "Assasinu Credi":0,
   "Mal":0
},
"deaths":{
   "Isgalamido":1,
   "Dono da Bola":2,
   "Zeh":0,
   "Oootsimo":1,
   "Chessus":0,
   "Assasinu Credi":2,
   "Mal":0
},
"weapons":{
   "MOD_TRIGGER_HURT":2,
   "MOD_ROCKET":1,
   "MOD_ROCKET_SPLASH":1,
   "MOD_BFG_SPLASH":1,
   "MOD_BFG":1
}
},
{
"game":14,
"totalKills":122,
"players":[
   "Isgalamido",
   "Dono da Bola",
   "Zeh",
   "Oootsimo",
   "Chessus",
   "Assasinu Credi",
   "Mal"
],
"kills":{
   "Isgalamido":22,
   "Dono da Bola":1,
   "Zeh":4,
   "Oootsimo":9,
   "Chessus":7,
   "Assasinu Credi":3,
   "Mal":-5
},
"deaths":{
   "Isgalamido":12,
   "Dono da Bola":25,
   "Zeh":21,
   "Oootsimo":11,
   "Chessus":14,
   "Assasinu Credi":19,
   "Mal":20
},
"weapons":{
   "MOD_RAILGUN":20,
   "MOD_TRIGGER_HURT":31,
   "MOD_ROCKET":23,
   "MOD_ROCKET_SPLASH":24,
   "MOD_MACHINEGUN":4,
   "MOD_BFG_SPLASH":10,
   "MOD_FALLING":5,
   "MOD_BFG":5
}
},
{
"game":15,
"totalKills":3,
"players":[
   "Zeh",
   "Assasinu Credi",
   "Dono da Bola",
   "Fasano Again",
   "Isgalamido",
   "Oootsimo"
],
"kills":{
   "Zeh":-3,
   "Assasinu Credi":0,
   "Dono da Bola":0,
   "Fasano Again":0,
   "Isgalamido":0,
   "Oootsimo":0
},
"deaths":{
   "Zeh":3,
   "Assasinu Credi":0,
   "Dono da Bola":0,
   "Fasano Again":0,
   "Isgalamido":0,
   "Oootsimo":0
},
"weapons":{
   "MOD_TRIGGER_HURT":3
}
},
{
"game":16,
"totalKills":0,
"players":[
   "Dono da Bola",
   "Oootsimo",
   "Isgalamido",
   "Assasinu Credi",
   "Zeh"
],
"kills":{
   "Dono da Bola":0,
   "Oootsimo":0,
   "Isgalamido":0,
   "Assasinu Credi":0,
   "Zeh":0
},
"deaths":{
   "Dono da Bola":0,
   "Oootsimo":0,
   "Isgalamido":0,
   "Assasinu Credi":0,
   "Zeh":0
},
"weapons":{

}
},
{
"game":17,
"totalKills":13,
"players":[
   "Dono da Bola",
   "Oootsimo",
   "Isgalamido",
   "Assasinu Credi",
   "Zeh",
   "UnnamedPlayer",
   "Mal"
],
"kills":{
   "Dono da Bola":-2,
   "Oootsimo":0,
   "Isgalamido":0,
   "Assasinu Credi":-3,
   "Zeh":0,
   "UnnamedPlayer":0,
   "Mal":-1
},
"deaths":{
   "Dono da Bola":2,
   "Oootsimo":3,
   "Isgalamido":1,
   "Assasinu Credi":4,
   "Zeh":2,
   "UnnamedPlayer":0,
   "Mal":1
},
"weapons":{
   "MOD_FALLING":3,
   "MOD_TRIGGER_HURT":6,
   "MOD_RAILGUN":2,
   "MOD_ROCKET_SPLASH":2
}
},
{
"game":18,
"totalKills":7,
"players":[
   "Dono da Bola",
   "Oootsimo",
   "Isgalamido",
   "Assasinu Credi",
   "Zeh",
   "Mal"
],
"kills":{
   "Dono da Bola":-1,
   "Oootsimo":0,
   "Isgalamido":1,
   "Assasinu Credi":2,
   "Zeh":2,
   "Mal":-1
},
"deaths":{
   "Dono da Bola":1,
   "Oootsimo":1,
   "Isgalamido":1,
   "Assasinu Credi":1,
   "Zeh":1,
   "Mal":2
},
"weapons":{
   "MOD_ROCKET_SPLASH":4,
   "MOD_ROCKET":1,
   "MOD_FALLING":1,
   "MOD_TRIGGER_HURT":1
}
},
{
"game":19,
"totalKills":95,
"players":[
   "Isgalamido",
   "Oootsimo",
   "Dono da Bola",
   "Assasinu Credi",
   "Zeh",
   "Mal"
],
"kills":{
   "Isgalamido":13,
   "Oootsimo":10,
   "Dono da Bola":12,
   "Assasinu Credi":8,
   "Zeh":20,
   "Mal":2
},
"deaths":{
   "Isgalamido":12,
   "Oootsimo":14,
   "Dono da Bola":15,
   "Assasinu Credi":17,
   "Zeh":18,
   "Mal":19
},
"weapons":{
   "MOD_TRIGGER_HURT":12,
   "MOD_ROCKET":27,
   "MOD_ROCKET_SPLASH":32,
   "MOD_SHOTGUN":6,
   "MOD_RAILGUN":10,
   "MOD_MACHINEGUN":7,
   "MOD_FALLING":1
}
},
{
"game":20,
"totalKills":3,
"players":[
   "Isgalamido",
   "Oootsimo",
   "Dono da Bola",
   "Assasinu Credi",
   "Zeh",
   "Mal"
],
"kills":{
   "Isgalamido":0,
   "Oootsimo":1,
   "Dono da Bola":1,
   "Assasinu Credi":0,
   "Zeh":0,
   "Mal":0
},
"deaths":{
   "Isgalamido":0,
   "Oootsimo":0,
   "Dono da Bola":1,
   "Assasinu Credi":1,
   "Zeh":1,
   "Mal":0
},
"weapons":{
   "MOD_ROCKET_SPLASH":2,
   "MOD_ROCKET":1
}
},
{
"game":21,
"totalKills":131,
"players":[
   "Isgalamido",
   "Oootsimo",
   "Dono da Bola",
   "Assasinu Credi",
   "Zeh",
   "Mal"
],
"kills":{
   "Isgalamido":17,
   "Oootsimo":21,
   "Dono da Bola":12,
   "Assasinu Credi":16,
   "Zeh":19,
   "Mal":6
},
"deaths":{
   "Isgalamido":19,
   "Oootsimo":18,
   "Dono da Bola":19,
   "Assasinu Credi":30,
   "Zeh":15,
   "Mal":30
},
"weapons":{
   "MOD_ROCKET":37,
   "MOD_TRIGGER_HURT":14,
   "MOD_RAILGUN":9,
   "MOD_ROCKET_SPLASH":60,
   "MOD_MACHINEGUN":4,
   "MOD_SHOTGUN":4,
   "MOD_FALLING":3
}
}
]
```
Or like this if formatted to XML:
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<root>
  <row>
    <game>1</game>
    <totalKills>0</totalKills>
    <players>Isgalamido</players>
    <kills>
      <Isgalamido>0</Isgalamido>
    </kills>
    <deaths>
      <Isgalamido>0</Isgalamido>
    </deaths>
    <weapons/>
  </row>
  <row>
    <game>2</game>
    <totalKills>11</totalKills>
    <players>Isgalamido</players>
    <players>Dono da Bola</players>
    <players>Mocinha</players>
    <kills>
      <Isgalamido>-7</Isgalamido>
      <Mocinha>0</Mocinha>
      <Dono_da_Bola>0</Dono_da_Bola>
    </kills>
    <deaths>
      <Isgalamido>10</Isgalamido>
      <Mocinha>1</Mocinha>
      <Dono_da_Bola>0</Dono_da_Bola>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>7</MOD_TRIGGER_HURT>
      <MOD_ROCKET_SPLASH>3</MOD_ROCKET_SPLASH>
      <MOD_FALLING>1</MOD_FALLING>
    </weapons>
  </row>
  <row>
    <game>3</game>
    <totalKills>4</totalKills>
    <players>Dono da Bola</players>
    <players>Mocinha</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <kills>
      <Mocinha>0</Mocinha>
      <Isgalamido>1</Isgalamido>
      <Zeh>-2</Zeh>
      <Dono_da_Bola>-1</Dono_da_Bola>
    </kills>
    <deaths>
      <Mocinha>1</Mocinha>
      <Isgalamido>0</Isgalamido>
      <Zeh>2</Zeh>
      <Dono_da_Bola>1</Dono_da_Bola>
    </deaths>
    <weapons>
      <MOD_ROCKET>1</MOD_ROCKET>
      <MOD_TRIGGER_HURT>2</MOD_TRIGGER_HURT>
      <MOD_FALLING>1</MOD_FALLING>
    </weapons>
  </row>
  <row>
    <game>4</game>
    <totalKills>105</totalKills>
    <players>Dono da Bola</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <players>Assasinu Credi</players>
    <kills>
      <Isgalamido>19</Isgalamido>
      <Zeh>20</Zeh>
      <Dono_da_Bola>9</Dono_da_Bola>
      <Assasinu_Credi>12</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>23</Isgalamido>
      <Zeh>27</Zeh>
      <Dono_da_Bola>31</Dono_da_Bola>
      <Assasinu_Credi>24</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>9</MOD_TRIGGER_HURT>
      <MOD_FALLING>11</MOD_FALLING>
      <MOD_ROCKET>20</MOD_ROCKET>
      <MOD_RAILGUN>8</MOD_RAILGUN>
      <MOD_ROCKET_SPLASH>51</MOD_ROCKET_SPLASH>
      <MOD_MACHINEGUN>4</MOD_MACHINEGUN>
      <MOD_SHOTGUN>2</MOD_SHOTGUN>
    </weapons>
  </row>
  <row>
    <game>5</game>
    <totalKills>14</totalKills>
    <players>Dono da Bola</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <players>Assasinu Credi</players>
    <kills>
      <Isgalamido>2</Isgalamido>
      <Zeh>1</Zeh>
      <Dono_da_Bola>0</Dono_da_Bola>
      <Assasinu_Credi>-1</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>0</Isgalamido>
      <Zeh>5</Zeh>
      <Dono_da_Bola>1</Dono_da_Bola>
      <Assasinu_Credi>8</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_ROCKET>4</MOD_ROCKET>
      <MOD_ROCKET_SPLASH>4</MOD_ROCKET_SPLASH>
      <MOD_TRIGGER_HURT>5</MOD_TRIGGER_HURT>
      <MOD_RAILGUN>1</MOD_RAILGUN>
    </weapons>
  </row>
  <row>
    <game>6</game>
    <totalKills>29</totalKills>
    <players>Fasano Again</players>
    <players>Oootsimo</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <players>Dono da Bola</players>
    <players>UnnamedPlayer</players>
    <players>Maluquinho</players>
    <players>Assasinu Credi</players>
    <players>Mal</players>
    <kills>
      <Oootsimo>8</Oootsimo>
      <Isgalamido>3</Isgalamido>
      <Zeh>7</Zeh>
      <UnnamedPlayer>0</UnnamedPlayer>
      <Maluquinho>0</Maluquinho>
      <Mal>0</Mal>
      <Fasano_Again>0</Fasano_Again>
      <Dono_da_Bola>2</Dono_da_Bola>
      <Assasinu_Credi>1</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>2</Oootsimo>
      <Isgalamido>7</Isgalamido>
      <Zeh>8</Zeh>
      <UnnamedPlayer>1</UnnamedPlayer>
      <Maluquinho>1</Maluquinho>
      <Mal>2</Mal>
      <Fasano_Again>0</Fasano_Again>
      <Dono_da_Bola>5</Dono_da_Bola>
      <Assasinu_Credi>3</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_ROCKET>5</MOD_ROCKET>
      <MOD_RAILGUN>2</MOD_RAILGUN>
      <MOD_SHOTGUN>4</MOD_SHOTGUN>
      <MOD_ROCKET_SPLASH>13</MOD_ROCKET_SPLASH>
      <MOD_TRIGGER_HURT>3</MOD_TRIGGER_HURT>
      <MOD_FALLING>1</MOD_FALLING>
      <MOD_MACHINEGUN>1</MOD_MACHINEGUN>
    </weapons>
  </row>
  <row>
    <game>7</game>
    <totalKills>130</totalKills>
    <players>Oootsimo</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <players>Dono da Bola</players>
    <players>Mal</players>
    <players>Assasinu Credi</players>
    <players>Chessus!</players>
    <players>Chessus</players>
    <kills>
      <Oootsimo>20</Oootsimo>
      <Isgalamido>14</Isgalamido>
      <Zeh>8</Zeh>
      <Mal>-3</Mal>
      <Chessus!>0</Chessus!>
      <Chessus>0</Chessus>
      <Dono_da_Bola>10</Dono_da_Bola>
      <Assasinu_Credi>19</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>19</Oootsimo>
      <Isgalamido>15</Isgalamido>
      <Zeh>21</Zeh>
      <Mal>28</Mal>
      <Chessus!>0</Chessus!>
      <Chessus>2</Chessus>
      <Dono_da_Bola>26</Dono_da_Bola>
      <Assasinu_Credi>19</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_FALLING>7</MOD_FALLING>
      <MOD_TRIGGER_HURT>20</MOD_TRIGGER_HURT>
      <MOD_ROCKET_SPLASH>49</MOD_ROCKET_SPLASH>
      <MOD_ROCKET>29</MOD_ROCKET>
      <MOD_SHOTGUN>7</MOD_SHOTGUN>
      <MOD_RAILGUN>9</MOD_RAILGUN>
      <MOD_MACHINEGUN>9</MOD_MACHINEGUN>
    </weapons>
  </row>
  <row>
    <game>8</game>
    <totalKills>89</totalKills>
    <players>Oootsimo</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <players>Dono da Bola</players>
    <players>Mal</players>
    <players>Assasinu Credi</players>
    <kills>
      <Oootsimo>15</Oootsimo>
      <Isgalamido>20</Isgalamido>
      <Zeh>12</Zeh>
      <Mal>-3</Mal>
      <Dono_da_Bola>1</Dono_da_Bola>
      <Assasinu_Credi>9</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>14</Oootsimo>
      <Isgalamido>11</Isgalamido>
      <Zeh>11</Zeh>
      <Mal>20</Mal>
      <Dono_da_Bola>16</Dono_da_Bola>
      <Assasinu_Credi>17</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>9</MOD_TRIGGER_HURT>
      <MOD_ROCKET>18</MOD_ROCKET>
      <MOD_ROCKET_SPLASH>39</MOD_ROCKET_SPLASH>
      <MOD_FALLING>6</MOD_FALLING>
      <MOD_RAILGUN>12</MOD_RAILGUN>
      <MOD_MACHINEGUN>4</MOD_MACHINEGUN>
      <MOD_SHOTGUN>1</MOD_SHOTGUN>
    </weapons>
  </row>
  <row>
    <game>9</game>
    <totalKills>67</totalKills>
    <players>Oootsimo</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <players>Dono da Bola</players>
    <players>Mal</players>
    <players>Assasinu Credi</players>
    <players>Chessus!</players>
    <players>Chessus</players>
    <kills>
      <Oootsimo>8</Oootsimo>
      <Isgalamido>1</Isgalamido>
      <Zeh>12</Zeh>
      <Mal>2</Mal>
      <Chessus!>0</Chessus!>
      <Chessus>8</Chessus>
      <Dono_da_Bola>1</Dono_da_Bola>
      <Assasinu_Credi>7</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>12</Oootsimo>
      <Isgalamido>3</Isgalamido>
      <Zeh>15</Zeh>
      <Mal>15</Mal>
      <Chessus!>0</Chessus!>
      <Chessus>3</Chessus>
      <Dono_da_Bola>5</Dono_da_Bola>
      <Assasinu_Credi>14</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>8</MOD_TRIGGER_HURT>
      <MOD_ROCKET_SPLASH>25</MOD_ROCKET_SPLASH>
      <MOD_SHOTGUN>1</MOD_SHOTGUN>
      <MOD_ROCKET>17</MOD_ROCKET>
      <MOD_MACHINEGUN>3</MOD_MACHINEGUN>
      <MOD_FALLING>3</MOD_FALLING>
      <MOD_RAILGUN>10</MOD_RAILGUN>
    </weapons>
  </row>
  <row>
    <game>10</game>
    <totalKills>60</totalKills>
    <players>Oootsimo</players>
    <players>Dono da Bola</players>
    <players>Zeh</players>
    <players>Chessus</players>
    <players>Mal</players>
    <players>Assasinu Credi</players>
    <players>Isgalamido</players>
    <kills>
      <Oootsimo>-1</Oootsimo>
      <Zeh>7</Zeh>
      <Chessus>5</Chessus>
      <Mal>1</Mal>
      <Isgalamido>5</Isgalamido>
      <Dono_da_Bola>3</Dono_da_Bola>
      <Assasinu_Credi>3</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>8</Oootsimo>
      <Zeh>5</Zeh>
      <Chessus>9</Chessus>
      <Mal>14</Mal>
      <Isgalamido>13</Isgalamido>
      <Dono_da_Bola>3</Dono_da_Bola>
      <Assasinu_Credi>8</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TELEFRAG>25</MOD_TELEFRAG>
      <MOD_TRIGGER_HURT>17</MOD_TRIGGER_HURT>
      <MOD_ROCKET>4</MOD_ROCKET>
      <MOD_ROCKET_SPLASH>1</MOD_ROCKET_SPLASH>
      <MOD_RAILGUN>7</MOD_RAILGUN>
      <MOD_BFG_SPLASH>2</MOD_BFG_SPLASH>
      <MOD_BFG>2</MOD_BFG>
      <MOD_MACHINEGUN>1</MOD_MACHINEGUN>
      <MOD_CRUSH>1</MOD_CRUSH>
    </weapons>
  </row>
  <row>
    <game>11</game>
    <totalKills>20</totalKills>
    <players>Dono da Bola</players>
    <players>Isgalamido</players>
    <players>Zeh</players>
    <players>Oootsimo</players>
    <players>Chessus</players>
    <players>Assasinu Credi</players>
    <players>UnnamedPlayer</players>
    <players>Mal</players>
    <kills>
      <Isgalamido>4</Isgalamido>
      <Zeh>0</Zeh>
      <Oootsimo>4</Oootsimo>
      <Chessus>0</Chessus>
      <UnnamedPlayer>0</UnnamedPlayer>
      <Mal>0</Mal>
      <Dono_da_Bola>-2</Dono_da_Bola>
      <Assasinu_Credi>-3</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>4</Isgalamido>
      <Zeh>2</Zeh>
      <Oootsimo>1</Oootsimo>
      <Chessus>3</Chessus>
      <UnnamedPlayer>0</UnnamedPlayer>
      <Mal>1</Mal>
      <Dono_da_Bola>5</Dono_da_Bola>
      <Assasinu_Credi>4</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>7</MOD_TRIGGER_HURT>
      <MOD_CRUSH>1</MOD_CRUSH>
      <MOD_ROCKET_SPLASH>4</MOD_ROCKET_SPLASH>
      <MOD_BFG_SPLASH>3</MOD_BFG_SPLASH>
      <MOD_MACHINEGUN>1</MOD_MACHINEGUN>
      <MOD_RAILGUN>4</MOD_RAILGUN>
    </weapons>
  </row>
  <row>
    <game>12</game>
    <totalKills>160</totalKills>
    <players>Isgalamido</players>
    <players>Dono da Bola</players>
    <players>Zeh</players>
    <players>Oootsimo</players>
    <players>Chessus</players>
    <players>Assasinu Credi</players>
    <players>Mal</players>
    <kills>
      <Isgalamido>24</Isgalamido>
      <Zeh>11</Zeh>
      <Oootsimo>12</Oootsimo>
      <Chessus>12</Chessus>
      <Mal>-7</Mal>
      <Dono_da_Bola>3</Dono_da_Bola>
      <Assasinu_Credi>18</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>21</Isgalamido>
      <Zeh>16</Zeh>
      <Oootsimo>23</Oootsimo>
      <Chessus>24</Chessus>
      <Mal>26</Mal>
      <Dono_da_Bola>31</Dono_da_Bola>
      <Assasinu_Credi>19</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>37</MOD_TRIGGER_HURT>
      <MOD_RAILGUN>38</MOD_RAILGUN>
      <MOD_ROCKET_SPLASH>35</MOD_ROCKET_SPLASH>
      <MOD_BFG_SPLASH>8</MOD_BFG_SPLASH>
      <MOD_ROCKET>25</MOD_ROCKET>
      <MOD_MACHINEGUN>7</MOD_MACHINEGUN>
      <MOD_BFG>8</MOD_BFG>
      <MOD_FALLING>2</MOD_FALLING>
    </weapons>
  </row>
  <row>
    <game>13</game>
    <totalKills>6</totalKills>
    <players>Isgalamido</players>
    <players>Dono da Bola</players>
    <players>Zeh</players>
    <players>Oootsimo</players>
    <players>Chessus</players>
    <players>Assasinu Credi</players>
    <players>Mal</players>
    <kills>
      <Isgalamido>-1</Isgalamido>
      <Zeh>2</Zeh>
      <Oootsimo>1</Oootsimo>
      <Chessus>0</Chessus>
      <Mal>0</Mal>
      <Dono_da_Bola>-1</Dono_da_Bola>
      <Assasinu_Credi>0</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>1</Isgalamido>
      <Zeh>0</Zeh>
      <Oootsimo>1</Oootsimo>
      <Chessus>0</Chessus>
      <Mal>0</Mal>
      <Dono_da_Bola>2</Dono_da_Bola>
      <Assasinu_Credi>2</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>2</MOD_TRIGGER_HURT>
      <MOD_ROCKET>1</MOD_ROCKET>
      <MOD_ROCKET_SPLASH>1</MOD_ROCKET_SPLASH>
      <MOD_BFG_SPLASH>1</MOD_BFG_SPLASH>
      <MOD_BFG>1</MOD_BFG>
    </weapons>
  </row>
  <row>
    <game>14</game>
    <totalKills>122</totalKills>
    <players>Isgalamido</players>
    <players>Dono da Bola</players>
    <players>Zeh</players>
    <players>Oootsimo</players>
    <players>Chessus</players>
    <players>Assasinu Credi</players>
    <players>Mal</players>
    <kills>
      <Isgalamido>22</Isgalamido>
      <Zeh>4</Zeh>
      <Oootsimo>9</Oootsimo>
      <Chessus>7</Chessus>
      <Mal>-5</Mal>
      <Dono_da_Bola>1</Dono_da_Bola>
      <Assasinu_Credi>3</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>12</Isgalamido>
      <Zeh>21</Zeh>
      <Oootsimo>11</Oootsimo>
      <Chessus>14</Chessus>
      <Mal>20</Mal>
      <Dono_da_Bola>25</Dono_da_Bola>
      <Assasinu_Credi>19</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_RAILGUN>20</MOD_RAILGUN>
      <MOD_TRIGGER_HURT>31</MOD_TRIGGER_HURT>
      <MOD_ROCKET>23</MOD_ROCKET>
      <MOD_ROCKET_SPLASH>24</MOD_ROCKET_SPLASH>
      <MOD_MACHINEGUN>4</MOD_MACHINEGUN>
      <MOD_BFG_SPLASH>10</MOD_BFG_SPLASH>
      <MOD_FALLING>5</MOD_FALLING>
      <MOD_BFG>5</MOD_BFG>
    </weapons>
  </row>
  <row>
    <game>15</game>
    <totalKills>3</totalKills>
    <players>Zeh</players>
    <players>Assasinu Credi</players>
    <players>Dono da Bola</players>
    <players>Fasano Again</players>
    <players>Isgalamido</players>
    <players>Oootsimo</players>
    <kills>
      <Zeh>-3</Zeh>
      <Isgalamido>0</Isgalamido>
      <Oootsimo>0</Oootsimo>
      <Assasinu_Credi>0</Assasinu_Credi>
      <Dono_da_Bola>0</Dono_da_Bola>
      <Fasano_Again>0</Fasano_Again>
    </kills>
    <deaths>
      <Zeh>3</Zeh>
      <Isgalamido>0</Isgalamido>
      <Oootsimo>0</Oootsimo>
      <Assasinu_Credi>0</Assasinu_Credi>
      <Dono_da_Bola>0</Dono_da_Bola>
      <Fasano_Again>0</Fasano_Again>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>3</MOD_TRIGGER_HURT>
    </weapons>
  </row>
  <row>
    <game>16</game>
    <totalKills>0</totalKills>
    <players>Dono da Bola</players>
    <players>Oootsimo</players>
    <players>Isgalamido</players>
    <players>Assasinu Credi</players>
    <players>Zeh</players>
    <kills>
      <Oootsimo>0</Oootsimo>
      <Isgalamido>0</Isgalamido>
      <Zeh>0</Zeh>
      <Dono_da_Bola>0</Dono_da_Bola>
      <Assasinu_Credi>0</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>0</Oootsimo>
      <Isgalamido>0</Isgalamido>
      <Zeh>0</Zeh>
      <Dono_da_Bola>0</Dono_da_Bola>
      <Assasinu_Credi>0</Assasinu_Credi>
    </deaths>
    <weapons/>
  </row>
  <row>
    <game>17</game>
    <totalKills>13</totalKills>
    <players>Dono da Bola</players>
    <players>Oootsimo</players>
    <players>Isgalamido</players>
    <players>Assasinu Credi</players>
    <players>Zeh</players>
    <players>UnnamedPlayer</players>
    <players>Mal</players>
    <kills>
      <Oootsimo>0</Oootsimo>
      <Isgalamido>0</Isgalamido>
      <Zeh>0</Zeh>
      <UnnamedPlayer>0</UnnamedPlayer>
      <Mal>-1</Mal>
      <Dono_da_Bola>-2</Dono_da_Bola>
      <Assasinu_Credi>-3</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>3</Oootsimo>
      <Isgalamido>1</Isgalamido>
      <Zeh>2</Zeh>
      <UnnamedPlayer>0</UnnamedPlayer>
      <Mal>1</Mal>
      <Dono_da_Bola>2</Dono_da_Bola>
      <Assasinu_Credi>4</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_FALLING>3</MOD_FALLING>
      <MOD_TRIGGER_HURT>6</MOD_TRIGGER_HURT>
      <MOD_RAILGUN>2</MOD_RAILGUN>
      <MOD_ROCKET_SPLASH>2</MOD_ROCKET_SPLASH>
    </weapons>
  </row>
  <row>
    <game>18</game>
    <totalKills>7</totalKills>
    <players>Dono da Bola</players>
    <players>Oootsimo</players>
    <players>Isgalamido</players>
    <players>Assasinu Credi</players>
    <players>Zeh</players>
    <players>Mal</players>
    <kills>
      <Oootsimo>0</Oootsimo>
      <Isgalamido>1</Isgalamido>
      <Zeh>2</Zeh>
      <Mal>-1</Mal>
      <Dono_da_Bola>-1</Dono_da_Bola>
      <Assasinu_Credi>2</Assasinu_Credi>
    </kills>
    <deaths>
      <Oootsimo>1</Oootsimo>
      <Isgalamido>1</Isgalamido>
      <Zeh>1</Zeh>
      <Mal>2</Mal>
      <Dono_da_Bola>1</Dono_da_Bola>
      <Assasinu_Credi>1</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_ROCKET_SPLASH>4</MOD_ROCKET_SPLASH>
      <MOD_ROCKET>1</MOD_ROCKET>
      <MOD_FALLING>1</MOD_FALLING>
      <MOD_TRIGGER_HURT>1</MOD_TRIGGER_HURT>
    </weapons>
  </row>
  <row>
    <game>19</game>
    <totalKills>95</totalKills>
    <players>Isgalamido</players>
    <players>Oootsimo</players>
    <players>Dono da Bola</players>
    <players>Assasinu Credi</players>
    <players>Zeh</players>
    <players>Mal</players>
    <kills>
      <Isgalamido>13</Isgalamido>
      <Oootsimo>10</Oootsimo>
      <Zeh>20</Zeh>
      <Mal>2</Mal>
      <Dono_da_Bola>12</Dono_da_Bola>
      <Assasinu_Credi>8</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>12</Isgalamido>
      <Oootsimo>14</Oootsimo>
      <Zeh>18</Zeh>
      <Mal>19</Mal>
      <Dono_da_Bola>15</Dono_da_Bola>
      <Assasinu_Credi>17</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_TRIGGER_HURT>12</MOD_TRIGGER_HURT>
      <MOD_ROCKET>27</MOD_ROCKET>
      <MOD_ROCKET_SPLASH>32</MOD_ROCKET_SPLASH>
      <MOD_SHOTGUN>6</MOD_SHOTGUN>
      <MOD_RAILGUN>10</MOD_RAILGUN>
      <MOD_MACHINEGUN>7</MOD_MACHINEGUN>
      <MOD_FALLING>1</MOD_FALLING>
    </weapons>
  </row>
  <row>
    <game>20</game>
    <totalKills>3</totalKills>
    <players>Isgalamido</players>
    <players>Oootsimo</players>
    <players>Dono da Bola</players>
    <players>Assasinu Credi</players>
    <players>Zeh</players>
    <players>Mal</players>
    <kills>
      <Isgalamido>0</Isgalamido>
      <Oootsimo>1</Oootsimo>
      <Zeh>0</Zeh>
      <Mal>0</Mal>
      <Dono_da_Bola>1</Dono_da_Bola>
      <Assasinu_Credi>0</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>0</Isgalamido>
      <Oootsimo>0</Oootsimo>
      <Zeh>1</Zeh>
      <Mal>0</Mal>
      <Dono_da_Bola>1</Dono_da_Bola>
      <Assasinu_Credi>1</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_ROCKET_SPLASH>2</MOD_ROCKET_SPLASH>
      <MOD_ROCKET>1</MOD_ROCKET>
    </weapons>
  </row>
  <row>
    <game>21</game>
    <totalKills>131</totalKills>
    <players>Isgalamido</players>
    <players>Oootsimo</players>
    <players>Dono da Bola</players>
    <players>Assasinu Credi</players>
    <players>Zeh</players>
    <players>Mal</players>
    <kills>
      <Isgalamido>17</Isgalamido>
      <Oootsimo>21</Oootsimo>
      <Zeh>19</Zeh>
      <Mal>6</Mal>
      <Dono_da_Bola>12</Dono_da_Bola>
      <Assasinu_Credi>16</Assasinu_Credi>
    </kills>
    <deaths>
      <Isgalamido>19</Isgalamido>
      <Oootsimo>18</Oootsimo>
      <Zeh>15</Zeh>
      <Mal>30</Mal>
      <Dono_da_Bola>19</Dono_da_Bola>
      <Assasinu_Credi>30</Assasinu_Credi>
    </deaths>
    <weapons>
      <MOD_ROCKET>37</MOD_ROCKET>
      <MOD_TRIGGER_HURT>14</MOD_TRIGGER_HURT>
      <MOD_RAILGUN>9</MOD_RAILGUN>
      <MOD_ROCKET_SPLASH>60</MOD_ROCKET_SPLASH>
      <MOD_MACHINEGUN>4</MOD_MACHINEGUN>
      <MOD_SHOTGUN>4</MOD_SHOTGUN>
      <MOD_FALLING>3</MOD_FALLING>
    </weapons>
  </row>
</root>
```
<br/><br/>
