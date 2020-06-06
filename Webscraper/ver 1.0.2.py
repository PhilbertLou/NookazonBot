from selenium import webdriver
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
            if i != 1 and i != 2 and i != 3:
                if ',' in info[i]:
                    print(info[i] + ' Bells')
                elif 'Accepting' not in info[i]: #Maybe include the types later
                    print(info[i])
        print()

