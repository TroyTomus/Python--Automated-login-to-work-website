from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

username="Y3823370W"
password="Anpw2020"

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.anteacheckin.es/")
driver.set_window_size(1920, 1080)
print("The script has just opened: ",driver.title)
#driver.quit()


#click the start button
startBtn=driver.find_element_by_id("btnInicioSesion")
startBtn.click()
print("The start btn was hit")


#enter user's username
usernamefield=driver.find_element_by_id("usuarioSesion")
usernamefield.send_keys(username)
print("The user name was inputted")


#enter user's password
passwordfield= driver.find_element_by_id("claveSesion")
passwordfield.send_keys(password)
passwordfield.send_keys(Keys.RETURN)
print("The password was inputted")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ContentPlaceHolder1_mainPrincipalPage"]/section/ul[1]/li[1]/article'))).click()

print("trying btn")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'ContentPlaceHolder1_mainRegistro_aEntrada'))).click()

print("trying btn")

