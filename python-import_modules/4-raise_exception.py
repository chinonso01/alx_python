def raise_exception():
    raise TypeError("[Excepted]")

try:
    raise_exception()
except TypeError as e:
    print("Exception raised")
