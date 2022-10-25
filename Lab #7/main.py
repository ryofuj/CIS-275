from TheaterSimulator import TheaterSimulator

def main():
    length = int(input('Enter the number of clock ticks: '))
    odds_of_new_customer = float(input('Enter the odds of a new arrival: '))
    for i in range(1, 4):
        print('Simulation with {} cashiers:'.format(i))
        t = TheaterSimulator(length, odds_of_new_customer)
        t.run_simulation(i)
        print()
main()