# Project Name: Inventory System
# Name: Alzraji Abdulla-Ali
# Date Created: 8-03-2022 
# Purpose: First python project, program will act as an inventory system for a small convience store

import inventoryClass

list = []

def addItem (): 
    NewItemName = input("Enter item name: ")
    NewItemExp = input("Enter experation Date: ")
    NewItemType = input("Enter type of Item (Grocey, tobaco, or taxable): ")
    NewItemPrice = input("Enter the selling price: ")
    NewItemCost = input("Cost of the product: ")
    newItemUnits = input("how many units being added: ")
    list.append ( inventoryClass.item(NewItemName, NewItemExp, NewItemType,NewItemPrice, NewItemCost, newItemUnits) )
    for obj in list:
        print(obj.NewItemName, NewItemExp, NewItemType,NewItemPrice, NewItemCost, newItemUnits)


   

#print("Welcome to your Inventory Control System")

#print("What would you like to do: ")
#print("A: Add an item")
#print("B: Remove an item")
#print("C: search for an item inventory")
#print("D: Print Inventory sheet")

addItem()
addItem()
addItem()
for obj in list:
    print(obj.NewItem)

