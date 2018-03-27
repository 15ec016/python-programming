# Python program to check if three points are 
# collinear or not using area of triangle.

# function to check if point collinear or not
def collinear(a1, b1, a2, b2, a3, b3):
    
    """ Calculation the area of triangle. We have  
        skipped multiplication with 0.5 to avoid 
        floating point computations """
    a = x1 * (b2 - b3) + a2 * (b3 - b1) + a3 * (b1 - b2)
 
    if (a == 0):
        print "Yes"
    else:
        print "No"
 
# driver function
a1, a2, a3, b1, b2, b3 = 1, 1, 1, 1, 4, 5
collinear(a1, b1, a2, b2, a3, b3)
