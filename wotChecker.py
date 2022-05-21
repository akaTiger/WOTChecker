import urllib.request as web
from html.parser import HTMLParser

class wot(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.location = None
        self.stats = []
        self.truck = []
        self.urlData = goOver(self)
        self.setId()
        self.getContent()
        
    def setId(self, id=None):
        if id != None:
            self.id = id
        else:
            usrin= input("Please enter your WOT usr id:\n")
            if usrin == "":
                id = 7156437
            else:
                id = int(usrin)
            self.id = id
    
    def setName(self, name):
        self.name = name
    
    def setLocation(self, where):
        self.location = where
            
    def getContent(self):
        response = web.urlopen("https://www.worldoftrucks.com/en/" + "/profile/" + str(self.id))
        raw = response.read().decode()
        mainAt = str(raw).find('<div class="main-wide">')
        body = raw[mainAt:]
        self.urlData.feed(body)

class goOver(HTMLParser):
    def __init__(self, obj: wot):
        super().__init__()
        self.__TAGS__ = {
            0: "a",
            1: "img",
            2: "div"
        }
        self.__TARGET__ = False
        self.__NONSTOP_TARGET__ = False
        self.result = obj
        self.noStop = 0
    def handle_starttag(self, tag, attrs):
        if (tag == self.__TAGS__[0]):
            try:
                if (attrs[0] == ('title', 'View user profile')):
                    self.__TARGET__ = "name"
            except:
                pass
        elif (tag == self.__TAGS__[1]):
            try:
                if ('/img/flags/' in attrs[0][1]):
                    self.result.setLocation(attrs[2][1])
            except:
                pass
        elif (tag == self.__TAGS__[2]):
            try:
                if (attrs[0] == ("class", "stats")):
                    self.__NONSTOP_TARGET__ = "stats"
                    self.noStop = 8
                elif (attrs[0] == ("class", "truck")):
                    self.__NONSTOP_TARGET__ = "truck"
                    self.noStop = 15
            except:
                pass
    
    def handle_endtag(self, tag):
        self.__TARGET__ = False
        
    def handle_data(self, data):
        if self.__TARGET__ == "name":
            self.result.setName(data)
        elif self.noStop == 0:
            self.__NONSTOP_TARGET__ == False
        elif self.noStop != 0:
            if self.__NONSTOP_TARGET__ == "stats":
                self.result.stats.append(data.strip())
            elif self.__NONSTOP_TARGET__ == "truck":
                self.result.truck.append(data.strip())
            self.noStop -= 1
        
        
