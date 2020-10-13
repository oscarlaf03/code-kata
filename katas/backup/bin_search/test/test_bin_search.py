from solution.bin_search import positive_int, sorted_array, bin_search
import pytest

def test_positive_int():
    assert positive_int() > 0

def test_sorted_array():
    arr = sorted_array()
    assert arr[0] < arr[len(arr)-1]


my_array = [1,2,3,4,5,6,7,8,9,900,1200,15000]

def test_bin_search_should_not_find():
    target = 750
    res = bin_search(my_array,target)
    assert res is False


def test_bin_search_should_find():
    target = 4
    res = bin_search(my_array,target)
    assert res is True