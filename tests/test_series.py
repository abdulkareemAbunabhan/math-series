import pytest
from a_series.series import fibonacci,lucas,sum_series

def test_fibonacci1():
    actual=fibonacci(1)
    expected=1
    assert actual==expected

def test_fibonacci0():
    actual=fibonacci(0)
    expected=0
    assert actual==expected

def test_fibonacci5():
    actual=fibonacci(5)
    expected=5
    assert actual==expected    

def test_fibonacci37():
    actual=fibonacci(11)
    expected=89
    assert actual==expected     

def test_lucas1():
    actual=lucas(1)
    expected=1
    assert actual==expected

def test_fibonacci0():
    actual=lucas(0)
    expected=2
    assert actual==expected

def test_lucas3():
    actual=lucas(3)
    expected=4
    assert actual==expected    

def test_lucas11():
    actual=lucas(11)
    expected=199
    assert actual==expected     


def test_sum_series():
    actual=sum_series(1)
    expected=1
    assert actual==expected

def test_sum_series0():
    actual=sum_series(0)
    expected=0
    assert actual==expected

def test_sum_series3():
    actual=sum_series(3)
    expected=2
    assert actual==expected    

def test_sum_series11():
    actual=sum_series(11)
    expected=89
    assert actual==expected     