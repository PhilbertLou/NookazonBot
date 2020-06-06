from selenium import webdriver
import re, time

#FIELDS
belReg = re.compile('[a-zA-Z]')
bidNum = 0
realBid = 0
amount = 1
links = [""]
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
    currency = input('Do you want to pay in Bells? Or NMT? (Enter Bells or NMT)\n').lower()
    amount = input('How much do you want to pay for it?\n') #moved from inside each if to out here
    
    #PAYING IN NMT
    if currency == 'nmt':
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
        elems = browser.find_elements_by_xpath('//a[@class="sc-AxjAm sc-fzqNqU bEEuGQ home-listing-button"]')
        links = [elem.get_attribute('href') for elem in elems] # fix to only get necessary ones (rewrite the for loop?)

        for listing in range(bidNum):
            try:
                browser.get(links[listing])
                time.sleep(1)
                browser.find_element_by_xpath('//button[text()="Make an Offer"]').click()
                time.sleep(1)
            except:
                continue

            checks = browser.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[2]/div[7]/div/div/a')
            word = ""
            for check in checks:
                word += check.text

            checkTypes = browser.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div')
            currencyType = ""
            for checkType in checkTypes:
                currencyType += checkType.text
        
            try:
                if word == 'Make an Offer':
                    inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/input')
                    inputM.send_keys(amount)
                    browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
                    time.sleep(1)
                    realBid += 1
                
                else:
                    inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/input')
                    inputM.send_keys(amount)
                    browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
                    time.sleep(1)
                    realBid += 1

            except:
                try:
                    if currencyType == 'Nook Miles Ticket':
                        inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/input')
                        inputM.send_keys(amount)
                        browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
                        time.sleep(1)
                        realBid += 1

                except:
                    continue

        print('You have bid on ' + str(realBid) + ' listings.')
        close = input('Do you want to bid some more? (y/n)').lower()
        if close == 'n':
            exit()

        bidNum = 0
        realBid = 0

    #IF PAYING IN BELLS
    elif currency == 'bells':
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
        elems = browser.find_elements_by_xpath('//a[@class="sc-AxjAm sc-fzqNqU bEEuGQ home-listing-button"]')
        links = [elem.get_attribute('href') for elem in elems] # fix to only get necessary ones (rewrite the for loop?)

        for listing in range(bidNum):
            try:
                browser.get(links[listing])
                time.sleep(1)
                browser.find_element_by_xpath('//button[text()="Make an Offer"]').click()
                time.sleep(1)
            except:
                continue

            checks = browser.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[2]/div[7]/div/div/a')
            word = ""
            for check in checks:
                word += check.text

            checkTypes = browser.find_elements_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div')
            currencyType = ""
            for checkType in checkTypes:
                currencyType += checkType.text
        
            try:
                if word == 'Make an Offer':
                    inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/input')
                    inputM.send_keys(amount)
                    browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
                    time.sleep(1)
                    realBid += 1
                
                else:
                    inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/input')
                    inputM.send_keys(amount)
                    browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
                    time.sleep(1)
                    realBid += 1

            except:
                try:
                    if currencyType == 'Bells':
                        inputM = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/input')
                        inputM.send_keys(amount)
                        browser.find_element_by_xpath('//button[text()="Submit Offer"]').click()
                        time.sleep(1)
                        realBid += 1

                except:
                    continue

        print('You have bid on ' + str(realBid) + ' listings.')
        close = input('Do you want to bid some more? (y/n)').lower()
        if close == 'n':
            exit()

        bidNum = 0
        realBid = 0

    #IF TYPED WRONG
    else:
        print('Please write Bells or NMT')
        
#browser.close()

"""
/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/input
/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/input

/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/input
/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/input


/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[2]/input



1. for listing price makes div[3] instead of div[2]
2. check that you are paying nmts not bells when only 1 option

/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/input

"""
