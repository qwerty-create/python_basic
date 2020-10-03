# class Dog:
#     def __init__(self):
#       self.color="brown"
#
#     def wash(self):
#         self.color="white"
#         return self.color
#
#
# dog1=Dog()
# print(dog1.color)
#
# color_new=dog1.wash()
# print(color_new)

import random
class Pound:
    def __init__(self):
        self.rare=True
        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
        self.value=1.00
        self.num_edges=1
        self.diameter=22.5
        self.thickness=3.15
        self.heads=True
        self.color="yellow"
    def rust(self):
        self.color="greenish"

    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("coin spent")


coin1=Pound()
print(coin1.thickness)
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)
coin1.flip()
print(coin1.heads)