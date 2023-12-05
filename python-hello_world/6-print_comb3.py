for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        combination = "{:02}".format(tens_digit * 10 + ones_digit)
        if ones_digit < 9:
            print(combination + ", ", end="")
        else:
            print(combination)

# To move to the next line after printing all combinations
print()

