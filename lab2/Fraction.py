"""
Ryo Fujimura
Lab 2
"""
class Fraction:
    """
    Create a class named Fraction that represents a fraction. 
    Each Fraction object will represent a numerical fraction (i.e. 3/5, 2/3, etc)
    Objects of this class should have two attributes: numerator and denominator.
    overload the greater than, equals, and string methods for this class.
    """
    
    def __init__(self, numerator, denominator):
        '''
        Constructor
        '''
        self.numerator = numerator
        self.denominator = denominator

    def __gt__(self, other):
        '''
        overload the greater than method
        '''
        if self.numerator/self.denominator > other.numerator/other.denominator:
            return str(self.numerator) + "/" + str(self.denominator) + " is greater than " + str(other.numerator) + "/" + str(other.denominator)
        else:
            return str(self.numerator) + "/" + str(self.denominator) + " is not greater than " + str(other.numerator) + "/" + str(other.denominator)
    
    def __eq__(self, other):
        '''
        overload the equals method
        '''
        if self.numerator/self.denominator == other.numerator/other.denominator:
            return str(self.numerator) + "/" + str(self.denominator) + " is equal to " + str(other.numerator) + "/" + str(other.denominator)
        else:
            return str(self.numerator) + "/" + str(self.denominator) + " is not equal to " + str(other.numerator) + "/" + str(other.denominator)

    def __str__(self):
        '''
        overload the string method
        '''
        return str(self.numerator) + "/" + str(self.denominator)
