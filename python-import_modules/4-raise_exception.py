def raise_exception():
    raise [Exception]

try:
    raise_exception()
except TypeError as e:
    print("Exception raised")
