FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5



# conversion function from F to C
def convert_to_celsius(fahrenheit): 
    return(fahrenheit- 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
     

# conversion function C to F
def convert_to_fahrenheit(celsius): return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    


try:
    temperature= int(input("Enter the temperature to convert: "))
    temperature_type= input("Is this temperature in Celsius or Fahrenheit? (C/F):")

    if temperature_type.upper() == "F":
       
       print(f"{temperature} F is {convert_to_celsius(temperature)}")

    elif temperature_type.upper()== "C":
        print(f" {temperature} °C is {convert_to_fahrenheit(temperature)} F")
    
    else:
        print("Invalid temperature. Please enter a numeric value.")

except ValueError:
    print("invalid input. enter a valid temperature")
