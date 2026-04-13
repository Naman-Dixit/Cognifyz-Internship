def convert_temp():
    print("Temperature Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choose = input("Enter your choice (1 or 2): ")
    if choose == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")

    elif choose == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    convert_temp()