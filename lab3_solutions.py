
''' (1) Exploring Arguments and Parameters '''

def print_two(a, b):
	print("Arguments: {} and {}".format(a,b))

#print_two() # invalid -- TypeError for omitting both required positional args
#print_two(4, 1) # valid
#print_two(41) # invalid -- TypeError for omitting 1 required positional arg
#print_two(a=4, 1) # invalid -- SyntaxError for having non-keyword arg after keyword arg
#print_two(4, a=1) # invalid -- TypeError for passing multiple values for 'a'
#print_two(4, 1, 1) # invalid -- TypeError for passing 3 positional args instead of 2
#print_two(b=4, 1) # invalid -- SyntaxError for having non-keyword arg after keyword arg
#print_two(a=4, b=1) # valid
#print_two(b=1, a=4) # valid
#print_two(1, a=1) # invalid -- TypeError for passing multiple values for 'a'
#print_two(4, 1, b=1) # invalid -- TypeError for passing multiple values for 'b'


def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

# keyword_args(5) # valid ==> a:  5 , b:  1 , c:  X , d:  None
# keyword_args(a=5) # valid, same output as above
# keyword_args(5, 8) # valid  ==> a:  5 , b:  8 , c:  X , d:  None
# keyword_args(5, 2, c=4) # valid ==> a:  5 , b:  2 , c:  4 , d:  None
# keyword_args(5, 0, 1) # valid ==> a:  5 , b:  0 , c:  1 , d:  None
# keyword_args(5, 2, d=8, c=4) # valid  ==> a:  5 , b:  2 , c:  4 , d:  8
# keyword_args(5, 2, 0, 1, "") # invalid -- TypeError for passing 5 args
# keyword_args(c=7, 1) # invalid -- SyntaxError for passing non-keyword arg after keyword arg
# keyword_args(c=7, a=1) # valid  ==> a:  1 , b:  1 , c:  7 , d:  None
# keyword_args(5, 2, [], 5) # valid ==> a:  5 , b:  2 , c:  [] , d:  5
# keyword_args(1, 7, e=6) # invalid -- TypeError for passing unexpected keyword arg 'e'
# keyword_args(1, c=7) # valid  ==> a:  1 , b:  1 , c:  7 , d:  None
# keyword_args(5, 2, b=4) # invalid -- TypeError for passing multiple values for'b'

def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

#variadic(2,3,5,7) # valid
  # Positional:  (2, 3, 5, 7)
  # Keyword:  {}

# variadic(1,1,n=1) # valid
  # Positional:  (1, 1)
  # Keyword:  {'n': 1}

# variadic(n=1, 2, 3) # invalid -- SyntaxError for passing non-keyword arg after keyword arg

# variadic() # valid
  # Positional:  ()
  # Keyword:  {}

# variadic(cs="Computer Science", pd="Product Design") # valid
  # Positional:  ()
  # Keyword:  {'pd': 'Product Design', 'cs': 'Computer Science'}

# variadic(cs="Computer Science", cs="CompSci", cs="CS") # invalid -- SyntaxError for repeating keyword arg

# variadic(5,8,k=1,swap=2) # valid
  # Positional:  (5, 8)
  # Keyword:  {'k': 1, 'swap': 2}

# variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'}) # valid
  # Positional:  (8, 3, 4, 5)
  # Keyword:  {'b': 'x', 'k': 1, 'a': 5}

# variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'}) # invalid -- SyntaxError for double *

# variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'}) # invalid -- SyntaxError for double *

# variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'}) # valid
  # Positional:  ({'b': 'x', 'a': 5}, 'b', 'a')
  # Keyword:  {'b': 'x', 'a': 5}

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

# all_together(2) #invalid -- TypeError: all_together() missing 1 required positional argument: 'y'

# all_together(2, 5, 7, 8, indent=False) # valid
  #  ==> x:  2 , y:  5 , z:  7
  # ==> nums:  (8,) , indent:  False , spaces:  4 , options:  {}

# all_together(2, 5, 7, 6, indent=None) # valid
 # ==> x:  2 , y:  5 , z:  7
 # ==> nums:  (6,) , indent:  None , spaces:  4 , options:  {}

# all_together() # invalid -- TypeError: all_together() missing 2 required positional arguments: 'x' and 'y'

# all_together(indent=True, 3, 4, 5) # invalid -- SyntaxError: non-keyword arg after keyword arg

# all_together(**{'indent': False}, scope='maximum') # invalid -- SyntaxError

# all_together(dict(x=0, y=1), *range(10)) # valid
  # ==> x:  {'x': 0, 'y': 1} , y:  0 , z:  1
  # ==> nums:  (2, 3, 4, 5, 6, 7, 8, 9) , indent:  True , spaces:  4 , options:  {}

# all_together(**dict(x=0, y=1), *range(10)) # invalid -- SyntaxError

# all_together(*range(10), **dict(x=0, y=1)) # invalid -- TypeError: got multiple values for 'x'

# all_together([1, 2], {3:4}) # valid
  # ==> x:  [1, 2] , y:  {3: 4} , z:  1
  # ==> nums:  () , indent:  True , spaces:  4 , options:  {}

# all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'}) # invalid -- TypeError: got multiple values for 'x'

# all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'}) # valid
  # ==> x:  8 , y:  9 , z:  10
  # ==> nums:  (2, 4, 6) , indent:  True , spaces:  0 , options:  {'b': 'x', 'a': [4, 5]}

# all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'}) # invalid -- SyntaxError



''' (2) Writing Functions '''

def speak_excitedly(msg, numExclamations=1, capitalize=False):
    result = msg + '!' * numExclamations
    print(result if not capitalize else result.upper())
	
# "I love Python!" ==> speak_excitedly("I love Python")
# "Keyword arguments are great!!!!" ==> speak_excitedly("Keyword arguments are great", 4)
# "I guess Java is okay..." ==> speak_excitedly("I guess Java is okay...", 0)
# "LET'S GO STANFORD!!" ==> speak_excitedly("let's go stanford", 3, True)



def average(*args):
    if not args: return 0   # avoid ZeroDivisionError if args is an empty tuple
    return sum(args) / len(args)

# average(*l)



def make_table(**kwargs):
    longestKey = max([len(key) for key in kwargs.keys()])
    longestValue = max([len(val) for val in kwargs.values()])
    upperLowerBound = '=' * (longestValue + longestKey + 5)

    print(upperLowerBound)
    for k, v in kwargs.items():

        left = '|' + k + ' ' * (longestKey - len(k) + 1)
        right = ' ' * (longestValue - len(v) + 1) + v
        print(left, right
            , sep='|', end='|\n')

    print(upperLowerBound)


''' (3) Function Nuances '''

def say_hello():
    print("Hello!")

print(say_hello())  # => None

def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())  # => None
print(echo(5)) # => 5
print(echo("Hello")) # => Hello

def drive(has_car):
    if not has_car:
        return
    return 100  # miles

print(drive(False))  # => None
print(drive(True)) # => 100











