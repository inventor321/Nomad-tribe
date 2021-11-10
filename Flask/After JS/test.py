import turtle
import random

encodage=[[True,True,True,True,True,True,False],#0
          [False,False,True,True,False,False,False],#1
          [False,True,True,False,True,True,True],#2
          [False,True,True,True,True,False,True],#3
          [True,False,True,True,False,False,True],#4
          [True, True, False, True, True, False, True],#5
          [True,True,False,True,True,True,True],#6
          [False,True,True,True,False,False,False],#7
          [True,True,True,True,True,True,True],#8
          [True,True,True,True,True,False,True]]#9
        

def dessinerChiffre(longeur, segments):
    bk(longeur/2)
    lt(90)
    pd()
    for i in range(7):
        if segments[i]:
            pd()    
        else:
            pu()
        fd(longeur)
        if i != 2 and i != 6:
            rt(90)
    pu()
    bk(longeur/2)

def dessinerHeure(longeur, heures, minutes):
    pu()
    bk(3*longeur)
    dessinerChiffre(longeur,encodage[heures//10])
    fd(longeur*1.5)
    dessinerChiffre(longeur,encodage[heures%10])
    fd(longeur*1.5)
    rt(90)
    fd(longeur/2)
    lt(90)
    dessinerChiffre(longeur/8,encodage[0])
    lt(90)
    fd(longeur)
    rt(90)
    dessinerChiffre(longeur/8,encodage[0])
    rt(90)
    fd(longeur/2)
    lt(90)
    fd(longeur*1.5)
    dessinerChiffre(longeur,encodage[minutes//10])
    fd(longeur*1.5)
    dessinerChiffre(longeur,encodage[minutes%10])
    bk(3*longeur)

pu()
lt(90)
fd(200)
rt(90)

for i in range(10):
    h=math.floor(random()*24)
    m=math.floor(random()*60)
    print("h : m", h,":",m)
    dessinerHeure(20, h, m)  
    pu()
    rt(90)
    fd(50)
    lt(90)
