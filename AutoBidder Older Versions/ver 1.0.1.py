from selenium import webdriver
import re, time

belReg = re.compile('[a-zA-Z]')
bidNum = 0
realBid = 0
NMT = 1

usr = input("Please enter your username\n")
passw = input("Please enter your password\n")
search = input("What/who do you want to bid on\n")

browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://nookazon.com')

browser.find_element_by_xpath('//a[@class="nav-link"]').click()
findU = browser.find_element_by_name('username')
findU.send_keys(usr)
findU = browser.find_element_by_name('password')
findU.send_keys(passw)
findU.submit()

time.sleep(2)

inputS = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[1]/div[1]/form/div[2]/input')
inputS.send_keys(search)
inputS.submit()
time.sleep(2)

try:
    browser.find_element_by_xpath('//a[@class="sc-AxjAm kCLLqI item-img"]').click()
except:
    print('Releach and please type in the EXACT name of the item you are looking for')
    exit()

time.sleep(1)

try:
    listDs = browser.find_elements_by_xpath('//div[@class="listing-product-info"]')

except:
    print('Was not able to find an element with that name.')

print('All Listings:')
for listD in listDs:
    if 'seconds' in listD.text or 'minutes' in listD.text:
        info = listD.text.splitlines()
        for i in range(len(info)):
            if i == 0:
                print('Listing: ' + info[i])
                print('Offer details/price:')
            elif i != 1 and i != 2 and i != 3:
                if belReg.search(info[i]) == None:
                    print(info[i] + ' Bells')
                elif 'Accepting' not in info[i]:
                    print(info[i])
        print()
        bidNum += 1

    
#time.sleep(5)
#HANDLE CASE WHERE NO BIDS ARE AVAILABLE

"""listings = browser.find_elements_by_xpath('//a[@class="sc-AxjAm sc-fzqNqU bEEuGQ home-listing-button"]')
print(len(listings))
print(bidNum)"""

elems = browser.find_elements_by_xpath('//a[@class="sc-AxjAm sc-fzqNqU bEEuGQ home-listing-button"]')
links = [elem.get_attribute('href') for elem in elems] # fix to only get necessary ones (rewrite the for loop?)

#print(links)
#try except in try except
for listing in range(bidNum):
    browser.get(links[listing])
    browser.find_element_by_xpath('//button[text()="Make an Offer"]').click()

    try:
        inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/input')
        inputM.send_keys(NMT)
        browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
        time.sleep(2)
        realBid += 1

    except:
        try:
            inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/input')
            inputM.send_keys(NMT)
            browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
            time.sleep(2)
            realBid += 1

        except:
            continue()

print('You have bid on ' + str(realBid) + ' listings.')
#browser.close()

