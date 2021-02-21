import random
class Player():
    def __init__(self, name,wins=0,health=500,moves = [], damage = {}, max_damage = 0):
        Possible_Moves = ["Punch", "Sword Slice", "Knife Swing", "Earthquake","Hypnosis","Electric Bolt","Nuclear Hit", "Lightsaber Stab"]
        Move_damage = {"Punch":70, "Sword Slice":80, "Knife Swing": 100, "Earthquake":150,"Hypnosis":200,"Electric Bolt":170,"Nuclear Hit": 180, "Lightsaber Stab": 200}
        self.wins = wins
        self.health = health
        self.battle_health = self.health
        self.moves = moves
        self.damage = damage
        self.max_damage = max_damage
        self.name = name
        self.dragons = []
        if not moves:
            choice = random.sample(Possible_Moves,2)
            for i in range(2):
                self.moves.append(choice[i])
                self.max_damage+=Move_damage[choice[i]]
                self.damage[choice[i]] = Move_damage[choice[i]]
    def upgrade(self):
        upgraded = False
        """Upgrades health and damage when you have a certain amount of wins"""
        if (self.wins >= 3 and self.wins < 5):
            self.health = 600
            upgraded = True
        elif (self.wins >= 5 and self.wins < 7):
            self.health = 900
            upgraded = True
        elif (self.wins >= 7 and self.wins < 10):
            self.health = 1100
            upgraded = True
        elif (self.wins >= 10):
            self.health = 1300
            upgraded = True
        self.battle_health = self.health
        if upgraded == True:
            for i in self.moves:
                self.damage[i]+=50
            self.max_damage +=100
    def complete_maze(self):
        choice = str(input("Would you like a new dragon or upgrade on attacks: "))
        if choice.lower() == 'new dragon':
            name = str(input('What name would you like your dragon to have: '))
            power = str(input('What power do you want for your dragon: '))
            self.dragons.append(Dragon(name, power))
        elif choice.lower() == 'upgrade':
            upgrade = str(input(f'Which move would you like to upgrade [{self.moves}]: '))
            if upgrade in self.moves:
                self.damage[upgrade]+=20
                self.max_damage+=20
            else:
                print("Move not found (This is case sensitive).")


class Dragon():
    def __init__(self, name, power):
        Possible_Powers = ['Electric', 'Ice', 'Fire', 'Terra', 'Wind', 'Dark', 'Sea']
        Possible_Moves = {'Electric': ['Electric Bolt', 'Thunder Storm', 'Lightning Strike', 'Death from Above'],
                         'Ice': ['Frozen Wave', 'Frost Nova', 'Blizzard Storm', 'Snow Swords'],
                         'Fire': ['Embers', 'Flaming Hit', 'Meteor Shower', 'Raging WildFire'],
                         'Terra': ['Earthquake', 'Rock Strike', 'Asteroid Hit', 'Mud Splat'],
                         'Wind':['WhirlWind', 'Tornado', 'Foggy Mist', 'Wind Shift'],
                         'Dark':['Stealth Blast', 'Night Vision', 'Darksaber Stab', 'Night Blades'],
                         'Sea': ['WhirlPool', 'Tsunami', 'Sea Volcano', 'Ocean Blast']}
        Move_damage = {'Electric Bolt': 170, 'Thunder Storm': 170, 'Lightning Strike': 160, 'Death from Above':180,
        'Frozen Wave': 150, 'Frost Nova': 170, 'Blizzard Storm': 160, 'Snow Swords': 180,
        'Embers': 130, 'Flaming Hit': 150, 'Meteor Shower': 170, 'Raging WildFire': 180,
        'Earthquake': 160, 'Rock Strike': 150, 'Asteroid Hit': 180, 'Mud Splat': 130,
        'WhirlWind': 160, 'Tornado': 180, 'Foggy Mist': 140, 'Wind Shift': 170,
        'Stealth Blast': 170, 'Night Vision': 160, 'Darksaber Stab': 200, 'Night Blades': 180,
        'WhirlPool': 160, 'Tsunami': 180, 'Sea Volcano': 200, 'Ocean Blast': 170
        }
        self.wins = 0
        self.moves = []
        self.max_damage = 0
        self.damage = {}
        self.name = name
        self.health = 500
        self.battle_health = self.health

        if power in Possible_Powers:
            choice = random.sample(Possible_Moves[power],2)
            for i in range(2):
                self.moves.append(choice[i])
                self.max_damage+=Move_damage[choice[i]]
                self.damage[choice[i]] = Move_damage[choice[i]]
    def __str__(self):
        return (f'{self.name}: {self.damage}')
    def upgrade(self):
        """Upgrades health and damage to dragon"""
        self.health += 100
        for i in self.moves:
            self.damage[i]+=30
            self.max_damage +=60
    def toPlayer(self):
        return Player(self.name, self.wins, self.health, self.moves, self.damage, self.max_damage)