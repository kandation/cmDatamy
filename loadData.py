from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import time
import requests
import json
import codecs

def scanData(start, stop):
    finalData = {}
    for sid in range(start, stop + 1):
        print("Now Scan " + str(sid))

        url = "https://www3.reg.cmu.ac.th/regist259/public/result.php?id=" + str(sid)
        res = requests.get(url)
        res.encoding = 'tis-620'
        raw = res.text

        soup = BeautifulSoup(raw, "html.parser")
        data = soup.find_all('tr', {"class": "msan8"})

        i = 0
        n = 0
        cs = []
        lec = []
        nam = []
        lab = []

        stdList = []
        listData = []

        if (len(data) > 0):
            for num in range(2, len(data)):
                raw_sidData = data[num].find_all('td')
                if (len(raw_sidData) > 0):
                    if (raw_sidData[0].text.isnumeric()):
                        for num2 in range(1, len(raw_sidData)):
                            #print (raw_sidData[num2].text)
                            ty = raw_sidData[num2].text.strip()
                            listData.append(ty)
                        list2 = [x for x in listData if x != []]

                    stdList.append(list2)
                    listData = []

        else:
            print("\tNow Scan " + str(sid) + " not regist!")

        finalData[sid] = stdList
        sleep(1)
        # print(json.dumps(finalData, indent=4))
    return finalData

def calData(obj,start, stop):
    print(obj)
    for sid in range(start, stop+1):
        for cs in range(len(obj[str(sid)])):
            for nsub in range(len(obj[str(sid)][cs])):
                print (obj[str(sid)][cs][nsub])


def writeFile(js,fn):
    with open("data/"+str(fn)+".txt", mode='a+', encoding='utf-8') as rt:
        rt.write(js)
        rt.close()

def readFile(fn):
    with open("data/"+str(fn)+".txt", mode='r+') as rt:
        k = rt.readline()
        we = json.loads(k, encoding='utf-8')
        return we

def countData(obj,start, stop):
    sub=[]
    for sid in range(start, stop + 1):
        for cs in range(len(obj[str(sid)])):
            sub.append(obj[str(sid)][cs][0])
            print(str(obj[str(sid)][cs][0])+"\t"+str(obj[str(sid)][cs][2])+"\t"+str(obj[str(sid)][cs][3])+"\t"+str(obj[str(sid)][cs][1]))

    print(sub.count('261200'))


def get_user(s,e):
    t0 = time.clock()
    j = json.dumps(scanData(s, e))
    print("Now i create new file")
    a = datetime.now().strftime('%Y%m%d%H%M%S')
    writeFile(j,a)
    #calData(readFile(a), s, e)
    #countData(readFile("20161119150631"), s, e)




