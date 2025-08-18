# 💰 Discount Calculator

## Overview

This project implements a discount calculator function that applies discounts to item prices based on specified criteria. The program calculates the final price after applying a discount only if the discount percentage meets the minimum threshold.

## Assignment Description

Create a function named `calculate_discount(price, discount_percent)` that calculates the final price after applying a discount. The function should take the original price (`price`) and the discount percentage (`discount_percent`) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

Using the `calculate_discount` function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

## Function Requirements

### `calculate_discount(price, discount_percent)`

**Parameters:**
- `price` (float): The original price of the item
- `discount_percent` (float): The discount percentage to apply

**Logic:**
- If `discount_percent >= 20`, apply the discount and return the discounted price
- If `discount_percent < 20`, return the original price unchanged

**Returns:**
- `float`: The final price (either discounted or original)

## Program Flow

1. **Input Collection**: Prompt user for original price and discount percentage
2. **Discount Calculation**: Call `calculate_discount()` function with user inputs
3. **Output Display**: Show the final price with appropriate messaging