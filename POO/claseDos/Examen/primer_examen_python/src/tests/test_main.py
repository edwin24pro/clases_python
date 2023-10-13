import pytest
from src.main import suma, is_greater_than, new_array, suma_array

def test_suma():
  assert suma(2,5) == 7

@pytest.mark.parametrize(
    "input_x, expected",
    [
      (18,'es mayor'),
      (17,'es menor'),
      (20,'es mayor'),
      (10,'es menor')
    ]
)
def test_is_greater_than(input_x, expected):
  assert is_greater_than(input_x) == expected

@pytest.mark.parametrize(
    "input_arr,input_num,expected",
    [
      ([4,5,9,6],8,[4,5,8,9,6]),
      ([10,15,13,12,18],20,[10,15,20,13,12,18])
    ]
)
def test_new_array(input_arr,input_num,expected):
  assert new_array(input_arr,input_num) == expected

@pytest.mark.parametrize(
    "input_arr,expected",
    [
      ([2,10,8],20),
      ([30,50,12],92)
    ]
)
def test_suma_array(input_arr,expected):
  assert suma_array(input_arr) == expected