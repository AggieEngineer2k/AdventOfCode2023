from functools import reduce

def factors(n : int) -> set:
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def lcm(n : "list(int)") -> int:
    if len(n) > 2:
        return lcm([n[0], lcm(n[1:])])
    else:
        greater = n[0] if n[0] > n[1] else n[1]
        while(True):
            if ((greater % n[0] == 0) and (greater % n[1] == 0)):
                x = greater
                break
            greater += 1
        return x