from exercicio5 import fizz_buzz

def test_multiples_of_3_become_fizz():
  assert fizz_buzz(4) == [1, 2, "Fizz", 4]

def test_multiples_of_5_become_buzz():
  assert fizz_buzz(10)[5 - 1] is "Buzz"
  assert fizz_buzz(10)[10 - 1] is "Buzz"

def test_multiple_of_3_and_5_become_fizzbuzz():
  assert fizz_buzz(30)[15 - 1] is "FizzBuzz"
  assert fizz_buzz(30)[30 - 1] is "FizzBuzz"