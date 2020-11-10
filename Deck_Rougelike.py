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
    # Sets the card's balloontip that will pop up when hovered over
    self.balloontip = None
    
  
    

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
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nUnleash a searing fireball.".format(self.name, self.damage, self.energyuse)

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
    self.balloontip = "{}\nGuard = {}\nEnergy = {}\nReady yourself with a sheild.".format(self.name, self.guard, self.energyuse)

class Adrenaline(Card):
  def __init__(self):
    self.name = "Adrenaline"
    self.image = "stim.png"
    self.damage = 1
    self.guard = 0
    self.debuff = []
    self.buff = ["Resistance"]
    self.stacks = 3
    self.energyuse = 0
    self.balloontip = "{}\nBuff = {}\nEnergy = {}\nA rush of adrenaline gives you \nmore guard the more you use energy."\
        .format(self.name, self.buff[0], self.energyuse)

  

class Lightning(Card):
  def __init__(self):
    self.name = "Lightning"
    self.image = "lightning.jpg"
    self.damage = 3
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 1
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nConjure a bolt of lightning from your fingers.".format(self.name, self.damage, self.energyuse)

class IceSpear(Card):
  def __init__(self):
    self.name = "Ice Spear"
    self.image = "icespear.jpg"
    self.damage = 3
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 1
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nSummon an ice spear and throw it with deadly accuracy.".format(self.name, self.damage, self.energyuse)

class ConjureBear(Card):
  def __init__(self):
    self.name = "Conjure Bear"
    self.image = "bear.jpg"
    self.damage = 10
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 3
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nConjure a ferocious bear to attack your foe.".format(self.name, self.damage, self.energyuse)

class MarksWoman(Card):
  def __init__(self):
    self.name = "Markswoman"
    self.image = "markswoman.jpg"
    self.damage = 5
    self.guard = 1
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 2
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nCall on a markswoman for a kill shot".format(self.name, self.damage, self.energyuse)

class Legionares(Card):
  def __init__(self):
    self.name = "Legionare"
    self.image = "legionare.jpg"
    self.damage = 0
    self.guard = 10
    self.debuff = []
    self.buff = []
    self.stacks = 0
    self.energyuse = 3
    self.balloontip = "{}\nGuard = {}\nEnergy = {}\nRoman Legionares come to your aid with their mighty shields.".format(self.name, self.guard, self.energyuse)

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
    self.energyuse = 0
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nSummon a vine to strike your for.".format(self.name, self.damage, self.energyuse)

class SwordFury(Card):
  def __init__(self):
    self.name = "Sword Fury"
    self.image = "sword.jpg"
    self.damage = 8
    self.guard = 0
    self.debuff = ["Bleeding"]
    self.buff = []
    self.stacks = 2
    self.energyuse = 3
    self.balloontip = "{}\nDamage = {}\nDebuff = {}\nEnergy = {}\nConjure two swords and attack with lightening fast speed.".format(self.name, self.damage, self.debuff[0], self.energyuse)

class PoisonArrow(Card):
  def __init__(self):
    self.name = "Poison Arrow"
    self.image = "poisonarrow.png"
    self.damage = 5
    self.guard = 0
    self.debuff = ["Poison"]
    self.buff = []
    self.stacks = 3
    self.stacks = 0
    self.energyuse = 2
    self.balloontip = "{}\nDamage = {}\nDebuff = {}\nEnergy = {}\nShoot your opponent with a poisoned arrow.".format(self.name, self.damage, self.debuff, self.energyuse)

class HealthPotion(Card):
  def __init__(self):
    self.name = "Health Potion"
    self.image = "healthpotion.jpg"
    self.damage = 0
    self.guard = 0
    self.debuff = []
    self.buff = ["Heal"]
    self.stacks = 1
    self.energyuse = 1
    self.balloontip = "{}\nBuff = {}\nEnergy = {}\nDrink a potion of healing to replenish your strength.".format(self.name, self.buff[0], self.energyuse)

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
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nSummon an avalanche of huge boulders.".format(self.name, self.damage, self.energyuse)

class LavaQuake(Card):
  def __init__(self):
    self.name = "Lava Quake"
    self.image = "lava.jpg"
    self.damage = 13
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = []
    self.energyuse = 3
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nSummon lava beneath your enemy's feet.".format(self.name, self.damage, self.energyuse)

class KnifeThrow(Card):
  def __init__(self):
    self.name = "Knife Throw"
    self.image = "knife.jpg"
    self.damage = 1
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.stacks = []
    self.energyuse = 0
    self.balloontip = "{}\nDamage = {}\nEnergy = {}\nThrow a knife.".format(self.name, self.damage, self.energyuse)

#################################################################################3
## CREATURE CARDS - These are the monster's attacks


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
        self.buff = []
        self.debuff = ['bleeding']
        self.stacks = 2
        self.energyuse = 1

class WolfPack(Card):
    def __init__(self):
        self.name = "Wolf Pack"
        self.damage = 0
        self.guard = 4
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
        self.damage = 0
        self.guard = 0
        self.debuff = ["Poison"]
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

class HeadSlam(Card):
    def __init__(self):
        self.name = "Head Slam"
        self.damage = 10
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 2

class TuskAttack(Card):
    def __init__(self):
        self.name = "Tusk Attack"
        self.damage = 5
        self.guard = 0
        self.debuff = ["Bleeding"]
        self.buff = []
        self.stacks = 2
        self.energyuse = 2

class ClawAttack(Card):
    def __init__(self):
        self.name = "Claw Attack"
        self.damage = 5
        self.guard = 0
        self.debuff = []
        self.buff = []
        self.stacks = []
        self.energyuse = 1

class Sting(Card):
    def __init__(self):
        self.name = "Sting"
        self.damage = 5
        self.guard = 0
        self.debuff = ["Poison"]
        self.buff = []
        self.stacks = 2
        self.energyuse = 1

class MasterSwordsmen(Card):
    def __init__(self):
        self.name = "Master Swordsmen"
        self.damage = 3
        self.guard = 0
        self.debuff = ["Bleeding"]
        self.buff = ["resistance"]
        self.stacks = 2
        self.energyuse = 3










##############################################################################
## ARTIFACT SECTION - These will be rewarded once at the begining of the game and once after every boss fight
## Sadly not enough time to implement

##class Artifact():
##  def __init__(self):
##    self.name = None
##    self.image = None
##    self.uses = None
##
##  def ability(self,user):
##    pass
##    
##
##
##class BalanceBraclet(Artifact):
##  def __init__(self):
##    self.name = "Balance Braclet"
##    self.image = "slime.jpg"
##    self.uses = 0
##
##  def ability(self,user):
##    if self.uses == 0:
##      user.maxenergy += 1
##      self.uses += 1
##    else:
##      pass
    

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

    
        
    

#########################################################################################
## STATUS FUNCTIONS

    # Add debuff function
    def adddebuff(self,card):
        # Debuff list to check against
        debufflist = ["Poison", "Bleeding"]
        for i in debufflist:
            # Applies debuff to target if there is one to give
            if card.debuff == i:
                # Makes sure that the debuff can only have set stacks
                while self.status.count(i) < (card.stack):
                    self.status.append(i)
            else:
                pass

    # Add buff function
    def addbuff(self,card):
        # Buff list to check against
        bufflist = ["Resistance","Heal"]
        for i in bufflist:
            # Applies buff to target if there is one to give
            if card.buff.count(i) == 1:
                # Makes sure that the buff can only have set stacks
                while self.status.count(i) < (card.stacks):
                    self.status.append(i)
            else:
                pass
        





      
    # Function that will apply user's buffs to the card use
    def applybuff(self,target):
      # Given list of all the different status effects
      # List of status effects: resistance, heal
      # If the user has an effect run the effect's function
      if self.status.count("Resistance") > 0:
        self.resistance()
      if self.status.count("Heal") > 0:
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
      # List of status effects: poison, bleeding
      # If the user has an effect run the effect's function
      if self.status.count("Poison") > 0:
        self.poison()
      if self.status.count("Bleeding") > 0:
        self.bleeding()

      else:
        pass
    # Poison function
    def poison(self):
      # Self takes 1 damage
      self.health -= 1

    # Bleeding function
    def bleeding(self):
      # Self takes 1 damage
      self.health -= 1





#################################################################################
## CARD USE FUNCTION

    # Card use function
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
      


################################################################################
## PLAYER CLASS

class Player(Creature):
    # Initializes the PLayer class
    def __init__(self,name):
        # Sets the player's name
        self.name = name
        # Sets the player's image
        self.image = "Hunter.jpg"
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
        self.deck = [Adrenaline(), Lightning(), KnifeThrow(), Lightning(), VineWhip(), Guard(), VineWhip(), Guard()]
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
        self.movelist = [Bite(),Bite(), DeadFlesh(), ZombieHoard()]
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

class WildBoar(Creature):
    def __init__(self):
        self.name = "Wild Boar"
        self.image = "boar.jpg"
        self.maxhealth = 15
        self.health = 15
        self.guard = 0
        self.status = []
        self.movelist = [HeadSlam(), HardenedSkin(), TuskAttack()]
        self.energy = 999

class GiantScoripion(Creature):
    def __init__(self):
        self.name = "Giant Scorpion"
        self.image = "scorpion.jpg"
        self.maxhealth = 15
        self.health = 15
        self.guard = 0
        self.status = []
        self.movelist = [ClawAttack(), Sting(), Bite()]
        self.energy = 999

class DarkKnight(Creature):
    def __init__(self):
        self.name = "Dark Knight"
        self.image = "darkknight.jpg"
        self.maxhealth = 45
        self.health = 45
        self.status = []
        self.movelist = [Guard(), MasterSwordsmen(), BodySlam(), SwordFury()]
        self.energy = 999

        

    

        


    
    

        
######################################################################
## GAME SECTION


class Game(Frame):

  # Sets the Game's font
  font = "Courier"
  # Sets the Game's button size
  buttonsizelarge = 20
  buttonsizemedium = 14
  buttonsizesmall = 5
  # Sets the Game's dimensions
  width = 795
  height = 412

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
    self.testmap = ["weak.jpg","miniboss.jpg","random.png","bonfire.jpg","boss.jpg"]

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

  # Background function
  def background(self,image):
    # Takes given image and sets it as the background
    background = Image.open(image)
    background = background.resize((Game.width,Game.height), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()
    
  # Creates the start screen
  def startscreen(self):
    # clear screen
    self.clearscreen()
    # Sets background
    self.background("mainmenu.jpg")
    #Make the Title Label
    start = Label(self, text = "Adventures' Guild")
    start.pack()
    # Place the Label
    start.place(x = 100,y = 125)
    # Set the font and font size
    start.config(font=("Courier", 44))

    # creating a button instance
    startButton = Button(self, text="Start Game", command =self.selectmap)
    # placing the button on my window
    startButton.place(x=315, y=300)
    # Set the font and font size
    startButton.config(font=(Game.font,Game.buttonsizelarge))

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
    # Returns the made map
    return newmap

  # Show map function
  def showmap(self,givenmap,row):
      # For each encounter in the given map print out a picture
      for i in range(0, len(givenmap)):
          # Sets the image as the given encounter
          encounter = Image.open(givenmap[i])
          encounter = encounter.resize((40, 40), Image.ANTIALIAS)
          encounterImg = ImageTk.PhotoImage(encounter)
          my_encounter = Label(self, image = encounterImg)
          my_encounter.image = encounterImg
          my_encounter.pack()
          my_encounter.place(x = (50 * (i+1)), y = row)

  # Show key popup function
  def showkeypopup(self):
      # Creates a new window
      top = Toplevel()
      # Sets the title
      top.title('Map Key')
      # Sets the geometry
      top.geometry("250x310")
      # Sets the key images
      keyimages = ["weak.jpg","miniboss.jpg","bonfire.jpg","random.png","boss.jpg"]
      # Sets the key names
      key = ["Weak Encounter","MiniBoss Encounter","Rest Encounter","Random Encounter","Boss Encounter"]
      # For every encounter make a picture and set text next to it
      for i in range(0, len(keyimages)):
          encounter = Image.open(keyimages[i])
          encounter = encounter.resize((40, 40), Image.ANTIALIAS)
          encounterImg = ImageTk.PhotoImage(encounter)
          my_encounter = Label(top, image = encounterImg)
          my_encounter.image = encounterImg
          my_encounter.pack()
          my_encounter.place(x = (0), y = (40 * (i + 1)))
          keyLabel = Label(top,text = key[i])
          keyLabel.config(font=(Game.font,10))
          keyLabel.place(x = (40), y = (8) + (40 * (i + 1)))
      # Makes close button that destroys the window
      closeButton = Button(top, text="Close", command =top.destroy)
      closeButton.place(x = 0 , y = 280)
      closeButton.config(font=(Game.font, 10))
      
  # Show key function - the same as the previous function but on the same window as the game
  def showkey(self,row):
      keyimages = ["weak.jpg","miniboss.jpg","bonfire.jpg","random.png","boss.jpg"]
      key = ["Weak Encounter","MiniBoss Encounter","Rest Encounter","Random Encounter","Boss Encounter"]
      for i in range(0, len(keyimages)):
          encounter = Image.open(keyimages[i])
          encounter = encounter.resize((40, 40), Image.ANTIALIAS)
          encounterImg = ImageTk.PhotoImage(encounter)
          my_encounter = Label(self, image = encounterImg)
          my_encounter.image = encounterImg
          my_encounter.pack()
          my_encounter.place(x = (5), y = row + (40 * (i + 1)))
          keyLabel = Label(self,text = key[i])
          keyLabel.config(font=(Game.font,10))
          keyLabel.place(x = (55), y = (row + 5) + (40 * (i + 1)))




  def selectmap(self):
    # Set variables for the columns and rows for organization
    column = 280
    row1 = 40
    row2 = 140
    row3 = 250
    row4 = 360
    
    # Clears the screen
    self.clearscreen()
    self.background("mainmenu.jpg")
    # Makes the show map buttons that take you to their respective map screen
    selectmap1Button = Button(self, text="Select Map 1")
    selectmap1Button.place(x = column , y = row1 + 41)
    selectmap1Button.config(font=(Game.font,Game.buttonsizelarge))
    selectmap1Button['command'] = lambda mapid = self.map1: self.createPlayer(mapid)
    # Print the map 1 encounter list
    self.showmap(self.map1,row1)
    selectmap2Button = Button(self, text="Select Map 2")
    selectmap2Button.place(x = column , y = row2 +41)
    selectmap2Button.config(font=(Game.font,Game.buttonsizelarge))
    selectmap2Button['command'] = lambda mapid = self.map2: self.createPlayer(mapid)
    # Print the map 2 encounter list
    self.showmap(self.map2,row2)
    selectmap3Button = Button(self, text="Select Map 3")
    selectmap3Button.place(x = column , y = row3 + 41)
    selectmap3Button.config(font=(Game.font,Game.buttonsizelarge))
    selectmap3Button['command'] = lambda mapid = self.map3: self.createPlayer(mapid)
    # Print the map 3 encounter list
    self.showmap(self.map3,row3)

    # Makes a test map encounter that only has one of each encounter
    testmapButton = Button(self, text="Test Map")
    testmapButton.place(x = 650 , y = 5)
    testmapButton.config(font=(Game.font, 10))
    testmapButton['command'] = lambda mapid = self.testmap: self.createPlayer(mapid)
    # Makes the map key button that makes a popup
    mapkeyButton = Button(self, text="Map Key")
    mapkeyButton.place(x = 5 , y = 350)
    mapkeyButton.config(font=(Game.font, 10))
    mapkeyButton['command'] = lambda : self.showkeypopup()
    
    
    # Makes a back button that takes you back to the start screen
    backButton = Button(self, text = "Back", command = self.startscreen)
    backButton.place(x = 350, y = row4)
    backButton.config(font=(Game.font,Game.buttonsizelarge))


  




  def createPlayer(self,chosemap):
    self.clearscreen()
    # Sets the background
    self.background("mainmenu.jpg")
    # Sets the picked map from the previos screen to the game map
    self.selectedmap = chosemap
    # Create the input that the player will use to make their name
    name = StringVar()
    playername = Entry(self, textvariable = name)
    playername.pack()
    playername.place(x = 250, y = 170)
    playername.config(font=(Game.font,Game.buttonsizelarge))
    name.set("Player")
 
    # This will start your adventure
    startadvButton = Button(self, text = "Start Adventure", command =lambda: self.postcreatePlayer(name.get()))
    startadvButton.place(x = 270, y = 250)
    startadvButton.config(font=(Game.font,Game.buttonsizelarge))
    
    # Makes a back button that takes you back to the start screen
    backButton = Button(self, text = "Back", command = self.selectmap)
    backButton.place(x = 350, y = 350)
    backButton.config(font=(Game.font,Game.buttonsizelarge))

  # Post create player function for cleanup sakes
  def postcreatePlayer(self,name):
    # Makes the Player class using the input name 
    P1 = Player(name)
    # Goes to the tip screens
    self.tipsscreen1(P1)

  # Tip screen function
  def tipsscreen1(self,op):
    self.clearscreen()
    # Sets background
    self.background("mainmenu.jpg")
    # Outputs a message to the player
    tipmessage = Label(self,text = "Travers the dungeon on a quest for the \nAdventurers' Guild and defeat the bosses \non your way to the center of the ruins. \nUse your skills to beat enemies and \nacquire new skills to beat harder \nmonsters. Also be careful you don't \nget lost on your way down.")
    tipmessage.place(x = 80,y = 10)
    tipmessage.config(font = (Game.font,Game.buttonsizelarge))
    
    # Continue button that takes you to the next tip screen
    continuebutton = Button(self, text = "Continue", command = lambda: self.tipsscreen2(op))
    continuebutton.place(x = 300, y = 340)
    continuebutton.config(font=(Game.font,Game.buttonsizelarge))
    


  # Tip screen 2 function
  def tipsscreen2(self,op):
    # Coordinates for placing labels
    PLAYER_INFO_X = 10
    PLAYER_INFO_Y = 200
    SPACING = 40
    # Clears the screen
    self.clearscreen()
    # Sets the background
    self.background("mainmenu.jpg")
    # Sets the player's image
    player = Image.open(op.image)
    player = player.resize((80,100), Image.ANTIALIAS)
    playerImg =  ImageTk.PhotoImage(player)
    my_player = Label(self,image=playerImg)
    my_player.image = playerImg
    my_player.pack()
    my_player.place(x = PLAYER_INFO_X, y = PLAYER_INFO_Y)
    # Shows player's name
    playername = Label(self,text = "{}".format(op.name))
    playername.place(x=PLAYER_INFO_X,y= (PLAYER_INFO_Y)-(4*SPACING))
    playername.config(font = (Game.font,Game.buttonsizelarge))
    # Shows the player's health
    playerhealth = Label(self,text = "HP {}/{}".format(op.health,op.maxhealth))
    playerhealth.place(x=PLAYER_INFO_X,y= (PLAYER_INFO_Y)-(3*SPACING))
    playerhealth.config(font = (Game.font,Game.buttonsizelarge))
    # Shows the player's guard
    playerguard = Label(self,text = "{} Guard".format(op.guard))
    playerguard.place(x=PLAYER_INFO_X,y= (PLAYER_INFO_Y)-(2*SPACING))
    playerguard.config(font = (Game.font,Game.buttonsizelarge))
    # Shows the player's energy
    playerenergy = Label(self,text = "{}/{} Energy".format(op.energy,op.maxenergy))
    playerenergy.place(x=PLAYER_INFO_X,y= (PLAYER_INFO_Y)-(1*SPACING))
    playerenergy.config(font = (Game.font,Game.buttonsizelarge))
    # Gives the user tips for playing the game
    playerhealthtip = Label(self,text = "<- Player's Name")
    playerhealthtip.place(x=PLAYER_INFO_X + 150,y= (PLAYER_INFO_Y)-(4*SPACING))
    playerhealthtip.config(font = (Game.font,Game.buttonsizelarge))
    playerhealthtip = Label(self,text = "<- Player's Health")
    playerhealthtip.place(x=(PLAYER_INFO_X + 150),y= (PLAYER_INFO_Y)-(3*SPACING))
    playerhealthtip.config(font = (Game.font,Game.buttonsizelarge))
    playerguard = Label(self,text = "<- Guard reduces the damage you take")
    playerguard.place(x=PLAYER_INFO_X+150,y= (PLAYER_INFO_Y)-(2*SPACING))
    playerguard.config(font = (Game.font,Game.buttonsizelarge))
    playerenergy = Label(self,text = "<- Energy is used to attack.")
    playerenergy.place(x=PLAYER_INFO_X+170,y= (PLAYER_INFO_Y)-(1*SPACING))
    playerenergy.config(font = (Game.font,Game.buttonsizelarge))
    playerenergy2 = Label(self,text = "Each attack has its \nown energy consumption")
    playerenergy2.place(x=PLAYER_INFO_X+230,y= (PLAYER_INFO_Y))
    playerenergy2.config(font = (Game.font,Game.buttonsizelarge))

    # Continue button that takes the player to the third tip screen
    continuebutton = Button(self, text = "Continue", command = lambda: self.tipsscreen3(op))
    continuebutton.place(x = 300, y = 340)
    continuebutton.config(font=(Game.font,Game.buttonsizelarge))
    



  # Tip screen 3 function
  def tipsscreen3(self,op):
    # Clears screen
    self.clearscreen()
    # Sets background
    self.background("mainmenu.jpg")
    # Sets test hand
    testhand = [Lightning(),FireBall(),KnifeThrow(),HealthPotion(),VineWhip()]
    # Prints out the test hand to show the player what their hand will look like along with its balloon tips
    for i in range(0,len(testhand)):
      card = Image.open(testhand[i].image)
      card = card.resize((100,60), Image.ANTIALIAS)
      cardImg =  ImageTk.PhotoImage(card)
      my_card = Button(self,image=cardImg)
      my_card.image = cardImg
      my_card.pack()
      my_card.place(x = (130*(i+1))-50, y = 270)
      cardtip = Pmw.Balloon(self)
      cardtip.bind(my_card,testhand[i].balloontip)

    
    # Outputs a message to the player
    tipmessage = Label(self,text = "This is your hand. Every turn you will \ndraw new cards from your deck until it \nis empty. It will then shuffle your \ncards back into your deck from the \ndiscard pile. You use a card by clicking it. \nYou can also see more info about \nthe card by hovering over it.")
    tipmessage.place(x = 40,y = 10)
    tipmessage.config(font = (Game.font,Game.buttonsizelarge))
    
    # Continue button that will take you to the process map function
    continuebutton = Button(self, text = "Continue", command = lambda: self.processmap(op))
    continuebutton.place(x = 300, y = 340)
    continuebutton.config(font=(Game.font,Game.buttonsizelarge))

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
    background = background.resize((350,460), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()
    my_background.place(x = 0, y = 0)

    # Outputs a message to the player
    chestmessage = Label(self,text = "You come upon a \nburning fire pit. \nYou feel at peace and \nsafe near the fire.\nWeirdly there are \nprovisions of food \nand water for you \naround the fire.")
    chestmessage.place(x = 390,y = 0)
    chestmessage.config(font = (Game.font,Game.buttonsizelarge))


    # Makes a walk away button 
    restButton = Button(self,text = "Rest", command = lambda: self.postencounter(player))
    restButton.pack()
    restButton.config(font = (Game.font,Game.buttonsizelarge))
    restButton.place(x = 510, y = 300)
    
    # Heals the player
    player.heal(20)
    

  # Weak chest encounter
  def weakchestencounter(self,player):
    # Clears the screen
    self.clearscreen()
    # Sets the background
    background = Image.open("chest.jpg")
    background = background.resize((350,600), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()
    my_background.place(x = 0, y = 0)

    # Outputs a message to the player
    chestmessage = Label(self,text = "A chest apears in \nfront of you.\nA warning is written \non the lid.\nOpen at your own risk.")
    chestmessage.place(x = 390,y = 0)
    chestmessage.config(font = (Game.font,Game.buttonsizelarge))

    # Makes a open chest button with the odds of the player succeding
    openButton = Button(self,text = "Open the chest. \n50% chance of success", command = lambda: self.openweakchest(player))
    openButton.pack()
    openButton.config(font = (Game.font,Game.buttonsizelarge))
    openButton.place(x = 390, y = 250)

    # Makes a walk away button 
    walkawayButton = Button(self,text = "Walk Away", command = lambda: self.postencounter(player))
    walkawayButton.pack()
    walkawayButton.config(font = (Game.font,Game.buttonsizelarge))
    walkawayButton.place(x = 480, y = 330)
    
  # Function if the player decides to open the chest
  def openweakchest(self,player):
    # Picks a random number
    prob = randint(0,100)
    # If the number is less than 70 then the player gets miniboss level loot
    if prob < 50:
      self.lootlevel = "miniboss"
      self.loot(player)
    # If the player fails then it takes 10 damage
    else:
      player.health -= 10
      self.postencounter(player)
    
    


  # Core encounter function
  def coreencounter(self,player):
    # Clears screen
    self.clearscreen()
    # Sets background
    self.background("core.jpg")
      
    # Outputs a message to the player
    tipmessage = Label(self,text = "You have reached the core of the ruins. \nAs you look around the room all you can see \nare mountains of gold, paintings, and statues. \nThere is a button in the middle of the room. \nThere is a plack on it that says \n'Press to Escape'. \nThere seems to be more gold than you can \ncarry so it seems you will have to comeback \nfor more rewards.")
    tipmessage.place(x = 20,y = 10)
    tipmessage.config(font = (Game.font,Game.buttonsizelarge))
    
    # Continue button that takes the player to the start screen
    continuebutton = Button(self, text = "Press to Escape", command = lambda: self.play())
    continuebutton.place(x = 260, y = 330)
    continuebutton.config(font=(Game.font,Game.buttonsizelarge))



  # Death screen function
  def deathscreen(self):
    self.clearscreen()
    # Sets background
    self.background("death.jpg")
    # Tell the player that they died 
    deathmessage = Label(self,text = "YOU DIED!! GET BETTER!")
    deathmessage.pack()
    deathmessage.place(x = 5,y = 125)
    deathmessage.config(font = (Game.font,44))
    # Restart button
    continueButton = Button(self, text = "Restart", command = lambda: self.play())
    continueButton.place(x = 315, y = 330)
    continueButton.config(font=(Game.font,Game.buttonsizelarge))
      
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
    weakmonsters = [Wolf(), Zombie(), Slime()]
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
    minibossmonsters = [Witch(), WildBoar(), GiantScoripion()]
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
    bossmonsters = [DarkKnight(), Orc()]
    randomcreature = bossmonsters[randint(0,len(bossmonsters)-1)]
    return randomcreature

########################################################################################################
## COMBAT SECTION  

  # Combat function
  def setupcombat(self,monster,player):
    # Player draws 5 cards
    self.drawcard(5,player)
    # Sets up variables for combat
    self.turn = 0
    player.guard = 0
    player.status = []
    player.energy = player.maxenergy
    # Starts combat
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
      my_card.place(x = 60 +(90*(i+1)), y = 300)
      cardtip = Pmw.Balloon(self)
      cardtip.bind(my_card,player.hand[i].balloontip)

    # End turn button that will end the player's turn
    endturnbutton = Button(self, text = "End Turn", command = lambda: self.endturn(player,monster))
    endturnbutton.place(x = 310, y = 360)
    endturnbutton.config(font=(Game.font,Game.buttonsizelarge))

    # Outputs the monster's attack on the player
    if self.turn > 0:
      # Print card used
      attackmessage = Label(self,text = "{} \nused \n{}".format(monster.name,self.monsterattack.name))
      attackmessage.pack()
      attackmessage.place(x = 600,y = 160)
      attackmessage.config(font = (Game.font,Game.buttonsizelarge))

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
    # Coords for placing labales
    PLAYER_X = 180
    PLAYER_Y = 160
    MONSTER_X = 490
    MONSTER_Y = 160
    SPACING = 25
    
    
    # Sets the background
    self.background("cave.png")

    # Sets the player's image
    player = Image.open(op.image)
    player = player.resize((80,100), Image.ANTIALIAS)
    playerImg =  ImageTk.PhotoImage(player)
    my_player = Label(self,image=playerImg)
    my_player.image = playerImg
    my_player.pack()
    my_player.place(x = PLAYER_X, y = PLAYER_Y)
    # Shows player's name
    playername = Label(self,text = "{}".format(op.name))
    playername.place(x=PLAYER_X,y= (PLAYER_Y)-(4*SPACING))
    playername.config(font = (Game.font,Game.buttonsizemedium))
    # Shows the player's health
    playerhealth = Label(self,text = "HP {}/{}".format(op.health,op.maxhealth))
    playerhealth.place(x=PLAYER_X,y= (PLAYER_Y)-(3*SPACING))
    playerhealth.config(font = (Game.font,Game.buttonsizemedium))
    # Shows the player's guard
    playerguard = Label(self,text = "{} Guard".format(op.guard))
    playerguard.place(x=PLAYER_X,y= (PLAYER_Y)-(2*SPACING))
    playerguard.config(font = (Game.font,Game.buttonsizemedium))
    # Shows the player's guard
    playerenergy = Label(self,text = "{}/{} Energy".format(op.energy,op.maxenergy))
    playerenergy.place(x=PLAYER_X,y= (PLAYER_Y)-(1*SPACING))
    playerenergy.config(font = (Game.font,Game.buttonsizemedium))
          
    # Shows the monster's image
    monster = Image.open(creature.image)
    monster = monster.resize((80,100), Image.ANTIALIAS)
    monsterImg =  ImageTk.PhotoImage(monster)
    my_monster = Label(self,image=monsterImg)
    my_monster.image = monsterImg
    my_monster.pack()
    my_monster.place(x = MONSTER_X, y = MONSTER_Y)
    # Shows monster's name
    monstername = Label(self,text = "{}".format(creature.name))
    monstername.place(x=MONSTER_X,y= (MONSTER_Y)-(3*SPACING))
    monstername.config(font = (Game.font,Game.buttonsizemedium))
    # Shows the monster's health
    monsterhealth = Label(self,text = "HP {}/{}".format(creature.health,creature.maxhealth))
    monsterhealth.place(x= MONSTER_X,y= (MONSTER_Y)-(2*SPACING))
    monsterhealth.config(font = (Game.font,Game.buttonsizemedium))
    # SHows the monster's guard
    monsterguard = Label(self,text = "{} Guard".format(creature.guard))
    monsterguard.place(x=MONSTER_X,y= (MONSTER_Y)-(1*SPACING))
    monsterguard.config(font = (Game.font,Game.buttonsizemedium))


  
       
  
    



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
    self.background("mainmenu.jpg")
    
    # Decides what level of loot is given
    if self.lootlevel == "weak":
      cardlist = [FireBall(), IceSpear(), PoisonArrow(), HealthPotion(), SwordFury()]
      # Set it equal so that the list is not messed up
      picklist = cardlist
      self.giveloot(player,picklist)
    if self.lootlevel == "miniboss":
      cardlist = [ConjureBear(), MarksWoman(), LavaQuake(), Legionares(), Avalanche()]
      # Set it equal so that the list is not messed up
      picklist = cardlist
      self.giveloot(player,picklist)
    if self.lootlevel == "boss":
      self.coreencounter(player)

  # Give loot function
  def giveloot(self,player,picklist):
    # Makes loot cards variable
    lootcards = []
    # Picks three random cards
    for i in range (0,3):
      randcard = randint(0,len(picklist)-1)
      lootcards.append(picklist[randcard])
      picklist.pop(randcard)
    # Presents the cards to the player to take 1
    for i in range(0,len(lootcards)):
      card = Image.open(lootcards[i].image)
      card = card.resize((140,160), Image.ANTIALIAS)
      cardImg =  ImageTk.PhotoImage(card)
      my_card = Button(self,image=cardImg)
      my_card['command'] = lambda idx =i: self.postloot(player,lootcards[idx])
      my_card.image = cardImg
      my_card.pack()
      my_card.place(x = (200*(i+1)-75), y = 90)
      cardtip = Pmw.Balloon(self)
      cardtip.bind(my_card,lootcards[i].balloontip)
    # Print label
    rewardmessage = Label(self,text = "Select a Reward Card to Progress")
    rewardmessage.pack()
    rewardmessage.place(x = 150,y = 350)
    rewardmessage.config(font = (Game.font,Game.buttonsizelarge))
    
    
    
    

  
  # Post loot function for cleanup
  def postloot(self,player,card):
    # Gives the player their chosen card
    player.deck.append(card)
    self.postencounter(player)
    
  # Post encounter function for cleanup
  def postencounter(self,player):
    self.clearscreen()
    self.background("mainmenu.jpg")
    # If player is dead then go to death screen
    if player.health < 1:
      self.deathscreen()
    # Shows player's name
    playername = Label(self,text = "{}".format(player.name))
    playername.place(x=320,y= 3)
    playername.config(font = (Game.font,Game.buttonsizemedium))
    # Shows the player's health
    playerhealth = Label(self,text = "HP {}/{}".format(player.health,player.maxhealth))
    playerhealth.place(x=450,y= 3)
    playerhealth.config(font = (Game.font,Game.buttonsizemedium))
    
    # Show the map
    for i in range(0, len(self.selectedmap)):
      encounter = Image.open(self.selectedmap[i])
      encounter = encounter.resize((59, 70), Image.ANTIALIAS)
      encounterImg = ImageTk.PhotoImage(encounter)
      my_encounter = Label(self, image = encounterImg)
      my_encounter.image = encounterImg
      my_encounter.pack()
      my_encounter.place(x =(61 * (i)), y = 100)
    # Shows the players position
    for i in range(0,self.mapposition):
      position = Image.open("X.jpg")
      position = position.resize((59, 70), Image.ANTIALIAS)
      positionImg = ImageTk.PhotoImage(position)
      my_position = Label(self, image = positionImg)
      my_position.image = positionImg
      my_position.pack()
      my_position.place(x =(61 * (i)), y = 100)
    self.showkey(170)
    
    # Button to continue onto the next encounter
    continueButton = Button(self, text = "Continue", command = lambda: self.processmap(player))
    continueButton.place(x = 325, y = 300)
    continueButton.config(font=(Game.font,Game.buttonsizelarge))

  
    

  # play the game
  def play(self):
    # make the start screen
    self.init_gamewindow()


###############################################################################
WIDTH = 795
HEIGHT = 412

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





