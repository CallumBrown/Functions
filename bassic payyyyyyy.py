#Cally B
#18-11-14
#defining a function

def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total

def calculate_overtime_pay(hours,pay):
    overtime_pay = (hours - 40) * (pay*1.5)
    basic_pay = 40 * pay
    total = overtime_pay + basic_pay 
    return total

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def work_details():
    hours = int(input("Please enter the amount of hours you have worked: "))
    pay = int(input("Please enter your pay rate: "))
    return hours, pay

def display_total_pay(total):
    print(total)

def calculate_pay():
    hours, pay = work_details()
    total = calculate_total_pay(hours,pay)
    display_total_pay(total)

calculate_pay()
    
    
