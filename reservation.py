from selenium import webdriver
import time
import winsound as sd
driver = webdriver.Chrome('C:\\chromedriver.exe')


def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

def main():


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
    #driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/header/label").click()
    #time.sleep(3)
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/nav/ul/li[1]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[9]/button").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/form/div[3]/div[3]/div[1]").click()
        time.sleep(3)
        for i in range(8,36,1):
            x_path="/html/body/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/span["+str(i)+"]"
            print(x_path)
            a=driver.find_element_by_xpath(x_path)
            green_chk = a.value_of_css_property('color')
            print(green_chk)
            if green_chk == "rgba(221, 221, 221, 1)" or green_chk == "rgba(0, 0, 0, 1)" :
                print("not available")
                beepsound()

    except:
        driver.get(url)
        driver.find_element_by_xpath("")

if __name__=="__main__":
    main()
