
# Created:ON:29 -October-2020
# Created by:Victor Nkuna
# E-mail:victor.nkuna@yahoo.com


# program to count die faces,and get the value afterwards


from random import randrange


class MSDie:
    """"
    The class msdie has three methods called attributes,this are functions that defined the property of the said class
    the init method is special since it contains reference to the object MSDie
    object they always contain their own data
    """

    def __init__(self, sides, value):
        self.sides = sides
        self.value = value  # why i am i not initializing variable attribute of the class MSDie called value

    def roll(self):
        self.value = 1
        self.value = randrange(1, self.sides + 1)

    def get_value(self):
        """"this attributes return the data of the class"""
        return self.value

    def set_value(self, value):
        self.value = value

def main():


    ("from outside the class=object constructor,the constructor is reffered to by the class name just like below\n"
     "the die1 = MSDie create a new object and ecute __init__ on that object,the power of instance variable we can use them to recall\n"
     "the state of objects\n")
    die1 = MSDie(12,8)
    # die1.set_value(8)
    print(die1.get_value())
main()