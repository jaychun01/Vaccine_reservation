from selenium import webdriver

driver = webdriver.Chrome('C:\\chromedriver.exe')


url =""
#waiting until chrome is opened
driver.implicitly_wait(5)
# move to website
driver.get(url)

#login page
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[1]/div[2]/div[1]/input").send_keys("")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[2]/div[2]/div[1]/input").send_keys("")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[3]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[4]/button").click()


# finding in detail
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[4]/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/button[1]").click()

# finding in detail
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/header/label").click()
driver.implicitly_wait(3)
try:
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/ul/li[1]").click()
except:
    driver.get(url)
 
