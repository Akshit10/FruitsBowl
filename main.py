
import pytest
import pytest_html

#A fruit bowl contains fruits - Apples, Oranges and Bananas. Segregate them into different bowls

class fruitBowl:
    def __init__(self, fruits):
        self.fruits = fruits

    def segregateFruits (self):
        fruitsList = list(self.fruits)
        fruitCount = 0
        bowlCount = 0
        uniqueFruits = set(fruitsList)

        for fruitIndex in uniqueFruits:
            bowlCount+= 1
            print("Bowl" + str(bowlCount), fruitsList.count(fruitIndex)*[fruitIndex,])
            fruitCount+=fruitsList.count(fruitIndex)
        return(fruitCount,len(fruitsList))


def test():
    getBowlFruits = [item for item in input("Enter the fruits items : ").split()]
    obj = fruitBowl(getBowlFruits)
    test = obj.segregateFruits()
    assert test[0] == test[1], "List are Not equal"



#https://github.com/Akshit10/FruitsBowl.git
