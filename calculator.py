#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 2, 2025
# This program asks the user for their grade level and
# tells them their percentage


def calculate(sign, first_number, second_number):
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        if second_number != 0:
            return first_number / second_number
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation."


def main():
    valid_sign = "+, -, *, /"

    while True:
        sign = input("Enter a valid sign: ")
        if sign in valid_sign:
            break
        else:
            print("Please enter a valid sign (+, -, *, /): ")
    while True:
        try:
            first_number = float(input("Enter a positive number: "))
            second_number = float(input("Enter a second positive number: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    result = calculate(sign, first_number, second_number)
    print("Result:", result)


if __name__ == "__main__":
    main()
