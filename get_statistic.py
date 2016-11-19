import json

def readFile(fn):
    with open("data/"+str(fn)+".txt", mode='r+') as rt:
        k = rt.readline()
        we = json.loads(k, encoding='utf-8')
        return we


def getminmax_key(obj):
    a = []
    for key in obj.keys():
       a.append(key)
    return {'min': min(a), 'max': max(a)}



def countData(obj,start, stop):
    sub=[]
    subclass = {}
    for sid in range(start, stop):

        for cs in range(len(obj[str(sid)])):
            sub.append(obj[str(sid)][cs][0])
            sec = {}
            try:
                subclass[str(obj[str(sid)][cs][0])]["count"] += 1
            except Exception:
                subclass[str(obj[str(sid)][cs][0])] = {"count":1}

            subclass[str(obj[str(sid)][cs][0])]["name"] = str(obj[str(sid)][cs][1])

            try:
                subclass[str(obj[str(sid)][cs][0])]["sec"][str(obj[str(sid)][cs][2])].append(str(sid))
            except KeyError:
                try:
                    subclass[str(obj[str(sid)][cs][0])]["sec"]
                except KeyError:
                    subclass[str(obj[str(sid)][cs][0])]["sec"] = {}

                try:
                    subclass[str(obj[str(sid)][cs][0])]["sec"][str(obj[str(sid)][cs][2])].append(str(sid))
                except Exception:
                    subclass[str(obj[str(sid)][cs][0])]["sec"][str(obj[str(sid)][cs][2])] = [str(sid)]
    print(subclass)


def getData(fileID):
    r = readFile(fileID)
    g = getminmax_key(r)
    countData(r,int(g['min']), int(g['max']))