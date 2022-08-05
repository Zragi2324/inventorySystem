# Project Name: Inventory System
# Name: Alzraji Abdulla-Ali
# Date Created: 8-03-2022 
# Purpose: First python project, program will act as an inventory system for a small convience store

from os import remove
import inventoryClass

list = []

def addItem (list): 
    NewItemName = input("Enter item name: ")
    NewItemExp = input("Enter experation Date: ")
    NewItemType = input("Enter type of Item (Grocey, tobaco, or taxable): ")
    NewItemPrice = input("Enter the selling price: ")
    NewItemCost = input("Cost of the product: ")
    newItemUnits = input("how many units being added: \n")
    list.append ( inventoryClass.item(NewItemName, NewItemExp, NewItemType,NewItemPrice, NewItemCost, newItemUnits) )
    
#FIX ME need to understand how to delete an object based on its attribute, while looping through the list
def removeItem(list):

    if len(list) == 0:
        print("Nothing to remove, no inventory to remove.\n")
        return
    deleteItem = input("Enter the name of the item you want to remove: ")
    for i in range (len(list)):
        if list[i].name == deleteItem:
            del list[i]

def searchItem(list, target):
    
    for i in range(len(list)):
        if list[i].name == target:
            print(list[i])
            return

    print("Item not found in inventory.\n")
    

def printInventory(list):
    for obj in list:
        print(obj)

def switch(case, list, target):
    if (case == 'A') or (case =='a'):
        addItem(list)
    elif (case == 'b') or (case == 'B'):
        removeItem(list)
    elif (case == 'c') or (case == 'C'):
        searchItem(list, target)
    elif (case == 'd') or (case == 'D'):
        printInventory(list)
    else: 
        return


quitChar = 'o'
newTarget = "searchItem"
newList = []

print("******************** Welcome to your Inventory Control System ********************\n")
while not (quitChar == 'q' or  quitChar == 'Q'):
   
    print("What would you like to do? Choose one of the following: \n")
    print("A: Add an item\n")
    print("B: Remove an item\n")
    print("C: search for an item inventory\n")
    print("D: Print Inventory sheet\n")

    quitChar = input("\nchoose an option: ")
    switch(quitChar, newList,newTarget)
