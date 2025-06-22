class Item:
    
    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quantity = q
    
    def print_item_info(self):
        print(f"the name is {self.name}, price is {self.price}, quantity is {self.quantity}")

    def __repr__(self):
        val = f"the object represents a {self.name} item"
        return val

    
    @classmethod
    def create_instance(cls, obj_details):
        name, price, quantity = obj_details.split(',')
        return cls(name,int(price),int(quantity))

    @staticmethod
    def validate_item_quantity(num):
        try:
            if num<=0:
                raise ValueError('quantity cannot be negative')
        except ValueError as e:
            print(e)
        
'''grey_sofa =Item('grey sofa',150, 2)
print(grey_sofa)
grey_sofa.print_item_info()

white_sofa =Item('white sofa',200, 3)
print(white_sofa)
white_sofa.print_item_info()
'''

table = Item.create_instance("side table,130,2")

#table.print_item_info()

print(Item.validate_item_quantity(table.quantity))
