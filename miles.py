'''
def sum(num1, num2):
    return num1 + num2

num1, num2 = input('Enter two numbers: ').split()
num1 = int(num1)
num2 = int(num2)
print("The sum of {} and {} is {}".format(num1, num2, sum(num1, num2)))
'''

'''
def solveEquation(equation):
    x, operator, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    if operator == "+":
        return "x = " + str(num2 - num1)
    elif operator == "-":
        return "x = " + str(num1 + num2)
    elif operator == "/":
        return "x = " + str(num1 * num2)
    elif operator == "*":
        return "x = " + str(num2 / num1)


print(solveEquation("x + 4 = 9"))
print(solveEquation("x - 4 = 9"))
print(solveEquation("x / 4 = 9"))
print(solveEquation("x * 4 = 9"))

def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)
mult, divide = mult_divide(6, 3)

print(mult, divide)
'''
'''
def isPrime(num):
    num = int(num)
    for i  in range(2, num):
        if (num % i == 0) :
            return False
    return True

num = input('Enter a number: ')

if (isPrime(num) == True):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
'''

'''
def isprime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def getPrime(maxValue):
    maxValue = int(maxValue)
    list_of_prime = []
    for i in range(2, maxValue):
        if (isprime(i)):
            list_of_prime.append(i)
    return list_of_prime

list_of_prime = getPrime(input("Enter a number: "))
for i in list_of_prime:
    print(i)
'''
'''
def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
 
print("The sum is: ", sumAll(2,3,4,5,6,6,4,3))
'''

'''
def solveForX(example):
    x, operator, num1, equal, num2 = example.split()
    num1 = int(num1)
    num2 = int(num2)
    if (operator == '+'):
        return (num2 - num1)
    elif (operator == '-'):
        return (num1 + num2)
    
print("x = {}".format(solveForX("x + 5 = 9")))

def prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    else:
        return
'''

'''
name = input("Please enter your name: ")

def greetings(name):
    print("Hello {name}".format(name = name))

greetings(name)
'''

'''
learners = ['john', 'fredy', 'ebuka', 'milke']

i = 0
while i < len(learners):
    print("{} is awsome".format(learners[i].capitalize()))
    i += 1

for learner in learners:
    print(f"{learner.capitalize()} is so so awsome")
'''


'''
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
word = word.lower()
found = []
for i in word:
    if i in vowels:
        if i not in found:
            found.append(i)
for letter in found:
    print(letter)
'''

class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User()
u.is_new