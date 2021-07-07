
import pytest
import pytest_html

#A fruit bowl contains fruits - Apples, Oranges and Bananas. Segregate them into different bowls

class fruitBowl:
    def __init__(self, fruits):
        self.fruits = fruits

    def printFruit(self):
        print(self.fruits, end=" ")



def test():
    dictFruits = {}
    getBowlFruits = [item for item in input("Enter the fruits items : ").split()]

    for fruitIndex in getBowlFruits:
        if fruitIndex not in dictFruits:
            dictFruits[fruitIndex] = [fruitBowl(fruitIndex)]
        else:
            dictFruits[fruitIndex].append(fruitBowl(fruitIndex))
    bowlCount=0
    for keys, value in dictFruits.items():
        bowlCount += 1
        print("Bowl"+ str(bowlCount), end=" ")

        for i in value:
            i.printFruit()
        print(end="\n")

    assert len(dictFruits.values()) == len(getBowlFruits), "List are Not equal"


#https://github.com/Akshit10/FruitsBowl.git

test()