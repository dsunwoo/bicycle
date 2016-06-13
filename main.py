from bicycle import *
import random

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
    cust1=customer("Dan",200,bikeshop)
    cust2=customer("Bob",500,bikeshop)
    cust3=customer("David",1000,bikeshop)
    
    # List of bicycles each customer can afford
    customers=[cust1, cust2, cust3]
    for cust in customers:
        print("\n{0}'s bicycle fund is ${1}".format(cust,cust.fund))
        print("\tand can afford the follwing bicycles from {0}:".format(bikeshop.name))
        cust.afford()
    
    # Customers purchase 1 bicycle each within their budget
    cust1.purchase(model5)
    cust2.purchase(model3)
    cust3.purchase(model4)
    
    # Show updated inventory
    bikeshop.show_inventory()
    
if __name__ == "__main__":
    main()