import time #thêm time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
###################PHAN IN RA MAN HINH#############
a = '0862693549'
b = 'Application999'
c = 'bobbystanoff'
d = 'Application999'

# a = input("hay nhap tai khoan fb : ")
# b = input("hay nhap nhap khau fb : ")
# c = input("hay nhap tai khoan ttc : ")
# d = input("hay nhap nhap khau ttc : ")
DELAYTIME = float(input('nhap thoi gian delay: '))
print('@@@@@@@@@@@@@@@@@@@@@@@')
print('1: job like')
print('2: job follow')
SELECTMODE = int(input('chon job muon lam: '))

############KHOI DONG SELENIUM########
chrome_options = Options()
#chrome_options.add_argument("--headless")

chrome_options.add_argument("--log-level=OFF")
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(executable_path='/home/bobby/Downloads/chromedriver', options=chrome_options)

driver.maximize_window()
origin_window = driver.current_window_handle

driver.get('https://www.facebook.com/login') #chạy facebook
time.sleep(1)
driver.find_element_by_id('email').send_keys(a) #UID facebook
time.sleep(1)
driver.find_element_by_id('pass').send_keys(b) #PASS facebook
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(3)
driver.get('https://tuongtaccheo.com/') #chạy ttc
time.sleep(2)
driver.execute_script('document.querySelector("#memberModal > div > div > div.modal-footer > div > button").click()')
time.sleep(0.5)
driver.find_element_by_id('name').send_keys(c) #tai khoan ttc
time.sleep(1)
driver.find_element_by_id('password').send_keys(d) #PASS ttc
time.sleep(1)
driver.find_element_by_name('submit').click()
time.sleep(3)

##########begining done ###########

############ DAY LA JOB LIKE ####################33
def LamJobLike():    # tao ham de chon mode like hay follow
    driver.get('https://tuongtaccheo.com/kiemtien/') #link like 

    reLoadJob = driver.find_element_by_id('tailai')  #nut tai lai, het job thi bam de tai them job moi
    def JobsListCount(): # ham de dem so job hien co 
        try:   #thu doan code duoi, neu bi loi thi bo qua 
            tempJobsList = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#dspost .col-md-2"))) # dem so job hien co
            return len(tempJobsList) # tra ve so job hien co. vi du co 10 job thi tra ve 10
        except: # neu bi loi doan code tren thi trả ve so 1 
            return 1
    def LikeAction(JobsList): # ham de thuc hien hanh dong like 
        for i in range(JobsList): # lap tu 1 den so job hien co 
            try:
                ttcRequest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default")))# nut lam job
                ttcRequest.click() # click nut lam job
                time.sleep(1)
            except:
                print('cant click?') # ko click duoc thi in ra man hinh
                break # in roi thi thoat khoi vong lap
            try:
                driver.switch_to.window(driver.window_handles[-1]) # chuyen sang tab moi mo
                likeButton =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t pfnyh3mw d2edcug0 hpfvmrgz ph5uu5jm b3onmgus iuny7tx3 ipjc6fyt']"))) #nut like
                time.sleep(DELAYTIME) #cho 
                likeButton.click() #nhan nut like
            except: # neu link loi thi thuc hien dong nay
                print('error link')
            time.sleep(1)
            driver.close() #dong tab fb
            # errorr heree
            driver.switch_to.window(origin_window) # chuyen ve tab ttc
            time.sleep(1)
            try: 
                moneyButton = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div[1]/div/div[{i+1}]/div/div/button')   #nut nhan tien  
                moneyButton.click() # click nut nhan tien 
            except: #neu bi loi thi in ra 
                print('ko nhan tien')
                break # thoat khoi vong lap
            time.sleep(1)
            soCash = driver.find_element_by_id('soduchinh').text # so xu hien co
            print(f'so xu hien tai: {soCash}') # in ra so xu hien co
            time.sleep(2)

    while True:       #lap 
        Jobslist = JobsListCount() # dem so job truoc roi gan vao bien nay
        LikeAction(Jobslist) # truyen bien nay vao ham thực hien hanh dong like
        reLoadJob.click() # tai lai danh sach job 
###################### HET JOB LIKE ############333

####################DAY LA JOB FOLLOW####################
def LamJobFollow():
    driver.get('https://tuongtaccheo.com/kiemtien/subcheo')
    reLoadJob = driver.find_element_by_id('tailai')
    def JobsListCount():
        try:
            tempJobsList = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#dspost .col-md-2")))
            return len(tempJobsList)
        except:
            return 1
    def FollowAction(Jobslist):
        for i in range(Jobslist):
            try:
                ttcRequest = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default")))
                tempLink = str(ttcRequest.get_attribute('title'))
                mbasicLink = tempLink.replace('www', 'mbasic').replace("'","")
                ttcRequest.click()
                time.sleep(1)
            except:
                print('khong the lam job nay')
                break
            try:
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(mbasicLink)            
                followButton1 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/a')))
                followButton2 =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[3]/table/tbody/tr/td[3]/a')))
                time.sleep(DELAYTIME)
                if followButton1.text in ['Theo dõi','Follow']:
                    followButton1.click()
                else:
                    followButton2.click()
                time.sleep(1)
            except:
                print('link loi')
            driver.close()
            driver.switch_to.window(origin_window)
            time.sleep(1)
            try:
                moneyButton = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[3]/div/div[1]/div/div[{i+1}]/div/div/button')     
                moneyButton.click()
            except:
                print('ko nhan tien')
                break
            time.sleep(1)
            soCash = driver.find_element_by_id('soduchinh').text
            print(f'so xu hien tai: {soCash}')
            time.sleep(2)

    while True:       
        Jobslist = JobsListCount()
        FollowAction(Jobslist)
        reLoadJob.click()


##################### HET JOB FOLLOW######################

############PHAN CHINH CUA TOOL############
if SELECTMODE == 1:
    LamJobLike()
elif SELECTMODE == 2:
    LamJobFollow()








