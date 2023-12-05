for number in range(100):
    formatted_number = "{:02}".format(number)
    if number < 99:
        print(formatted_number + ", ", end="")
    else:
        print(formatted_number)