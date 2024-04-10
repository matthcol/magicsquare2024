import pytest

from checker import is_magic_rows, magic_sum
from data import *

def test_is_magic_rows_ok_1():
    assert is_magic_rows(square3_ok, 3, 15)
    
def test_is_magic_rows_ko_1():
    assert not is_magic_rows(square3_ko_row, 3, 15)
    
@pytest.mark.parametrize(
    ["square", "n", "ms"], 
    [
        (square3_ok, 3, 15),
        (square5_ok, 5, 65),
        (square12_willem_barink, 12, 870),
    ],
    ids=[
        "size 3",
        "size 5",
        "size 12",
    ]
)
def test_is_magic_rows_ok(square, n, ms):
    assert is_magic_rows(square, n, ms)

@pytest.mark.parametrize(
    ["square", "n", "ms"], 
    [
        (square3_ko_row, 1, 15),
        (square4_josep_maria_subirachs, 4, 34),
    ],
    ids=[
        "2 bad rows",
        "other sum"
    ]
)
def test_is_magic_rows_ko(square, n, ms):
    assert not is_magic_rows(square, n, ms)
    
# Exercise
# 1 test only: n= 3
def test_magic_sum_1():
    assert magic_sum(3) == 15
    

# with @pytest.mark.parametrize
@pytest.mark.parametrize(
    ["n", "ms"], 
    [
        (1, 1), 
        (3, 15),
        (4, 34),
        (5, 65),
        (8, 260),
        (12, 870),
    ]
)
def test_magic_sum(n, ms):
    assert magic_sum(n) == ms
    
