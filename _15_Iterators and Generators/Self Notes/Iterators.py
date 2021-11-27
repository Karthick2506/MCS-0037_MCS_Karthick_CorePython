'''
Iterators are everywhere in Python.

They are elegantly implemented within for loops, comprehensions, generators etc. but are hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__(),
collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it.
Most built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

iter()----->gives ther object of the iterator
next()------>gives the next object'''


my_list = [1, 2, 3, 4, 5]

# get an iterator using iter()
my_iter = iter(my_list)
print(my_iter.__next__())

# iterate through it using next()
print(next(my_iter)) # Output 1
print(next(my_iter)) # Output 2
print(my_iter.__next__()) # Output 3
print(my_iter.__next__()) # Output 4
# print(my_iter.__next__())  #stopIteration occurs


"""Creating our own object or iterator"""

# print even numbers from 1 to 15.

class samplee:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = samplee()

print(next(values))
print(next(values))

for i in values:
    print(i)








