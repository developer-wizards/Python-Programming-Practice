#!/usr/bin/env python

# simple_generator.py

def gen():

   x, y = 1, 5
   yield x, y
   
   x += 1
   yield x, y

g = gen()

print(next(g))
print(next(g))


try:
   print(next(g))
   
except StopIteration:
   print("Iteration finished")
