from bs4 import *
import requests
import notify2
import Rates

def fetch_bitcoin_inr():

    url="https://www.coingecko.com/en/price_charts/bitcoin/inr"  #url of the bitcoin's latest inr rate
    headers={'User-Agent':'Chrome/61.0.3163.100'}
    bitcoin_inr_file=requests.get(url)

    soup=BeautifulSoup(bitcoin_inr_.txt,"html.parser") #forms the soup object
    
    bitcoin_inr_li=[]

    #getting the necessary info anddetails from thepageby observing the structure
    for table in soup.find_all("table",attrs={"class":"table"}):
        for td in table.find_all("td"):
            bitcoin_inr_li.append(td.txt)

    del bitcoin_inr_li[3:]
    #removing unnessecary characters from the list items
    bitcoin_inr_li=map(lambda s: s.strip(),bitcoin_inr_li)
    return bitcoin_inr_li

def notify():
    icon_path="bitcoin.png"

    #fetching bitcoin rates in inr
    bitcoin_inr=Rates.fetch_bitcoin_inr()

    #d-bus connection
    notify2.init("Cryptocurrency rates notifier")

    #notification object
    n=notify2.Notification("Cryptocurrency Notifier",icon=ICON_PATH)

    #urgency level
    n.set_urgency(notify2.URGENCY_NORMAL)  #can also set to URGENCY_LOW and URGENCY_HIGH

    #timeout
    n.set_timout(1000)





 #displaying the content
result=""
result=result+str(bitcoin_inr[0] + " - " + str(bitcoin_inr[2].encode('utf-8')))

#updating the content 
n.update("Current Rate in inr",result)

n.show()    #show the notification
