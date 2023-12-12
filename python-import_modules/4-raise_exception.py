def raise_exception():
    raise TypeError("Exception has been raised")

try:
    raise_exception()
except TypeError as e:
    print()
