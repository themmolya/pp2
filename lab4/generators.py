# Iterators and Generators Practice

# 1. Custom Iterator
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

print("Iterator Example:")
for num in Counter(5):
    print(num)


# 2. Generator Function
def square_generator(n):
    for i in range(n):
        yield i * i

print("\nGenerator Function Example:")
for val in square_generator(5):
    print(val)


# 3. Generator Expression
print("\nGenerator Expression Example:")
gen_exp = (x * 2 for x in range(5))
for val in gen_exp:
    print(val)
