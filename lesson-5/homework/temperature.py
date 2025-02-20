def convert_cel_to_far(celcius):
    fahrenheit = round((celcius * 9 / 5 + 32), 2)
    print(f"{celcius} degree celcius = {fahrenheit} degrees fahrenheit")
def convert_far_to_cel(fahrenheit):
    celcius = round(((fahrenheit-32) * 5 / 9), 2)
    print(f"{fahrenheit} degree fahrenheit = {celcius} degrees celcius")


celcius = float(input("Enter the temperature in celcius: "))
convert_cel_to_far(celcius)

fahrenheit = float(input("Enter the temperature in fahrenheit: "))
convert_far_to_cel(fahrenheit)