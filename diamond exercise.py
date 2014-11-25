#Callum Brown
#25-11-14
#diamond exercise

def input_odd_number():
    odd_number = int(input("Please enter an odd number: "))
    return odd_number

def bottom_half(odd_number):
    counter = odd_number -2
    if odd_number % 2 == 1:
        while counter >0:
            list1 = ""
            for count in range(counter):
                list1 = list1 + "*"
            counter = counter - 2
            print("{0:^{1}}".format(list1,odd_number))

def top_half(odd_number):
    counter = 1
    if odd_number % 2 == 1:
        while counter <= odd_number:
            list1 = ""
            for count in range(counter):
                list1 = list1 + "*"
            counter = counter + 2
            print("{0:^{1}}".format(list1,odd_number))

def diamond():
    odd_number = input_odd_number()
    top_half(odd_number)
    bottom_half(odd_number)

diamond()





