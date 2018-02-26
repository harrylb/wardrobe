What Is This?
-------------

This is a program that utilities object oriented programing (OOP) with classes
and class inheritance. There is one super-class and two sub-classes (Shirt and socks)

-----------------------
The Wardrobe class

The Wardrobe class allows the user to access certain methods for a specific piece of Clothing.
Here are the available methods:
addClothing(article)
viewAllClothes()
viewAllJackets()
viewAllShirts()
viewAllSocks()
findCleanClothing()
showDirty()
findClothingBySleeveLength(sleeves)
cleanClothes()

Each one is self explanatory and does not need an in-depth explanation due to their simplicity
--------------------------
The Shirt, Socks, and Jacket classes

Shirt class

The shirt class is a sub-class of the Wardrobe class do it has all of its
previous properties with a few extra.
Here are the new methods added

getSleeves()
-Returns either "short" or "long" based on what's in the list in the runner

Socks class
Like the Shirt class, the Socks class inherits all of the previous properties
found in the Wardrobe class.
Here are the new methods added

getNumber()
-Returns the number of socks (You never know. Some people have 3 feet)

Jacket class
getSize()
-Returns size of the jacket. Can be the following: small, medium, large
getBrand()
-Returns the brand specific to that jacket. Ex. Gucci
