while True:
    tc = int(input("Enter the temperature in Celsius: "))
    conversor = (tc * 9/5) + 32
    print(f"{tc}°C is equal to {conversor}°F.")
    choice = input("Do you want to convert another temperature? (yes/no): ")
    if choice.lower() != "yes":
        print("Thank you for using the temperature conversor!")
        break