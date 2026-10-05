ActualPrice = float(input("Enter the actual price of the product: "))
DiscountPercentage = float(input("Enter the discount percentage: "))
DiscountAmount = ActualPrice * (DiscountPercentage / 100)
FinalPrice = ActualPrice - DiscountAmount
print(f"The discount amount is: ${DiscountAmount:.2f}")
print(f"The final price after discount is: ${FinalPrice:.2f}")