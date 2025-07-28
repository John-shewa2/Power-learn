# A function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        final_price = price - price * discount_percent/100
        return final_price
    else:
        return price


print("Final Price: ", calculate_discount(2000, 15))


# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
# Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        final_price = price - price * discount_percent/100
        return final_price
    else:
        return price


price = float(input("what is the price: "))
discount_percent = int(input("what is the discount percent: "))

print("Final Price: ", calculate_discount(price, discount_percent))
