import loadData
import get_statistic
import os
from collections import OrderedDict


def main():
    print("What Do You Want?")
    while True:
        manu()


def manu():
    print("[1] Get Data Form internet")
    print('[7] Get Data From internet V2.0 (new)')
    print("[2] See my File data")
    print("[3] Get json Statistic")
    print("[4] Get only subject name")
    print("[5] View people in Class")
    print("[6] Exit program")
    item = int(input(">> "))
    if item == 1:
        mi=580610614
        ma=580610695
        while True:
            mi = int(input("Min Students ID : "))
            ma = int(input("max Students ID : "))
            if ma == 0 and mi == 0:
                print("Welcome CPE now i get for U")
                mi = 580610614
                ma = 580610695
                break
            elif mi <= ma:
                print("OK I get it")
                break
            else:
                print("Min should less than max. Try agine")

        print("Wait Me Now i get data Form internet")
        loadData.get_user(mi, ma)
    elif item == 7:
        sample_sid = 0
        id = 1
        while True:
            sample_sid = int(input("Start Students ID in faculty: "))
            if sample_sid == 0:
                print("Welcome CPE now i get for U")
                sample_sid = '580610614'
                id = 6
                break

        print("Wait Me Now i get data Form internet")
        year = '25'+str(sample_sid)[0:2]

        loadData.get_user_v2(id, year)


    elif item == 2:
        for x in os.listdir("data"):
            print("\t"+str(x))

    elif item == 3:
        menu_item3(0)

    elif item == 4:
        menu_item4()

    elif item == 5:
        r = menu_item3(1)
        menu_item4()
        print("Enter subject ID")
        sbid = input(">> ")
        try:
            print("\n"+str(sbid)+" "+str(r[sbid]['name']))
            for n in r[sbid]['sec']:
                for sid in r[sbid]['sec'][n]:
                    print("\t"+str(sid))
            print()
        except Exception:
            print("Not found this subject in list")

    elif item == 6:
        exit(0)

    else:
        print("Sorry I don't know this item\n")


def get_lastest():
    a = []
    for x in os.listdir("data"):
        a.append(str(x).split(".")[0])
    if a == []:
        a.append(0)
    return int(max(a))


def menu_item3(arg):
    r = ""
    if get_lastest() == 0:
        print("Data not found plz Select Menu [1]")
    else:
        if arg == 0:
            print("Input filename (withOut .txt) or Enter for get lastest file")
        while True:

            if arg == 0:
                y = input(">> ")
            else:
                y = ""
            try:
                if y == "":
                    r = get_statistic.getData(get_lastest())
                    if arg == 0:
                        print(r)
                    print("")
                else:
                    r = get_statistic.getData(int(y))
                    print(r)

                if arg ==0:
                    print("Do you Want to Exit (Y | N)")
                    iex = input(">> ")
                    if iex.lower() == "y" or iex.lower() == "yes":
                        exit(0)
                break
            except Exception as e:
                print("Error file name Wrong try agin",str(e) )

        return r


def menu_item4():
    r = menu_item3(1)
    itemlist = {}
    print("------------------")
    for x in r:
        itemlist[x] = r[x]['name']
    keylist = itemlist.keys()
    keylist = sorted(keylist)
    for key in keylist:
        print('({counter})'.format(counter=r[key]['count']),key, itemlist[key])
    print("------------------\n")



if __name__ == "__main__":
    main()