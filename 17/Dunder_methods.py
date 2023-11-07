class Vector:
    """A 2D vector class"""

    def __init__(self, x, y):
        """Initialize a new Vector instance with x and y coordinates."""
        self.x = x
        self.y = y
        
    def __add__(self, other):
        """Return the vector addition of self and other."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Return the vector subtraction of self and other."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """Check the equality of two vectors."""
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        """Return the string representation of the vector."""
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        """Return the string format of the vector."""
        return f"({self.x}, {self.y})"
    
    def __len__(self):
        """Return the length of the vector, i.e., the number of dimensions."""
        return 2
    
    def __getitem__(self, index):
        """Return the x or y coordinate of the vector based on the index."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError('Index out of range')

# Demonstrating the dunder methods
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Vector addition
print(v1 + v2)  # Output: Vector(6, 8)

# Vector subtraction
print(v1 - v2)  # Output: Vector(-2, -2)

# Equality checking
print(v1 == v2)  # Output: False

# String representation and format
print(repr(v1))  # Output: Vector(2, 3)
print(str(v1))   # Output: (2, 3)

# Length of the vector
print(len(v1))  # Output: 2

# Indexing into the vector
print(v1[0])  # Output: 2
print(v1[1])  # Output: 3

# Displaying the documentation
print("\nDocumentation of Vector class:")
help(Vector)
