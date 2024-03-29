from compiler import *
###################################################
# header_game_menus.py
# This file contains declarations for game menus
# DO NOT EDIT THIS FILE!
###################################################


#menu flags:
mnf_join_battle            = 0x00000001 #Consider this menu when the player joins a battle
mnf_auto_enter             = 0x00000010 #Automatically enter the town with the first menu option. 
mnf_enable_hot_keys        = 0x00000100 #Enables P,I,C keys
mnf_disable_all_keys       = 0x00000200 #Disables all keys
mnf_scale_picture          = 0x00001000 #Scale menu picture to offest screen aspect ratio

def menu_text_color(color):
  return color << 32
