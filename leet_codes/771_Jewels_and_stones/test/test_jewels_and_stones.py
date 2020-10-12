from solution.jewels_and_stones import jewels

def test_jewels():
    J, S = "aA","aAAbbbb"
    res = jewels(J,S)
    assert res == 3

