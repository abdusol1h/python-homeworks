import math

class Vector:
    def __init__(self, *components):
        """Initialize a vector with any number of components."""
        self.components = tuple(components)

    def __str__(self):
        """String representation of the vector."""
        return f"Vector{self.components}"

    def __add__(self, other):
        """Vector addition (element-wise)."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        """Vector subtraction (element-wise)."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        """Dot product if multiplying by another vector, scalar multiplication otherwise."""
        if isinstance(other, Vector):  # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*(other * a for a in self.components))
        else:
            raise TypeError("Unsupported operation")

    def __rmul__(self, other):
        """Ensure scalar multiplication works in both orders."""
        return self * other

    def magnitude(self):
        """Compute and return the magnitude of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        """Return the unit vector (normalized version of this vector)."""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(a / magnitude for a in self.components))

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)          
print(v1 + v2)        
print(v2 - v1)        
print(v1 * v2)      
print(3 * v1)         
print(v1.magnitude())   
print(v1.normalize())  