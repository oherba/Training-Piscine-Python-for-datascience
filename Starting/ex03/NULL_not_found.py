def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing: {}".format(object),end=" ")
    elif object != object:
        print("Cheese: {}".format(object),end=" ")
    elif object == 0:
        print("Zero: {}".format(object),end=" ")
    elif object == '':
        print("Empty: {}".format(object),end=" ")
    elif object == False:
        print("Fake: {}".format(object),end=" ")
    else:
        print("Type not Found")
        return 1
    print(type(object))
    return 0