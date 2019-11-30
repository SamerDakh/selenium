from selenium import webdriver

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=C:\\Users\\Samer\\AppData\\Local\\Google\\Chrome\\User Data\\Samer") # change to profile path
chrome_options.add_argument("--user-data-dir=C:\\chromedriver") # change to profile path

# chrome_options.add_argument('--profile-directory=Samer')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://alarab.co.il')
elem = driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[8]/a')


elem.click()


elem2 = driver.find_element_by_xpath('//*[@id="left_content"]/div[2]/div[2]/h1')

print(elem2.text)

if elem2.text == 'مسلسلات رمضان 2019' :
    print("Pass")
else:
    print("Failed")

driver.quit()


