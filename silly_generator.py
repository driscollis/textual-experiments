def my_generator():
    yield "a"
    yield "b"
    return 42

#a, b, c = my_generator()
for item in my_generator():
    print(item)

generator = my_generator()
print(next(generator))
print(next(generator))
print(next(generator))

try:
    generator = my_generator()
    for item in range(3):
        print(next(generator))
except StopIteration as exc:
    print(exc.value)