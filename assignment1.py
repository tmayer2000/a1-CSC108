import math
g = 9.81
pi = math.pi

def get_distance(velocity:float, angle:float)-> float:
    """
    Calculates the distance a projectile travels on a flat surface
    given its intial velocity, as well as the angle of fire relative
    to the x-axis. The angle is given in radian. This function assumes
    perfect physics, i.e., constant gravity, no air resistance, etc.

    >>> get_distance(0, 1)
    0.0
    >>> get_distance(1, 0)
    0.0
    >>> get_distance(10, 0.25*pi)
    10.19367991845056
    """
    return ((velocity**2)*math.sin(2*angle))/g

def degrees_to_radians(d:float)-> float:
    """
    Takes in an angle in degrees, d, and returns an equivalent
    angle in radians

    >>> degrees_to_radians(0)
    0.0
    >>> degrees_to_radians(180)
    3.141592653589793
    """
    return d*(pi/180)

def get_radian_of(angle_string: str)-> float:
    """
    Takes in a valid input angle_str and returns the numerical value of the
    angle in radians.

    Examples:
    >>> get_radian_of("1.2r")
    1.2
    >>> get_radian_of("45d")
    0.7853981633974483
    """
    r = angle_string.find('r')
    R = angle_string.find('R')
    d = angle_string.find('d')
    D = angle_string.find('D')
    if 'r' in angle_string:
        return float(angle_string[:r:])
    elif 'R' in angle_string:
        return float(angle_string[:R:])
    elif 'd' in angle_string:
       c = float(angle_string[:d:])
       return degrees_to_radians(c)
    else:
        C = float(angle_string[:D:])
        return degrees_to_radians(C)


def is_a_number(s:str)-> bool:
    """
    Returns True if and only if s is a string representing a positive number.

    Examples:
    >>> is_a_number("1")
    True
    >>> is_a_number("One")
    False
    >>> is_a_number("-3")
    False
    >>> is_a_number("3.")
    True
    >>> is_a_number("3.1.2")
    False
    """
    if s.isnumeric() == True:
        if float(s) > 0:
            return True
    elif '.' in s:
        try:
            float(s) > 0
            b = True
        except ValueError:
            b = False
        return b
    else:
        return False


def is_valid_angle(s:str)-> bool:
    """
    Returns True if and only if s is a valid angle. See the assignment
    description and examples for more information regarding what's valid

    Examples:
    >>> is_valid_angle("85.3d")
    True
    >>> is_valid_angle("85.3.7D")
    False
    >>> is_valid_angle("90d")
    False
    >>> is_valid_angle("0.001r")
    True
    >>> is_valid_angle("1.5R")
    True
    """
    s = get_radian_of(s)
    if 0<s<(pi/2):
        return True
    else:
        return False

def approx_equal(x, y, tol):
    """
    Returns True if and only if x and y are with tol of each other.

    Examples:
    >>> approx_equal(1,2,1)
    True
    >>> approx_equal(4,3,1)
    True
    >>> approx_equal(4,3,0.99)
    False
    >>> approx_equal(-1.5,1.5,3)
    True
    """
    M = (x>=y)*x+(y>x)*y
    m = (x<=y)*x+(y<x)*y
    if M-m <= tol:
        return True
    else:
        return False


"""
DO NOT MODIFY THE CODE BELOW.

You are not required/expected to understand the following code.
If you're interested though, take a look.
"""
if __name__ == "__main__":
    while True:
        target = float(input("Enter a target distance: "))
        tol = float(input("Enter how close you need to be to your target: "))
        target_hit = False
        while not target_hit:
            valid_velocity = False
            while not valid_velocity:
                v = input("Enter a valid velocity: ")
                valid_velocity = is_a_number(v)   
            valid_angle = False
            v = float(v)
            while not valid_angle:
                theta = input("Enter a valid angle: ")
                valid_angle = is_valid_angle(theta)
            theta = get_radian_of(theta)
            d = get_distance(float(v), theta)
            target_hit = approx_equal(target, d, tol)
            if target_hit:
                print("Congratulations! You hit the target.")
            elif target > d:
                print("The shot hit short of the target, try again.")
            else: 
                print("The shot hit past the target, try again.")
            
                
