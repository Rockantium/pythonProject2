# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def strengthen_password(password):
    strengthened_password = ""

    for char in password:
        if char == 'i':
            strengthened_password += '!'
        elif char == 'a':
            strengthened_password += '@'
        elif char == 'm':
            strengthened_password += 'M'
        elif char == 'B':
            strengthened_password += '8'
        elif char == 'o':
            strengthened_password += '.'
        else:
            strengthened_password += char

    strengthened_password += 'q*s'
    return strengthened_password


# Test the program
input_password = input("Enter a simple password: ")
stronger_password = strengthen_password(input_password)
print("The stronger password is:", stronger_password)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
