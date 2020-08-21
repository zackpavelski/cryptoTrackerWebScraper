import urllib.request as ul
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import wx, wx.grid
class Currency:
    def __init__(self, name):
        self.name = name
        self.url = ""
        self.value = self.getPrice()
    def getURL(self):
        #'https://coinmarketcap.com/currencies/ethereum/'
        self.url = 'https://coinmarketcap.com/currencies/'+self.name
        return
    def getPrice(self):
        req = Request('https://coinmarketcap.com/currencies/'+self.name) # WEBSITE FOR ETH PRICES
        page = urlopen(req).read()  
        soup = BeautifulSoup(page, 'html.parser')
        price_box = soup.find('span', attrs=
                              {'class':'cmc-details-panel-price__price'})
        price = price_box.text
        try:
            #print(price)
            #print("Catch 1 Success")
            return price
        except Exception:
            print("Exception 1")
            try:
                price = price_box
                print(price)
            except Exception:
                print("None type error")
                return
        return
    def getCurrencies(self):
        return open('currencies.txt','a+').read().split("-")
    def writeCurrency(self):
        file = open('currencies.txt','a+').write(self.name+"-").close()
        return
    def getName(self):
        return self.name   
def getCurList():
    file = open('currencies.txt', 'r').read().split('-')
    print("OPENING")
    print(file)
    
    objList = []
    for currency in file:
        temp = Currency(currency)
        objList.append(temp)
    return objList
class OtherFrame(wx.Frame):
    """
    Class used for creating frames other than the main one
    """
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Show()
class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        btn = wx.Button(self, label='Trade ETH/BTC', pos=(0,0))
        btn.Bind(wx.EVT_BUTTON, self.onClick)
        self.frame_number = 1
        btn2 = wx.Button(self, label='ETH Predictions', pos=(100, 0))
        btn2.Bind(wx.EVT_BUTTON, self.onClick2)
        self.frame_number = 1
    def on_new_frame(self, event):
        title = 'SubFrame {}'.format(self.frame_number)
        frame = OtherFrame(title=title)
        self.frame_number += 1
    def onClick(self, event):
        import webbrowser
        url = 'https://www.binance.com/en/trade/ETH_BTC'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    def onClick2(self, event):
        import webbrowser
        url = 'https://smartereum.com/2279/ethereum-price-predictions-2019-cryptocurrencys-value-could-triple-how-high-can-the-price-of-ethereum-go-in-2019-ethereum-news-mon-jan-07/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Links', size=(450, 210))
        panel = MyPanel(self)
        self.Show()
class GridFrame(wx.Frame):
    def OC(self, event):
        import webbrowser
        url = 'https://www.binance.com/en/trade/ETH_BTC'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    def OC2(self, event):
        import webbrowser
        url = 'https://smartereum.com/2279/ethereum-price-predictions-2019-cryptocurrencys-value-could-triple-how-high-can-the-price-of-ethereum-go-in-2019-ethereum-news-mon-jan-07/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    def Refresh(self, event):
        self.Close()
        app = wx.App(0)
        frame = GridFrame(None)
        app.MainLoop()
    def on_new_frame():
        title = 'SubFrame {}'.format(self.frame_number)
        frame = OtherFrame(title=title)
        self.frame_number += 1
    def __init__(self, parent):
        currencies = getCurList()
        self.frame_number = 1       
        wx.Frame.__init__(self, parent, title='CryptoChecker', size=(470, 175))
        if len(currencies) <= 4:
            multiplier = 470
        else:
            multiplier = ((len(currencies) - 4) * 117) + 470
        self.SetMaxSize(size=(multiplier,175))
        self.SetMinSize(size=(multiplier,175))
        grid = wx.grid.Grid(self, -1)
        grid.CreateGrid(2, len(currencies))
        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)
        x = 0
        y = 0
        for cur in currencies:
            grid.SetCellValue(x,y, cur.getName())
            y+=1
        x+=1
        y=0
        for cur in currencies:
            grid.SetCellValue(x,y, cur.getPrice())
            y+=1
        x=0
        y=0
        for i in range(len(currencies)):
            grid.SetColLabelValue(y, 'CURRENCY_'+str(i))
            y+=1
        grid.SetRowLabelValue(0, 'CURRENCY')
        grid.SetRowLabelValue(1, 'COST')
        # 0 0 - 0 1 - 0 2 - 0 3 
        x=0
        y=0
        attr = wx.grid.GridCellAttr()
        attr.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        for i in range(len(currencies)):
            grid.SetReadOnly(x,y)
            grid.SetReadOnly(x+1,y)
            grid.SetAttr(x,y,attr)
            grid.SetAttr(x+1,y,attr)
            y+=1
        x=0
        y=0
        grid.SetLabelBackgroundColour((227,175,188))
        grid.SetDefaultCellBackgroundColour((255,255,255))      
        button = wx.Button(grid, wx.ID_ANY, 'Test', (180, 200))
        button.Bind(wx.EVT_BUTTON, self.OC)     
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, wx.ID_ANY, 'TRADE_ETH')
        qmi2 = wx.MenuItem(fileMenu, wx.ID_ANY, 'CHECK_PREDICTIONS')
        qmi3 = wx.MenuItem(fileMenu, wx.ID_ANY, 'REFRESH')
        fileMenu.Append(qmi)
        fileMenu.Append(qmi2)
        fileMenu.Append(qmi3)
        self.Bind(wx.EVT_MENU, self.OC, qmi)
        self.Bind(wx.EVT_MENU, self.OC2, qmi2)
        self.Bind(wx.EVT_MENU, self.Refresh, qmi3)
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("bitcoin.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.Show()

if __name__ == '__main__':
    app = wx.App(0)
    frame = GridFrame(None)
    app.MainLoop()
