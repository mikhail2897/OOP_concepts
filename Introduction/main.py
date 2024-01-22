class Item:
    def calculate_tot_price(self, price_x, quantit_y):
        return price_x * quantit_y


item1 = Item()
item2 = Item()

item1.name = "Phone"
item1.price = 100
item1.quantity = 5

item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

print("Total price of Item 1 is ",item1.calculate_tot_price(item1.price, item1.quantity))
print("Total price of Item 2 is ",item1.calculate_tot_price(item2.price, item2.quantity))
