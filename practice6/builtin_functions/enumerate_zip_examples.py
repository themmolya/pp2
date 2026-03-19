names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

# enumerate()
print("Enumerate:")
for i, name in enumerate(names):
    print(i, name)

# zip()
print("\nZip:")
for name, score in zip(names, scores):
    print(name, score)

# type conversions
num_str = "123"
num_int = int(num_str)
print("\nConverted:", num_int, type(num_int))