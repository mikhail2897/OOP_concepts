import csv
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name  # To add __ before the attribute makes it private ie you cannot access it outside this class
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property decorator = Read-Only Attribute
    def name(self):
        return self.__name

    ''' Even though in the above function we are making name as a 
    Read Only property using @property. We can declare a new type 
    of decorator i.e @name_of_attribute.setter so that we can 
    change the name of the attribute. '''
    @name.setter
    def name(self, new_value):
        if len(new_value) >=20:
            raise Exception("Name too long!")
        else:
            self.__name = new_value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            #print(reader)
            items = list(reader)
            #print(items)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

'''    @property       # Decorater used to create a property where once we intialize an instance user cannot change the the value of that attribute
    def read_only_name(self):'''
