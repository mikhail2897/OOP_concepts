class Item:
    def __init__ (self, price:float, name:str, quantity = 0):
        assert price >= 0, f"Price {price} is not greater than or equal to 0\n"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0\n"

        self.price = price
        self.quantity = quantity
        self.name = name
    
    def calculate_tot_price1(self):
        return self.price * self.quantity
    
'''    def calculate_grand_total(self):
        return self.item1.total_phone + self.item2.total_laptop'''

    
item1 = Item(450, 'Phone', 20)
item2 = Item(2000, 'Laptop', 8)

print(f"The total value of of {item1.name} is {item1.calculate_tot_price1()}\n")
print(f"The total value of of {item2.name} is {item2.calculate_tot_price1()}\n")

'''item1.total_phone = item1.calculate_tot_price1()
item2.total_laptop = item2.calculate_tot_price1()'''

print(f"Grand total price of {item1.name} and {item2.name} is {item1.calculate_tot_price1() + item2.calculate_tot_price1()}\n")
