from Cashier import Cashier
from Customer import Customer

class TheaterSimulator:
    def __init__(self, length, odds_of_new_customer):
        self._odds_of_new_customer = odds_of_new_customer
        self._simulation_length = length
        self._cashier = Cashier()

    def run_simulation(self, cashier):
        for current_time in range(self._simulation_length):
            customer = Customer.generate_customer(self._odds_of_new_customer, current_time)
            if customer is not None:
                self._cashier.add_customer(customer)
            self._cashier.serve_customer(current_time)
        self._cashier.print_statistics()