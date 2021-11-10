import random
from flask import Flask,render_template,Response,redirect,url_for,request
import time
import math
import multiprocessing
import jyserver.Flask as jsf

from flask import Flask, render_template
from flask.helpers import safe_join
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
Leather = 0
Firstclick = False
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
Atlatlvis="hidden"
Sackvis ="hidden"
Hutvis ="hidden"

Weapons= ["Wooden Sword", "Stone Sword", "Iron Sword", "Steel Sword","Wooden Spear", "Stone Spear", "Iron Spear", "Steel Spear", "Atlatl"]
WeaponVisibility=[WSwvis, StoSwvis, ISwvis, SteSwvis, WSpvis, StoSpvis, ISpvis, SteSpvis, Atlatlvis]
WoodWeaponrequirement= [50, 25, 25, 25, 100, 75, 75, 75]
WeaponIndexdamage=[1,5,9,13,1,1,1,1]
WeaponIndex = 1
FoodGatheringIndex = 1
WoodGatheringIndex = 1

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

Sackdisplay="none"
UpgradeHutdisplay="none" 
Hutdisplay="none"

Sackcounter = 0
Hutcounter = 0

ProductionUpgrades = ["Ressourceproduction"]
ToolsUpgrades = ["Stonetools","Irontools","Steeltools"]
FoodGatheringUpgrades = ["HuntingStrategies", "Spears", "Atlatl"]
Upgrades=["Ressourceproduction","Stonetools","Irontools","Steeltools","HuntingStrategies", "Spears", "Atlatl", "Sack", "Hut"]

WoodUpgraderequirement=[0,25,25,25,0,60,160,30,200]
FoodUpgraderequirement=[50,0,0,0,20,0,0,10,50]
ScienceUpgraderequirement=[25,25,50,75,10,40,100,10,50]



BattleReport = "You win, you gather"
ListBattleWood = [1]
BattleWood=1
ListBattleFood = [3,10,20,30]
BattleFood=0
ListBattleLeather = [1,3,5,10]
BattleLeather=0


Health=20
lh=0
AttackSpeed = 1.5
eAttackSpeed = 1
ListeHealth=[5,15,20,40]
eHealth=1
elh=0
ListeAttack=[1,3,5,10]
eAttack=1
iterationcount=10
eiterationcount=10
ListEnemyEntity = ["Rat", "Group of Rats", "Huge Rat", "Wolf"]
EnemyEntity=""




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
  print (wood)
  return render_template('menu.html',Sackvis = Sackvis, Hutvis=Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)


  
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
  global Atlatlvis
  global TTdisplay
  global Hutvis
  global Sackvis
  global Sackcounter
  global Hutcounter

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
  elif x==8:
    Atlatlvis = "hidden"
    return
  elif x==9:
    Sackcounter +=1
    if Sackcounter >= 5:
      Sackvis = "hidden"
    return
  elif x==10:
    Hutcounter +=1
    if Hutcounter >= 5:
      Hutvis = "hidden"
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

  global Sackdisplay
  global Hutdisplay
  global UpgradeHutdisplay

  global StoSwvis
  global ISwvis
  global SteSwvis
  global WSpvis
  global StoSpvis
  global ISpvis
  global SteSpvis
  global Atlatlvis
  global TTdisplay
  global FoodGatheringIndex
  global WoodGatheringIndex
  global Hutvis
  global Sackvis
  



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
    FoodGatheringIndex += 0.25
    UpgradeSpearsdisplay=""
  elif x==5:
    Spearsdisplay=""
    FoodGatheringIndex += 0.3
    UpgradeAtlatldisplay=""
    WSpvis="visible"
  elif x==6:
    Atlatlvis="visible"
    Atlatldisplay=""
    FoodGatheringIndex += 0.3
  elif x==7:
    Sackvis="visible"
    Sackdisplay=""
    UpgradeHutdisplay=""
    FoodGatheringIndex += 0.5
    WoodGatheringIndex += 0.5
  elif x==8:
    Hutvis="visible"
    Hutdisplay=""



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
    global Atlatlvis
    global Sackvis
    global Hutvis

    global WoodGatheringIndex
    global FoodGatheringIndex

    global WeaponIndexdamage

    Workers = population - FW - WW
    
    
    Gather=""
    try:

      Gather = request.form['Gather']
      tabcheck(1)
      MagicCrystalaccess(5)
      replacement="hidden"
      f= FoodGatheringIndex *(random.randint(20,50))
      w= WoodGatheringIndex * random.randint(20,50)
      wood = wood + w
      food = food + f
      chat.insert(0,"You gather a few sticks and berries.")
      return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
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
          WeaponIndex = WeaponIndexdamage[i+1] 
          print(WeaponIndex)
          chat.insert(0,f"You have crafted a {weapon}.")
        else:
          chat.insert(0,f"You don't have enough wood: {WoodWeaponrequirement[i]} wood required")
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
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
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        WW= WW + 1

        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
    elif W == "-WW":
      if WW==0:
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        WW= WW - 1
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
    elif W == "+FW":
      if Workers ==0:
        chat.insert(0,f"You do not have any free workers")
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        FW= FW + 1
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
    elif W == "-FW":
      if FW==0:
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)
      else:
        FW= FW - 1
        return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)


    return render_template('menu.html', Sackvis = Sackvis, Hutvis = Hutvis, Leather = Leather, Atlatlvis=Atlatlvis, TTdisplay=TTdisplay, MCdisplay=MCdisplay, WSwvis=WSwvis, StoSwvis=StoSwvis, ISwvis=ISwvis, SteSwvis=SteSwvis, WSpvis=WSpvis, StoSpvis=StoSpvis, ISpvis=ISpvis, SteSpvis=SteSpvis, populationmax=populationmax, Gcheck=Gcheck, Ccheck=Ccheck, Tcheck=Tcheck, wood = wood, food=food, population=population, FW=FW, WW=WW, chat=chat, exploredarea = exploredarea, Totalarea=Totalarea, percantage=percantage, replacement=replacement)


 













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
  Choseenemy(WeaponIndex)
  if (((eHealth/(WeaponIndex/AttackSpeed)))>(Health/(eAttack/eAttackSpeed))):
    lh=0
    elh=int(math.ceil(eHealth - (Health/(eAttack/eAttackSpeed))/AttackSpeed))
    iterationcount=int((eHealth-elh)/WeaponIndex)
    eiterationcount=int((Health-lh)/eAttack)
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
    elh=0
    lh= int(math.ceil(Health - math.floor(eHealth/(WeaponIndex/AttackSpeed))*eAttack))
    iterationcount=int((eHealth-elh)/WeaponIndex)
    eiterationcount=int((Health-lh)/eAttack)
  #print("iteration count" , iterationcount, "// (eHealth) : ",  (eHealth), "// (elh) : ",  (elh), "// Weapondindex : ", WeaponIndex)
  #print("eiteration count" , eiterationcount, "// (eHealth/(WeaponIndex/AttackSpeed)) : ",  math.ceil(eHealth/(WeaponIndex/AttackSpeed)), "// (lh) : ",  (lh), "// eAttack: ", eAttack)
  return render_template('wilderness.html',eAttackSpeed=eAttackSpeed,AttackSpeed=AttackSpeed, EnemyEntity=EnemyEntity, BattleReport=BattleReport,BattleWood =BattleWood , BattleFood =BattleFood , WeaponIndex=WeaponIndex, eAttack=eAttack, Health=Health, eHealth=eHealth, iterationcount=iterationcount, eiterationcount=eiterationcount, lh=lh, elh=elh)


def Choseenemy(D):
  global ListEnemyEntity
  global EnemyEntity
  global eAttack
  global eHealth
  global ListeAttack
  global ListeHealth

  for i in range(10):
    EnemyEntity =random.choices(ListEnemyEntity, weights=(1, 10*math.sqrt(D-1), D-1, (D*D-1)/100), k=1)
    #print(EnemyEntity)
  
  EnemyEntity = ''.join(str(x) for x in EnemyEntity)
  index = ListEnemyEntity.index(EnemyEntity)
  eAttack = ListeAttack[index]
  eHealth = ListeHealth[index]

  print(EnemyEntity)
  print(eAttack)
  print(eHealth)

  '''
  totalweight = 100 + 20*math.sqrt(D-1) + 2*(D-1) + (D*D-1)/100
  Ratweight = 100 / totalweight
  gorweight = (10*math.sqrt(D-1)) / totalweight
  grweight = (D-1) / totalweight
  wweight = ((D*D-1)/100)/totalweight

  
  
  print("groups of rats" , 10*math.sqrt(D-1))
  print ("giant rat", D-1)
  print("wolf", (D*D-1)/100 )

  print("total weight" , totalweight)
  print("Rat prob : " , Ratweight) 
  print("group of rat prob : " , gorweight)
  print("giant rat prob : " , grweight)
  print("wolf prob : " , wweight)'''
  return




@app.route('/spaceship')  
def spaceship():
    calculateRes(WW,FW)
    return render_template('spaceship.html')





@app.route('/techtree')  
def techtree():
    calculateRes(WW,FW)
    print("loading techtree")
    return render_template('techtree.html',Sackdisplay=Sackdisplay, Hutdisplay=Hutdisplay, UpgradeHutdisplay=UpgradeHutdisplay, Atlatldisplay=Atlatldisplay, UpgradeAtlatldisplay=UpgradeAtlatldisplay, Steeltoolsdisplay=Steeltoolsdisplay, UpgradeSteeltoolsdisplay=UpgradeSteeltoolsdisplay, Irontoolsdisplay=Irontoolsdisplay, UpgradeIrontoolsdisplay=UpgradeIrontoolsdisplay, HuntingStrategiesdisplay=HuntingStrategiesdisplay, Ressourceproductiondisplay=Ressourceproductiondisplay, Stonetoolsdisplay=Stonetoolsdisplay, UpgradeSpearsdisplay=UpgradeSpearsdisplay, Spearsdisplay=Spearsdisplay)

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
      return render_template('techtree.html',Sackdisplay=Sackdisplay, Hutdisplay=Hutdisplay, UpgradeHutdisplay=UpgradeHutdisplay, Atlatldisplay=Atlatldisplay, UpgradeAtlatldisplay=UpgradeAtlatldisplay, Steeltoolsdisplay=Steeltoolsdisplay, UpgradeSteeltoolsdisplay=UpgradeSteeltoolsdisplay, Irontoolsdisplay=Irontoolsdisplay, UpgradeIrontoolsdisplay=UpgradeIrontoolsdisplay, HuntingStrategiesdisplay=HuntingStrategiesdisplay, Ressourceproductiondisplay=Ressourceproductiondisplay, Stonetoolsdisplay=Stonetoolsdisplay, UpgradeSpearsdisplay=UpgradeSpearsdisplay, Spearsdisplay=Spearsdisplay)
    except:
      print("trying...")
      pass


  return render_template('techtree.html',Sackdisplay=Sackdisplay, Hutdisplay=Hutdisplay, UpgradeHutdisplay=UpgradeHutdisplay, Atlatldisplay=Atlatldisplay, UpgradeAtlatldisplay=UpgradeAtlatldisplay, Steeltoolsdisplay=Steeltoolsdisplay, UpgradeSteeltoolsdisplay=UpgradeSteeltoolsdisplay, Irontoolsdisplay=Irontoolsdisplay, UpgradeIrontoolsdisplay=UpgradeIrontoolsdisplay, HuntingStrategiesdisplay=HuntingStrategiesdisplay, Ressourceproductiondisplay=Ressourceproductiondisplay, Stonetoolsdisplay=Stonetoolsdisplay, UpgradeSpearsdisplay=UpgradeSpearsdisplay, Spearsdisplay=Spearsdisplay)


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

@jsf.use(app)
class App:
  def __init__(self): 
    self.count = 0
  
  def increment(self):
    self.count += 1
    self.js.document.getElementById("count").innerHTML = self.count

@app.route('/testt/')
def testt():

  return App.render(render_template('testt.html'))




def cooldowneffect(seconds,visi):
    print("running")
    time.sleep(seconds)
    visi="hidden"
    print("done")
    return render_template('multiprocessingg.html')

if __name__ == '__main__':
  app.run(debug=True)




