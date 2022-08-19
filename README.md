# Quake Log Parser

This script extracts information of each game that is logged in the given file, given the log follows the Quake 3 Arena server log files patterns.

The output should be like the shown in the example below:

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

In order to run the script correctly, the log file must be located at the same folder as the .py script, and must be named "serverlog.log"
