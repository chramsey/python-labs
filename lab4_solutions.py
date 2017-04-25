""" (1) FUNCTIONAL TOOLS """

## Maps
 def test_map():
    map(int, ['12', '-2', '0']) 
    # change strings to ints
    # ['12', '-2', '0'] -> [12, -2, 0]
    map(len, ['hello', 'world'])
    # convert from string to string length
    # ['hello', 'world'] -> [5, 5]
    map(lambda s: s[::-1], ['hello', 'world'])
    # change strings to their sorted selves
    # ['hello', 'world'] -> ['olleh', 'dlrow']
    map(lambda n: (n, n ** 2, n ** 3), range(2, 6))
    # change a number to a tuple: (n, n^2, n^3)
    # range(2, 6) -> [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
    map(lambda l, r: l * r, zip(range(2, 5), range(3, 9, 2)))
    # (2 * 3, 3 * 5, 4 * 7)
    # zip(range(2, 5), range(3, 9, 2)) -> [6, 15, 28]

## Filter
def filter_test():
  filter(lambda x: int(x) >= 0, ['12', '-2', '0']) 
  # check if int version is positive
  # ['12', '-2', '0'] -> ['12', '0']
  filter(lambda x: x == 'world', ['hello', 'world'])
  # check if value is 'world'
  # ['hello', 'world'] -> ['world']
  filter(lambda x: x[0] == 'S', ['Stanford', 'Cal', 'UCLA'])
  # check if string begins with 'S'
  # ['Stanford', 'Cal', 'UCLA'] -> ['Stanford']
  filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20))
  # check if number is divisible by 3 or 5
  # range(20) -> [0, 3, 5, 6, 9, 10, 12, 15, 18]
  
""" (2) OTHER USEFUL TOOLS """

## functools
import operator
from functools import reduce

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def lcm(*args):
  return functools.reduce(lambda x, y: x * y / gcd (x, y), args) 


## operator
import operator
from functools import reduce

def fact(n):
    return functools.reduce(operator.mul, range(n))

fact

# => 6
fact(7)  # => 5040
  
## Custom Comparison
words = ['pear', 'cabbage', 'apple', 'bananas']
min(words)  # => 'apple'
words.sort(key=lambda s: s[-1])  # Alternatively, key=operator.itemgetter(-1)
words  # => ['cabbage', 'apple', 'pear', 'bananas']
#... Why 'cabbage' < 'apple'?
# Because the builtin sort is stable - even though they both have the smae
# value after application of the key function, cabbage appears before apple
# in the original list, so it also is before apple in the sorted list
max(words, key=len)  # 'cabbage' ... Why not 'bananas'?
# same reason - because the sort is stable, in the event of a tie, the element
# that originally appears first is the one with a "lower" value
x= min(words, key=lambda s: s[1::2])  # What will this value be?
# bananas, since it's aaa under the action of the sort key
print(x)
    
    
    
    
def alpha_score(upper_letters):
  return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha_score('ABC')
# 6 => 'A' = 1, 'B' = 2, 'C' = 3 => 1 + 2 + 3 = 6

def two_best(words):
  words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
  return words[:2]

two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn'])
# => ['PyThOn', 'wOrLD']    

""" (3) PURELY FUNCTIONAL PROGRAMMING """

## Replacing Control Flow
def original_block(score):
  if score == 1:
    return "Winner"
  elif score == -1:
    return "Loser"
  else:
    return "Tied"

def better_block(score):
  return (score == 1 and "Winner") or (score == -1 and "Loser") or "Tied"
 

 
 """ (4) ITERATORS """
it = iter(range(100))
# 67 in it  # => True
# next(it)  # => 68
# 37 in it  # => False
# next(it)  # => StopIteration

## Module: itertools
import itertools
import operator

for el in itertools.permutations('XKCD', 2):
    print(el, end=', ')
# ('X', 'K'), ('X', 'C'), ('X', 'D'), ('K', 'X'), ('K', 'C'), ('K', 'D'), ('C', 'X'), ('C', 'K'), ('C', 'D'), ('D', 'X'), ('D', 'K'), ('D', 'C'),

for el in itertools.cycle('LO'):
    print(el, end='')  # Don't run this one. Why not?
# LOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLOLO........

itertools.starmap(operator.mul, itertools.zip_longest([3,5,7],[2,3], fillvalue=1))
# this zips the lists together, filling in any missing value with a one:
# (3,2), (5,3), (7,1)
# then it multiplies the resulting structures
# 6, 15, 7




## Dot Product
def dot_product(u, v):
  return sum([s[0]*s[1] for s in zip(u,v)])
# or:
def dot_product(u, v):
  return sum(itertools.starmap(operator.mul, zip(u,v)))
 
## Linear Algebra
def transpose(m):
 return tuple(zip(*m))
#  What does this look like?
#      | 1 2 3 |
# m =  | 4 5 6 |
#      | 7 8 9 |
#   = [ [1,2,3], [4,5,6], [7,8,9] ]
# mT = transpose(m):
#      | 1 4 7 |
# mT = | 2 5 8 |
#      | 3 6 9 |
# mT = [ [1,4,7], [2,5,8], [3,6,9] ]

# Matrix Multiplication
def matmul(m1, m2):
  return tuple(map(lambda row: tuple(dot_product(row, col) for col in transpose(m2)), m1))


#  Lazy Generation
def lazy_transpose(m):
  return zip(*m)
 
def lazy_matmul(m1,m2):
  return map(lambda row: (dot_product(row, col) for col in transpose(m2)), m1)
 
""" (5) GENERATOR EXPRESSIONS AND GENERATORS """
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 

# 1 - Searching for a given entity in the entries of a 1TB database.
# => Generator expression: we only need to keep track of the current element for comparison
# 2 - Calculate cheap airfare using journey-to-destination flight information.
# => List comprehension: need to keep track of your flight paths and the cost of each leg
# 3 - Finding the first palindromic Fibonacci number greater than 1,000,000.
# => 
# 4 - Determine all multi-word anagrams of user-supplied 1000-character-or-more strings (very expensive to do).
# => 
# 5 - Generate a list of names of Stanford students whose SUNet ID numbers are less than 5000000.
# => List comprehension
# 6 - Return a list of all startups within 50 miles of Stanford.
# => List comprehension

## Generators
def generate_triangles():
 n = 0
 total = 0
 while True:
  total += n
  n += 1
  yield total

 def triangles_under(n):
  for triangle in generate_triangles():
   if triangle >= n:
    break
   print(triangle)
  
  """ (6) FUNCTIONS IN DATA STRUCTURES """
def make_divisibility_test(n):
 return lambda m: m % n == 0                         
  
def primes_under(n):
 tests = []
 for i in range(2,n):
  if not any(map(lambda test: test(i), tests)):
   tests.append(make_divisibility_test(i))
   yield i
    
# If a number isn't a prime, then it's composite:
def generate_composites():
 tests = []
 i = 2
 while True:
#  test if it's prime:
  if not any(map(lambda test: test(i), tests)):
   tests.append(make_divisibility_test(i))
#   otherwise it's composite:
  else:
   yield i
  i += 1
  
 def nth_composite(n):
  g = generate_composites()
  for i in range(n - 1):
   next(g)
  return nex(g)
 
 
 """ (7) NESTED FUNCTIONS AND CLOSURES """ 
 def outer():
    def inner(a):
        return a
    return inner

f = outer()
print(f)  # <function outer.<locals>.inner at 0x1044b61e0>
f(10)  # => 10

f2 = outer()
print(f2)  # <function outer.<locals>.inner at 0x1044b6268> (Different from above!)
f2(11)  # => 11
    
# 'f' and 'f2' were created at different times:
# 'f' at the first call of outer() and 'f2' at the second call of outer().

## Closure
def outer(l):
    def inner(n):
        return l * n
    return inner
    
l = [1, 2, 3]
f = outer(l)
print(f(3))  # => [1, 2, 3, 1, 2, 3, 1, 2, 3]

l.append(4)
print(f(3))  # => [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
"""
What's happening? `f`, when it was defined as `inner`, wrapped a closure around
a *reference* to the list object `l`. Closures don't copy the objects, but rather
copy the references to the enclosed objects. So, when the underlying list `l` changes
then when `f` executes and tries to resolve the name `l`, it find the original `l` object
which has been changed.
"""
    
 """ (8) Building Decorators """
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 
# TO DO TO DO TO DO TO DO 

##print_args
def bind_args(function, *args, **kwargs):
    """Returns an map from the names of function's arguments to values given by *args and **kwargs
    This is more or less an implementation of Python argument bind semantics, but it's not super accurate
    ¯\_(ツ)_/¯
        For example, it doesn't resolve any closure elements or anything, because ahh that's awful
    First, positional arguments are bound
    If you're a student reading this, you can ignore this implementation.
    Pre: *args and **kwargs represent valid parameters
    """
    sig = inspect.Signature.from_function(function)
    ba = sig.bind(*args, **kwargs)
    return ba.arguments


def print_args(function):
    """Decorate the given function to print out it's arguments and return val if not None
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        bound_arguments = bind_args(function, *args, **kwargs)
        print("{name}({call})".format(
            name=function.__name__,
            call=', '.join("{}={}".format(arg, val) for arg, val in bound_arguments.items())
        ))
        retval = function(*args, **kwargs)
        if retval is not None:
            print("(return) {!r}".format(retval))
        return retval
    return wrapper

   
   
## Automatic Caching
def cache(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in function._cache:
            return function._cache[key]
        retval = function(*args, **kwargs)
        function._cache[key] = retval
        return retval
    return wrapper
   
 @cache
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1

fib(10)  # 55 (takes a moment to execute)
fib(10)  # 55 (returns immediately)
fib(100) # doesn't take forever
fib(400) # doesn't raise RuntimeError

## Cache Challenge Options
def cache_challenge(max_size=None, eviction_policy='LRU'):
    assert eviction_policy in ['LRU', 'MRU', 'random']
    def decorator(function):
        function._cache = collections.OrderedDict()
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key in function._cache:
                # Before accessing this element, move it to the MRU side
                # of the list
                function._cache.move_to_end(key)
                return function._cache[key]
            retval = function(*args, **kwargs)

            # Check for eviction
            if max_size and len(function._cache) == max_size:
                if eviction_policy == 'LRU':
                    function._cache.popitem(last=False)
                elif eviction_policy == 'MRU':
                    function._cache.popitem(last=True)
                else:
                    randkey = random.choice(list(function._cache.keys()))
                    function._cache.pop(randkey)
            # Now that we know there's space, insert the element
            function._cache[key] = retval
            return retval
        return wrapper
    return decorator

@cache_challenge(max_size=16, eviction_policy='LRU')
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1

""" (9) STATIC TYPE CHECKER """
def enforce_types(function):
    expected = function.__annotations__
    if not expected:
        return function
    assert(all(map(lambda exp: type(exp) == type, expected.values())))
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        bound_arguments = bind_args(function, *args, **kwargs)
        for arg, val in bound_arguments.items():
            if arg in expected and not isinstance(val, expected[arg]):
                print("(Bad Argument Type!) argument '{arg}={val}': expected {exp}, received {r}".format(
                    arg=arg,
                    val=val,
                    exp=expected[arg],
                    r=type(val)
                ))

        retval = function(*args, **kwargs)

        # Check the return value
        if 'return' in expected and not isinstance(retval, expected['return']):
            print("(Bad Return Value!) return '{ret}': expected {exp}, received {r}".format(
                ret=retval,
                exp=expected['return'],
                r=type(retval)
            ))
        return retval
    return wrapper

@enforce_types
# def foo(a: int, b: str) -> bool:
    # if a == -1:
    #     return 'Gotcha!'
    # return b[a] == 'X'

foo(3, 'XYZXYZ')  # => True
foo(2, 'python')  # => False
foo(1, 4)  # prints "(Bad Argument Type!) argument b=4: expected <class 'str'>, received <class 'int'>" and then crashes
foo(-1, '')  # prints "(Bad Return Value!) return Gotcha!: expected <class 'bool'>, received <class 'str'>" and returns "Gotcha!"


## BONUS: OPTION DEBUG ASSIGNMENT
def enforce_types_challenge(severity=1):
    assert severity in [0, 1, 2]
    if severity == 0:
        # Return a no-op decorator
        return lambda function: function

    def message(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)

    def decorator(function):
        expected = function.__annotations__
        if not expected:
            return function
        assert(all(map(lambda exp: type(exp) == type, expected.values())))

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            bound_arguments = bind_args(function, *args, **kwargs)
            for arg, val in bound_arguments.items():
                if arg in expected and not isinstance(val, expected[arg]):
                    msg("(Bad Argument Type!) argument '{arg}={val}': expected {exp}, received {r}".format(
                        arg=arg,
                        val=val,
                        exp=expected[arg],
                        r=type(val)
                    ))

            retval = function(*args, **kwargs)

            # Check the return value
            if 'return' in expected and not isinstance(retval, expected['return']):
                msg("(Bad Return Value!) return '{ret}': expected {exp}, received {r}".format(
                    ret=retval,
                    exp=expected['return'],
                    r=type(retval)
                ))
            return retval
        return wrapper
    return decorator


@enforce_types_challenge(severity=2)
def bar(a: list, b: str) -> int:
    return 0

@enforce_types_challenge()  # Note that there are parentheses
def baz(a: bool, b: str) -> str:
    return ''

if __name__ == '__main__':
    """Runs each of the lab solution functions and prints the docstring"""
