#Write a program using functions to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)

print(f"Temperature in Fahrenheit: {f}")
