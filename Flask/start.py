import random
from flask import Flask,render_template,Response,redirect,url_for,request
import time
import math
import multiprocessing

from flask import Flask, render_template
from werkzeug.datastructures import CallbackDict, ViewItems
from werkzeug.wrappers import ETagRequestMixin
app = Flask(__name__)
 
count=0

population=5
populationmax=5
science=1000
Workers = population
wood = 1000
WW=0
food = 1000
FW=0    
Firstclick = False
hutbutton="hidden"
woodswordbutton = "hidden"
chat=["You wake up, alone, in the middle of an unknown forest."]
Gcheck="checked"
Ccheck=""
Tcheck=""

visi="hidden"
contentt=";url=http://127.0.0.1:5000/multiprocessingg/"

WSwvis="visible"
StoSwvis="hidden"
ISwvis="hidden"
SteSwvis="hidden"
WSpvis="hidden"
StoSpvis="hidden"
ISpvis="hidden"
SteSpvis="hidden"

Weapons= ["Wooden Sword", "Stone Sword", "Iron Sword", "Steel Sword","Wooden Spear", "Stone Spear", "Iron Spear", "Steel Spear"]
WeaponVisibility=[WSwvis, StoSwvis, ISwvis, SteSwvis, WSpvis, StoSpvis, ISpvis, SteSpvis]
WoodWeaponrequirement= [50, 25, 25, 25, 100, 75, 75, 75]
WeaponIndex = 1

exploredarea = 500
Totalarea="???"
percantage="???"

replacement="visible"



MagicCrystal=0
MCdisplay="none"
TTdisplay="none"




Ressourceproductiondisplay="none"

Stonetoolsdisplay="none"
UpgradeIrontoolsdisplay="none"
Irontoolsdisplay="none"
UpgradeSteeltoolsdisplay="none"
Steeltoolsdisplay="none"

HuntingStrategiesdisplay="none"
UpgradeSpearsdisplay="none" 
Spearsdisplay="none"
UpgradeAtlatldisplay="none" 
Atlatldisplay="none"


ProductionUpgrades = ["Ressourceproduction"]
ToolsUpgrades = ["Stonetools","Irontools","Steeltools"]
FoodGatheringUpgrades = ["HuntingStrategies", "Spears", "Atlatl"]
Upgrades=["Ressourceproduction","Stonetools","Irontools","Steeltools","HuntingStrategies", "Spears", "Atlatl"]

WoodUpgraderequirement=[0,25,25,25,0,60,160]
FoodUpgraderequirement=[50,0,0,0,20,0,0]
ScienceUpgraderequirement=[25,25,50,75,10,40,100]

Health=20
lh=0
eHealth=10
elh=0
iterationcount=10
eiterationcount=10

BattleReport = "You win, you gather"
BattleWood = 1
BattleFood = 1

@app.route('/')
def index():
  if Firstclick:
    print("you are being redirected")
    return redirect(url_for('menu'))
  return render_template('index.html')

@app.route('/menu/')
def menu():
  global Firstclick
  Firstclick = True
  calculateRes(WW,FW)
  buttonenabler()
  print (wood)
  return render_template('menu.html',TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)





def buttonenabler():
  print('verifying')
  if wood>199:
    global hutbutton
    hutbutton = "visible"
  elif wood>49:
    global woodswordbutton
    woodswordbutton = "visible"
  
def calculateRes(WW, FW):
  global food
  global wood
  global count
  global population
  count += 1

  wood += (WW) 
  food += (FW)
  if count%5==0:
    if food<population & population>1:
      food=0
      population-=1
    else:
      food-=population
 
def tabcheck(t):
  if t==1:
    global Gcheck
    global Ccheck
    global Tcheck
    Gcheck="Checked"
    Ccheck=""
    Tcheck=""
    return Gcheck,Ccheck,Tcheck
  elif t==2:
    Gcheck=""
    Ccheck="Checked"
    Tcheck=""
    return Gcheck,Ccheck,Tcheck
  elif t==3:
    Gcheck=""
    Ccheck=""
    Tcheck="Checked"
    return Gcheck,Ccheck,Tcheck

def MagicCrystalaccess(x):
  global exploredarea
  global MCdisplay
  exploredarea+=x
  if exploredarea > 499 :
    if random.randint(0,20)==1:
      MCdisplay=""
      chat.insert(0,f"While searching for ressources you stumble upon a magical crystal.")
      
  return

def UpdateWeaponvisibility(x):
  global  WSwvis
  global StoSwvis
  global ISwvis
  global SteSwvis
  global WSpvis
  global StoSpvis
  global ISpvis
  global SteSpvis
  global TTdisplay

  global Stonetoolsdisplay
  global Irontoolsdisplay
  global Steeltoolsdisplay


  if x==0:
    WSwvis = "hidden"
    TTdisplay = ""
    chat.insert(0,"Seems like you're interested in upgrades. You have now access to the tech tree.")
    return
  elif x==1:
    StoSwvis = "hidden" 
    if Irontoolsdisplay=="":
      ISwvis="visible"
    return 
  elif x==2:
    ISwvis = "hidden"
    if Steeltoolsdisplay=="":
      SteSwvis="visible"
    return 
  elif x==3:
    SteSwvis = "hidden"
    return 
  elif x==4:
    WSpvis = "hidden"
    if Stonetoolsdisplay=="":
      StoSpvis="visible"
    return 
  elif x==5:
    StoSpvis = "hidden"
    if Irontoolsdisplay=="":
      ISpvis="visible"
    return 
  elif x==6:
    ISpvis = "hidden"
    if Steeltoolsdisplay=="":
      SteSpvis="visible"
    return 
  elif x==7:
    SteSpvis = "hidden"
    return

def UpdateUpgradevisibility(x):
  global Ressourceproductiondisplay

  global Stonetoolsdisplay
  global UpgradeIrontoolsdisplay
  global Irontoolsdisplay
  global UpgradeSteeltoolsdisplay
  global Steeltoolsdisplay

  global HuntingStrategiesdisplay
  global UpgradeSpearsdisplay
  global Spearsdisplay
  global UpgradeAtlatldisplay
  global Atlatldisplay

  global StoSwvis
  global ISwvis
  global SteSwvis
  global WSpvis
  global StoSpvis
  global ISpvis
  global SteSpvis
  global TTdisplay
  



  if x == 0:
    Ressourceproductiondisplay=""
  elif x==1:
    Stonetoolsdisplay=""
    UpgradeIrontoolsdisplay=""
    StoSwvis="visible"
    if Spearsdisplay=="" and WSpvis == "hidden":
      StoSpvis="visible"
  elif x==2:
    Irontoolsdisplay=""
    UpgradeSteeltoolsdisplay=""
    if StoSwvis == "hidden":
      ISwvis="visible"
    if Spearsdisplay=="" and StoSpvis == "hidden" and WSpvis == "hidden":
      ISpvis="visible" 
  elif x==3:
    Steeltoolsdisplay=""
    if ISwvis == "hidden" and StoSwvis == "hidden":
      SteSwvis="visible"
    if Spearsdisplay=="" and ISpvis == "hidden" and StoSpvis == "hidden" and WSpvis == "hidden":
      SteSpvis="visible"
  elif x==4:
    HuntingStrategiesdisplay=""
    UpgradeSpearsdisplay=""
  elif x==5:
    Spearsdisplay=""
    UpgradeAtlatldisplay=""
    WSpvis="visible"
  elif x==6:
    Atlatldisplay=""



  return













@app.route('/menu/',methods=['GET','POST'])
def update():
    
    global population
    global food
    global wood  
    global WW
    global FW
    global Workers
    global chat
    global replacement
    global Gcheck
    global Ccheck
    global Tcheck
    global  Weapons
    global WeaponVisibility
    global WoodWeaponrequirement
    global WeaponIndex
    global WSwvis
    global StoSwvis
    global ISwvis
    global SteSwvis
    global WSpvis
    global StoSpvis
    global ISpvis
    global SteSpvis
    Workers = population - FW - WW
    
    
    Gather=""
    try:

      Gather = request.form['Gather']
      tabcheck(1)
      MagicCrystalaccess(5)
      replacement="hidden"
      f= WeaponIndex *(random.randint(20,50))
      w=random.randint(20,50)
      wood = wood + w
      food = food + f
      chat.insert(0,"You gather a few sticks and berries.")
      return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
    except:
      replacement="visible"
      
    w=""
    i=-1
    for weapon in Weapons:
      try: 
        i+=1
        print(weapon)
        
        w=request.form[weapon]
        tabcheck(2)
        if wood >= WoodWeaponrequirement[i]:
          UpdateWeaponvisibility(i)
          wood=wood-WoodWeaponrequirement[i]
          print(WeaponIndex)
          WeaponIndex +=4 
          print(WeaponIndex)
          chat.insert(0,f"You have crafted a {weapon}")
        else:
          chat.insert(0,f"You don't have enough wood: {WoodWeaponrequirement[i]} wood required")
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      except:
        print("trying...")
        pass
    
    print("howdy")

    W=""
    try:
      W =request.form['+WW']
      tabcheck(2)
    except:
      pass
    try:
      W =request.form['-WW'] 
      tabcheck(2)
    except:
      pass   
    try:
      W =request.form['+FW']
      tabcheck(2)
    except:
      pass
    try:
      W =request.form['-FW']
      tabcheck(2)
    except:
      pass





  
    
    
    
    if W == "+WW":
      if Workers ==0:
        chat.insert(0,f"You do not have any free workers")
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        WW= WW + 1

        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
    elif W == "-WW":
      if WW==0:
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        WW= WW - 1
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
    elif W == "+FW":
      if Workers ==0:
        chat.insert(0,f"You do not have any free workers")
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        FW= FW + 1
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
    elif W == "-FW":
      if FW==0:
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        FW= FW - 1
        return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)


    return render_template('menu.html', TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)


 













@app.route('/disco')
def disco():
    hex = '#{:02x}{:02x}{:02x}'.format(*random.sample(range(256), 3))
    return render_template('disco.html', hex=hex)

@app.route('/crystal')
def crystal():         
  calculateRes(WW,FW)  
       
  return render_template('crystal.html')   
    
@app.route('/results')  
def results():
    calculateRes(WW,FW)
    return render_template('results.html')

def Eliminatepop():
  global population
  global Workers
  global WW
  global FW
  if Workers == 0 and population == 1:
    population = 0
    chat.insert(0, "You lose, everyone in you village is dead.")
  elif population > Workers:
    population-=1
    chat.insert(0, "You lost a brave warrior")
  elif FW == 0:
    WW -= 1
    population-=1
    chat.insert(0, "You lost a brave warrior")
  elif WW == 0:
    FW -= 1
    population -=1
    chat.insert(0, "You lost a brave warrior")
  else:
    WW -= 1
    population-=1
    chat.insert(0, "You lost a brave warrior")
  return

@app.route('/wilderness')  
def wilderness():
  global iterationcount
  global eiterationcount
  global elh
  global lh
  global BattleReport
  global BattleFood
  global BattleWood
  global population
  global food
  global wood
  print(WeaponIndex)
  calculateRes(WW,FW)
  if (eHealth/(WeaponIndex/1.5)>(Health/(1))):
    iterationcount=int(math.ceil(Health/(1)/1.5))
    eiterationcount=int(math.ceil(Health/(1)))
    lh=0
    elh=int(eHealth - Health/(1)/1.5)
    BattleReport = "You lose, you lose"
    BattleFood  = 20
    BattleWood = 10
    wood-=10
    food-=20
    Eliminatepop()
  else:
    BattleReport = "You win, you gather"
    BattleFood  = 5
    BattleWood = 1
    wood+=1
    food+=5
    iterationcount=int(math.ceil(eHealth/(WeaponIndex/1.5)/1.5))
    eiterationcount=int(math.ceil(eHealth/(WeaponIndex/1.5)))
    elh=int(eHealth - iterationcount*WeaponIndex)
    lh= int((Health - eHealth/(WeaponIndex/1.5)))

  print(WeaponIndex)
  return render_template('wilderness.html',BattleReport=BattleReport,BattleWood =BattleWood , BattleFood =BattleFood , WeaponIndex=WeaponIndex, Health=Health, eHealth=eHealth, iterationcount=iterationcount, eiterationcount=eiterationcount, lh=lh, elh=elh)

@app.route('/spaceship')  
def spaceship():
    calculateRes(WW,FW)
    return render_template('spaceship.html')

@app.route('/techtree')  
def techtree():
    calculateRes(WW,FW)
    print("loading techtree")
    return render_template('techtree.html',Atlatldisplay=Atlatldisplay, UpgradeAtlatldisplay=UpgradeAtlatldisplay, Steeltoolsdisplay=Steeltoolsdisplay, UpgradeSteeltoolsdisplay=UpgradeSteeltoolsdisplay, Irontoolsdisplay=Irontoolsdisplay, UpgradeIrontoolsdisplay=UpgradeIrontoolsdisplay, HuntingStrategiesdisplay=HuntingStrategiesdisplay, Ressourceproductiondisplay=Ressourceproductiondisplay, Stonetoolsdisplay=Stonetoolsdisplay, UpgradeSpearsdisplay=UpgradeSpearsdisplay, Spearsdisplay=Spearsdisplay)

@app.route('/techtree',methods=['GET','POST'])
def UpgradeUpdate():
  global wood
  global food
  global science

  global Ressourceproductiondisplay

  global Stonetoolsdisplay
  global UpgradeIrontoolsdisplay
  global Irontoolsdisplay
  global UpgradeSteeltoolsdisplay
  global Steeltoolsdisplay

  global HuntingStrategiesdisplay
  global UpgradeSpearsdisplay
  global Spearsdisplay
  global UpgradeAtlatldisplay
  global Atlatldisplay
 
  print("hey")

  w=""
  i=-1
  for upgrade in Upgrades:
    try: 
      i+=1
      print(upgrade)
      
      w=request.form[upgrade]
      print("passed")
      print(wood)
      print(food)
      print(science)
      print(wood >= WoodUpgraderequirement[i])
      print(food >= FoodUpgraderequirement[i] and science >= ScienceUpgraderequirement[i] )
      print(science >= ScienceUpgraderequirement[i] )
      if wood >= WoodUpgraderequirement[i] and food >= FoodUpgraderequirement[i] and science >= ScienceUpgraderequirement[i] :
        print("passed #2")
        UpdateUpgradevisibility(i)
        wood=wood-WoodUpgraderequirement[i]
        food=food-FoodUpgraderequirement[i]
        science=science-ScienceUpgraderequirement[i]
      else:
        print("you dont have enough ressources")
      return render_template('techtree.html',Atlatldisplay=Atlatldisplay, UpgradeAtlatldisplay=UpgradeAtlatldisplay, Steeltoolsdisplay=Steeltoolsdisplay, UpgradeSteeltoolsdisplay=UpgradeSteeltoolsdisplay, Irontoolsdisplay=Irontoolsdisplay, UpgradeIrontoolsdisplay=UpgradeIrontoolsdisplay, HuntingStrategiesdisplay=HuntingStrategiesdisplay, Ressourceproductiondisplay=Ressourceproductiondisplay, Stonetoolsdisplay=Stonetoolsdisplay, UpgradeSpearsdisplay=UpgradeSpearsdisplay, Spearsdisplay=Spearsdisplay)
    except:
      print("trying...")
      pass


  return render_template('techtree.html',Atlatldisplay=Atlatldisplay, UpgradeAtlatldisplay=UpgradeAtlatldisplay, Steeltoolsdisplay=Steeltoolsdisplay, UpgradeSteeltoolsdisplay=UpgradeSteeltoolsdisplay, Irontoolsdisplay=Irontoolsdisplay, UpgradeIrontoolsdisplay=UpgradeIrontoolsdisplay, HuntingStrategiesdisplay=HuntingStrategiesdisplay, Ressourceproductiondisplay=Ressourceproductiondisplay, Stonetoolsdisplay=Stonetoolsdisplay, UpgradeSpearsdisplay=UpgradeSpearsdisplay, Spearsdisplay=Spearsdisplay)



@app.route('/multiprocessingg/')  
def multiprocessingg():
    contentt=request.url 
    print(contentt)
    return render_template('multiprocessingg.html',contentt=contentt,chat=chat)

@app.route('/multiprocessingg/',methods=['GET','POST'])
def cool():
  print("hey")
  contentt=request.url 
  Gather=""
  print(contentt)
  try:
    Gather = request.form['Gather']
    chat.insert(0,"Gathered")
    return render_template('menu.html',contentt=contentt, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
  except:
    pass
  Hunt=""
  try:
    Hunt = request.form['Hunt']
    chat.insert(0,"Hunted")
    return render_template('menu.html',contentt=contentt,wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
  except:
    pass

  return render_template('multiprocessingg.html',contentt=contentt,chat=chat)

  

@app.route('/test/')
def test():

  return render_template('test.html')



def cooldowneffect(seconds,visi):
    print("running")
    time.sleep(seconds)
    visi="hidden"
    print("done")
    return render_template('multiprocessingg.html')




if __name__ == '__main__':
  app.run(debug=True)




