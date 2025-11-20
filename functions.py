#CREATE FUNCTIONS FOR MAIN

#PRINCIPAL VERIFICATION
def principalv(): 
    prin = input("How much is the principal of your loan? Please use whole numbers. ")
    try:
        prin = int(prin)
    except ValueError:
        print("Try entering a whole number instead of a string or decimals.")
    else:    
        if prin < 500:
            print("Are you sure you need a micro loan? Why don't you try saving up some money for this purchase :)")    
        elif prin > 10000000:
            print("Whoa there Mr. Moneybags! Why don't you consult your personal wealth manager with this one. ")
        else: prin = int(prin) 
        print(prin) #data validation displays exit value for error checking   

#PAYMENT VERIFICATION
def paymentsv(): 
    pmt = input("How much is the payment of your loan? Please use whole numbers. ")
    try:
        pmt = int(pmt)
    except ValueError:
        print("Try entering a whole number instead of a string or decimals.")
    else:    
        if pmt < 50:
            print("Are you sure you need a micro loan? Why don't you try saving up some money for this purchase :)")    
        elif pmt > 100000:
            print("Whoa there Mr. Moneybags! Why don't you consult your personal wealth manager with this one. ")
        else: pmt = int(pmt) 
        print(pmt) #data validation displays exit value for error checking

#INTEREST VERIFICATION
def interestv(): 
    irate = input("How much is the interest rate per year? Enter as a decimal without a '%' sign. ")
    try:
        irate = float(irate)
    except ValueError:
        print("Try entering a number instead of a string.")
    else:    
        if irate < 0.01:
            print("Did grandma give you this loan? Try using an interest rate greater than or equal to 0.01.")    
        elif irate > 0.30:
            print("What is this, a payday loan? Usuary is a crime. Know your rights.")
        else: irate = float(irate) 
        print(irate) #data validation displays exit value for error checking

#TERM VERIFICATION
def termv(): 
    term = input("What is the term of your loan in years? ")
    try:
        term = int(term)
    except ValueError:
        print("Try entering a whole number instead of a string or decimals.")
    else:    
        if term < 1:
            print("Please try using a term of 1 year or greater.")    
        elif term > 40:
            print("What kind of dystopian term is this? Try using a term of 40 years or less.")
        else: term = int(term) 
        print(term) #data validation displays exit value for error checking

#FUNCTION TO CALCULATE APR
#def apr(prin, irate, term):
#math goes here

#FUNCTION TO GENERATE AMORTIZATION SCHEDULE
#def amort(pmt, prin, irate, term):
#for/while loop goes here

#FUNCTION TO GENERATE A GRAPH
#def graph():
#graph goes here

#FUNCTION TO EXPORT?
#def export():
#export to CSV



#LOAN DETAILS
#def mortgage_calc():
#       principal = float(input("How much is the princiapl of your loan? "))
#    irate = float(input("What is the interest rate? "))
#    term = integar(input("What is the term of the loan in years? "))
#    table = input("Would you like a schedule of payments? Y/N "