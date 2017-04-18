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

fact(3)  # => 6
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
def original_block():
  if score == 1:
    return "Winner"
  elif score == -1:
    return "Loser"
  else:
    return "Tied"

def better_block():



  
