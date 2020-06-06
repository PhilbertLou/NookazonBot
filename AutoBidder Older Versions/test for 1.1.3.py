from selenium import webdriver
import re, time

#FIELDS
belReg = re.compile('[a-zA-Z]')
bidNum = 0
realBid = 0
amount = 1
currency = 'nmt'

#START OF PROGRAM
usr = input('Please enter your username\n')
passw = input('Please enter your password\n')
search = ''

#OPEN AND LOGS IN
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://nookazon.com')
browser.find_element_by_xpath('//a[@class="nav-link"]').click()
findU = browser.find_element_by_name('username')
findU.send_keys(usr)
findU = browser.find_element_by_name('password')
findU.send_keys(passw)
findU.submit()
time.sleep(2)

#LOOPING PROGRAM
while True:
    search = input('What/who do you want to bid on\n')
    inputS = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[1]/div[1]/form/div[2]/input').clear()
    inputS = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[1]/div[1]/form/div[2]/input')
    inputS.send_keys(search)
    inputS.submit()
    time.sleep(1)

    try:
        browser.find_element_by_xpath('//a[@class="sc-AxjAm kCLLqI item-img"]').click()
    except:
        print('Relaunch and please type in the EXACT name of the item you are looking for')
        continue

    time.sleep(1)

    try:
        listDs = browser.find_elements_by_xpath('//div[@class="listing-product-info"]')
    except:
        print('Was not able to find an element with that name.')

    print('All Listings:')
    for listD in listDs:
        if 'seconds' in listD.text or 'minutes' in listD.text:
            bidNum += 1
                
    elems = browser.find_elements_by_xpath('//a[@class="sc-AxjAm sc-fzqNqU bEEuGQ home-listing-button"]')
    #links = [elem.get_attribute('href') for elem in elems] # fix to only get necessary ones (rewrite the for loop?)

    links = []

    for elem in range(bidNum):
        links.append(elems[elem].get_attribute('href'))
    
    for listing in range(bidNum):
        try:
            print(links[listing])
        except:
            continue

