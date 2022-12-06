'''One of the most common uses of a heap is the K-largest algorithm which finds the K largest values in a List. For example, if K = 4, the algorithm finds the 4 largest values in a List.

    Write some code to create a List and fill it with 100 random numbers, each ranging in value from 1-100.
    Ask the user what value the want for K (should be between 1 and 100).
    Print the K-largest numbers in the list. Do not use list's built-in sort method. Rather, use your MaxHeap class to accomplish this!
'''

import random
from MaxHeap import MaxHeap
from MinHeap import MinHeap

def main():
    # Create a list of 100 random numbers
    random_list = []
    for count in range(100):
        random_list.append(random.randint(1, 100))

    # Ask the user for a value of K
    k = int(input("What value of K would you like to use? (1-100)"))

    # Create a MaxHeap from the list
    max_heap = MaxHeap()
    for item in random_list:
        max_heap.add(item)

    # Print the K-largest numbers in the list
    print("The K-largest numbers in the list are: ")
    for count in range(k):
        print(max_heap.pop(), end=" ")

if __name__ == "__main__":
    main()
