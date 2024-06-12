'''Module 1'''
#Write a python program to input a time in seconds and print the time in
#HH:MM:SS format.
def convert(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    print(f"Time in HH:MM:SS is : {hour}:{minutes}:{seconds}")
    
def circle(radius):
    print("Area of a circle is : ", 3.14*radius*radius)
    print("Circumference of a circle is : ", 2*3.14*radius)

#Program that accepts the length of three sides of a triangle as input and determine
#whether or not the triangle is right angled or not
def isrightAngled(a,b,c):
    if a**2 + b**2 == c**2:
        print("The triangle is right angled")
    else:
        print("The triangle is not right angled")
        
#Program to input a point and find the quadrant.
def checkQuadrant(x, y):
    if x > 0 and y > 0:
        print(f"Point ({x},{y}) is in quadrant 1")
    elif x < 0 and y > 0:
        print(f"Point ({x},{y}) is in quadrant 2")
    elif x < 0 and y < 0:
        print(f"Point ({x},{y}) is in quadrant 3")
    elif x > 0 and y < 0:
        print(f"Point ({x},{y}) is in quadrant 4")
    elif x == 0 and y == 0:
        print(f"Point ({x},{y}) is at the origin")
    elif x == 0:
        print(f"Point ({x},{y}) is on the y-axis")
    elif y == 0:
        print(f"Point ({x},{y}) is on the x-axis")

#Program to find the Sum of the digits of a number.        
def sumofdigits(number):
    temp = number
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    print(f"Sum of digits of number {temp} is {sum}")

import cmath
#Program to find the roots of a quadratic eq
def roots(a,b,c):
    d = b**2 -4*a*c
    
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print("Roots are real and different.")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif d == 0:
        root = -b / (2*a)
        print("Roots are real and the same.")
        print(f"Root: {root}")
    else:
        root1 = (-b + cmath.sqrt(d)) / (2*a)
        root2 = (-b - cmath.sqrt(d)) / (2*a)
        print("Roots are imaginary.")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
        
def isPrime(number):
    if number < 1:
        print(f"{number} is not prime")
    elif number == 1:
        print(f"{number} is not prime not composite")
    else:
        f = 0
        for i in range(2, number):
            if number % i == 0:
                f = 1
                break
        
        if f:
            print(f"{number} is not prime")
        else:
            print(f"{number} is prime")
        
#Python program to find the sum of even numbers from N given numbers.
def evenSum(numbers):
    sum = 0
    for x in numbers:
        if x % 2 == 0:
            sum += x
    print(f"Sum of all even numbers is : {sum}")
    
'''Write a Python program which takes a positive integer n as input and finds
the sum of cubes of all positive even numbers less than or equal to the
number'''
def cubeSum(number):
    if number <= 0:
        print("Error")
    else:
        sum = 0
        for i in range(2, number + 1, 2): 
            sum += i**3
        print(f"Sum is {sum}")


def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
fibonacci(10)

if __name__ == "__main__":
    seconds = int(input("Enter a time in seconds : "))
    convert(seconds)
    
    radius = int(input("\nEnter the radius of the circle: "))
    circle(radius)
    
    input_sides = input("\nEnter 3 sides of the triangle : ").split()
    a, b, c = map(int, input_sides)
    max_side = max(a, b, c)

    if max_side == a:
        isrightAngled(b, c, a)
    elif max_side == b:
        isrightAngled(a, c, b)
    else:
        isrightAngled(a, b, c)
    
    x = int(input("\nEnter the x coordinate of the point : "))
    y = int(input("Enter the y coordinate of the point : "))
    checkQuadrant(x,y)
    
    num = int(input("\nEnter a number: "))
    sumofdigits(num)
    
    input_coeff = input("\nEnter coeff of ax^2 + bx +c : ").split()
    a, b, c = map(int, input_coeff)
    roots(a,b,c)
    
    num = int(input("\nEnter a number: "))
    isPrime(num)
    
    evenSum([1,3,4,2,6,7,3,9,10])
    
    num = int(input("\nEnter a number: "))
    cubeSum(num)
    