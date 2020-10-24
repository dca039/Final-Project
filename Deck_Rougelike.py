from random import randint
from tkinter import *
import tkinter as tk


##############################################################################
## CARD SECTION
class Card:
  def __init__(self,name,damage = 0,guard = 0,debuff = None, buff = None):
    self.name = name
    self.damage = damage
    self.guard = guard
    self.debuff = debuff
    self.buff = buff
    
  def __str__(self):
    return "{} , Attack = {} , Guard = {} , Buff = {} , Debuff = {}".format(self.name,self.damage,self.guard,self.buff,self.debuff)


##############################################################################
## CREATURE SECTION
class Creature():
    def __init__(self):
        self.name = None
        self.health = None
        self.guard = None
        self.buff = []
        self.debuff = []
        

    def prtmoves(self):
      return (self.movelist[0].name + " , " +self.movelist[1].name)

    def __str__(self):
        return "{}, Health = {} , Buff = {}, Debuff = {} , Moveset = {}".format(self.name,self.health,self.buff,self.debuff,self.prtmoves())

    def carduse(card,user,creature):
      damage = 0
      strengthcount = 3
      creature.debuff = card.debuff
      user.status = card.buff
      card.whenused()
      # Check buffs
      if user.buff == "strength":
          damage = card.damage + 2
      
      user.guard = user.guard + card.guard
      realdamage = damage - creature.guard
      if realdamage > 0:
          givendamage = realdamage
      else:
          givendamage = 0
      creature.health = creature.health - givendamage


class Slime(Creature):
    def __init__(self):
        self.name = Slime
        self.health = 20
        self.guard = 0
        self.buff = []
        self.debuff = []
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]

class Orc(Creature):
    def __init__(self):
        self.name = Orc
        self.health = 20
        self.guard = 0
        self.buff = []
        self.debuff = []
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
  
class Wolf(Creature):
    def __init__(self):
        self.name = Wolf
        self.health = 20
        self.guard = 0
        self.buff = []
        self.debuff = []
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]

class Zombie(Creature):
    def __init__(self):
        self.name = Zombie
        self.health = 20
        self.guard = 0
        self.buff = []
        self.debuff = []
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        
class Player(Creature):
    def __init__(self,name):
        self.name = name
        self.health = 50
        self.guard = 0
        self.buff = []
        self.debuff = []
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2),Card("Fireball", 2,0,"burn"),Card("Guard",0,2),Card("Fireball", 2,0,"burn"),Card("Guard",0,2),Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        self.gold = 0
        self.deck = []
        self.hand = []
        self.trash = []
        self.energy = 3
        


    
    
def miniboss():
    randomminiboss = randint(0,2)
    if randomminiboss == ogre:
        monster = Ogre()
    if randomminiboss == mimic:
        monster = Mimic()
    if randomminiboss == spectre:
        monster = Spectre()
        
        
######################################################################
## GAME SECTION


class Game(Frame):

  font = "Courier"
  buttonsize = 20 

  def __init__(self, master=None):
    Frame.__init__(self, master)                 
    self.master = master
    self.map1 = self.mapmaker()
    self.map2 = self.mapmaker()
    self.map3 = self.mapmaker()

    #Creation of init_window
  def init_gamewindow(self):

    # changing the title of our master widget      
    self.master.title("GUI")

    # allowing the widget to take the full space of the window
    self.pack(fill=BOTH, expand=1)

    self.startscreen()

  def clearscreen(self):
    for widget in Game.winfo_children(self):
      widget.destroy()

  def startscreen(self):
    # clear screen
    self.clearscreen()
    #create start screen
    #Make the Title Label
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

  def mapmaker(self):
    newmap =[]
    
    while len(newmap)<12:
        counter = randint(0,4)
        if counter == 0 or counter == 1 or counter == 2:
            newmap.append("weak")
        if counter == 3 and len(newmap) > 3 and newmap[-1] != "miniboss" and newmap[-2] != "miniboss":
            newmap.append("miniboss")
        if counter == 4 and len(newmap) > 2 and newmap[-1] != "rest":
            newmap.append("rest")
    newmap.append("boss")
    return newmap



  def selectmap(self):
    # Set variables for the columns and rows for organization
    column = 280
    row1 = 100
    row2 = 250
    row3 = 400
    row4 = 500
    
    # Clears the screen
    self.clearscreen()
    # Makes the show map buttons that take you to their respective map screen
    showmap1Button = Button(self, text="Show Map 1", command = self.map1screen)
    showmap1Button.place(x = column , y = row1)
    showmap1Button.config(font=(Game.font,Game.buttonsize))
    showmap2Button = Button(self, text="Show Map 2", command = self.map2screen)
    showmap2Button.place(x = column , y = row2)
    showmap2Button.config(font=(Game.font,Game.buttonsize))
    showmap3Button = Button(self, text="Show Map 3", command = self.map3screen)
    showmap3Button.place(x = column , y = row3)
    showmap3Button.config(font=(Game.font,Game.buttonsize))
    # Makes a back button that takes you back to the start screen
    backButton = Button(self, text = "Back", command = self.startscreen)
    backButton.place(x = 330, y = row4)
    backButton.config(font=(Game.font,Game.buttonsize))


  # Shows the selected map
  def map1screen(self):
    self.clearscreen()
    self.selectedmap = self.map1
    # Makes a select map button for when you select a map
    # This will start your adventure
    selectmapButton = Button(self, text = "Create Character", command = self.createPlayer)
    selectmapButton.place(x = 210, y = 410)
    selectmapButton.config(font=(Game.font,Game.buttonsize))
    backButton = Button(self, text = "Back", command = self.selectmap)
    backButton.place(x = 325, y = 500)
    backButton.config(font=(Game.font,Game.buttonsize))
    
  # Shows the selected map
  def map2screen(self):
    self.clearscreen()
    self.selectedmap = self.map2
    # Makes a select map button for when you select a map
    # This will start your adventure
    selectmapButton = Button(self, text = "Create Character", command = self.createPlayer)
    selectmapButton.place(x = 210, y = 410)
    selectmapButton.config(font=(Game.font,Game.buttonsize))
    backButton = Button(self, text = "Back", command = self.selectmap)
    backButton.place(x = 325, y = 500)
    backButton.config(font=(Game.font,Game.buttonsize))

  # Shows the selected map
  def map3screen(self):
    self.clearscreen()
    self.selectedmap = self.map3
    # Makes a select map button for when you select a map
    # This will start your adventure
    selectmapButton = Button(self, text = "Create Character", command = self.createPlayer)
    selectmapButton.place(x = 210, y = 410)
    selectmapButton.config(font=(Game.font,Game.buttonsize))
    backButton = Button(self, text = "Back", command = self.selectmap)
    backButton.place(x = 325, y = 500)
    backButton.config(font=(Game.font,Game.buttonsize))




  def createPlayer(self):
    self.clearscreen()
    # Create the input that the player will use to make their name
    name = StringVar()
    playername = Entry(self, textvariable = name)
    playername.pack()
    playername.place(x = 250, y = 300)
    playername.config(font=(Game.font,Game.buttonsize))
    name.set("Player")
 
    # This will start your adventure
    startadvButton = Button(self, text = "Start Adventure", command =lambda: self.processmap(name.get()))
    startadvButton.place(x = 150, y = 400)
    startadvButton.config(font=(Game.font,Game.buttonsize))



  # Function that processes the given map
  def processmap(self,name):
    self.clearscreen()
    # This should take in the map list and start procceding through the map encounters
    #selectedmap[self.mapposition]

    # For testing purposes this is here
    P1 = Player(name)
    print(P1)
    self.weakencounter(P1)

########################################################################################################
## COMBAT SECTION  

  # Weak encounter function
  def weakencounter(self,player):
    # Randomly select a weak monster from the pool
    monster = self.getweak()
    # Start combat with the player and monster
    self.combat(monster,player)

  # Combat function
  def combat(self,monster,player):
    # Sets the deck to the player's moveset
    player.deck = player.movelist
    # Start the combat with an empty hand and empty trash

    # Player draws 5 cards and they show up on the screen
    #cardbuttons
    self.drawcard(5,player)
    
    # Once the player runs out of energy the monster attacks and player replenishes energy
    if player.energy < 1:
      creatureattack(monster)
      self.turnend()
     
    # Once the moster dies the player is taken to the loot screen
    if monster.health < 1:
      self.loot()

  # Function that runs everything that happens after a round has ended
  def turnend(self,player):
    # Moves the remaining cards in the player's hand to the trash
    player.trash = player.trash + player.hand
    # Clears the player's hand
    player.hand = []
    # Draws 5 cards
    self.drawcard(5,player)
    # Restore the player's energy
    player.energy = 3
    # status effects are removed
    self.removestats()

  # Draw cards function
  def drawcard(self,draws,player):
    # Draw i amount of cards
    for i in range(0,draws):
      # Randomly picks a card from the player's moveset
      card = player.movelist[randint(0,(len(player.deck)-1))]
      # Adds it to the hand
      player.hand.append(card)
      # Removes it from the deck
      player.deck.remove(card)
      # If the deck runs out of cards then it will grab them from the trash, then clear the trash
      if len(player.deck) == 0:
        player.deck = player.trash 
        player.trash = []

  # Removes statuses function
  def removestats(self,player):
    # Given list off all the different status effects
    statuses = ["strength"]
    for i in range(0,len(statuses)):
      # If the player has at least one of these effects subtract one from the list
      if player.stats(statuses[i]) < 0:
        # Remove said status
        player.stats.remove(statuses[i])

  # Creature attacks function
  def creatureattack(creature):
    # Picks a random move
    randmove = randint(0,len(creature.movelist()))
    print (randmove)
    # Uses move on player
    carduse(creature.movelist(randmove),creature,P1)
 
  # Fetches a weak monster from a list
  def getweak(self):
    weakmonsters = [Slime(),Orc(),Wolf(),Zombie()]
    randomcreature = weakmonsters[randint(0,3)]
    return randomcreature

  # Gives player loot
  def loot(self):
    # Give loot
    self.gold += 30



  # play the game
  def play(self):
    # make the start screen
    self.init_gamewindow()


###############################################################################
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("Adventure Guild")
window.geometry("800x600")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()





