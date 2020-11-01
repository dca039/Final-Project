from random import randint
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

##############################################################################
## CARD SECTION
class Card:
  def __init__(self,name,damage = 0,guard = 0,debuff = [], buff = [], energyuse = 0):
    self.name = name
    self.damage = damage
    self.guard = guard
    self.debuff = debuff
    self.buff = buff
    self.energyuse = energyuse
    
  
    

class FireBall(Card):
  def __init__(self):
    self.name = "FireBall"
    self.image = "fireball.jpg"
    self.damage = 20
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.energyuse = 1

class Guard(Card):
  def __init__(self):
    self.name = "Guard"
    self.image = "guard.png"
    self.damage = 0
    self.guard = 5
    self.debuff = []
    self.buff = []
    self.energyuse = 1

class Adrenaline(Card):
  def __init__(self):
    self.name = "Adrenaline"
    self.image = "stim.png"
    self.damage = 20
    self.guard = 0
    self.debuff = []
    self.buff = ["resistance","resistance","resistance"]
    self.energyuse = 1

class Lightning(Card):
  def __init__(self):
    self.name = "Lightning"
    self.image = "lightning.jpg"
    self.damage = 5
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.energyuse = 1

class IceSpear(Card):
  def __init__(self):
    self.name = "Ice Spear"
    self.image = "icespear.jpg"
    self.damage = 5
    self.guard = 0
    self.debuff = []
    self.buff = []
    self.energyuse = 1


##############################################################################
## CREATURE SECTION
class Creature():
    def __init__(self):
        self.name = None
        self.health = None
        self.guard = None
        self.status = []
        
    def heal(self,regen):
      self.health += regen
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

    def applybuff(self,target):
      # Given list off all the different status effects
      # List of status effects: resistance
      if self.status.count("resistance") > 0:
        self.resistance()
      else:
         pass

     
        
    def resistance(self):
      self.guard += 3
      








#################################################################################
## CARD USE FUNCTION

    def carduse(self,card,target):
      addeddamage = 0
      # Apply Buffs
      target.debuff = target.status + card.debuff
      self.status = self.status + card.buff

      # Check buffs
      self.applybuff(target)
      # Apply Guard
      self.guard = self.guard + card.guard
      # Apply Damage
      damage = addeddamage + card.damage
      target.guard = target.guard - damage
      if target.guard < 1:
        stabdamage = abs(target.guard)
        target.guard = 0
      else:
        stabdamage = 0
      target.health = target.health - stabdamage
      if target.health < 0:
        target.health = 0
      # Subtract energy
      self.energy = self.energy - card.energyuse
      print(card.name)
      print("Player health")
      print(self.health)
      print("Monster health")
      print(target.health)


################################################################################
## PLAYER CLASS

class Player(Creature):
    def __init__(self,name):
        self.name = name
        self.maxhealth = 50
        self.health = 50
        self.guard = 0
        self.status = []
        self.movelist = [Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline()]
        self.gold = 0
        self.deck = [Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline(),Adrenaline()]
        self.hand = []
        self.trash = []
        self.energy = 3




################################################################################
##  MONSTER CLASSES

class Slime(Creature):
    def __init__(self):
        self.name = "Slime"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [FireBall(),Guard()]
        self.energy = 999

class Orc(Creature):
    def __init__(self):
        self.name = "Orc"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [FireBall(),Guard()]
        self.energy = 999
  
class Wolf(Creature):
    def __init__(self):
        self.name = "Wolf"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [FireBall(),Guard()]
        self.energy = 999

class Zombie(Creature):
    def __init__(self):
        self.name = "Zombie"
        self.maxhealth = 20
        self.health = 20
        self.guard = 0
        self.status = []
        self.movelist = [FireBall(),Guard()]
        self.energy = 999
        

    

        


    
    

        
######################################################################
## GAME SECTION


class Game(Frame):

  font = "Courier"
  buttonsize = 20 

  def __init__(self, master=None):
    Frame.__init__(self, master)                 
    self.master = master
    self.mapposition = 0
    self.turn = 0
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
        counter = randint(0,6)
        if counter == 0 or counter == 1 or counter == 2:
            newmap.append("weak")
        if counter == 3 and len(newmap) > 3 and newmap[-1] != "miniboss" and newmap[-2] != "miniboss":
            newmap.append("miniboss")
        if (counter == 4 or counter == 5) and len(newmap) > 2 and newmap[-1] != "rest":
            newmap.append("rest")
        if (counter == 6 and newmap[-1] != "random" and len(newmap) > 2):
          newmap.append("random")
    newmap.append("boss")
    print(newmap)
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
    startadvButton = Button(self, text = "Start Adventure", command =lambda: self.postcreatePlayer(name.get()))
    startadvButton.place(x = 150, y = 400)
    startadvButton.config(font=(Game.font,Game.buttonsize))


  def postcreatePlayer(self,name):
    P1 = Player(name)
    self.processmap(P1)

  # Function that processes the given map
  def processmap(self,player):
    self.clearscreen()
    
    position = self.mapposition
    self.mapposition += 1
    # This should take in the map list and start procceding through the map encounters
    if self.selectedmap[position] == "weak":
      self.weakencounter(player)
    elif self.selectedmap[position] == "miniboss":
      self.minibossencounter(player)
    elif self.selectedmap[position] == "boss":
      self.bossencounter(player)
    elif self.selectedmap[position] == "rest":
      self.restencounter(player)
    elif self.selectedmap[position] == "random":
      self.weakchestencounter(player)
    else:
      self.processmap(player)
    
   



#######################################################################################################
## EVENT ENCOUNTER SECTION

  def restencounter(self,player):
    player.heal(20)
    self.postencounter(player)

  def weakchestencounter(self,player):
    self.clearscreen()
    background = Image.open("chest.jpg")
    background = background.resize((600,700), Image.ANTIALIAS)
    backgroundImg =  ImageTk.PhotoImage(background)
    my_background = Label(self,image=backgroundImg)
    my_background.image = backgroundImg
    my_background.pack()
    my_background.place(x = 0, y = 0)

    chestmessage = Text(self, height=5, width=50)
    chestmessage.pack()
    chestmessage.insert(tk.END, "A chest apears in front of  you.\n A warning is written on the lid.\n Open at your own risk")
    chestmessage.place(x = 650,y = 10)
    chestmessage.config(font = (Game.font,Game.buttonsize))

    openButton = Button(self,text = "Open the chest. 70% chance of success", command = lambda: self.openweakchest(player))
    openButton.pack()
    openButton.config(font = (Game.font,Game.buttonsize))
    openButton.place(x = 650, y = 600)

    walkawayButton = Button(self,text = "Walk Away", command = lambda: self.postencounter(player))
    walkawayButton.pack()
    walkawayButton.config(font = (Game.font,Game.buttonsize))
    walkawayButton.place(x = 650, y = 650)
    

  def openweakchest(self,player):
    prob = randint(0,100)
    if prob < 0:
      self.lootlevel = "weak"
      self.loot(player)
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

  # Fetches a weak monster from a list
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

  # Fetches a weak monster from a list
  def getboss(self):
    bossmonsters = [Slime()]
    randomcreature = bossmonsters[randint(0,len(bossmonsters)-1)]
    return randomcreature

########################################################################################################
## COMBAT SECTION  

  # Combat function
  def setupcombat(self,monster,player):
    # Sets the deck to the player's moveset
    #player.deck = player.movelist
    player.printmovelist()
    # Player draws 5 cards and they show up on the screen
    self.drawcard(5,player)
    self.turn = 0
    self.combat(player,monster)
    

  def combat(self,player,monster):
    self.clearscreen()
    # Sets the battlefield up
    self.battlefield(player,monster)
    for i in range(0,len(player.hand)):
      card = Image.open(player.hand[i].image)
      card = card.resize((80,40), Image.ANTIALIAS)
      cardImg =  ImageTk.PhotoImage(card)
      my_card = Button(self,image=cardImg)
      my_card['command'] = lambda idx =i, binst = my_card: self.cardpress(idx,binst,player,monster)
      my_card.image = cardImg
      my_card.pack()
      my_card.place(x = (100*(i+1)), y = 400)

    endturnbutton = Button(self, text = "End Turn", command = lambda: self.endturn(player,monster))
    endturnbutton.place(x = 210, y = 510)
    endturnbutton.config(font=(Game.font,Game.buttonsize))

    if self.turn > 0:
      # Print card used
      attackmessage = Label(self,text = "{} used {}".format(monster.name,self.monsterattack.name))
      attackmessage.pack()
      attackmessage.place(x = 650,y = 600)
      attackmessage.config(font = (Game.font,Game.buttonsize))

    # Once the moster dies the player is taken to the loot screen
    if monster.health < 1:
      self.postcombat(player)

    if player.health < 1:
      self.deathscreen()
    

  def postcombat(self,player):
    player.deck = player.deck + player.hand + player.trash
    player.hand = []
    player.trash = []
    self.loot(player)
     

  def cardpress(self,idx,binst,player,monster):
    binst.destroy()
    player.carduse(player.hand[idx],monster)
    player.trash.append(player.hand[idx])
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

    player = Image.open("Hunter.jpg")
    player = player.resize((80,40), Image.ANTIALIAS)
    playerImg =  ImageTk.PhotoImage(player)
    my_player = Label(self,image=playerImg)
    my_player.image = playerImg
    my_player.pack()
    my_player.place(x = PLAYER_X, y = PLAYER_Y)
    playerhealth = Label(self,text = "{}/{}".format(op.health,op.maxhealth))
    playerhealth.place(x=PLAYER_X,y= (PLAYER_Y + 40))
    playerhealth.config(font = (Game.font,Game.buttonsize))
          

    monster = Image.open("Slime.jpg")
    monster = monster.resize((80,40), Image.ANTIALIAS)
    monsterImg =  ImageTk.PhotoImage(monster)
    my_monster = Label(self,image=monsterImg)
    my_monster.image = monsterImg
    my_monster.pack()
    my_monster.place(x = MONSTER_X, y = MONSTER_Y)
    monsterhealth = Label(self,text = "{}/{}".format(creature.health,creature.maxhealth))
    monsterhealth.place(x= MONSTER_X,y= (MONSTER_Y + 40))
    monsterhealth.config(font = (Game.font,Game.buttonsize))



  
       
  
    



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
    player.energy = 3
    # Removes Guard
    player.guard = 0

    self.turn += 1
    
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
    ailments = ["resistance"]
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
    
    
 
  # Fetches a weak monster from a list
  def getweak(self):
    weakmonsters = [Slime(),Orc(),Wolf(),Zombie()]
    randomcreature = weakmonsters[randint(0,3)]
    return randomcreature

  # Gives player loot
  def loot(self,player):
    self.clearscreen()
    lootcards = []
    # Decides what level of loot is given
    if self.lootlevel == "weak":
      weakcardlist = [FireBall(),FireBall(),FireBall()]
      # Set it equal so that the list is not messed up
      picklist = weakcardlist
    if self.lootlevel == "miniboss":
      weakcardlist = [Lightning(),Lightning(),Lightning()]
      # Set it equal so that the list is not messed up
      picklist = weakcardlist
    if self.lootlevel == "boss":
      weakcardlist = [IceSpear(),IceSpear(),IceSpear()]
      # Set it equal so that the list is not messed up
      picklist = weakcardlist
    for i in range (0,3):
      randcard = randint(0,len(picklist)-1)
      lootcards.append(picklist[randcard])
      picklist.pop(randcard)

    for i in range(0,len(lootcards)):
      card = Image.open(lootcards[i].image)
      card = card.resize((180,70), Image.ANTIALIAS)
      cardImg =  ImageTk.PhotoImage(card)
      my_card = Button(self,image=cardImg)
      my_card['command'] = lambda idx =i: self.postloot(player,lootcards[idx])
      my_card.image = cardImg
      my_card.pack()
      my_card.place(x = (200*(i+1)), y = 300)
    
    
    
    

  

  def postloot(self,player,card):
    player.deck.append(card)
    player.printmovelist()
    self.postencounter(player)
    

  def postencounter(self,player):
    self.clearscreen()
    if player.health < 1:
      self.deathscreen()
    # Show the map
    # Let the player look at deck
    # Button to continue onto the next encounter
    continueButton = Button(self, text = "Continue", command = lambda: self.processmap(player))
    continueButton.place(x = 325, y = 500)
    continueButton.config(font=(Game.font,Game.buttonsize))


  def deathscreen(self):
    self.clearscreen()
    deathmessage = Label(self,text = "YOU DIED!! GET BETTER!!")
    deathmessage.pack()
    deathmessage.place(x = 650,y = 600)
    deathmessage.config(font = (Game.font,Game.buttonsize))

    continueButton = Button(self, text = "Restart", command = lambda: self.play())
    continueButton.place(x = 325, y = 500)
    continueButton.config(font=(Game.font,Game.buttonsize))
    

  # play the game
  def play(self):
    # make the start screen
    self.init_gamewindow()


###############################################################################
#WIDTH = 1366
#HEIGHT = 768

window = Tk()
window.title("Adventure Guild")
window.geometry("1366x768")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()





