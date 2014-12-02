#Callum Brown
#28-11-14
#conversion activity




def input_conversion():
    from_conversion = input("Please enter the currencey you are using now (pound,euro,dollar): ")
    to_conversion = input("Please enter the currency you would like to change to(pound,euro,dollar): ")
    amount = float(input("Please enter the amount you would like to be converted: "))
    return from_conversion, to_conversion, amount
#£££
def converting_from_pounds(to_conversion, from_conversion,amount):
          if to_conversion == "dollar":
              GBP_dollar(amount)
          elif to_conversion == "euro":
              GBP_euro(amount)
          else:
              print("Nah")
def GBP_dollar(amount):
    total = amount * 1.601
    print("{0:.2f}".format(total))

def GBP_euro(amount):
    total = amount * 1.229
    print("{0:.2f}".format(total))

#€€€€
def converting_from_euro(to_conversion, from_conversion,amount):
          if to_conversion == "pound":
              euro_GBP(amount)
          elif to_conversion == "dollar":
              euro_dollar(amount)
          else:
              print("Nah")

def euro_GBP(amount):
    total = amount * 0.814
    print("{0:.2f}".format(total))

def euro_dollar(amount):
    total = amount * 1.302
    print("{0:.2f}".format(total))

#$$$$$$

def converting_from_dollars(to_conversion, from_conversion,amount):
          if to_conversion == "pound":
              dollar_GBP(amount)
          elif to_conversion == "euro":
              dollar_euro(amount)
          else:
              print("Nah")
def dollar_GBP(amount):
    total = amount * 0.625
    print("{0:.2f}".format(total))

def dollar_euro(amount):
    total = amount * 0.768
    print("{0:.2f}".format(total))





def converting_from_dollars(to_conversion, from_conversion,amount):
          if to_conversion == "pound":
              dollar_GBP(amount)
          elif to_conversion == "euro":
              dollar_euro(amount)
          else:
              print("Nah")

def currency_conversion(from_conversion,to_conversion,amount):
          if from_conversion == "pound":
              converting_from_pounds(to_conversion,from_conversion,amount)
          elif from_conversion == "euro":
              converting_from_euro(to_conversion,from_conversion,amount)
          else:
              converting_from_dollars(to_conversion,from_conversion,amount)

def conversion():
          to_conversion,from_conversion,amount = input_conversion()
          total = currency_conversion(to_conversion,from_conversion,amount)

conversion()


              
              
              
              
              
              
              
                            
    

          
    
    
