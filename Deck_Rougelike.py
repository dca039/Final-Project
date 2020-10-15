from random import randint
from tkinter import *

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
    


class Game(Frame):
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

  def selectmap(self):
    self.clearscreen()
    map1Button = Button(self, text="Map 1")
    map1Button.place(x = 325 , y = 100)
    map2Button = Button(self, text="Map 2")
    map2Button.place(x = 325 , y = 250)
    map3Button = Button(self, text="Map 3")
    map3Button.place(x = 325 , y = 400)
    backButton = Button(self, text = "Back", command = self.startscreen)
    backButton.place(x = 325, y = 500)

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
    startButton.config(font=("Courier", 18))


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