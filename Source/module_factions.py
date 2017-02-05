from compiler import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac. is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("deserters", -0.05)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game and their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),

  ("culture_1",   "{!}culture_1",  0, 0.9, [], []),
  ("culture_2",   "{!}culture_2",  0, 0.9, [], []),
  ("culture_3",   "{!}culture_3",  0, 0.9, [], []),
  ("culture_4",   "{!}culture_4",  0, 0.9, [], []),
  ("culture_5",   "{!}culture_5",  0, 0.9, [], []),
  ("culture_6",   "{!}culture_6",  0, 0.9, [], []),
  ("culture_7",   "{!}culture_7",  0, 0.9, [], []),
  ("culture_8",   "{!}culture_8",  0, 0.9, [], []),
  ("culture_9",   "{!}culture_9",  0, 0.9, [], []),
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("deserters", -0.02)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Aki Clan", 0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0xEE7744),
  ("kingdom_2",  "Arima Clan",    0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0xCCBB99),
  ("kingdom_3",  "Asari Clan", 0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0xCC99FF),
  ("kingdom_4",  "Akamatsu Clan",    0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0x33DDDD),
  ("kingdom_5",  "Akizuki Clan",  0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0x33DD33),
  ("kingdom_6",  "Amago Clan",  0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0xDDDD33),
  ("kingdom_7",  "Anegakoji Clan",  0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0xDDDD33),
  ("kingdom_8",  "Anto Clan",  0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0xDDDD33),
  ("kingdom_9",  "Asakura Clan",  0, 0.9, [("outlaws",-0.05),("deserters", -0.02)], [], 0xDDDD33),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("player_faction",-0.1)], [], 0x888888),
  ("slavers","Slavers", 0, 0.5,[("outlaws",-0.4),("deserters",-0.2),("commoners",-0.1)], []),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
]
