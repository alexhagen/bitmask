from bitmask import Bitmask

def test_init():
    bm = Bitmask(True, True, True, True)
    assert str(bm) == '1111'
    assert bm[0]
    bm = Bitmask('1111')
    assert str(bm) == '1111'
    assert bm[0]


def test_compare():
    bm1 = Bitmask(True, True, False, None, False)
    bm2 = Bitmask('11X00')
    assert bm1 == bm2

if __name__ == "__main__":
    test_init()
    test_compare()