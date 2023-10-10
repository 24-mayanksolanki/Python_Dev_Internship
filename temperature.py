#Temperature converter

#To determine whether the temperature is in Celsius or Fahrenheit
deg = input("Is the temperature in Celsius or Fahrenheit (C/F): ")

#Input temperature value
temp = float(input("Enter the temperature value: "))

#Conversion and output
if deg == "C" or deg == "c":    #Temperature is in Celsius
    temp = round((9*temp) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp}°F" )

elif deg == "F" or deg == "f":    #Temperature is in Fahrenheit
    temp = round((temp-32) * 5 / 9, 2)
    print(f"The temperature in Celsius is: {temp}°C" )

else:      #Temperature is neither is Celsius nor in Fahrenheit
    print(f"{deg} is an invalid degree.")
