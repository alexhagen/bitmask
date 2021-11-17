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

def test_desc():
    bm = Bitmask('11X00',
                 columns=['it is hot', 'it is sunny',
                          'it is humid', 'it has rained',
                          'the ground is wet'
                         ])
    desc = bm.desc()
    assert desc == 'if it is hot and it is sunny and not it has rained and not the ground is wet'

if __name__ == "__main__":
    test_init()
    test_compare()
    test_desc()