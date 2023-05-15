def reverse_number(number):
    # Convert the number to a string
    number_str = str(number)

    # Check if the number is negative
    is_negative = False
    if number_str[0] == '-':
        is_negative = True
        number_str = number_str[1:]  # Remove the negative sign

    # Reverse the number string
    reversed_str = number_str[::-1]

    # Remove leading zeros if any
    reversed_str = reversed_str.lstrip('0')

    # Add back the negative sign if necessary
    if is_negative:
        reversed_str = '-' + reversed_str

    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)

    return reversed_number


# Example usage
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
