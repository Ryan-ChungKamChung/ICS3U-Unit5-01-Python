#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Program prints integers in the range of 1000 and 2000

def fahrenheit():
    # Function prints integers in the range of 1000 and 2000

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
            # Outtput
            print("This isn't a valid input")

    temperature_in_fahrenheit = celsius * (9/5) + 32

    print("The fahrenheit conversion is {}ºF"
          .format(temperature_in_fahrenheit))


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
