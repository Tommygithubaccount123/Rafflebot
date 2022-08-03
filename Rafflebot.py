from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time, logging

#log
logging.basicConfig(filename="raffles.txt", format='%(asctime)s %(message)s', filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.INFO) 

options = webdriver.ChromeOptions() 
options.add_argument('--user-data-dir=C:/Users/stink/AppData/Local/Google/Chrome/User Data/') #Path to your chrome profile

browser = webdriver.Chrome(executable_path="C:\\Users\stink\OneDrive\Documents\webdrivers\chromedriver", options=options)
browser.set_page_load_timeout(7)
browser.get('https://scrap.tf/raffles')
time.sleep(1)

#browser.find_element_by_xpath('//body').send_keys(Keys.END)

rafflesfailedtojoin=[]
rafflesentered=[]
def raffletry(number):
    xpath='//*[@id="raffles-list"]/div['+str(number)+']/div[1]/div[1]/a'
    try:
        raffle=browser.find_element(By.XPATH,xpath)
        raffle.click()
        time.sleep(1)
        try:
            enterraffle=browser.find_element(By.XPATH,'//*[@id="main-container"]/div/div[2]/div[5]/div[2]/button[2]')
            enterraffle.click()
            print('Entered raffle '+str(number))
            logging.info('Entered raffle '+str(number))
            rafflesentered.append(1)
            rafflesfailedtojoin.clear()
            time.sleep(1)
        except:
            try:
                enterraffle=browser.find_element(By.XPATH,'//*[@id="main-container"]/div/div[2]/div[7]/div[2]/button[2]') 
                enterraffle.click()
                print('Entered raffle '+str(number))
                logging.info('Entered raffle '+str(number))
                rafflesentered.append(1)
                rafflesfailedtojoin.clear()
                time.sleep(1)
            except:
                print('No enter raffle '+str(number))
                logging.info('No enter raffle '+str(number))
                rafflesfailedtojoin.append(1)
        browser.back()
        #browser.
        time.sleep(1.5) #edit this number
    except:
        print('No raffle found '+str(number))
        logging.info('No raffle  found '+str(number))
        rafflesfailedtojoin.append(1)
        time.sleep(1)


def getnumberofrafflesavailable():
    thenumber=(browser.find_element(By.XPATH,'//*[@id="main-container"]/div[2]/div[2]/div/div[1]/h1')).text
    print(thenumber)
    for x in range(len(thenumber)):
        if thenumber[x]=='/':
            thenumber=thenumber[(x+1):len(thenumber)]
            return thenumber

def failedrafflestopper():
    if len(rafflesfailedtojoin)==2:
        browser.refresh()
    if len(rafflesfailedtojoin)>4:
        print('Too many failed raffles, stopped')
        logging.info('Too many failed raffles, stopped')
        return 0
    else:
        return 1


def countenterredraffles():
    total=0
    for i in rafflesentered:
        total=total+i
    return total
y=getnumberofrafflesavailable()
print(y+' number of raffles')
logging.info(y+' number of raffles')  
numberofraffles=1

#time.sleep(15)

while numberofraffles<int(y) and failedrafflestopper()==1:
    raffletry(numberofraffles)
    numberofraffles += 1
print('%d raffles entered' % countenterredraffles())
logging.info('%d raffles entered' % countenterredraffles())
