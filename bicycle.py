import random

class model(object):
    def __init__(self, name, weight, production_cost, number):
        self.name = name
        self.weight = weight
        self.production_cost = production_cost
        self.count=number
    def __str__(self):
        return self.name
    
class bicycle_shop(object):
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = []
        self.pricesheet = {}

    def add_inventory(self, bname):
        self.inventory.append(bname)
        inventory = self.inventory
        return inventory
    
    def show_inventory(self):
        print("{} Current Inventory: \n".format(self.name))
        for bmodel in self.inventory:
            bprice = bmodel.production_cost*(1+self.margin)
            self.pricesheet[bmodel]=bprice
            print("{0}: \tPrice = ${1} \t\tTotal Weight = {2} lbs \t\tIn Stock = {3}"
            .format(bmodel.name, bprice, bmodel.weight, bmodel.count))
        bsheet=self.pricesheet    
        return bsheet
    
class customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.owned = []
        
    def __str__(self):
        return self.name
    
    def afford(self, shop):
        self.shop=shop
        for bmodel in shop.inventory:
            bprice = bmodel.production_cost*(1+shop.margin)
            if self.fund>=bprice:
                print("{0} is available for you. Sale price = ${1}"
                .format(bmodel, bprice))
    
    def purchase(self):
        pass
        
def main():
    # Bicycle Models with random count of each model
    model1=model("Trainer", 30, 200,random.randint(1,15))
    model2=model("Roadster", 20, 250,random.randint(1,10))
    model3=model("Speedster", 10, 350,random.randint(1,10))
    model4=model("ProRacer", 5, 700,random.randint(1,5))
    model5=model("Youthster", 13, 100,random.randint(1,15))
    model6=model("Todler", 8, 50,random.randint(1,10))
    
    # Add models to the Shop inventory
    models=[model1, model2, model3, model4, model5, model6]
    bikeshop=bicycle_shop("FlatTrax", 0.2)
    for m in models:
        bikeshop.add_inventory(m)
    
    bikeshop.show_inventory()
        
    # Customers
    cust1=customer("Dan",200)
    cust2=customer("Bob",500)
    cust3=customer("David",1000)
    
    # List of bicycles each customer can afford
    customers=[cust1, cust2, cust3]
    for cust in customers:
        print("\n{0}'s bicycle fund is ${1}".format(cust,cust.fund)),
        print(" and can afford the follwing bicycles from {0}:".format(bikeshop.name))
        cust.afford(bikeshop)
    
if __name__ == "__main__":
    main()