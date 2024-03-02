# Q.14 Write a Python program to find the second smallest number in a list. 


def second_smalllest(numbers):
    return sorted(numbers)[1]
my_list = [8,4,5,6,3,1]
print ("second smalllest number:", second_smalllest(my_list))