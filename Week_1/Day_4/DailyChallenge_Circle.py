import math

# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

class Circle:
  def __init__(self, radius):
    self.radius = radius

  @property
  def diameter(self):
    return self.radius * 2

  @diameter.setter
  def diameter(self, value):
    self.radius = value / 2

  def area(self):
    return math.pi * self.radius ** 2

  def __str__(self):
    return f"Circle(radius={self.radius})"

  def __add__(self, other):
    return Circle(self.radius + other.radius)

  def __gt__(self, other): return self.radius > other.radius   # >
  def __lt__(self, other): return self.radius < other.radius   # <
  def __eq__(self, other): return self.radius == other.radius  # ==



c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(5)

print(c1)                    # Circle(radius=5)
print(c1.diameter)           # 10
c1.diameter = 20
print(c1.radius)             # 10.0
print(f"Area: {c1.area():.2f}")

c4 = c1 + c2
print(c4)                    # Circle(radius=20.0)

print(c1 > c2)              # False (radius 10 == 10 — not greater)
print(c1 == c2)             # True  (both radius 10)
print(c1 == c3)             # False (radius 10 != 5)

circles = [Circle(8), Circle(3), Circle(12), Circle(1), Circle(5)]
for c in sorted(circles):
    print(f"  {c} — area: {c.area():.2f}")

