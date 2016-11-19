import loadData
import get_statistic
import os


def main():
    print("What Do You Want?")
    while True:
        manu()


def manu():
    print("[1] Get Data Form internet")
    print("[2] See my File data")
    print("[3] Get json Statistic")
    print("[4] Exit program")
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
    elif item == 2:
        for x in os.listdir("data"):
            print("\t"+str(x))

    elif item == 3:

        if get_lastest() == 0:
            print("Data not found plz Select Menu [1]")
        else:
            print("Input filename (withOut .txt) or Enter for get lastest file")
            while True:

                y = input(">> ")
                try:
                    if y == "":
                        get_statistic.getData(get_lastest())
                        print("")
                    else:
                        get_statistic.getData(int(y))

                    print("Do you Want to Exit (Y | N)")
                    iex = input(">> ")
                    if iex.lower() == "y" or iex.lower() == "yes":
                        exit(0)
                    break
                except Exception:
                    print("Error file name Wrong try agin")
    elif item == 4:
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


if __name__ == "__main__":
    main()