import random as rm
import time as t
import ppretty as ppretty

def DisplayIntro():
    print()
    print("--------𝔚𝔢𝔩𝔠𝔬𝔪𝔢 𝔱𝔬 𝔈𝔯𝔡𝔞𝔡𝔬𝔯, 𝔱𝔥𝔢 ☠ 𝕯𝖀𝕹𝕲𝕰𝕺𝕹 ☠ 𝔬𝔣 𝔱𝔥𝔢 𝔤𝔬𝔟𝔩𝔦𝔫𝔰.--------")
    t.sleep(1.5)
    print("--------ℑ𝔫 𝔬𝔯𝔡𝔢𝔯 𝔱𝔬 𝔰𝔲𝔯𝔳𝔦𝔳𝔢 𝔱𝔥𝔦𝔰 𝔥𝔢𝔩𝔩𝔦𝔰𝔥 𝔩𝔞𝔫𝔡𝔰𝔠𝔞𝔭𝔢--------")
    t.sleep(1.5)
    print("--------𝔶𝔬𝔲 𝔴𝔦𝔩𝔩 𝔫𝔢𝔢𝔡 𝔱𝔬 𝔠𝔥𝔬𝔬𝔰𝔢 𝔟𝔢𝔱𝔴𝔢𝔢𝔫 4 𝔠𝔥𝔞𝔯𝔞𝔠𝔱𝔢𝔯𝔰 𝔱𝔥𝔞𝔱 𝔠𝔞𝔫 𝔥𝔢𝔩𝔭 𝔶𝔬𝔲 𝔰𝔲𝔯𝔳𝔦𝔳𝔢--------")
    t.sleep(1.5)
    print()

Available_Characters = ["Mage", "mage", "Warrior", "warrior", "Rouge", "rouge", "Healer", "healer"]
#-----------Character classification#-----------
class Mage:             
    def __init__(self):
        self.attack = range(2,16)
        self.defense = 5
        self.health = 6
        self.ability = range(1,11)         #This ability will launch a fireball with a 8.33% of being successfull causing 25% damage of targets health
        self.ability_stats = 0.25 

class Warrior:
    def __init__(self):
        self.attack = range(6,11)
        self.defense = 8
        self.health = 10
        self.ability = range(1,11)     #This ability (called rage) will increase increase all stats by 35% with a 8.33 percentage chance of being succesfull
        self.ability_stats = 1.35

class Rouge:
    def __init__(self):    
        self.attack = range(1,17)
        self.defense = 4
        self.health = 5
        self.ability = range(1,11)     #This ability (called sneak) will decrease enemy chance of landing critical hits by 20%
        self.ability_stats = 0.20

class Healer:
    def __init__(self):
        self.attack = 8
        self.defense = 5
        self.health = 12
        self.ability = range(1,11) #This ability allows you heal 10% of your damaged health, with 8.3% chance of being successfull
        self.ability_stats = 1.10
#-----------Character classification#-----------


#-----------Enemy classification#-----------
class GoblinMinion:
    def __init__(self):    
        self.attack = rm.randint(1,6)
        self.defense = rm.randint(1,7)
        self.health = rm.randint(1,5)
        

class GoblinBoss:
    def __init__(self):
        self.attack = rm.randint(8,15)
        self.defense = rm.randint(8,11)
        self.health = rm.randint(10,50)
#-----------Enemy classification#-----------



def characterChoice():
    print("ℭ𝔥𝔬𝔬𝔰𝔢 𝔶𝔬𝔲𝔯 𝔠𝔥𝔞𝔯𝔞𝔠𝔱𝔢𝔯")
    print("♝𝔐𝔞𝔤𝔢♝\n, ♚𝔚𝔞𝔯𝔯𝔦𝔬𝔯♚\n, ♞ℜ𝔬𝔲𝔤𝔢♞\n, ♛ℌ𝔢𝔞𝔩𝔢𝔯♛\n")
    player = input(" ") 
    while player != str(Available_Characters):    #This will make sure that Player input is resevered to character selection
        global player_selection
        if player == "Mage" or "mage":
            print("These are the stats for: ♝𝔐𝔞𝔤𝔢♝")
            
            m = Mage()
            print(f"Attack DMG: {m.attack}, Defense: {m.defense}, {m.health}")
            print(f"Mage special ability(Fireball): Throw a fireball at an enemy causing {m.ability_stats} dmg of targets health")
            player_selection
            player_selection = "Mage"
            player = m
        
        if Player == "Warrior" or "warrior":
            print("These are the stats for: ♚𝔚𝔞𝔯𝔯𝔦𝔬𝔯♚")
            
            w = Warrior()
            print(f"Attack DMG: {w.attack}, Defense: {w.defense}, {w.health}")
            print(f"Warrior special ability(Rage): The ability rage will increase all stats by {w.ability_stats} %")
            player_selection
            player_selection = "Warrior"
            player = m
            
        
        if Player == "Rouge" or "rouge":
            print("These are the stats for: ♞ℜ𝔬𝔲𝔤𝔢♞")
            
            r = Rouge()
            print(f"Attack DMG: {r.attack}, Defense: {r.defense}, {r.health}")
            print(f"Rouge special ability(Sneak): {r.ability_stats} dmg of targets health")
            player_selection
            player_selection = "Rouge"
            player = r
        
        if Player == "Healer" or "healer":
            print("These are the stats for: ♛ℌ𝔢𝔞𝔩𝔢𝔯♛")
            h = Healer()
            print(f"Attack DMG: {h.attack}, Defense: {h.defense}, {h.health}")
            print(f"Healer special ability(Healing): Heal yourself by {h.ability_stats}% your damaged health")
            player_selection
            player_selection = "Healer"
            player = h
        
        



characterChoice()