
import pytest
import pytest_html

#A fruit bowl contains fruits - Apples, Oranges and Bananas. Segregate them into different bowls

class fruitBowl:      #Class Declaration
    def __init__(self, fruits):   #Constructor Initialiser.
        self.fruits = fruits

    def printFruit(self):      #Print Fruits.
        print(self.fruits, end=" ")



def test():          #Pytest initialiser

    dictFruits = {}   #Dictionary initialiser
    fruitsCount=0       # Count number of fruits.
    bowlCount = 0       # Number of Bowls.



    getBowlFruits = [item for item in input("Enter the fruits items : ").split()]

    for fruitIndex in getBowlFruits:

        if fruitIndex not in dictFruits:
            dictFruits[fruitIndex] = [fruitBowl(fruitIndex)]
            fruitsCount += 1
        else:
            dictFruits[fruitIndex].append(fruitBowl(fruitIndex))
            fruitsCount += 1


    for keys, value in dictFruits.items():    #Dictionary Fruit Objects.
        bowlCount+=1
        print("Bowl" + str(bowlCount), end=" ")
        print(value)
        for i in value:                         #iterating object one by one.
            i.printFruit()
        print(end="\n")

    assert fruitsCount == len(getBowlFruits), "List are Not equal"    #assert Fruit count should be equal to Given number of Fruits.


#https://github.com/Akshit10/FruitsBowl.git
