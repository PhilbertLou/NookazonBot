from selenium import webdriver
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://nookazon.com/product/1096505003')

count = 0

try:
    listDs = browser.find_elements_by_class_name('listing-date')
    #listPs = browser.find_elements_by_xpath("//div[text()='Accepting']")

except:
    print('Was not able to find an element with that name.')



for listD in listDs:
    if 'seconds' in listD.text or 'minutes' in listD.text:
        #print('1x Raymond')
        print('1x Raymond\n' + listD.text + '\n')
        #print(listPs[count].text)
        #count = count + 1
        #print(listPs[count].text)
