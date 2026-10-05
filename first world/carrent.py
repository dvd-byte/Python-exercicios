diasAlugados = int(input("Enter the number of days you rented the car: "))
kmRodados = float(input("Enter the number of kilometers driven: "))
print(f"The total cost of the car rental is: ${diasAlugados * 60 + kmRodados * 0.15:.2f}")