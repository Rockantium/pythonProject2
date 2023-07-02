# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def make_stronger_password(password):
  """Makes a password stronger by replacing characters and appending "q*s" to the end.

  Args:
    password: The password to make stronger.

  Returns:
    The stronger password.
  """

  password = password.replace("i", "!")
  password = password.replace("a", "@")
  password = password.replace("m", "M")
  password = password.replace("B", "8")
  password = password.replace("o", ".")
  return password + "q*s"


def main():
  password = input("Enter a password: ")
  stronger_password = make_stronger_password(password)
  print(f"The stronger password is: {stronger_password}")


if __name__ == "__main__":
  main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
