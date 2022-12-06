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

'''
Ryo Fujimura
CIS 275C
Homework #4 Pt.3
'''

from PriorityQueue import PriorityQueue
from Array import Array
import random


class Plane:
    def __init__(self):
        self.fuel = random.randint(5, 15)
        self.transaction_time = random.randint(1, 3)
        self.time_in_queue = 0

    def __le__(self, other):
        return self.fuel <= other.fuel

    def __str__(self):
        return "Fuel: " + str(self.fuel) + ", Transaction Time: " + str(self.transaction_time) + ", Time in Queue: " + str(self.time_in_queue)

def main():
    takeoff_queue = PriorityQueue()
    landing_queue = PriorityQueue()
    runway = None
    takeoff_wait_times = Array(0)
    landing_wait_times = Array(0)
    takeoff_time = 0
    landing_time = 0
    takeoff_count = 0
    landing_count = 0
    takeoff_chance = int(input("Enter the chance of a plane taking off each clock tick (1-100): "))
    landing_chance = int(input("Enter the chance of a plane landing each clock tick (1-100): "))
    clock_ticks = int(input("Enter the number of clock ticks to run the simulation for: "))
    for i in range(clock_ticks):
        if random.randint(1, 100) <= landing_chance:
            landing_queue.add(Plane())
        if random.randint(1, 100) <= takeoff_chance:
            takeoff_queue.add(Plane())
        if runway is None:
            if not landing_queue.is_empty():
                runway = landing_queue.pop()
            elif not takeoff_queue.is_empty():
                runway = takeoff_queue.pop()
        else:
            runway.transaction_time -= 1
            if runway.transaction_time == 0:
                if runway in landing_queue:
                    landing_wait_times.append(runway.time_in_queue)
                    landing_time += runway.time_in_queue
                    landing_count += 1
                else:
                    takeoff_wait_times.append(runway.time_in_queue)
                    takeoff_time += runway.time_in_queue
                    takeoff_count += 1
                runway = None
        for plane in landing_queue:
            plane.time_in_queue += 1
            if plane.time_in_queue > plane.fuel:
                print("A plane crashed!")
                return
        for plane in takeoff_queue:
            plane.time_in_queue += 1
    print("Average time spent waiting for takeoff: " + str(takeoff_time / takeoff_count))
    print("Longest time spent waiting for takeoff: " + str(max(takeoff_wait_times)))
    print("Average time spent waiting to land: " + str(landing_time / landing_count))
    print("Longest time spent waiting to land: " + str(max(landing_wait_times)))
    print("Did a plane crash? " + str(runway is not None and runway.time_in_queue > runway.fuel))
    print("Total planes that took off and landed: " + str(landing_count + takeoff_count))
    
if __name__ == "__main__":
    main()
    