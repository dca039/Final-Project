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
    def __init__(self):
        self.name = "David"
        self.health = 50
        self.guard = 0
        self.buff = None
        self.debuff = None
        self.movelist = [Card("Fireball", 2,0,"burn"),Card("Guard",0,2)]
        


    


def creatureattack(creature):
    randmove = randint(0,len(creature.moveset()))
    print (randmove)
    carduse(creature.moveset(randmove),creature,P1)

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
    


class Game(Frame):

  font = "Courier"
  buttonsize = 20 

  def __init__(self, master=None):
    Frame.__init__(self, master)                 
    self.master = master

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
    start = Label(self, text = "Adventures' Guild")
    start.pack()
    start.place(x = 100,y = 225)
    start.config(font=("Courier", 44))

    # creating a button instance
    startButton = Button(self, text="Start Game", command =self.selectmap)

    # placing the button on my window
    startButton.place(x=325, y=400)
    startButton.config(font=(Game.font,Game.buttonsize))

  def selectmap(self):
    column1 = 200
    column2 = 400
    row1 = 100
    row2 = 250
    row3 = 400
    row4 = 500
    self.clearscreen()
    selectedmap = tk.IntVar()
    map1button = Radiobutton(self,variable = selectedmap, value = 0, text = "Map 1")
    map1button.place(x = column1, y = row1)
    map1button.config(font=(Game.font,Game.buttonsize))
    map2button = Radiobutton(self,variable = selectedmap, value = 1, text = "Map 2")
    map2button.place(x = column1, y = row2)
    map2button.config(font=(Game.font,Game.buttonsize))
    map3button = Radiobutton(self,variable = selectedmap, value = 2, text = "Map 3")
    map3button.place(x = column1, y = row3)
    map3button.config(font=(Game.font,Game.buttonsize))
    showmap1Button = Button(self, text="Show Map 1")
    showmap1Button.place(x = column2 , y = row1)
    showmap1Button.config(font=(Game.font,Game.buttonsize))
    showmap2Button = Button(self, text="Show Map 2")
    showmap2Button.place(x = column2 , y = row2)
    showmap2Button.config(font=(Game.font,Game.buttonsize))
    showmap3Button = Button(self, text="Show Map 3")
    showmap3Button.place(x = column2 , y = row3)
    showmap3Button.config(font=(Game.font,Game.buttonsize))
    selectmapButton = Button(self, text = "Start Adventure")
    selectmapButton.place(x = 150, y = row4)
    selectmapButton.config(font=(Game.font,Game.buttonsize))
    backButton = Button(self, text = "Back", command = self.startscreen)
    backButton.place(x = 475, y = row4)
    backButton.config(font=(Game.font,Game.buttonsize))

  def mapscreen(self):
    self.clearscreen()
    backButton = Button(self, text = "Back", command = self.selectmap)
    backButton.place(x = 325, y = 500)
    
  def processmap(self):
    encounter = selectedmap[self.mapposition]
    if encounter == "weak":
      Game.weakencounter

  def encounter(self):
    monster = Game.weakencounter()

    # Monster attacks and player replenishes energy
    if player.energy < 1:
      pass
    if monster.health < 1:
      Game.loot()

  def loot(self):
    # Give loot
    pass

  def weakencounter(self):
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