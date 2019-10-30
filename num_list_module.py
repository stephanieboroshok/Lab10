
def backwardslist(array):
    array.reverse()
    print (array)
    """ Takes in a list and returns the list backwards"""

def minimum(array):
    print(min(array))
    """ Returns the lowest number in an list of numbers"""

def firsthalfsum(array):

    """Returns the sum of the first half of the list.
        ***IF THE LIST HAS AN ODD NUMBER OF ELEMENTS, split the middle element in
        half and add it to the sum.
        """

def divisibleby(array, divisor):
    for i in array:
        if i%divisor == 0:
            print (i)
        else:
            pass
    """ Returns each element divisible by the paramater 'divisor' """

def maximum(array):
    print(max(array))
    """ Returns the highest number in a list of numbers """

def avg(array):
    import statistics
    print (statistics.mean(array))
    """ Returns the average of a list of numbers"""

def suprise():
    print('You Win!!')
    """ Create a surprise function for the person that receives your code.
        Feel free to get creative change parameters, print out shapes,  etc."""


################################
####    BONUS FUNCTION       ###
################################
def gcd(array):
    """ Returns the greatest common Divisor of a list of numbers """
    """ Greatest Common Divisor is the greatest number that each number in the list is 
        divisible by. 
        EXAMPLE: [500, 50, 20] Greatest Common Divisor = 10
                 [18, 30, 42]  Greatest Common Divisor = 6
                 [33, 66, 99, 101] Greatest Common Divisor = 1"""


