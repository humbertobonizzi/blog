from selenium import webdriver

browser = webdriver.Chrome() 
browser.implicitly_wait(10)   
browser.get('http://127.0.0.1:8000')
#browser.get('https://www.google.com')
print(browser.title)

assert 'sucesso!' in browser.title

browser.quit()