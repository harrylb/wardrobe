from wardrobe import *
from clothing import *
from shirt import *
from jacket import *
from socks import *

def main():
    clothingInput = [(Shirt("Gucci Shirt", "White", True, "Short")),(Shirt("Shawn White Shirt", "Ugly Color", False, "Short")),(Shirt("Sexy lookin tee", "A sexy color", True, "Long")),(Shirt("Regular tee", "Red", False, "Short")),(Jacket("Leather Jacket", "Black", False, "Medium", "Gucci")),(Jacket("Cotton Jacket", "Azul", True, "Large", "Target")),(Jacket("Rain Jacket", "Yellow", False, "Small", "Rain Co.")),(Jacket("Silly Jacket", "Every Color", False, "Small", "Walmart")),(Socks("Regular Socks", "White", False, 2)),(Socks("Ugly Socks", "Yellow", False, 1)), (Socks("Flashy Socks", "Bright Red", True, 2)), (Socks("Formal Socks", "Black", True, 2))]
    wardrobe = Wardrobe(clothingInput)

    "Show All Clothing Items"
    print("\n==== Full Wardrobe ====")
    allClothes = wardrobe.viewAllClothes()
    print(allClothes)
    print()

    "Add Article Of Clothing"
    print("Adding Everyday Jacket Into The Wardrobe...")
    wardrobe.addClothing((Jacket("Everyday Jacket", "Grey", True, "Medium", "Union Los Angeles")))

    "Show Jackets"
    print("\n==== All Jackets ====")
    allJackets = wardrobe.viewAllJackets()
    print(allJackets)

    "Show Shirts"
    print("\n==== All Shirts ====")
    allShirts = wardrobe.viewAllShirts()
    print(allShirts)

    "Show Socks"
    print("\n==== All Socks ====")
    allSocks = wardrobe.viewAllSocks()
    print(allSocks)

    "Show Red Clothes"
    print("\n==== Red Clothes ====")
    redClothes = wardrobe.showColor("Red")
    print(redClothes)

    "Show Dirty Clothes"
    print("\n==== Dirty Clothes ====")
    dirtyClothes = wardrobe.showDirty()
    print(dirtyClothes)

    "Show Clean clothes"
    print("\n==== Clean Clothes ====")
    cleanClothes = wardrobe.viewAllClothes()
    print(cleanClothes)

    "Show Sleeved Shirts"
    print("\n==== Sleeved Clothes ====")
    sleevedClothes = wardrobe.findClothingBySleeveLength("Short")
    print(sleevedClothes)
    print()

    print("Let's Wash Some Clothes :)")

    "Show Clean Shirts"
    print("\n==== Cleaned Clothes ====")
    cleanClothes = wardrobe.cleanClothes()
    print(cleanClothes)

if __name__ == "__main__":
    main()
