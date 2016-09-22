'''
The rabbits are free at last, free from that horrible zombie science experiment. They need a happy, safe home, where they can recover.
You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first, you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.
Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).
Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.
The vertices list will contain exactly three elements, and each element will be a list of two integers representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. The three vertices will not be collinear.

'''



def answer(vertices):
    # Uses Pick's Theorem: Area = Boundary_Points/2 + Interior_Points -1
    from fractions import Fraction, gcd
    v_0, v_1, v_2 = vertices[0], vertices[1], vertices[2]
    # Get area of Triange
    area = abs(v_0[0] * (v_1[1] - v_2[1]) + \
               v_1[0] * (v_2[1] - v_0[1]) + \
               v_2[0] * (v_0[1] - v_1[1])) / 2
    # Helper: Get number of lattice points for line
    def get_bounds(vert1, vert2):
        y = vert2[1] - vert1[1]
        x = vert2[0] - vert1[0]
        return abs(gcd(y, x))
    # Get Total lattice points
    bounds = get_bounds(v_0, v_2) + get_bounds(v_1, v_2) + get_bounds(v_0, v_1)
    return area - (bounds / 2) + 1
