import sys

def main():
    
    if len(sys.argv) > 2:
        raise AssertionError("Enter only one argument.")
    elif len(sys.argv) == 2:
        mystr = sys.argv[1]
    else:
        mystr = input("What is the text to count?\n")
    
    counter = {
        'lower letter': 0,
        'upper letter': 0,
        'punctuation mark': 0,
        'space': 0,
        'digit': 0
    }
    
    for char in mystr:
        if (char.islower()):
            counter['lower letter'] +=1
        elif (char.isupper()):
            counter['upper letter'] +=1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            counter['punctuation mark'] +=1
        elif (char.isnumeric()):
            counter['digit'] +=1
        elif (char.isspace()):
            counter['space'] +=1
    _sum = sum(counter.values())
    print(f"The text contains {_sum} character{'s' if counter != 1 else ''}")
    print(*[f"{val} {key}{'s' if val != 1 else ''}" for key, val in counter.items()], sep="\n")
      



if __name__ == "__main__":
    main()