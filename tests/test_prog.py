import pytest
from main import LiFo, balance_checker

test_str1 = '(((([{}]))))'
test_str2 = '[([])((([[[]]])))]'
test_str3 = '{()}'
test_str4 = '{{[()]}}'

test_bad_str1 = '}{}'
test_bad_str2 = '{{[(])]}}'
test_bad_str3 = '[[{())}]'

answer_good = 'Сбалансированно'
answer_bad = 'Несбалансированно'


def test_good_str():
    assert balance_checker(test_str1) == answer_good
    assert balance_checker(test_str2) == answer_good
    assert balance_checker(test_str3) == answer_good
    assert balance_checker(test_str4) == answer_good


def test_bad_str():
    assert balance_checker(test_bad_str1) == answer_bad
    assert balance_checker(test_bad_str2) == answer_bad
    assert balance_checker(test_bad_str3) == answer_bad
