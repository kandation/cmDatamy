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
    #print(subclass)
    return subclass

def countData_v2(obj):
    sub=[]
    subclass = {}


    for dsid in obj:
        sid = dsid

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
    #print(subclass)
    print(subclass)
    return subclass


def getData(fileID):
    r = readFile(fileID)
    g = getminmax_key(r)
    return countData_v2(r)