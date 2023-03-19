from home1 import MyOwnThread
while(True):

    t = input("Enter filename: ")
    if t == "end":
        break
    try:
        with open(t, "r") as file:
            p = MyOwnThread(t, 1)
            p.start()
    except  Exception as Ex:
            print(str(Ex))