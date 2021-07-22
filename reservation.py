


from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\천재관\\Downloads\\chromedriver_win32\\chromedriver.exe')


url =""
# 암묵적으로 웹 자원을 (최대) 5초 기다리기DRIVER_DIR)
driver.implicitly_wait(5)
# 크롬 브라우저가 실행되며 해당 url로 이동한다.
driver.get(url)

#로그인페이지
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[1]/div[2]/div[1]/input").send_keys("")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[2]/div[2]/div[1]/input").send_keys("")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[3]/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[4]/button").click()


# 2페이지
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[4]/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/button[1]").click()
#예약가능한 병원 클릭
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/header/label").click()
driver.implicitly_wait(3)
try:
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/ul/li[1]").click()
except:
    driver.get(url)
