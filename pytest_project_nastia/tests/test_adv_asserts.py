def test_bigger_then_zero():
    a = 25
    assert a > 0

def test_word_in_str():
    a = "hello world"
    assert "hello" in a

def test_list():
    list_1 = [1, 5, 6]
    assert len(list_1) > 0

def test_length():
    list_2 = [1, 2, 5]
    assert len(list_2) == 3

def test_type():
    a = 666
    assert isinstance(a, int)

    