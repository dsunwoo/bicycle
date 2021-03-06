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
        inventorylist=self.pricesheet
        return inventorylist
    
    def profit(self, bmodel, saleprice):
        self.bmodel=bmodel
        salesprofit=saleprice-bmodel.production_cost
        bmodel.count-=1
        return salesprofit, bmodel.count
        
class customer(object):
    def __init__(self, name, fund, shop):
        self.name = name
        self.fund = fund
        self.owned = []
        self.shop = shop
    def __str__(self):
        return self.name
    
    def afford(self):
        shop=self.shop
        for bmodel in shop.inventory:
            bprice = bmodel.production_cost*(1+shop.margin)
            if self.fund>=bprice:
                print("{0}: \tSale price = ${1}"
                .format(bmodel, bprice))
        
    def purchase(self, modelname):
        self.modelname = modelname
        shop = self.shop
        bprice = modelname.production_cost*(1+shop.margin)
        if bprice<=self.fund:
            self.owned=self.modelname
            fund_remain=self.fund-bprice
            print("{} now owns a {}".format(self.name,self.modelname)),
            print("Remaining amount in bicycle fund: ${0}".format(fund_remain))
        shop.profit(self.modelname, bprice)