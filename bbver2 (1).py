import time #thêm time
from selenium import webdriver
from selenium.webdriver.common.by import By

#hiphopnerversai9@gmail.com
#XZGFFHHKLNK
a = input("hay nhap tai khoan ")
b = input("hay nhap nhap khau ")
print('nhap job muon lam')
print('1: Job Youtube')
print('2: Job like facebook')
print('3: Job share facebook')
print('4: All job')
vj = int(input('chon : '))

likeButton = ''
shareButton = ''
innerShareButton = ''


def YoutubeJobBot():
    driver.execute_script('document.querySelector("#root > section > section > main > div > div > div > div:nth-child(2) > div > div > div > div.gx-module-sidenav.gx-d-none.gx-d-lg-flex > div > div > div > div:nth-child(1) > ul > li:nth-child(8) > span > span").click()')#lọc jon ytb
    time.sleep(1)
    while True:
        driver.execute_script('document.querySelector("sup.ant-scroll-number.ant-badge-count.ant-badge-multiple-words").click()')#nhấp vào làm job ytb
        time.sleep(1)

        driver.execute_script('document.querySelector("div.ant-row-flex").click()') #nnhấp dô làm việc để chạy ytb
        time.sleep(2)
        #driver.find_element_by_class_name("ytp-large-play-button ytp-button").click()
        # Store iframe web element
        iframe = driver.find_element(By.TAG_NAME, "iframe")

        # switch to selected iframe
        driver.switch_to.frame(iframe)


        # Now, Click on the button
        driver.find_element(By.CSS_SELECTOR, "button[class='ytp-large-play-button ytp-button']").click()

        time.sleep(50)
        driver.switch_to.default_content()

        driver.find_element(By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary ant-btn-sm']").click()
        time.sleep(1.5)


def LikePostJobBot(likeButton):
    driver.execute_script('document.querySelector("#root > section > section > main > div > div > div > div:nth-child(2) > div > div > div > div.gx-module-sidenav.gx-d-none.gx-d-lg-flex > div > div > div > div:nth-child(1) > ul > li:nth-child(4) > span > span").click()')
    time.sleep(1)
    while True:
        driver.execute_script('document.querySelector("sup.ant-scroll-number.ant-badge-count.ant-badge-multiple-words").click()')#nhấp vào làm job ytb
        time.sleep(1)
        driver.execute_script('document.querySelector("div.ant-row-flex").click()')
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(4)
        if driver.title.find('Watch') != -1:
            driver.find_element(By.CSS_SELECTOR, "div[class='_3l2t  _18vj']").click()
            time.sleep(0.5)
        else:
            driver.find_element(By.CSS_SELECTOR, f"i[class='{likeButton}']").click()
            time.sleep(0.5)
        driver.close()
        driver.switch_to.window(origin_window)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary ant-btn-sm']").click()
        time.sleep(1.5)


def SharePostJobBot(shareButton, innerShareButton):
    driver.execute_script('document.querySelector("#root > section > section > main > div > div > div > div:nth-child(2) > div > div > div > div.gx-module-sidenav.gx-d-none.gx-d-lg-flex > div > div > div > div:nth-child(1) > ul > li:nth-child(7) > span > span").click()')
    time.sleep(1)
    while True:
        driver.execute_script('document.querySelector("sup.ant-scroll-number.ant-badge-count.ant-badge-multiple-words").click()')#nhấp vào làm job ytb
        time.sleep(1)
        driver.execute_script('document.querySelector("div.ant-row-flex").click()')
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)
    
        driver.find_element(By.CSS_SELECTOR, f"i[class='{shareButton}']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, f"i[class='{innerShareButton}']").click()
        time.sleep(3)
        driver.close()
        driver.switch_to.window(origin_window)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "button[class='ant-btn ant-btn-primary ant-btn-sm']").click()
        time.sleep(1.5)


driver = webdriver.Chrome(executable_path='/home/bobby/Downloads/chromedriver')
driver.maximize_window()
origin_window = driver.current_window_handle
driver.get('https://www.facebook.com//login') #chạy facebook
time.sleep(1)
driver.find_element_by_id('email').send_keys(a) #UID facebook
time.sleep(1)
driver.find_element_by_id('pass').send_keys(b) #PASS facebook
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(3)
driver.get('https://like2like.org/signin') #chạy l2l
time.sleep(3)
driver.execute_script('document.querySelector("#root > div > div > div > div.gx-app-login-content > button:nth-child(2)").click()')#login l2l
time.sleep(2)

driver.get('https://like2like.org/app/get-money') #vào link get opp
#captcha appear here
time.sleep(7)



if vj == 4:
    print('DMM dang hoc de code =)))')    
elif vj == 1:

    YoutubeJobBot()
elif vj == 2:

    LikePostJobBot(likeButton)
elif vj == 3:

    SharePostJobBot(shareButton, innerShareButton)
else:
    print('nahh')
