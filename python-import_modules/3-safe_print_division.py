def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
    
a = 5
b = 6
result = safe_print_division(a, b)
print("{} / {} = {}".format(a, b, result))