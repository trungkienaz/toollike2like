import time #thêm time
from selenium import webdriver
from selenium.webdriver.common.by import By

a = input("hay nhap tai khoan fb : ")

b = input("hay nhap nhap khau fb : ")
c = input("hay nhap tai khoan ttc : ")
d = input("hay nhap nhap khau ttc : ")
driver = webdriver.Chrome(executable_path='/home/bobby/Downloads/chromedriver')
#driver.set_window_size(400,500)
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
driver.get('https://tuongtaccheo.com/') #chạy ttc
time.sleep(3)
driver.execute_script('document.querySelector("#memberModal > div > div > div.modal-footer > div > button").click()')
time.sleep(2)
driver.find_element_by_id('name').send_keys(c) #tai khoan ttc
time.sleep(1)
driver.find_element_by_id('password').send_keys(d) #PASS ttc
time.sleep(1)
driver.find_element_by_name('submit').click()
time.sleep(3)
driver.get('https://tuongtaccheo.com/kiemtien/')
time.sleep(6)

driver.execute_script('document.querySelector("button.btn.btn-default").click()')
time.sleep(3)

driver.switch_to.window(driver.window_handles[-1])

time.sleep(6)

#driver.execute_script('document.querySelector(".rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.hpfvmrgz.ph5uu5jm.b3onmgus.iuny7tx3.ipjc6fyt").click()')
driver.find_element_by_css_selector("[class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 hpfvmrgz ph5uu5jm b3onmgus iuny7tx3 ipjc6fyt']").click()
time.sleep(0.5)

# driver.close()
# driver.switch_to.window(origin_window)
# time.sleep(1)
     

# driver.close()
input()
