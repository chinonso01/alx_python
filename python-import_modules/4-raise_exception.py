def raise_exception():
    raise TypeError()

try:
    raise_exception()
except TypeError as e:
    print("Exception raised")
