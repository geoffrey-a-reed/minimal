import minimal


def test_add_positive_integers():
    assert minimal.add(1, 2) == 3


def test_add_negative_integers():
    assert minimal.add(-1, -2) == -3
    
    
def test_add_zeros():
    assert minimal.add(0, 0) == 0
    

def test_add_strings():
    assert minimal.add('a', 'b') == 'ab'