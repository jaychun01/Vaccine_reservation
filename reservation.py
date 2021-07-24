from selenium import webdriver
import time
import winsound as sd
driver = webdriver.Chrome('C:\\chromedriver.exe')


def beepsound():
    fr = 2000     # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    while 1==1:
        sd.Beep(fr, du) # winsound.Beep(frequency, duration)

def searchingCalendar():
    month_chk=""
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[9]/button").click()

    #checkbox check logic here
    #click calendar
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/form/div[3]/div[3]/div[1]").click()
    time.sleep(3)
    # in next 3 months
    for i in range(3):
        #it shows green color when reservation is available
        for i in range(8,36,1):
            x_path="/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/span["+str(i)+"]"
            print(x_path)
            a=driver.find_element_by_xpath(x_path)
            green_chk = a.value_of_css_property('color')
            print(green_chk)
            if green_chk == "rgba(221, 221, 221, 1)" or green_chk == "rgba(0, 0, 0, 1)" :
                print("not available")
            #when it is avaiable, notice with beepsound
            else:
                beepsound()
        #next month click
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/header/span[3]").click()
    month_chk="none"
    return month_chk

def findingByPlace():
    # finding in detail by place
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/button[1]").click()

    # finding in avaiable only
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/header/label/input").click() #인풋박스 체크가 잘 안됨
    if driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/header/label/input").get_attribute('checked'):
        print("-----------------checked--------------------------")
    time.sleep(5)
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/ul/li[1]").click()
        chk=searchingCalendar()
    except:
        driver.get(url)
        findingByPlace()
    return chk

def main():
    global url
    url = ""
    #waiting until chrome is opened
    driver.implicitly_wait(5)
    # move to website
    driver.get(url)

    #login page
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[1]/div[2]/div[1]/input").send_keys("")
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[2]/div[2]/div[1]/input").send_keys("")
    #checkbox check logic here
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[3]/input").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div[4]/button").click()

    result=findingByPlace()
    print(result)

if __name__=="__main__":
    main()
