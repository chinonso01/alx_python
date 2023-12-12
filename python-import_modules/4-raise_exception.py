def raise_exception():
    raise [Expected]

try:
    raise_exception()
except TypeError as e:
    print()
