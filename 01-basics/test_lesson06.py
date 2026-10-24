from lesson06_functions import is_even, reverse_string, count_vowels

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True

def test_reverse_string():
    assert reverse_string('ayet') == 'teya'
    assert reverse_string('') == ''

def test_count_vowels():
    assert count_vowels('hello') == 2
    assert count_vowels('xyz') == 0