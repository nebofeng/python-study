from selenium import  webdriver
d = webdriver.Chrome()
d.get('http://www.baidu.com')
d.find_element_by_id('kw').send_keys('nebofeng')
d.implicitly_wait(5)
