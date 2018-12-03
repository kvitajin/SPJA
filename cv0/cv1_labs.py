"""
This is the script for Exercise 1
Complete the code.
"""

def add(a, b):
    """Adds parameters."""
    return a + b

def what_number(number):
    """Returns string positive/zero/negative specifying
    value of the number."""
    if number>0:
         return "positive"
    elif number==0:
         return "zero"
    elif number<0:
         return "negative"
    else:
         return "wrong input"


def sum_of_numbers(numbers):
    """Returns sum of the numbers in the list."""
    sum=0
    for l in numbers:
        sum+=l
    return sum
    #return sum(numbers)    a nemusim mit tu posranou funkci nad tim

def ship_name(fleet, designated_no):
    """Return ship's name for specified designated number
    from the fleet."""
    # has dictionary a key? Use syntax: key in dictionary
    if designated_no in fleet:
        return fleet[designated_no]
    else:
        return None

    pass

def how_many_5(numbers):
    """Returns number of numbers greater than 5."""
    # Modify example to take argument that specifies threshold
    higher=0
    # for l in numbers:
    #     if l>5:
    #         higher+=1
    # return higher
    return len([1 for x in numbers if x>5])

def gen_list_gt(lst, no):
    """Returns list with numbers greater than no."""
    #syntax: [ item for item in lst if_condition ]
    return [x for x in lst if x>no]

print(add(1, 3))
#print(add([1, 2, 3], [4, 5, 6]))
# Try addition of strings or different data type and see what happens

#if statement example
n = 5
print("Number", n, "is:", what_number(n))

#for example: sum of the list example
lst = [1, 2, 3, 6, 7, 8]
print("Sum is:", sum_of_numbers(lst))

#dictionary example
fleet = {'BS62': 'Pegasus', "BS75": "Galactica", 36: 'Valkirie'}
designated_no = "BS62"
print("We've got {} in the fleet".format(ship_name(fleet, designated_no)))

#function to count how many numbers > 5 are in the list
lst = [1, 2, 5, 6, 7, 10, 12, 40, 3]
print("There are {} numbers greater than 5".format(how_many_5(lst)))

#generating list example
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
no = 5
print("List with numbers > {}: {}".format(no, gen_list_gt(lst, no)))
