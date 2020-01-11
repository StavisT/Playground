# how to use class with type assertion and config files
import json
from utils import Typed, typeassert

app_state_types = json.load(open('data/app_state_types.json'))

@typeassert(**app_state_types)
class Stock2:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def monetary_value(self):
        return self.shares * self.price

if __name__ == '__main__':
    app_state = json.load(open('data/app_state.json'))
    apple = Stock2(**app_state)
    apple_share_value = apple.monetary_value
    print(apple_share_value)


# other example:
# @typeassert(name=str, shares=int, price=float)
# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price