#Callum Brown
#25-11-14
#output symbols revison ex 1

def input_integer():
    integer = int(input("Please enter a number of times you would like the symbol to be shown: "))
    return integer

def input_character():
    character = input("Please enter a character that you would like to be displayed: ")
    return character

def program(integer,character):
    list1 = ""
    for count in range(integer):
        list1 = list1 + character
    return list1

def display(list1):
    print(list1)

def main():
    integer = input_integer()
    character = input_character()
    list1 = program(integer,character)
    display(list1)

main()

    
