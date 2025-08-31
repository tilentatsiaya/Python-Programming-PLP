#
# This program defines a function to calculate a discounted price based on a set condition.
# It then prompts the user for input and displays the final price.
#

def calculate_discount(price, discount_percent):
    
    # Check if the discount percentage is 20 or greater
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price by subtracting the discount
        final_price = price - discount_amount
        # Return the discounted price
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price



# Prompt the user for the original price and convert the input to a float
original_price = float(input("Enter the original price of the item: "))

# Prompt the user for the discount percentage and convert the input to a float
discount_percentage = float(input("Enter the discount percentage: "))

# Call the calculate_discount function with the user's input
final_price = calculate_discount(original_price, discount_percentage)

# Check if the final price is different from the original price to determine if a discount was applied
if final_price < original_price:
    # If a discount was applied, print the final price
    print(f"Final price after applying the discount: ${final_price}")
else:
    # If no discount was applied, print a message and the original price
    print("No discount was applied.")
    print(f"The original price remains: ${original_price}")