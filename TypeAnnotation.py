# Dictionary

from typing import TypeDict

class Movie(TypeDict):
    title: str
    year: int
    rating: float


movie = Movie(title="Dune",year=2021,rating=9)


# Union
from typing import Union

def square(x:Union[int,float]) --> float:
    return x *x

x = 5
x = 1.234

# Optional

from typing import Optional

def nice_message(name:Optional[str]) -> None:
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")

# Any

from typing import Any

def print_value(value:Any):
    print(x)

## Lambda Functions
square = lambda x:x *x
print(square(5))
nums = [1,2,3,4,5]
squares = list(map(lambda x: x *x,nums))
# shortcut to write a smalll function





