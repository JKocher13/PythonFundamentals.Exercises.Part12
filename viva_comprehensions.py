from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Creates a list that starts at the variable start(inclusive) and ends at the
    variable stop. It will give you even odd or even numbers depending on the
    variable Parity

    :param start: and int representing the start of the range
    :param stop: and int representing the end of the range
    :param parity: will determine if number is odd or even
    :return: List[int]
    """
    if parity == Parity.ODD:
        x = [value for value in range(start,stop)if value%2!=0]
        return x
    if parity == Parity.EVEN:
        x = [value for value in range(start,stop)if value%2==0]
        return x


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start: and int representing the start of the range
    :param stop: and int representing the end of the range
    :param strategy: will determine how to manipulate the range
    :return: Dict
    """
    x = {value : strategy(value) for value in range(start,stop)}
    return x

def gen_set(val_in: str) -> Set:
    """
    this function does something  that Roberto wants it to do and 
    still not sure how to put it into words

    :param val_in: str
    :return: Set
    """
    if val_in.islower():
        a = []
        for i in val_in:
            a.append(i.upper())
        return set(a)
    elif not val_in.isupper():
        a = []
        for i in val_in:
            if i.islower():
                a.append(i.upper())
        return set(a)
    elif val_in.isupper():
        return set()
