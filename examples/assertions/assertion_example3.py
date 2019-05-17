
try:
    assert ( 1 < 0)
except AssertionError:
    print("assert error found")
finally:
    print("Finally")

    # assert error    found
    # Finally
