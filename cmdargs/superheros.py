#!/usr/bin/python3

import argparse


heros =  {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, 
         "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"},
         "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

parser = argparse.ArgumentParser(description='Hero info')
parser.add_argument('superhero', type=str, help='Choose one (Flash, Batman, Superman)')
parser.add_argument('herostats', type=str, help='Choose one (strength, speed, intelligence)')
args = parser.parse_args()

#char_name = input("Which character do you want to know about? (Flash, Batman, Superman) : ")


#char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence) : ")

def get_hero_stats(char_name, char_stat):
    

    if char_name.lower() == "flash":
        stat = heros[char_name].get(char_stat)
        print(char_name.capitalize() + "'s " + char_stat + " is: " + stat)
    elif char_name.lower() == "batman":
        stat = heros[char_name].get(char_stat)
        print(char_name.capitalize() + "'s " + char_stat + " is: " + stat)
    elif char_name.lower() == "superman":
        stat = heros[char_name].get(char_stat)
        print(char_name.capitalize() + "'s " + char_stat + " is: " + stat)
    else :
        print("Please provide a valid input!")


if __name__ == '__main__':
    get_hero_stats(args.superhero, args.herostats)
