from selenium import webdriver
import re

belReg = re.compile('[a-zA-Z]')

browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://nookazon.com/product/1096505003')

try:
    listDs = browser.find_elements_by_xpath('//div[@class="listing-product-info"]')

except:
    print('Was not able to find an element with that name.')


for listD in listDs:
    if 'seconds' in listD.text or 'minutes' in listD.text:
        #if len(listD.text.split()) > 1:
            #print(listD.text + '\n')
        info = listD.text.splitlines()
        for i in range(len(info)):
            if i == 0:
                print('Listing: ' + info[i])
                print('Offer details/price:')
            elif i != 1 and i != 2 and i != 3:
                #if ',' in info[i] and 'Nook' not in info[i]: #Only works when getting villagers
                if belReg.search(info[i]) == None:
                    print(info[i] + ' Bells')
                #elif 'Accepting' in info[i] and 'or' in info[i] and 'Wishlist' in info[i]: #not 100% Accurate
                    #print('Accepting Bells, NMT, or Wishlist items')
                #elif 'Accepting' in info[i]:
                    #print(type(listD))
                elif 'Accepting' not in info[i]:
                    print(info[i])
        print()

browser.close()
