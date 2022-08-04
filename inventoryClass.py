class item:
    def __init__(self,name,expDate,itemType,sellingPrice,cost, numUnits):
        self.name = name
        self.expDate = expDate
        self.itemType = itemType
        self.sellingPrice = sellingPrice
        self.cost = cost
        self.Units = numUnits
        

    def __repr__(self) -> str:
        return "item()"    
    def __str__(self):
        return "\nName: " + f"{self.name}" + "\nExperation Date: " + f"{self.expDate}" + "\nType of Item: " + self.itemType +"\nSale price: " + f"{self.sellingPrice}" "\nCost of each unit: " + f"{self.cost}" "\nNumber of units in storage: " + f"{self.Units}"

   
