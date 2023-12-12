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
    

print("{}".format(safe_print_division(5, 7)))