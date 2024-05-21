#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    c1 = Customer(name='Tito')
    c2 = Customer(name='Conner')
    c3 = Customer(name='Luna')

    co1 = Coffee(name='Mocha')
    co2 = Coffee(name='Latte')
    co3 = Coffee(name='Cappuccino')

    o1 = Order(customer=c1, coffee=co1, price=2.0)
    o2 = Order(customer=c1, coffee=co1, price=2.0)
    o3 = Order(customer=c1, coffee=co2, price=3.0)

    o4 = Order(customer=c2, coffee=co3, price=4.0)
    o5 = Order(customer=c2, coffee=co1, price=2.0)

    o6 = Order(customer=c3, coffee=co3, price=4.0)
    o7 = Order(customer=c3, coffee=co2, price=3.0)
    o8 = Order(customer=c3, coffee=co1, price=2.0)

    # co1.order() # => list with 4 
    # c1.orders()
    # co1.customers()
    # c1.coffees()

    ipdb.set_trace()
