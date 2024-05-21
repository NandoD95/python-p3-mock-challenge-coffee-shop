import ipdb

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >=3 and not hasattr(self, "name"):
            self._name = new_name
        
    def orders(self):
        # ipdb.set_trace()
        return[order for order in Order.all if order.coffee == self]
    
    def customers(self):
        # ipdeb.set_trace()
        return list ({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum(order.price for order in self.orders()) / self.num_orders() if self.num_orders() > 0 else 0

    def __repr__(self):
        return f"Coffee('{self.name}')"

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15 :
            self._name = new_name
        
    def orders(self):
        # ipdb.set_trace()
        return[order for order in Order.all if order.customer == self]
    
    def coffees(self):
        # ipdb.set_trace()
        return list ({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        # order matters with keyword arguments 
        # return Order(self, coffee, price)

        #order doenst matter with keyword arguments 
        return Order(coffee=coffee, customer=self, price=price)

    def orders_for_specific_coffee (self, coffee):
        return [order for order in self.orders() if order.coffee == coffee]

    def total_for_specific_coffee(self, coffee):
        return sum(order.price for order in self.orders_for_specific_coffee(coffee))

    @classmethod
    def add_new_customer(cls, new_customer):
        cls.all.append(new_customer)

    @classmethod
    def most_aficionado(cls, coffee):
        if coffee.orders():
            return max(cls.all, key=lambda customer: customer.total_for_specific_coffee(coffee))
        else:
            return None
        # aficionados = [customer for customer in cls.all if coffee in customer.coffees()]

    def __repr__(self):
        return f"Customer('{self.name}')"
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.add_new_order(self)

    @classmethod
    def add_new_order(cls, new_order):
        cls.all.append(new_order)

    @property 
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and 1.0 <= new_price <= 10.0 and not hasattr(self, '_price'):
            self._price = new_price

    @property
    def customer (self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee

    def __repr__(self):
        return f'<Order customer={self.customer.name} coffee= {self.coffee.name} price={self.price.name}'