def amount_of_money_and_price_of_apple():
    Money = int(input("Money you have: "))
    Apple = int(input("Price of the apple:"))
    return Money, Apple

def compute_amount():
    apples_you_can_get = (Money // apple_price)
    remaining_money = (Money & (apples_you_can_get // Apple))
    you_can_get = (Money & (apples_you_can_get // Apple))
    return apples_you_can_get, remaining_money, you_can_get

def display_remaining_money(remaining_money):
    print(f"You can buy {apples_you_can_get} apples and your change is {remaining_money} pesos.")






#Create a program which you will enter the amount of money you have, 
# it will also ask for the price of an apple.
print("How much money do you have?: ")
Apple, Money = amount_of_money_and_price_of_apple()
#Display the maximum number of apples that you can buy and the remaining money that you will have.
apple_price = Apple
apples_you_can_get = compute_amount
remaining_money = Money, apple_price, Apple
#Display the output in the following format.

#You can buy ___ apples and your change is ___ pesos.
display_remaining_money = remaining_money
