## Declare function ##
def CalculateCustomerID():
    ## user input for name ##
    Surname = input("Key in Surname")
    ## find the length of surname ##
    Length = len(Surname)
    ## create the value of CustomerID for later use ##
    CustomerID = 0
    ## begin for loop so that entire name is covered ##
    for i in range(Length):
        ## NextChar will equal the single character that is in i location of the string (starting from zero) ##
        NextChar = Surname[i]
        ## NextCodeNumber will equal the denary value of said specific ASCII value (NextChar being the ASCII value) ##
        NextCodeNumber = ord(NextChar)
        ## CustomerID just sums the denary value (integer)##
        CustomerID += NextCodeNumber
    ## output of denary value found within CustomerID after full name is covered ##
    print("customer ID is",CustomerID)
## run the function
CalculateCustomerID()
