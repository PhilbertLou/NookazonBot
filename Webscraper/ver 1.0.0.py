from selenium import webdriver
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://nookazon.com/product/1096505003')
try:
    posts = browser.find_elements_by_class_name('listing-date')

except:
    print('Was not able to find an element with that name.')

for post in posts:
    if 'seconds' in post.text or 'minutes' in post.text:
        print(post.text)
