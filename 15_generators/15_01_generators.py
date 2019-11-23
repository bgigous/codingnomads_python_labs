'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
def fib(n):
    """
    Generate the first n terms of the fibonacci sequence
    :param n: nth term of the sequence
    :return:
    """
    a, b = 0, 1
    if n >= 1: yield a
    if n >= 2: yield b
    i = 2
    while i < n:
        a, b = b, a+b
        yield b
        i += 1

my_fib_generator = (x for x in fib(0))
print(my_fib_generator)
for num in my_fib_generator:
    print(num)
