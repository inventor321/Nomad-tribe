from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

import datetime
date_change = datetime.timedelta(days=2)
time_change = datetime.timedelta(minutes=1)
import schedule
import time
import random
from datetime import datetime, date

sleeptime = 50

Path = "C:/Users/all32/Downloads/chromedriver_win32/Chromedriver.exe"
driver = webdriver.Chrome(Path)

username= "allen.pinchuk@umontreal.ca"
password= "Udemf00t"
textforusername = '/html/body/form/div/div[2]/div/div/div[3]/div/input'
textforpassword = '/html/body/form/div/div[2]/div/div/div[4]/div/input'
locationofreservationinmenu = '/html/body/div[1]/aside/div[2]/ul/li[1]/ul/li[9]/div/div/a'
locationofreservationonscreen = '/html/body/div[1]/form/div/div/div[2]/div[2]/div[1]/a'
locationofreservationoffirstimagebutton = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/div[1]/div[2]/span'
locationofreservationofsecondimagebutton = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/span'
locationofnameofsport = "/html/body/div[3]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/span"
annulerboutton = "/html/body/div[3]/div/div[2]/div/div[2]/div[4]/button[2]"


tempsdumardia10h50min = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/div[4]/a'
tempsdumardia12h10min= '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/div[5]/a'
tempsdujeudi = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/div[2]/a'

timetoexecute = ' 19:20'
timetoexecutea = 0

a=1
b=0.5
c=1
d=1
e=1
f=1
g=1

dateexecution = date.today()
locationofexecutiontime = "/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/div/span"



def gettime():
    global timetoexecute
    global timetoexecutea
    print ("I'm working...")
    driver.get("https://interactif.cepsum.umontreal.ca/CapNet/login.coba")
    time.sleep(a)
    try:
        driver.find_element_by_xpath(textforusername).send_keys(username)
        driver.find_element_by_xpath(textforpassword).send_keys(password)
        button = driver.find_element_by_class_name("primaire")
        print(button)
        time.sleep(b)
        button.click()
        time.sleep(c)
        driver.find_element_by_xpath(locationofreservationinmenu).click()
        time.sleep(d)
        driver.find_element_by_xpath(locationofreservationonscreen).click()
        time.sleep(e)
        #driver.find_element_by_xpath(locationofreservationoffirstimagebutton).click()
        print("checking tab")
        checktab()
        print("tabchecked")
        time.sleep(f)
        text = driver.find_element_by_xpath(locationofexecutiontime).text
        print(text)
        index = text.find(":")
        timetoexecutea = text[index-3:index+3] 
        print(timetoexecutea)
        timetoexecute = datetime.strptime(dateexecution.strftime("%Y-%m-%d") + timetoexecutea ,"%Y-%m-%d %H:%M")-time_change
        print(timetoexecute)
        #driver.quit()
    

    except:
        print("failed program")
    return

gettime()

def checktab():
    print("getting text")
    
    for elem in driver.find_elements_by_xpath(locationofreservationoffirstimagebutton):
        print(elem.text)
    if textt == "Accès aux murs d'escalade":
        print("notwanting escalade")
        driver.find_element_by_xpath(locationofreservationofsecondimagebutton).click()
    else:
        driver.find_element_by_xpath(locationofreservationoffirstimagebutton).click()
    return


def reserve(timee):
    reservebutton = False
    while not reservebutton:
        try:
            Addtocart = addButton = driver.find_element_by_xpath(locationofexecutiontime)
            print("Button aint ready") 
            
            time.sleep(1)
            driver.refresh()
        except:
            Addtocart = addButton = driver.find_element_by_xpath(timee)
            print("button was clicked")
            Addtocart.click
            reservebutton = True
    return

def job():
    global timetoexecute
    global timetoexecutea
    print ("I'm working...")
    driver.get("https://interactif.cepsum.umontreal.ca/CapNet/login.coba")
    time.sleep(a)
    try:
        driver.find_element_by_xpath(textforusername).send_keys(username)
        driver.find_element_by_xpath(textforpassword).send_keys(password)
        button = driver.find_element_by_class_name("primaire")
        print(button)
        time.sleep(b)
        button.click()
        time.sleep(c)
        driver.find_element_by_xpath(locationofreservationinmenu).click()
        time.sleep(d)
        driver.find_element_by_xpath(locationofreservationonscreen).click()
        time.sleep(e)
        checktab()
        time.sleep(f)
        #reserve()
        

        
        #gettime()
        driver.quit()
    except:
        print("failed program")
        return

#schedule.every().sunday.do(job)

def setjobs():
    global sleeptime
    print("executing jobs")
    for i in range(sleeptime):

        schedule.every().sunday.at('19:59:30').do(job)
        schedule.every().monday.at('18:59:30').do(job)
        schedule.every().minute.do(job)


while True:
    now = datetime.now()
    execution = datetime.strptime(dateexecution.strftime("%Y-%m-%d") + timetoexecute ,"%Y-%m-%d %H:%M")
    print(execution)
    print("time before execution: ", execution - datetime.now()) 
    schedule.run_pending()
    
    if timetoexecutea == 0 :
        #gettime()
        setjobs()
    time.sleep(sleeptime)






'''
    

Path = "C:/Users/all32/Downloads/chromedriver_win32/Chromedriver.exe"
driver = webdriver.Chrome(Path)


dateexecution = date.today() + date_change

username= "allen.pinchuk@umontreal.ca"
password= "Udemf00t"
textforusername = '/html/body/form/div/div[2]/div/div/div[3]/div/input'
textforpassword = '/html/body/form/div/div[2]/div/div/div[4]/div/input'
locationofreservationinmenu = '/html/body/div[1]/aside/div[2]/ul/li[1]/ul/li[9]/div/div/a'
locationofreservationonscreen = '/html/body/div[1]/form/div/div/div[2]/div[2]/div[1]/a'
locationofreservationimagebutton = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/div[1]'

tempsdumardi = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/div[2]/a'
tempsdumercredi= '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/div[2]/a'
tempsdujeudi = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div[2]/div/div[3]/div[2]/a'

print ("I'm working...")
driver.get("https://interactif.cepsum.umontreal.ca/CapNet/login.coba")
time.sleep(a)
#try:
print("sending username")
driver.find_element_by_xpath(textforusername).send_keys(username)
print("sending password")
driver.find_element_by_xpath(textforpassword).send_keys(password)
button = driver.find_element_by_class_name("primaire")
print("found button")
print(button)
time.sleep(b)
button.click()
time.sleep(c)
driver.find_element_by_xpath(locationofreservationinmenu).click()
time.sleep(d)
driver.find_element_by_xpath(locationofreservationonscreen).click()
time.sleep(e)
driver.find_element_by_xpath(locationofreservationimagebutton).click()
print("gathering text")
time.sleep(f)
text = driver.find_element_by_xpath(locationofexecutiontime).text
print(text)
index = text.find(":")
timetoexecute = text[index-3] + text[index-2] + text[index-1] + text[index] + text[index+1] + text[index+2]
print(timetoexecute)
timetoexecute = datetime.strptime(dateexecution.strftime("%Y-%m-%d") + timetoexecute ,"%Y-%m-%d %H:%M")-time_change
print(timetoexecute)

#except:
#    print("failed program")
#




def tryc():
    try:
        button = driver.find_element_by_class_name("primaire")
        print(button)
        print("found button")
    except:
        print("id not found")

def trya():
    try:
        button = driver.find_element_by_class_name("pagecoba")
        print(button)
        tryc()
    except:
        print("id not found")

def tryb():
    try:
        button = driver.find_element_by_class_name("login-droite")
        print(button)
        trya()
    except:
        print("id not found")

try:
    button = driver.find_element_by_id("mainfrm")
    print(button)
    tryc()
except:
    print("id not found")



try:
    text = driver.find_element_by_link_text("Mot de passe oublié ?")
    time.sleep(2)
    text.click()
except:
    print("text not found")

C9DB_btnConnecter id and name
'''
