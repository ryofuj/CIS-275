from TheaterSimulator import TheaterSimulator

'''
 call TheaterSimulator's run_simulation function three times: 
 Once with one Cashier, once with two Cashiers, and once with three Cashiers. T
 his will allow the user to see the results of running the simulation with the same number of clock ticks and odds of customer arrival with three separate cashier amounts.
'''

def main():
    length = int(input('How many clock ticks should the simulation run for? '))
    odds_of_new_customer = float(input('What is the odds of a new customer arriving? '))

    # t = TheaterSimulator(length, odds_of_new_customer)
    # t.run_simulation()
    t = TheaterSimulator(length, odds_of_new_customer)
    t.run_simulation()

    t = TheaterSimulator(2)
    t.run_simulation(100, 0.1)
    t = TheaterSimulator(3)
    t.run_simulation(100, 0.1)

main()