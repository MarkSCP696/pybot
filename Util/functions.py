#Selenium import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#Close connection
def OpenConnection():
    #Loading Chrome web driver
    driver = webdriver.Chrome('./drivers/chromedriver')
    print(' *** ' + driver.title)

    #Connect to Instagram
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")
    driver.maximize_window()
    driver.get("https://www.instagram.com/accounts/login/")


    #Close cookie pop-up by xPath
    driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()

    #Insert Username and Pass and button click
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys("luca.baccol2244659")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys("simone12e£!")
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()


    #Do not save credentials
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))).click()
    return driver

#Close connection
def CloseConnection(driver):
    time.sleep(3)
    driver.close()

#refresh anf follow
def AutFollow(loops , excNumber):
    driver = OpenConnection()
    counter = 0
    for k in range(loops):
        if(k > 0):
            driver.refresh()
        for x in range(5):
            if(counter == excNumber ) :
                break
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[' + str(x+1) + ']/div[3]/button'))).click()
            counter += 1
    print("Number of new people followed : " + str(counter))
    CloseConnection(driver)

#remove people to follow
def RemoveFollow(loop , exactNumber):
    driver = OpenConnection()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div'))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))).click()
    elem = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')[0].text
    time.sleep(3)
    #Element to apply the scroll To 
    fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
    time.sleep(3)
  
    # scroll progression
    increase = 300
    verical_ordinate = increase
    # visible elements
    visible_elemets = 5
    #counter
    counter = 0

    divo = '3'
    #loop for each scroll to do
    for j in range(loop):
        #loop for each element to unfollow   
        for k in range(visible_elemets):
            value = str((j*visible_elemets) +(k+1))
            if(j>0):
                divo = '2'                
            if(int(value) > int(exactNumber)) :
                break  
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div[3]/ul/div/li[' + value +']/div/div[' + divo +']/button'))).click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[1]'))).click()
            time.sleep(1)
            counter += 1
        driver.execute_script('arguments[0].scrollTop = arguments[1];', fBody, verical_ordinate)
        verical_ordinate += increase
        time.sleep(2)
    fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
    #print("*** fList len is {}".format(len(fList)))
    print("Number of removed followers : " + str(counter))

    CloseConnection(driver)