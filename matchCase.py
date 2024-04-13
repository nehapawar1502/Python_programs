x= 4

match x:
    case 0:
        print("0")
    case 1:
        print("1")
    case 2:
        print("2")
    case 4:
        print("4")
    # below is the default case we can tak 4 cases of default
    case _ if x!= 5:
        print(x)
    case _ if x!= 4:
        print(x)
    case _:
        print("error")