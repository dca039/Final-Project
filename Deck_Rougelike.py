from random import randint
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import Pmw

##############################################################################
## CARD SECTION
class Card:
  # Initializes the Card class
  def __init__(self):
    # Sets the card's name
    self.name = None
    # Sets the card's damage
    self.damage = None
    # Sets the card's guard
    self.guard = None
    # Sets the card's debuffs
    self.debuff = []
    # Sets the card's buffs
    self.buff = []
    # Sets how many stacks of buffs/debuffs the card will give
    self.stacks = None
    # Sets the card's energy use
    self.energyuse = None
    
  
    

class FireBall(Card):
  def __init__(self):
    self.name = "FireBall"
    self.image = "fireball.jpg"
    self.damage = 5
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 1
    self.balloontip = "{}\nDamage = {}\nUnleash a searing fireball.".format(self.name,self.damage)

class Guard(Card):
  def __init__(self):
    self.name = "Sheild"
    self.image = "guard.png"
    self.damage = 0
    self.guard = 5
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 1
    self.balloontip = "{}\nGuard = {}\nReady yourself with a sheild.".format(self.name,self.guard)

class Adrenaline(Card):
  def __init__(self):
    self.name = "Adrenaline"
    self.image = "stim.png"
    self.damage = 5
    self.guard = 0
    self.debuff = []
    self.buff = ["Resistance"]
    self.stacks = 3
    self.energyuse = 1
    self.balloontip = "{}\nBuff = {}\nA rush of adrenaline gives you \nmore guard the more you use energy.".format(self.name,self.buff[0])

  

class Lightning(Card):
  def __init__(self):
    self.name = "Lightning"
    self.image = "lightning.jpg"
    self.damage = 4
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 1
    self.balloontip = "{}\nDamage = {}\nConjure a bolt of lightning from your fingers.".format(self.name,self.damage)

class IceSpear(Card):
  def __init__(self):
    self.name = "Ice Spear"
    self.image = "icespear.jpg"
    self.damage = 5
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 1

class ConjureBear(Card):
  def __init__(self):
    self.name = "Conjure Bear"
    self.image = "bear.jpg"
    self.damage = 10
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 2

class MarksWomn(Card):
  def __init__(self):
    self.name = "Markswoman"
    self.image = "markswoman.jpg"
    self.damage = 5
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 1

class Legionares(Card):
  def __init__(self):
    self.name = "Legionare"
    self.image = "legionare.jpg"
    self.damage = 0
    self.guard = 10
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 2

class VineWhip(Card):
  def __init__(self):
    self.name = "Vine Whip"
    self.image = "vine.jpg"
    self.damage = 1
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.energy = 0
    self.stacks = 0
    self.energyuse = 1

class SwordFury(Card):
  def __init__(self):
    self.name = "Sword Fury"
    self.image = "sword.jpg"
    self.damage = 10
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.energyuse = 2

class PoisonArrow(Card):
  def __init__(self):
    self.name = "Poison Arrow"
    self.image = "poisonarrow.jpg"
    self.damage = 5
    self.guard = 0
    self.debuff = ["poison"]
    self.buff = []
    self.stacks = 3
    self.stacks = 0
    self.energyuse = 1

class HealthPotion(Card):
  def __init__(self):
    self.name = "Health Potion"
    self.image = "healthpotion.jpg"
    self.damage = 0
    self.guard = 0
    self.debuff = []
    self.buff = ["heal"]
    self.stacks = 1
    self.energyuse = 1

class Avalanche(Card):
  def __init__(self):
    self.name = "Avalanche"
    self.image = "avalanche.jpg"
    self.damage = 10
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = []
    self.energyuse = 2

class LavaSmash(Card):
  def __init__(self):
    self.name = "Lava Smash"
    self.image = "lava.jpg"
    self.damage = 20
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = []
    self.energyuse = 3

class KnifeThrow(Card):
  def __init__(self):
    self.name = "Knife Throw"
    self.image = "knife.jpg"
    self.damage = 1
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = []
    self.energyuse = 1

#################### Creature Cards ###############################


class Bite(Card):
    def __init__(self):
        self.name = "Bite"
        self.damage = 5
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 1

class Scratch(Card):
    def __init__(self):
        self.name = "Scratch"
        self.damage = 3
        self.guard = 0
        self.debuff = ['bleeding']
        self.stacks = 2
        self.energyuse = 1

class WolfPack(Card):
    def __init__(self):
        self.name = "Wolf Pack"
        self.damage = 0
        self.guard = 3
        self.debuff = 0
        self.buff = []
        self.stacks = 3
        self.energyuse = 1

class SlimeWave(Card):
    def __init__(self):
        self.name = "Slime Wave"
        self.damage = 5
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 1

class Slippery(Card):
    def __init__(self):
        self.name = "Slip"
        self.damage = 1
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 1

class SlimeThrow():
    def __init__(self):
        self.name = "Slime Throw"
        self.damage = 3
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 1

class Slimey(Card):
    def __init__(self):
        self.name = "Slimey"
        self.damage = 0
        self.guard = 0
        self.debuff = []
        self.buff = ["restiance"]
        self.stacks = 1
        self.energyuse = 1

class ClubSmash(Card):
    def __init__(self):
        self.name = "Club Smash"
        self.damage = 10
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 2

class HardenedSkin(Card):
    def __init__(self):
        self.name = "Hardened Skin"
        self.damage = 0
        self.guard = 0
        self.debuff = []
        self.buff = ["Resistance"]
        self.stacks = 3
        self.energyuse =1

class BodySlam(Card):
    def __init__(self):
        self.name = "Body Slam"
        self.damage = 5
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 1

class DeadFlesh(Card):
    def __init__(self):
        self.name = "Dead Flesh"
        self.damage = 3
        self.guard = 0
        self.debuff = ["poison"]
        self.buff = ["Resistance"]
        self.stacks = 2
        self.energyuse = 2

class ZombieHoard(Card):
    def __init__(self):
        self.name = "Zombie Hoard"
        self.damage = 0
        self.guard = 3
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 2




















##############################################################################
## ARTIFACT SECTION - These will be rewarded once at the begining of the game and once after every boss fight

class Artifact():
  def __init__(self):
    self.name = None
    self.image = None
    self.uses = None

  def ability(self,user):
    pass
    


class BalanceBraclet(Artifact):
  def __init__(self):
    self.name = "Balance Braclet"
    self.image = "slime.jpg"
    self.uses = 0

  def ability(self,user):
    if self.uses == 0:
      user.maxenergy += 1
      self.uses += 1
    else:
      pass
    

##############################################################################
## CREATURE SECTION
class Creature():
    # Initializes the Creature class
    def __init__(self):
        # Sets the creature's name
        self.name = None
        # Sets the creature's health
        self.health = None
        # Sets the creature's guard
        self.guard = None
        # Sets the creature's status
        self.status = []

    # Function that heals the user    
    def heal(self,regen):
      # Gives the user a certain amount of health back
      self.health += regen
      # If the user heals more than their max health then cap it at the max health
      if self.health > self.maxhealth:
        self.health = self.maxhealth
      else:
        pass

    def printmovelist(self):
      mymovelist = ""
      for i in range(0,len(self.deck)):
        mymovelist = mymovelist + self.deck[i].name
      print (mymovelist)
        
    

#########################################################################################
## STATUS FUNCTIONS

    def adddebuff(self,card):
        debufflist = ["poison", "bleeding"]
        for i in debufflist:
            if card.debuff == i:
                while self.status.count(i) < (card.stack):
                    self.status.append(i)
            else:
                pass

    def addbuff(self,card):
        bufflist = ["Resistance"]

        for i in bufflist:
            if card.buff.count(i) == 1:
                while self.status.count(i) < (card.stacks):
                    self.status.append(i)
            else:
                pass
        





      
    # Function that will apply user's buffs to the card use
    def applybuff(self,target):
      # Given list off all the different status effects
      # List of status effects: resistance
      if self.status.count("Resistance") > 0:
        self.resistance()
      if self.status.count("heal") > 0:
        self.heal()
      else:
         pass

     
    # Resistance function that adds 1 guard every time a card is used
    def resistance(self):
      # Adds one guard
      self.guard += 1
      


    # Function that applies status effects at the end of turns
    def endturneffects(self):
      # Given list off all the different status effects
      # List of status effects: poison
      if self.status.count("poison") > 0:
        self.poison()
      if self.status.count("bleeding") > 0:
        self.bleeding()

      else:
        pass

    def poison(self):
      self.health -= 1

    def bleeding(self):
      self.health -= 1





#################################################################################
## CARD USE FUNCTION

    def carduse(self,card,target):
      addeddamage = 0
      # Apply Buffs
      target.adddebuff(card)
      self.addbuff(card)

      # Check buffs
      self.applybuff(target)
      # Apply Guard
      self.guard = self.guard + card.guard
      # Apply Damage
      # Adds the damage from buffs to the damage of the card
      damage = addeddamage + card.damage
      # Subtracts the guard from the damage
      target.guard = target.guard - damage
      # If the guard is less than one 
      if target.guard < 1:
        # Set the remaining damage to damage that will be inflicted
        stabdamage = abs(target.guard)
        # Sets the guard to 0
        target.guard = 0
      # If the damage does not get through the guard
      else:
        # No damage is taken
        stabdamage = 0
      # Subtracts the final damage from the target's health
      target.health = target.health - stabdamage
      # If the target's health is less than 0 set it to 0
      if target.health < 0:
        target.health = 0
      # Subtract energy
      self.energy = self.energy - card.energyuse
      print(self.status)


################################################################################
## PLAYER CLASS

class Player(Creature):
    # Initializes the PLayer class
    def __init__(self,name):
        # Sets the player's name
        self.name = name
        # Sets the player's max health
        self.maxhealth = 50
        # Sets the player's health
        self.health = 50
        # Sets the player's guard
        self.guard = 0
        # Sets the player's status
        self.status = []
        # Sets the player's gold
        self.gold = 0
        # Sets the player's deck
        self.deck = [Adrenaline(),Lightning(),Lightning(),Lightning(),Lightning(),Lightning(),Lightning()]
        # Sets the player's hand
        self.hand = []
        # Sets the player's trash
        self.trash = []
        # Sets the player's max energy
        self.maxenergy = 3
        # Sets the player's energy
        self.energy = 3




################################################################################
##  MONSTER CLASSES

class Slime(Creature):
    def __init__(self):
        self.name = "Slime"
        self.image = "Slime.jpg"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [SlimeWave(), SlimeThrow(), Slippery(), Slimey()]
        self.energy = 999


class Orc(Creature):
    def __init__(self):
        self.name = "Orc"
        self.image = "orc.jpg"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [ClubSmash(), HardenedSkin(), BodySlam()]
        self.energy = 999
  
class Wolf(Creature):
    def __init__(self):
        self.name = "Wolf"
        self.image = "wolf.jpg"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [Bite(), Scratch(), WolfPack()]
        self.energy = 999

class Zombie(Creature):
    def __init__(self):
        self.name = "Zombie"
        self.image = "zombie.jpg"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [Bite(), DeadFlesh(), ZombieHoard()]
        self.energy = 999

class Witch(Creature):
    def __init__(self):
        self.name = "Witch"
        self.image = "witch.jpg"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [FireBall(), Lightning(), HealthPotion()]
        self.energy = 999


        

    

        


    
    

        
######################################################################
## GAME SECTION


class Game(Frame):

  # Sets the Game's font
  font = "Courier"
  # Sets the Game's button size
  buttonsize = 20 

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    # Sets the Game's map position
    self.mapposition = 0
    # Sets the Game's turn number
    self.turn = 0
    # Sets the Game's map choices
    self.map1 = self.mapmaker()
    self.map2 = self.mapmaker()
    self.map3 = self.mapmaker()
    self.testmap = ["weak.jpg","miniboss.jpg","bonfire.jpg","random.png","boss.jpg"]

  #Creation of init_window
  def init_gamewindow(self):
    
    # changing the title of our master widget      
    self.master.title("GUI")

    # allowing the widget to take the full space of the window
    self.pack(fill=BOTH, expand=1)

    self.startscreen()

  # Clears the screan of widgets
  def clearscreen(self):
    for widget in Game.winfo_children(self):
      widget.destroy()

  # Creates the start screen
  def startscreen(self):
    # clear screen
    self.clearscreen()
    #Make the Title Label
    background = Image.open("Slime.jpg")
    background = background.resize((800,600), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()

    
    start = Label(self, text = "Adventures' Guild")
    start.pack()
    # Place the Label
    start.place(x = 100,y = 225)
    # Set the font and font size
    start.config(font=("Courier", 44))

    # creating a button instance
    startButton = Button(self, text="Start Game", command =self.selectmap)
    # placing the button on my window
    startButton.place(x=325, y=400)
    # Set the font and font size
    startButton.config(font=(Game.font,Game.buttonsize))

  # Function that makes the maps randomly
  def mapmaker(self):
    # Makes an empty map
    newmap = []
    
    # While the map has less than 12 encounters
    while len(newmap)<12:
        # Random number that will decide which encounter is chosen
        counter = randint(0,6)
        if counter == 0 or counter == 1 or counter == 2:
            # Adds a weak encounter
            newmap.append("weak.jpg")
        if counter == 3 and len(newmap) > 3 and newmap[-1] != "miniboss.jpg" and newmap[-2] != "miniboss.jpg":
            # Adds a miniboss encounter
            newmap.append("miniboss.jpg")
        if (counter == 4 or counter == 5) and len(newmap) > 2 and newmap[-1] != "bonfire.jpg":
            # Adds a rest encounter
            newmap.append("bonfire.jpg")
        if (counter == 6 and len(newmap) > 2 and newmap[-1] != "random.png"):
            # Adds a random encounter
            newmap.append("random.png")
    # Adds a boss fight at the end of the map
    newmap.append("boss.jpg")
    print(newmap)
    # Returns the made map
    return newmap

  def showmap(self,givenmap,row):
      for i in range(0, len(givenmap)):
          encounter = Image.open(givenmap[i])
          encounter = encounter.resize((40, 30), Image.ANTIALIAS)
          encounterImg = ImageTk.PhotoImage(encounter)
          my_encounter = Label(self, image = encounterImg)
          my_encounter.image = encounterImg
          my_encounter.pack()
          my_encounter.place(x = (50 * (i+1)), y = row)

  def showkey(self,givenmap,row):
      key = ["Weak Encounter","MiniBoss Encounter","Rest Encounter","Random Encounter","Boss Encounter"]
      for i in range(0, len(givenmap)):
          encounter = Image.open(givenmap[i])
          encounter = encounter.resize((40, 30), Image.ANTIALIAS)
          encounterImg = ImageTk.PhotoImage(encounter)
          my_encounter = Label(self, image = encounterImg)
          my_encounter.image = encounterImg
          my_encounter.pack()
          my_encounter.place(x = (50), y = row + (35 * (i + 1)))
          keyLabel = Label(self,text = key[i])
          keyLabel.config(font=(Game.font,10))
          keyLabel.place(x = (100), y = (row + 5) + (35 * (i + 1)))
          




  def selectmap(self):
    # Set variables for the columns and rows for organization
    column = 280
    row1 = 50
    row2 = 170
    row3 = 290
    row4 = 410
    
    # Clears the screen
    self.clearscreen()
    # Makes the show map buttons that take you to their respective map screen
    selectmap1Button = Button(self, text="Select Map 1")
    selectmap1Button.place(x = column , y = row1 + 30)
    selectmap1Button.config(font=(Game.font,Game.buttonsize))
    selectmap1Button['command'] = lambda mapid = self.map1: self.createPlayer(mapid)
    self.showmap(self.map1,row1)
    selectmap2Button = Button(self, text="Select Map 2")
    selectmap2Button.place(x = column , y = row2 +30)
    selectmap2Button.config(font=(Game.font,Game.buttonsize))
    selectmap2Button['command'] = lambda mapid = self.map2: self.createPlayer(mapid)
    self.showmap(self.map2,row2)
    selectmap3Button = Button(self, text="Select Map 3")
    selectmap3Button.place(x = column , y = row3 + 30)
    selectmap3Button.config(font=(Game.font,Game.buttonsize))
    selectmap3Button['command'] = lambda mapid = self.map2: self.createPlayer(mapid)
    self.showmap(self.map3,row3)

 
    testmapButton = Button(self, text="Test Map")
    testmapButton.place(x = 650 , y = 5)
    testmapButton.config(font=(Game.font, 10))
    testmapButton['command'] = lambda mapid = self.testmap: self.createPlayer(mapid)
    #Key
    self.showkey(self.testmap,350)
    
    # Makes a back button that takes you back to the start screen
    backButton = Button(self, text = "Back", command = self.startscreen)
    backButton.place(x = 330, y = row4)
    backButton.config(font=(Game.font,Game.buttonsize))


  




  def createPlayer(self,chosemap):
    self.clearscreen()
    self.selectedmap = self.testmap
    # Create the input that the player will use to make their name
    name = StringVar()
    playername = Entry(self, textvariable = name)
    playername.pack()
    playername.place(x = 250, y = 300)
    playername.config(font=(Game.font,Game.buttonsize))
    name.set("Player")
 
    # This will start your adventure
    startadvButton = Button(self, text = "Start Adventure", command =lambda: self.postcreatePlayer(name.get()))
    startadvButton.place(x = 150, y = 400)
    startadvButton.config(font=(Game.font,Game.buttonsize))


  def postcreatePlayer(self,name):
    P1 = Player(name)
    self.processmap(P1)

  # Function that processes the given map
  def processmap(self,player):
    self.clearscreen()
    # Grabs the map position
    position = self.mapposition
    # Increments it up
    self.mapposition += 1
    # Checks what encounter to run then runs it
    if self.selectedmap[position] == "weak.jpg":
      self.weakencounter(player)
    if self.selectedmap[position] == "miniboss.jpg":
      self.minibossencounter(player)
    if self.selectedmap[position] == "boss.jpg":
      self.bossencounter(player)
    if self.selectedmap[position] == "bonfire.jpg":
      self.restencounter(player)
    if self.selectedmap[position] == "random.png":
      self.weakchestencounter(player)
    
    
   



#######################################################################################################
## EVENT ENCOUNTER SECTION

  # Rest encounter function
  def restencounter(self,player):
    # Sets the background
    background = Image.open("bonfire.jpg")
    background = background.resize((600,700), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()
    my_background.place(x = 0, y = 0)

    # Outputs a message to the player
    firepitmessage = Text(self, height=5, width=50)
    firepitmessage.pack()
    firepitmessage.insert(tk.END, "You come upon a burning fire pit. You feel\nat peace and safe near the fire.\nWeirdly there are provisions of food and\nwater for you around the fire.")
    firepitmessage.place(x = 650,y = 10)
    firepitmessage.config(font = (Game.font,Game.buttonsize))

    # Makes a walk away button 
    restButton = Button(self,text = "Rest", command = lambda: self.postencounter(player))
    restButton.pack()
    restButton.config(font = (Game.font,Game.buttonsize))
    restButton.place(x = 650, y = 650)
    
    # Heals the player
    player.heal(20)
    

  # Weak chest encounter
  def weakchestencounter(self,player):
    # Clears the screen
    self.clearscreen()
    # Sets the background
    background = Image.open("chest.jpg")
    background = background.resize((600,700), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()
    my_background.place(x = 0, y = 0)

    # Outputs a message to the player
    chestmessage = Text(self, height=5, width=50)
    chestmessage.pack()
    chestmessage.insert(tk.END, "A chest apears in front of  you.\n A warning is written on the lid.\n Open at your own risk")
    chestmessage.place(x = 650,y = 10)
    chestmessage.config(font = (Game.font,Game.buttonsize))

    # Makes a open chest button with the odds of the player succeding
    openButton = Button(self,text = "Open the chest. 70% chance of success", command = lambda: self.openweakchest(player))
    openButton.pack()
    openButton.config(font = (Game.font,Game.buttonsize))
    openButton.place(x = 650, y = 600)

    # Makes a walk away button 
    walkawayButton = Button(self,text = "Walk Away", command = lambda: self.postencounter(player))
    walkawayButton.pack()
    walkawayButton.config(font = (Game.font,Game.buttonsize))
    walkawayButton.place(x = 650, y = 650)
    
  # Function if the player decides to open the chest
  def openweakchest(self,player):
    # Picks a random number
    prob = randint(0,100)
    # If the number is less than 70 then the player gets weak level loot
    if prob < 70:
      self.lootlevel = "weak"
      self.loot(player)
    # If the player fails then it takes 10 damage
    else:
      player.health -= 10
      self.postencounter(player)
    
    

########################################################################################################
## COMBAT ENCOUNTERS SECTION  

  # Weak encounter function
  def weakencounter(self,player):
    # Randomly select a weak monster from the pool
    monster = self.getweak()
    # Sets the loot given at the end of combat
    self.lootlevel = "weak"
    # Start combat with the player and monster
    self.setupcombat(monster,player)

  # Fetches a weak monster from a list
  def getweak(self):
    weakmonsters = [Wolf(),Zombie()]
    randomcreature = weakmonsters[randint(0,len(weakmonsters)-1)]
    return randomcreature

  # Weak encounter function
  def minibossencounter(self,player):
    # Randomly select a weak monster from the pool
    monster = self.getminiboss()
    # Sets the loot given at the end of combat
    self.lootlevel = "miniboss"
    # Start combat with the player and monster
    self.setupcombat(monster,player)

  # Fetches a miniboss monster from a list
  def getminiboss(self):
    minibossmonsters = [Orc()]
    randomcreature = minibossmonsters[randint(0,len(minibossmonsters)-1)]
    return randomcreature

  # Weak encounter function
  def bossencounter(self,player):
    # Randomly select a weak monster from the pool
    monster = self.getboss()
    # Sets the loot given at the end of combat
    self.lootlevel = "boss"
    # Start combat with the player and monster
    self.setupcombat(monster,player)

  # Fetches a boss monster from a list
  def getboss(self):
    bossmonsters = [Slime()]
    randomcreature = bossmonsters[randint(0,len(bossmonsters)-1)]
    return randomcreature

########################################################################################################
## COMBAT SECTION  

  # Combat function
  def setupcombat(self,monster,player):
    # Player draws 5 cards and they show up on the screen
    self.drawcard(5,player)
    self.turn = 0
    player.guard = 0
    player.status = []
    player.energy = player.maxenergy
    self.combat(player,monster)
    

  def combat(self,player,monster):
    self.clearscreen()
    # Sets the battlefield up
    self.battlefield(player,monster)
    #Shows the cards in the player's hand
    for i in range(0,len(player.hand)):
      card = Image.open(player.hand[i].image)
      card = card.resize((80,40), Image.ANTIALIAS)
      cardImg =  ImageTk.PhotoImage(card)
      my_card = Button(self,image=cardImg)
      my_card['command'] = lambda idx =i: self.cardpress(idx,player,monster)
      my_card.image = cardImg
      my_card.pack()
      my_card.place(x = (100*(i+1)), y = 400)
      cardtip = Pmw.Balloon(self)
      cardtip.bind(my_card,player.hand[i].balloontip)

    # End turn button that will end the player's turn
    endturnbutton = Button(self, text = "End Turn", command = lambda: self.endturn(player,monster))
    endturnbutton.place(x = 210, y = 510)
    endturnbutton.config(font=(Game.font,Game.buttonsize))

    # Outputs the monster's attack on the player
    if self.turn > 0:
      # Print card used
      attackmessage = Label(self,text = "{} used {}".format(monster.name,self.monsterattack.name))
      attackmessage.pack()
      attackmessage.place(x = 650,y = 600)
      attackmessage.config(font = (Game.font,Game.buttonsize))

    # Once the moster dies the player is taken to the loot screen
    if monster.health < 1:
      self.postcombat(player)

    # If the player dies it takes them to the death screen
    if player.health < 1:
      self.deathscreen()
    
  # After combat function for clean up 
  def postcombat(self,player):
    # Re-assembles the player's deck
    player.deck = player.deck + player.hand + player.trash
    # Clears the hand and trash
    player.hand = []
    player.trash = []
    # Proceed to the loot room
    self.loot(player)
     
  # Card function that will activate when a card is pressed
  def cardpress(self,idx,player,monster):
    # If player does not have enough energy then they can not use the card
    if (player.energy - player.hand[idx].energyuse) < 0:
      self.combat(player,monster)
    # If they do have enough energy
    else:
      # Player uses the card
      player.carduse(player.hand[idx],monster)
      # They move the card to the trash
      player.trash.append(player.hand[idx])
      # Removes the card from their hand
      player.hand.remove(player.hand[idx])
      self.combat(player,monster)
      

    
  def battlefield(self, op, creature):
    PLAYER_X = 150
    PLAYER_Y = 250
    MONSTER_X = 910
    MONSTER_Y = 200
    # Sets the background
    background = Image.open("cave.jpg")
    background = background.resize((1200,500), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()

    # Sets the player's image
    player = Image.open("Hunter.jpg")
    player = player.resize((80,40), Image.ANTIALIAS)
    playerImg =  ImageTk.PhotoImage(player)
    my_player = Label(self,image=playerImg)
    my_player.image = playerImg
    my_player.pack()
    my_player.place(x = PLAYER_X, y = PLAYER_Y)
    # Shows the player's health
    playerhealth = Label(self,text = "{}/{}".format(op.health,op.maxhealth))
    playerhealth.place(x=PLAYER_X,y= (PLAYER_Y + 40))
    playerhealth.config(font = (Game.font,Game.buttonsize))
    # Shows the player's guard
    playerguard = Label(self,text = "{} Guard".format(op.guard))
    playerguard.place(x=PLAYER_X,y= (PLAYER_Y + 80))
    playerguard.config(font = (Game.font,Game.buttonsize))
          
    # Shows the monster's image
    monster = Image.open("Slime.jpg")
    monster = monster.resize((80,40), Image.ANTIALIAS)
    monsterImg =  ImageTk.PhotoImage(monster)
    my_monster = Label(self,image=monsterImg)
    my_monster.image = monsterImg
    my_monster.pack()
    my_monster.place(x = MONSTER_X, y = MONSTER_Y)
    # Shows the monster's health
    monsterhealth = Label(self,text = "{}/{}".format(creature.health,creature.maxhealth))
    monsterhealth.place(x= MONSTER_X,y= (MONSTER_Y + 40))
    monsterhealth.config(font = (Game.font,Game.buttonsize))
    # SHows the monster's guard
    monsterguard = Label(self,text = "{} Guard".format(creature.guard))
    monsterguard.place(x=MONSTER_X,y= (MONSTER_Y + 80))
    monsterguard.config(font = (Game.font,Game.buttonsize))


  
       
  
    



  # Function that runs everything that happens after a round has ended
  def endturn(self,player,monster):
    # Removes monster guard
    monster.guard = 0
    self.creatureattack(monster,player)
    # Moves the remaining cards in the player's hand to the trash
    player.trash = player.trash + player.hand
    # Clears the player's hand
    player.hand = []
    # Draws 5 cards
    self.drawcard(5,player)
    # Restore the player's energy
    player.energy = player.maxenergy
    # Removes Guard
    player.guard = 0
    # Increments the turn number
    self.turn += 1
    player.endturneffects()
    monster.endturneffects()
    # status effects are removed
    self.removestats(player)
    self.removestats(monster)
    self.combat(player,monster)

  # Draw cards function
  def drawcard(self,draws,player):
    # Draw i amount of cards
    for i in range(0,draws):
      # Randomly picks a card from the player's moveset
      cardposition = randint(0,(len(player.deck)-1))
      card = player.deck[cardposition]
      # Adds it to the hand
      player.hand.append(card)
      # Removes it from the deck
      player.deck.remove(card)
      # Shows card in hand
      # If the deck runs out of cards then it will grab them from the trash, then clear the trash
      if len(player.deck) == 0:
        player.deck = player.trash 
        player.trash = []



  # Removes statuses function
  def removestats(self,creature):
    # Given list off all the different status effects
    ailments = ["Resistance"]
    for i in range(0,len(ailments)):
      # If the player has at least one of these effects subtract one from the list
      if creature.status.count(ailments[i]) > 0:
        # Remove said status
        creature.status.remove(ailments[i])
      else:
        pass

  # Creature attacks function
  def creatureattack(self,creature,player):
    # Picks a random move
    randmove = randint(0,len(creature.movelist)-1)
    
    # Uses move on player
    creature.carduse(creature.movelist[randmove],player)
    self.monsterattack = creature.movelist[randmove]
    
    

  # Gives player loot
  def loot(self,player):
    self.clearscreen()
    lootcards = []
    # Decides what level of loot is given
    if self.lootlevel == "weak":
      cardlist = [FireBall(),FireBall(),FireBall()]
      # Set it equal so that the list is not messed up
      picklist = cardlist
    if self.lootlevel == "miniboss":
      cardlist = [Lightning(),Lightning(),Lightning()]
      # Set it equal so that the list is not messed up
      picklist = cardlist
    if self.lootlevel == "boss":
      cardlist = [IceSpear(),IceSpear(),IceSpear()]
      # Set it equal so that the list is not messed up
      picklist = cardlist
    # Picks 3 cards from the list
    for i in range (0,3):
      randcard = randint(0,len(picklist)-1)
      lootcards.append(picklist[randcard])
      picklist.pop(randcard)
    # Presents the cards to the player to take 1
    for i in range(0,len(lootcards)):
      card = Image.open(lootcards[i].image)
      card = card.resize((180,70), Image.ANTIALIAS)
      cardImg =  ImageTk.PhotoImage(card)
      my_card = Button(self,image=cardImg)
      my_card['command'] = lambda idx =i: self.postloot(player,lootcards[idx])
      my_card.image = cardImg
      my_card.pack()
      my_card.place(x = (200*(i+1)), y = 300)
    
    
    
    

  
  # Post loot function for cleanup
  def postloot(self,player,card):
    # Gives the player their chosen card
    player.deck.append(card)
    self.postencounter(player)
    
  # Post encounter function for cleanup
  def postencounter(self,player):
    self.clearscreen()
    # If player is dead then go to death screen
    if player.health < 1:
      self.deathscreen()
    # Show the map
    # Let the player look at deck
    # Button to continue onto the next encounter
    continueButton = Button(self, text = "Continue", command = lambda: self.processmap(player))
    continueButton.place(x = 325, y = 500)
    continueButton.config(font=(Game.font,Game.buttonsize))

  # Death screen function
  def deathscreen(self):
    self.clearscreen()
    # Tell the player that they died 
    deathmessage = Label(self,text = "YOU DIED!! GET BETTER!!")
    deathmessage.pack()
    deathmessage.place(x = 650,y = 600)
    deathmessage.config(font = (Game.font,Game.buttonsize))
    # Restart button
    continueButton = Button(self, text = "Restart", command = lambda: self.play())
    continueButton.place(x = 325, y = 500)
    continueButton.config(font=(Game.font,Game.buttonsize))
    

  # play the game
  def play(self):
    # make the start screen
    self.init_gamewindow()


###############################################################################
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("Adventure Guild")
window.geometry("{}x{}".format(WIDTH,HEIGHT))
Pmw.initialise(window)

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()





