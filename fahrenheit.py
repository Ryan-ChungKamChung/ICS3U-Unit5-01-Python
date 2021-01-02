#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program converts celsius to fahrenheit

def fahrenheit():
    # Function converts celsius to fahrenheit

    # Process and output
    print("I convert celcius into farenheit!")

    while True:
        # Input
        celsius_string = input("Enter a temperature (ºC): ")

        # Process
        try:
            celsius = int(celsius_string)
            break
        except Exception:
            # Output
            print("This isn't a valid input")

    temperature_in_fahrenheit = celsius * (9/5) + 32
    # Output
    print("The fahrenheit conversion is {}ºF"
          .format(temperature_in_fahrenheit))


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
