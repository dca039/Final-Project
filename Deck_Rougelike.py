from random import randint
from tkinter import *
import tkinter as tk

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


class Slime(Creature):
    def __init__(self):
        self.name = Slime
        self.health = 20
        self.guard = 0
        self.buff = None
        self.debuff = None
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        
class Player(Creature):
    def __init__(self,name):
        self.name = name
        self.health = 50
        self.guard = 0
        self.buff = None
        self.debuff = None
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        self.gold = 0
        


    




def weakencounter():
  weakmonsters = [Slime(),Orc(),Wolf(),Zombie()]
  randomcreature = weakmonsters[randint(0,3)]
  return randomcreature
    
def miniboss():
    randomminiboss = randint(0,2)
    if randomminiboss == ogre:
        monster = Ogre()
    if randomminiboss == mimic:
        monster = Mimic()
    if randomminiboss == spectre:
        monster = Spectre()
        
        



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
    playername = Entry(self)
    playername.pack()
    playername.place(x = 250, y = 300)
    playername.config(font=(Game.font,Game.buttonsize))
    
    # This will start your adventure
    startadvButton = Button(self, text = "Start Adventure", command = self.processmap)
    startadvButton.place(x = 150, y = 400)
    startadvButton.config(font=(Game.font,Game.buttonsize))



  # Function that processes the given map
  def processmap(self,name):
    self.clearscreen()
    #selectedmap[self.mapposition]
    P1 = Player(str(name))
    print(P1)

  def weakencounter(self):
    monster = Game.getweak()


    # Monster attacks and player replenishes energy
    if player.energy < 1:
      creatureattack(monster)
    if monster.health < 1:
      Game.loot()

  def creatureattack(creature):
    randmove = randint(0,len(creature.moveset()))
    print (randmove)
    carduse(creature.moveset(randmove),creature,P1)

  def loot(self):
    # Give loot
    self.gold += 30

  def getweak(self):
    weakmonsters = [Slime(),Orc(),Wolf(),Zombie()]
    randomcreature = weakmonsters[randint(0,3)]
    return randomcreature
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





