#method: function inside a class
#function: outside a class
#typing, assert
#instance attributes vs class attributes: instance attributes are unique to each instance, class attributes are shared by all instances

import csv

class Item:
    pay_rate = 0.8 #class attribute
    all=[]
    #magic method
    #executed when an object is created
    def __init__(self, name, price, quantity=0):
        #run validation
        assert price>=0, f"Price {price} is not greater than 0"
        assert quantity>=0, f"Quantity {quantity} is not greater than 0"
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
    
    def calculate_total_price(self, price, quantity):
        return price * quantity

    def calc_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate
    
    # class method is used to create a new instance of a class 
    @classmethod  
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            # print(item)
            Item(name=item.get('name'), price=float(item.get('price')), quantity=int(item.get('quantity')))
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


    
# item1 = Item("iPhone", 100, 4)
# # item1.name="iPhone"
# # item1.price=350
# # item1.quantity=4
# item1.apply_discount()
# print(item1.price)
# print(item1.calculate_total_price(item1.price, item1.quantity))

# print(type(item1)) # <class '__main__.Item'>
# print(type(item1.name)) # <class 'str'>

# item2 = Item("Macbook", 1000)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
# # item2.name="Macbook"
# # item2.price=550
# # item2.quantity=2
# item2.has_numpad=False
# print(item2.calc_total_price())
# print(item2.has_numpad)
# print(Item.pay_rate) # creating instance not required

# print(Item.__dict__) # All attributes of a class
# print(item1.__dict__) # All attributes of an instance


if __name__=='__main__':
    Item.instantiate_from_csv()
    print(Item.all)
    # item1 = Item("iPhone", 100, 4)
    # item2 = Item("Macbook", 1000, 3)
    # item3 = Item("Mouse", 10, 10)
    # item4 = Item("Keyboard", 50, 5)
    # item5 = Item("Monitor", 200, 2)
    
    # print(Item.all)
    # for instance in Item.all:
    #     print(instance.name, end=" ")
    