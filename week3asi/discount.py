#creating a function to calculate final price
def calculate_discount(price, discount_percent):
    message = "The final price is "

    #condition to check if the discount percentage is greater than or equal to 20%
    if discount_percent >= 20:
        finalprice = price - (price * (discount_percent/100))
        print(message + str(finalprice)) #converting the final price to string for string concatination

    elif discount_percent < 0:
        print("You can not apply a negative discount")

    else:
        finalprice = price
        print(message + str(finalprice))
    
#using the function to prompt user to enter the required data
calculate_discount(price = int(input("Enter the original price of the item: ")), discount_percent = int(input("Enter the discount percentage: ")))