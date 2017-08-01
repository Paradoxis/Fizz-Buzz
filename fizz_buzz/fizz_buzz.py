from typing import Iterator


def fizz_buzz(amount: int=100) -> Iterator[str]:
    """
    Fizz all the buzzes
    :param amount: How many times should we fuzz the bizz?
    :return: An iterator containing all of your fizzable buzzes
    """
    for i in range(1, amount + 1):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 5 == 0:
            yield "Buzz"
        elif i % 3 == 0:
            yield "Fizz"
        else:
            yield str(i)
