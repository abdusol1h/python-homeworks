mytuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

nested_tuple = (
    mytuple[:3],   # First 3 elements (1, 2, 3)
    mytuple[3:6],  # Next 3 elements (4, 5, 6)
    mytuple[6:]    # Remaining elements (7, 8, 9)
)

print(nested_tuple)