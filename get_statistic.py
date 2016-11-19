import json
import pprint


def readFile(fn):
    with open(str(fn)+".txt", mode='r+') as rt:
        k = rt.readline()
        we = json.loads(k, encoding='utf-8')
        return we

def countData(obj,start, stop):
    sub=[]
    subclass = {}
    secStudent = {}
    section = {}
    print(subclass)

    for sid in range(start, stop + 1):

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

            #print("-------------------------")
            #print(str(obj[str(sid)][cs][3]))
            #print(str(obj[str(sid)][cs][0])+"\t"+str(obj[str(sid)][cs][2])+"\t"+str(obj[str(sid)][cs][3]))

    print(sub.count('261200'))
    print(subclass)


def main(s,e):
    countData(readFile("20161119150631"), s, e)

if __name__ == "__main__":
    main(614,695)