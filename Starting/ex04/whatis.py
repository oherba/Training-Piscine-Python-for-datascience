import sys

if (len(sys.argv) == 2 ):
    try:
        nbr =  int(sys.argv[1])
    except :
        print('AssertionError: argument is not an integer')
    else:
        if((int(sys.argv[1]) % 2) == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.") 
if (len(sys.argv) > 2):
    print('AssertionError: more than one argument is provided')