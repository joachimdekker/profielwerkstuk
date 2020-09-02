from typing import NewType
import Vector

linline = NewType("linline", object)

class linline():
    def __init__(self, rc, b) -> None:
        self.rc = rc
        self.b = b

    def intersect(self, other: linline) -> Vector.Vector:
        """Calculate the point on which the two lines intersect
        
        The two lines intersect on one point. Intersect() calculates
        that point and give back a vector.

        Args:
            other: a linline; the line that intersects
        """
        new_x = (other.b - self.b) / (self.rc - other.rc)
        return Vector.Vector(new_x, self.calc(new_x))

    def calc(self, x: float) -> float:
        """Calculate the output with a given x value

        The mathematical equivalent of f(x). Calc() calculates
        the value that corresponds to the x value given.

        Args:
            x: a float; the x value for the value to be calculated
        """
        return self.rc * x + self.b

if __name__ == "__main__":
    l1 = linline(3,7)
    l2 = linline(-14,1)

    print(l1.calc(6))
    print(l1.intersect(l2))
