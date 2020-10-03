import random

class Coin:
    def __init__(self, rare=False, clean=True,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        # not all coins are rare.If coin is rare , its value increases by 25%
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rust_color

    # not all coins turn green when rusty
    def rust(self):
        self.color = self.rusty_color

    # not all coins are gold when clean
    def clean(self):
        self.color = self.clean_color

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
 #This method is called when print() or str() function is invoked on an object
    def __str__(self):
        if self.original_value >= 1:
            return "£{} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))


class One_Pence(Coin):
    def __init__(self):
        data = {"original_value": 0.01,
                "clean_color": "bronze",
                "rusty_color": "brownish",
                "num_edges": 1,
                "diameter": 20.3,
                "thickness": 1.52,
                "mass": 3.56,
                }
        super().__init__(**data)

class Two_Pence(Coin):
    def __init__(self):
        data = {"original_value": 0.02,
                "clean_color": "bronze",
                "rusty_color": "brownish",
                "num_edges": 1,
                "diameter": 25.9,
                "thickness": 1.85,
                "mass": 7.12,
                }
        super().__init__(**data)

pence_coin = Two_Pence()
# print(pence_coin.color)
class Five_Pence(Coin):
    def __init__(self):
        data = {"original_value": 0.05,
                "clean_color": "silver",#we need to override this new behaviour and redefine rust & clean method.Polymorphisms
                "rusty_color": None,
                "num_edges": 1,
                "diameter": 18.0,
                "thickness": 1.77,
                "mass": 3.25,
                }
        super().__init__(**data)
#     #polymorphism - same function name - different versions/forms of itself.
#     #Here we override original rust method in parent class to define new clean & rust colors
    def rust(self):
        self.color=self.clean_color

#
class Ten_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.10,
                "clean_color":"silver",
                "rusty_color":None,
                "num_edges" : 1,
                "diameter": 24.5,
                "thickness": 1.85,
                "mass":6.50,
            }

        super().__init__(**data)
    #polymorphism - same function name - different versions/forms of itself.
    #Here we override original rust method in parent class to define new clean & rust colors
    def rust(self):
        self.color=self.clean_color

class Twenty_Pence(Coin):
    def __init__(self):
        data = {"original_value": 0.20,
                "clean_color": "silver",
                "rusty_color": None,
                "num_edges": 7,
                "diameter": 21.4,
                "thickness": 1.7,
                "mass": 5.00,
                }

        super().__init__(**data)
    #polymorphism - same function name - different versions/forms of itself.
    #Here we override original rust method in parent class to define new clean & rust colors
    def rust(self):
        self.color=self.clean_color

class Fifty_Pence(Coin):
    def __init__(self):
        data = {"original_value": 0.50,
                "clean_color": "silver",
                "rusty_color": None,
                "num_edges": 7,
                "diameter": 27.3,
                "thickness": 1.78,
                "mass": 8.00,
                }

        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color


class One_Pound(Coin):
    def __init__(self):
        data={"original_value":1.00,"clean_color":"gold","rusty_color":"greenish"
              ,"num_edges":1,"diameter":22.5,"thickness":3.15,"mass":9.5}
        super().__init__(**data)

class Two_Pound(Coin):
    def __init__(self):
        data = {"original_value": 2.00,
                "clean_color": "gold & silver",
                "rusty_color": "greenish",
                "num_edges": 1,
                "diameter": 28.4,
                "thickness": 2.50,
                "mass": 12.00,
                }
        super().__init__(**data)
coin_five_pence=Five_Pence()
print(coin_five_pence.color)
coin_five_pence.rust()
print(coin_five_pence.color)


def __str__(self):
    if self.original_value >= 1:
        return "£{} Coin".format(int(self.original_value))
    else:
        return "{}p Coin".format(int(self.original_value * 100))
coins=[One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),Twenty_Pence(),Fifty_Pence(),One_Pound(),Two_Pound()]
for coin in coins:
    argument=[coin,coin.color,coin.value,coin.diameter,coin.thickness,coin.num_edges,coin.mass]
    my_string = "{} - color: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(
        *argument)
    print(my_string)
