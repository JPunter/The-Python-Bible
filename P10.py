#coins

import random

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin spent!")

    def flip(self):
        options = [True, False]
        choice = random.choice(options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "£{} coin".format(int(self.original_value))
        else:
            return "{}p coin".format(int(self.original_value * 100))
    


class OnePence(Coin):
    def __init__(self):
        data = {"original_value": 0.01,
                "clean_colour": "bronze",
                "rusty_colour": "brownish",
                "edges": 1,
                "diameter": 20.3,
                "thickness": 1.6,
                "mass": 3.56,
            }
        super().__init__(**data)


class TwoPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "greenish",
            "edges": 1,
            "diameter": 25.9,
            "thickness": 2.05
            }
        super().__init__(**data)


class FivePence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "edges": 1,
            "diameter": 18.0,
            "thickness": 1.75
            }
        super().__init__(**data)


class TenPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "edges": 1,
            "diameter": 24.5,
            "thickness": 1.85
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

class TwentyPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "edges": 1,
            "diameter": 21.2,
            "thickness": 1.75
            }
        super().__init__(**data)


class FiftyPence(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "edges": 1,
            "diameter": 27.3,
            "thickness": 1.75
            }
        super().__init__(**data)


class OnePound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "edges": 1,
            "diameter": 22.5,
            "thickness": 3.15
            }
        super().__init__(**data)


class TwoPound(Coin):
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "edges": 1,
            "diameter": 28.4,
            "thickness": 2.5
            }
        super().__init__(**data)


coins = [OnePence(), TwoPence(), FivePence(), TenPence(), TwentyPence(),
         FiftyPence(), OnePound(), TwoPound()]

for coin in coins:
    arguments = [coin,  coin.colour, coin.value, coin.diameter, coin.thickness]

    string = "{} - Colour: {}, Value: £{}, Diameter: {}mm, Thickness: {}mm".format(*arguments)
    print(string)
        
