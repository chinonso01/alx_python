def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
    
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print("{}".format(safe_print_division(a, b)))