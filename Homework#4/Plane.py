'''When the user runs the program, let them decide the % chance that a plane will show up to land and the % chance that a plane will show up to take off each clock tick (have them enter a number between 1 and 100). Let them also decide how many clock ticks to run the simulation for. Each loop iteration represents one clock tick (or unit of time). In each iteration, you need to:

    Randomly decide if a plane should join the take-off queue
    Randomly decide if a plane should join the landing priority queue

Create a Plane class.

    In the constructor, randomly generate its amount of remaining fuel and its transaction time.
        The fuel should range from 5 to 15 and the transaction time from 1 to 3.
    If a plane's remaining fuel is lower than the number of clock ticks it has been in the priority queue when it reaches the front and is ready to start landing, it crashed!
    Plane objects need to implement the __le__ method (for less than or equal to). One plane should be considered less than or equal to another plane if it has less than or the same amount of remaining fuel as the other.
    Since our priority queue uses a MinHeap, the plane with the least amount of fuel will always be at the front.

Each plane has a "transaction time" indicating how long it requires to land or take off.

    While a plane is landing or taking off, the runway is considered "in use", and no other plane is allowed on the runway.
        You can signify with a variable named 'current_plane'. When a plane starts taking off or landing, remove it from its queue and assign it to 'current_plane'. Each clock tick, decrement its transaction time. When this reaches 0, the runway is freed up for another plane. 
    When the runway is done being used, check the landing priority queue.
        If it contains any planes, remove the next one to start landing.
            However, if the plane crashed (its remaining fuel is lower than the number of clock ticks it's been in the priority queue), end the simulation early and tell the user a plane crashed!
    If there are no planes in the landing queue, check the takeoff queue. If it contains a Plane, it may start taking off.  

Record interesting statistics from your simulation in your final report

    What is the average time spent waiting for takeoff?
    What is the longest time spent waiting for takeoff?
    What is the average time spent waiting to land?
    What is the longest time spent waiting to land?
    Did a plane crash?
    How many planes total took off and landed during the simulation?

If you do not like the results you are getting (a plane crashed, no planes were able to take off, etc.) feel free to tweak your numbers until the results are more realistic. 
'''

from ArrayQueue import ArrayQueue
from random import randint
from random import random

class Plane:
    def __init__(self):
        self.fuel = randint(5, 15)
        self.transaction_time = randint(1, 3)
        self.time_in_queue = 0

    def __le__(self, other):
        return self.fuel <= other.fuel

    def __repr__(self):
        return "Plane with {} fuel and {} transaction time".format(self.fuel, self.transaction_time)

class Airport:
    def __init__(self, landing_queue, takeoff_queue, landing_chance, takeoff_chance, clock_ticks):
        self.landing_queue = landing_queue
        self.takeoff_queue = takeoff_queue
        self.landing_chance = landing_chance
        self.takeoff_chance = takeoff_chance
        self.clock_ticks = clock_ticks
        self.current_plane = None
        self.total_takeoff_time = 0
        self.total_landing_time = 0
        self.longest_takeoff_time = 0
        self.longest_landing_time = 0
        self.planes_taken_off = 0
        self.planes_landed = 0

    def run(self):
        for i in range(self.clock_ticks):
            if random() * 100 <= self.landing_chance:
                self.landing_queue.add(Plane())
            if random() * 100 <= self.takeoff_chance:
                self.takeoff_queue.add(Plane())
            if self.current_plane is None:
                if not self.landing_queue.is_empty():
                    self.current_plane = self.landing_queue.pop()
                    self.planes_landed += 1
                elif not self.takeoff_queue.is_empty():
                    self.current_plane = self.takeoff_queue.pop()
                    self.planes_taken_off += 1
            else:
                self.current_plane.transaction_time -= 1
                if self.current_plane.transaction_time == 0:
                    self.current_plane = None
            for plane in self.landing_queue:
                plane.time_in_queue += 1
                if plane.fuel < plane.time_in_queue:
                    print("Plane crashed!")
                    return
            for plane in self.takeoff_queue:
                plane.time_in_queue += 1
                if plane.fuel < plane.time_in_queue:
                    print("Plane crashed!")
                    return
        print("Planes taken off: {}".format(self.planes_taken_off))
        print("Planes landed: {}".format(self.planes_landed))

def main():
    landing_queue = ArrayQueue()
    takeoff_queue = ArrayQueue()
    landing_chance = int(input("Enter landing chance: "))
    takeoff_chance = int(input("Enter takeoff chance: "))
    clock_ticks = int(input("Enter number of clock ticks: "))
    airport = Airport(landing_queue, takeoff_queue, landing_chance, takeoff_chance, clock_ticks)
    airport.run()

if __name__ == "__main__":
    main()
