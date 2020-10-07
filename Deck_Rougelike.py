<<<<<<< HEAD
from random import randint

class Card:
  def __init__(self,name,damage = 0,guard = 0,debuff = None, buff = None):
    self.name = name
    self.damage = damage
    self.guard = guard
    self.debuff = debuff
    self.buff = buff
    
  def __str__(self):
    return "{} , Attack = {} , Guard = {} , Buff = {} , Debuff = {}".format(self.name,self.damage,self.guard,self.buff,self.debuff)

class Creature():
    def __init__(self,name,health,guard,buff=None,debuff=None):
        self.name = name
        self.health = health
        self.guard = guard
        self.buff = buff
        self.debuff = debuff
        

    def prtmoves(self):
      return (self.movelist[0].name + " , " +self.movelist[1].name)

    def __str__(self):
        return "{}, Health = {} , Buff = {}, Debuff = {} , Moveset = {}".format(self.name,self.health,self.buff,self.debuff,self.prtmoves())


class Slime(Creature):
    def __init__(self):
        self.name = Slime
        self.health = 20
        self.guard = 0
        self.buff = None
        self.debuff = None
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        
class Player(Creature):
    def __init__(self):
        self.name = "David"
        self.health = 50
        self.guard = 0
        self.buff = None
        self.debuff = None
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        

def carduse(card,user,creature):
    damage = 0
    strengthcount = 3
    creature.debuff = card.debuff
    user.status = card.buff
    if user.buff == "strength":
        damage = card.damage + 2
    user.guard = user.guard + card.guard
    realdamage = damage - creature.guard
    if realdamage > 0:
        givendamage = realdamage
    else:
        givendamage = 0
    creature.health = creature.health - givendamage
    
#Turns
def combat(creature):
#3 card uses
    while creature.health != 0:
        input=carduse(F1,P1,creature)
        input=carduse(G1,P1,creature)
        input=carduse(F1,P1,creature)
        creatureattack(creature)
        turnchange()

def creatureattack(creature):
    randmove = randint(0,len(creature.moveset()))
    print (randmove)
    carduse(creature.moveset(randmove),creature,P1)

def weakencounter():
    randomcreature = randint(0,3)
    if randomcreature == slime:
        monster = Slime()
    if randomcreature == orc:
        monster = Orc()
    if randomcreature == wolf:
        monster = Wolf()
    if randomcreature == zombie:
        monster = Zombie()
    
def miniboss():
    randomminiboss = randint(0,2)
    if randomminiboss == ogre:
        monster = Ogre()
    if randomminiboss == mimic:
        monster = Mimic()
    if randomminiboss == spectre:
        monster = Spectre()
        
        
def mapmaker(newmap):
    
    while len(newmap)<12:
        counter = randint(0,4)
        if counter == 0 or counter == 1 or counter == 2:
            newmap.append("weak")
        if counter == 3 and len(newmap) > 3 and newmap[-1] != "miniboss" and newmap[-2] != "miniboss":
            newmap.append("miniboss")
        if counter == 4 and len(newmap) > 2 and newmap[-1] != "rest":
            newmap.append("rest")
    newmap.append("boss")
    
        
    


P1 = Player()
print (P1)
map1 = []
map2 = []
map3 = []
mapmaker(map1)
mapmaker(map2)
=======
from random import randint

class Card:
  def __init__(self,name,damage = 0,guard = 0,debuff = None, buff = None):
    self.name = name
    self.damage = damage
    self.guard = guard
    self.debuff = debuff
    self.buff = buff
    
  def __str__(self):
    return "{} , Attack = {} , Guard = {} , Buff = {} , Debuff = {}".format(self.name,self.damage,self.guard,self.buff,self.debuff)

class Creature():
    def __init__(self,name,health,guard,buff=None,debuff=None):
        self.name = name
        self.health = health
        self.guard = guard
        self.buff = buff
        self.debuff = debuff
        

    def prtmoves(self):
      return (self.movelist[0].name + " , " +self.movelist[1].name)

    def __str__(self):
        return "{}, Health = {} , Buff = {}, Debuff = {} , Moveset = {}".format(self.name,self.health,self.buff,self.debuff,self.prtmoves())


class Slime(Creature):
    def __init__(self):
        self.name = Slime
        self.health = 20
        self.guard = 0
        self.buff = None
        self.debuff = None
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        
class Player(Creature):
    def __init__(self):
        self.name = "David"
        self.health = 50
        self.guard = 0
        self.buff = None
        self.debuff = None
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        

def carduse(card,user,creature):
    damage = 0
    strengthcount = 3
    creature.debuff = card.debuff
    user.status = card.buff
    if user.buff == "strength":
        damage = card.damage + 2
    user.guard = user.guard + card.guard
    realdamage = damage - creature.guard
    if realdamage > 0:
        givendamage = realdamage
    else:
        givendamage = 0
    creature.health = creature.health - givendamage
    
#Turns
def combat(creature):
#3 card uses
    while creature.health != 0:
        input=carduse(F1,P1,creature)
        input=carduse(G1,P1,creature)
        input=carduse(F1,P1,creature)
        creatureattack(creature)
        turnchange()

def creatureattack(creature):
    randmove = randint(0,len(creature.moveset()))
    print (randmove)
    carduse(creature.moveset(randmove),creature,P1)

def weakencounter():
    randomcreature = randint(0,3)
    if randomcreature == slime:
        monster = Slime()
    if randomcreature == orc:
        monster = Orc()
    if randomcreature == wolf:
        monster = Wolf()
    if randomcreature == zombie:
        monster = Zombie()
    
def miniboss():
    randomminiboss = randint(0,2)
    if randomminiboss == ogre:
        monster = Ogre()
    if randomminiboss == mimic:
        monster = Mimic()
    if randomminiboss == spectre:
        monster = Spectre()
        
        
def mapmaker(newmap):
    
    while len(newmap)<12:
        counter = randint(0,4)
        if counter == 0 or counter == 1 or counter == 2:
            newmap.append("weak")
        if counter == 3 and len(newmap) > 3 and newmap[-1] != "miniboss" and newmap[-2] != "miniboss":
            newmap.append("miniboss")
        if counter == 4 and len(newmap) > 2 and newmap[-1] != "rest":
            newmap.append("rest")
    newmap.append("boss")
    
        
    


P1 = Player()
print (P1)
map1 = []
map2 = []
map3 = []
mapmaker(map1)
mapmaker(map2)
>>>>>>> d45acf1a95fb3560ae33dd6f87461feced932445
mapmaker(map3)