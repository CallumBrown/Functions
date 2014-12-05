#Callum Brown
#05-12-14
#Conversion, imperial + metric



def input_measurments():
    print("1 for imperial")
    print("2 for metric")
    F=0
    I=0
    M=0
    CM=0
    type1 = int(input("Please enter the measurement you are using: "))
    if type1 == 1:
        F = float(input("Please enter the amount of feet there are: "))
        I = float(input("Please enter the amount of inches there are: "))
        
    elif type1 == 2:
        M = float(input("Please enter the amount of metres there are: "))
        CM = float(input("Please enter the amount of centimetres there are: "))
        
    else:
         print("Invalid")
    return type1,F,I,M,CM

def M_I(M,CM):
    CM = CM + (M*100)
    I = CM /2.54
    F = I//12
    I = I%12
    print ("{0:.2f} feet and {1:.2f} inches".format(F,I))

def I_M(F,I):
    I = I + (F*12)
    CM = I * 2.54
    M=CM//100
    CM=CM%100
    print ("{0:.2f} metres and {1:.2f} centimetres".format(M,CM))
    
def choice(type1,M,CM,F,I):
    if type1 == 1:
        I_M(F,I)
    elif type1==2:
        M_I(M,CM)

def main():
    type1,F,I,M,CM = input_measurments()
    choice(type1,M,CM,F,I)
    

main()
