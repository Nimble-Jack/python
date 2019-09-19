def _is_equal(x,y):
    return x == y

try:
    assert True == _is_equal(3,3)
    assert True == _is_equal(3, 2)
    print("they are equal")
except:
    print("they are not equal")
