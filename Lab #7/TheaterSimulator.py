from Cashier import Cashier
from Customer import Customer
from random import random

'''
Add another parameter indicate how many Cashiers should be open for the simulation. Update the 'self._cashier' attribute to be a list of Cashier objects and create the required amount in the constructor, appending each to the list.
'''

class TheaterSimulator:
    def __init__(self, num_cashiers):
        self._cashier = [Cashier() for i in range(num_cashiers)]
        self._customer = Customer()
        self._time = 0

    def run_simulation(self, num_seconds):
        """ Run the simulation for self._simulation_length clock ticks """
        for i in range(num_seconds):
            self._time += 1
            self._customer.update()
            for cashier in self._cashier:
                cashier.update(self._customer)
        print(self)

    def __str__(self):
        result = "Theater Simulator:"
        for cashier in self._cashier:
            result += str(cashier) + ""
        return result


from Cashier import Cashier
from Customer import Customer


# class TheaterSimulator:
#     def __init__(self, length, odds_of_new_customer):
#         self._odds_of_new_customer = odds_of_new_customer
#         self._simulation_length = length
#         self._cashier = Cashier()

#     def run_simulation(self):
#         """ Run the simulation for self._simulation_length clock ticks """
#         for cur_time in range(self._simulation_length):
#             # Attempt to generate a new customer each clock tick
#             new_customer = Customer.generate_customer(self._odds_of_new_customer, cur_time)

#             if new_customer is not None:
#                 self._cashier.add_customer(new_customer)

#             self._cashier.serve_customer(cur_time)

#         self._cashier.print_statistics()