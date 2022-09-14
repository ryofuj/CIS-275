"""
Ryo fujimura
Homework#1

main.py
write a simple driver program which demonstrates the use of the updated Array class. 
"""

from Array import Array

def main():
    a1 = Array(5)
    a1[0] = 1
    a1[1] = 2
    a1[2] = 3
    print(a1)
    print(len(a1))
    print(a1.logical_size())
    
    '''
    # raise IndexError("Index out of range")
    a1[3] = 10
    print(a1)
    '''

    '''
    # raise ValueError("Cannot set to None")
    a1[1] = None
    print(a1)
    '''
    # test eq
    a2 = Array(5)
    a2[0] = 1
    a2[1] = 2
    a2[2] = 3
    print(a1 == a2)

    a3 = Array(5)
    a2[0] = 1
    a2[1] = 2
    print(a3 == a2)
    
main()

'''
ryofuji@dhcp-39-110-219 CIS-275 % /usr/local/bin/python3 /Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/main.py
    [1, 2, None, None, None]
    5
    2
    Traceback (most recent call last):
    File "/Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/main.py", line 21, in <module>
        main()
    File "/Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/main.py", line 18, in main
        a1[1] = None
    File "/Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/Array.py", line 53, in __setitem__
        raise ValueError("Cannot set to None")
    ValueError: Cannot set to None
ryofuji@dhcp-39-110-219 CIS-275 % /usr/local/bin/python3 /Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/main.py
    [1, 2, None, None, None]
    5
    2
    Traceback (most recent call last):
    File "/Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/main.py", line 26, in <module>
        main()
    File "/Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/main.py", line 20, in main
        a1[3] = 10
    File "/Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/Array.py", line 51, in __setitem__
        raise IndexError("Index out of range")
ryofuji@dhcp-39-110-219 CIS-275 % /usr/local/bin/python3 /Users/ryofuji/Documents/GitHub/CIS-275/Homework#1/main.py
    [1, 2, 3, None, None]
    5
    3
    True
    False
'''