class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other: object) -> object:
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, __value: object) -> bool:
        return (self.x + self.y) == (__value.x + __value.y)
    
    def __str__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"
    
    def __call__(self) -> str:
        return "I'm a Vector and I was called"
 

v1 = Vector(10, 20)
v2 = Vector(30, 40)
v4 = Vector(10, 20)

v3 = v1 + v2

print(v3)
print(v1 == v4)
