#Callum Brown
#25-11-14
#revison ex 2

def input_odd_number():
    odd_number = int(input("Please enter an odd number: "))
    return odd_number

def main(odd_number):
    counter = odd_number
    if odd_number % 2 == 1:
        while counter >0:
            list1 = ""
            for count in range(counter):
                list1 = list1 + "*"
            counter = counter - 2
            print("{0:^{1}}".format(list1,odd_number))

def display(odd_number):
    main(odd_number)

def pyramid():
    odd_number = input_odd_number()
    main(odd_number)
    

pyramid()

    

            
        
    
