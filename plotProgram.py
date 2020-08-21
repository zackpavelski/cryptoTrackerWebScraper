##########################
#MATPLOTLIB FOR CURRENCIES
##########################
from bs4 import BeautifulSoup
import numpy as np
from matplotlib import pyplot as plt
import urllib.request as ul
from urllib.request import Request, urlopen
import pylab
from datetime import datetime
def createGraph():
    vals = getValues('ethereum')
    vals = vals.split("-")
    datas = ([])
    xCount = len(vals)
    
    for val in vals:
        datas.append([xCount, float(val)])
        xCount-=1
    #print((datas))
    datas = datas[::-1]
    print(datas)
    data = np.array([
        datas
    ])
    x, y = data.T
    plt.xlabel('Date Proximity to Today')
    plt.ylabel('Value')
    plt.title('Value of currency')
    fig = pylab.gcf()
    fig.canvas.set_window_title('Currency Value')
    plt.scatter(x,y)
    plt.show()
def getValues(name):
    #PROTOTYPE
    currentDay = str(datetime.now().day)
    currentMonth = str(datetime.now().month)
    if len(currentDay) <= 1:
        currentDay = "0" + currentDay
    if len(currentMonth) <= 1:
        currentMonth = "0" + currentMonth
    URL = Request('https://coinmarketcap.com/currencies/'+name+'/historical-data/?start=20190110&end=2019'+currentMonth+currentDay)
    final = ""
    occurances = []
    content = urlopen(URL).read()  

    soup = BeautifulSoup(content, 'html.parser')
    historicalData = soup.find_all('div', attrs=
                               {'id':'historical-data'})
    for value in historicalData:
        trOccurance = value.find_all('tr', attrs=
                                     {'class':'text-right'})
        for val in trOccurance:
            tdOccurance = val.find_all('td')
            for i in range(len(tdOccurance)):
                if i%5==2:
                    occurances.append(tdOccurance[i].get_text())
                else:
                    continue
    occurances = '-'.join(occurances)
    return occurances
    print(occurances)
createGraph()
