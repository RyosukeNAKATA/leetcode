"""
Question: Generate Random Point in a Circle
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:
1.input and output values are in floating-point.
2.radius and x-y position of the center of the circle is passed into the class constructor.
3.a point on the circumference of the circle is considered to be in the circle.
4.randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        output = []
        r = self.r * math.sqrt(random.uniform(0, 1))
        if r == 0:
            output.append([0, 0])
            return output
        theta = 2 * math.pi * random.random()
        x = r * math.cos(theta) + self.x
        y = r * math.sin(theta) + self.y
        output.append(x)
        output.append(y)
        return output

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()