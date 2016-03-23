ACTIV_RESULT = "https://activufrj.nce.ufrj.br/rest/"\
    "evaluation/result/%s/Participacao%s_"
ACTIV = "https://activufrj.nce.ufrj.br"
from urllib.request import urlopen
import json
import urllib


class Plot(object):
    """Plot votings for a community in ACTIV"""
    def __init__(self, year="15", community="Inteligencia_Coletiva"):
        super(Plot, self).__init__()
        self.request = ACTIV_RESULT % (community, year)

    def login(self, url=ACTIV):
        jdata = urlopen(url).readall()
        xsrf = jdata.decode('utf-8').split(
            '<input type="hidden" name="_xsrf" value="')[1].split('"/>')[0]
        pdata = dict(_xsrf=xsrf, user="carlo", passwd="labase4ct1v")
        data = urllib.parse.urlencode(pdata).encode('ascii')
        print(data)

        #  request = urllib.request.Request(url=url, data=data)

        result = urlopen(url+"/login", pdata).readall()
        print(xsrf, result)

    def read(self):
        jdata = urlopen(self.request + "01").readall()
        print(jdata)
        data = json.loads(jdata.decode('utf-8'))
        print(data)

if __name__ == "__main__":
    #  Plot().read()
    Plot().login()
    pass
