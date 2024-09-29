# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Correct factor for Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Correct factor for Celsius to Fahrenheit
FAHRENHEIT_OFFSET = 32  # Offset for Fahrenheit to Celsius conversion

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

# Main script logic
def temperature_conversion():
    try:
        # Prompt the user to enter the temperature
        temp_input = float(input("Enter the temperature to convert: "))

        # Ask whether the input is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {fahrenheit}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {celsius}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Execute the temperature conversion tool
if __name__ == "__main__":
    temperature_conversion()