'''

As you ponder sneaky strategies for assisting with the great rabbit escape,
you realize that you have an opportunity to fool Professor Booleans guards
into thinking there are fewer rabbits total than there actually are.
By cleverly lining up the rabbits of different heights, you can obscure the
sudden departure of some of the captives.
Beta Rabbits statisticians have asked you for some numerical analysis of how
this could be done so that they can explore the best options.
Luckily, every rabbit has a slightly different height, and the guards are lazy
and few in number. Only one guard is stationed at each end of the rabbit
line-up as they survey their captive population.
With a bit of misinformation added to the facility roster, you can make the
guards think there are different numbers of rabbits in holding.
To help plan this caper you need to calculate how many ways the rabbits can be
lined up such that a viewer on one end sees x rabbits, and a viewer on the other
end sees y rabbits, because some taller rabbits block the view of the shorter
ones.
For example, if the rabbits were arranged in line with heights 30 cm, 10 cm,
50 cm, 40 cm, and then 20 cm,a guard looking from the left would see 2 rabbits
while a guard looking from the right side would see 3 rabbits.
Write a method answer(x,y,n) which returns the number of possible ways to
arrange n rabbits of unique heights along an east to west line, so that only x
are visible from the west, and only y are visible from the east. The return
value must be a string representing the number in base 10.
If there is no possible arrangement, return "0".
The number of rabbits (n) will be as small as 3 or as large as 40
The viewable rabbits from either side (x and y) will be as small as 1 and as
large as the total number of rabbits (n).
'''

# let z be the biggest person: index of z  > x-1 and < n2 - (y)
# once first and last element are decided, all elements lower than both can go anywhere
import pdb


def answer(x, y, n):
    import math
    def nCr(n, r):
        f = math.factorial
        return f(n) / f(r) / f(n - r)
    def nPr(n, r):
        f = math.factorial
        return f(n) / f(n-r)

    if x + y > n+1:
        return "0"
    if (x == n) or (y == n):
        return "1"

    count = 0
    for first in range(1, n+1):
        for z in range(x, n-y):
            for last in range(1, n+1):
                # go to next iteration of there are repeats

                if len({first,z,last}) < 3:
                    continue
                print(first, z, last)
                if first == max(first,last):
                    # number of combinations of ascending elements to go from 0 to z
                    pre_element_combinations = nCr(n-first-1,x-1)
                    # number of ways they can be arranged
                    pre_element_arangments = nCr(z-2, x-1)
                    # total number of pre_z posibilities for ascending elements
                    pre_ascending_count = pre_element_combinations * pre_element_arangments

                    # number of combinations of descending elements to go from z to n-1
                    # (repeat, basically)
                    post_element_combinations = nCr(n-last-(x-1), y-1)
                    post_element_arangments = nCr(n-z-1, y-1)
                    post_descending_count = post_element_combinations * post_element_arangments
                    # number of other elements
                    other_element_count =  n-(x-1)- (y-1)-1
                    # arrangments of other elements (they can be in any order)
                    other_element_arangments = nPr(n, other_element_count)

                    count += pre_ascending_count*post_descending_count*other_element_arangments

    return count
pdb.set_trace()



def left_view_count(li):
    current_max = li[0]
    count = 1
    for number in li:
        if number > current_max:
            current_max = number
            count += 1
    return count

def right_view_count(li):
    return left_view_count(list(reversed(li)))
