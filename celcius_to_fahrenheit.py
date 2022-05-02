#!/usr/bin/env python3

# Created by Samuel Webster
# Created on May 2022
# This program converts Celcius to fahrenheit using functions


def convert():
    # I calculate circumference

    # input
    str_celcius = input("Enter a temperature (°C): ")

    # process & output
    try:
        flt_celcius = float(str_celcius)
        fahrenheit = 32 + (flt_celcius * 9 / 5)
        print("{0} °C is equal to {1}°F.".format(flt_celcius, fahrenheit))
    except Exception:
        print("Please enter a valid temperature")

    print("\nDone.")


def main():
    convert()


if __name__ == "__main__":
    main()
