from functools import reduce

def factors(n : int) -> set:
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def lcm(x, y) -> int:
   greater = x if x > y else y
   while(True):
       if ((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm