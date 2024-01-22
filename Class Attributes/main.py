class Item:
    pay_rate = 0.8 #rate after discount of 20%
    all_list = []
    all_str = []
    def __init__ (self, price:float, name:str, quantity = 0):
        # Run validations for the recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0\n"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0\n"

        # Assign to self object
        self.price = price      # self is used to access the attributes at instance level
        self.quantity = quantity
        self.name = name

        # Action to execute
        Item.all_list.append(self)
        Item.all_str.append(self)
    
    def calculate_tot_price1(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate     
        '''If we write Item.pay_rate here and below as mentioned for item2 instance and 
        change the pay_rate there it will not take the updated one. As best practice 
        always use self.pay_rate'''

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        ''' To make the list of all the instances and their attributes appear properly we 
        use the magic function __repr__ '''

    def __str__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    
item1 = Item(200, 'Phone', 1)
item2 = Item(2000, 'Laptop', 1)
''' The class attribute can be accessed directly by 
referencing the class or by referencing the instance of that class'''
print(Item.pay_rate)    # direct reference to class
print(item1.pay_rate)   # instance of class
print(item2.pay_rate)   # instance of class

print("\n\n\n")

print(Item.__dict__)    # All the attributes for instance level
print("\n")
print(item1.__dict__)   # All attributes for instance level

print("\n\n\n")

item1.apply_discount()
print(item1.price)      # this will return the price from apply_discount function in Item class

print("\n\n\n")
item2.pay_rate = 0.7    
'''You can mention the pay_rate at instance level and change it for 
this very instance as you don't need to go back to the class level to change it but make sure 
that in the function you need to use self.attribute_name rather than class.attribute_name'''
item2.apply_discount()
print(item2.price)

print("\n\n\n")

item1 = Item(200, 'Phone', 1)
item2 = Item(2000, 'Laptop', 1)
item3 = Item(200, 'Cable', 3)
item4 = Item(2000, 'Mouse', 2)
item5 = Item(200, 'Keyboard', 2)

print(Item.all_list)     
''' This list is not just going to give you an visual array of all the values in that instance. 
To resolve this we use the __repr__ magic function'''
print("\n\n")
for instance in Item.all_list:
    print(instance.name)
    print(type(instance.all_list))

print("\n\n")
print(Item.all_str)

for instance in Item.all_str:
    print(instance.name)
    print(type(instance.all_str))


''' Difference between __str__ vs __repr__
Watch this video : https://www.youtube.com/watch?v=FIaPZXaePhw '''

