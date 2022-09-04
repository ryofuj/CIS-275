'''
Ryo Fujimura
CIS 275C
'''
def main():
    """
    user input a string
    count all the vouls in a string
    print each vowel and the number of times it appears
    """
    vowels = "aeiou"
    string = input("Enter a string: ")
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    print("The number of vowels in the string is "+str(count))
    for i in vowels:
        print(i+" : "+str(string.count(i))+" times.")


main()