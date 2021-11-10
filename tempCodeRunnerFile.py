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
    driver.find_element_by_xpath(locationofreservationimagebutton).click()
    time.sleep(f)
    driver.find_element_by_xpath(tempsdumardia10h50min).click()

    
    gettime()
    driver.quit()
except:
    print("failed program")