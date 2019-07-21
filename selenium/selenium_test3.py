from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('selenium/data/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(5)

id='tkddnzld123'
pw=''

# driver.find_element_by_name('id').send_keys(id)
# driver.find_element_by_name('pw').send_keys(pw)
driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
time.sleep(1)
