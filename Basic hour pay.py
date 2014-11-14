#Callum Brown
#14-11-14

basic_rate = float(input("Please enter your basic rate: "))
basic_hours = float(input("Please enter your basic amount of hours: "))
overtime = float(input("Please enter your everytime hourse : "))

hours = basic_hours + overtime
basic_pay = hours * basic_rate
basic_pay = round(basic_pay,2)
print("You should get £{0}".format(basic_pay))
