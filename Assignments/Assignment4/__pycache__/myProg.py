import math

# 1. Palindrome Check
def palindrome_demo():
    print("Program: Palindrome Check")
    print("""
def is_palindrome(s):
    s = str(s)
    return s == s[::-1]
    """)
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome(12321) -> True")
    print("Test Case 3: is_palindrome('hello') -> False")
    print("Explanation: A palindrome reads the same forward and backward.")

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


# 2. Factorial (Recursive)
def factorial_demo():
    print("Program: Factorial (Recursive)")
    print("""
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
    """)
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(0) -> 1")
    print("Explanation: Uses recursion where factorial(n) = n * factorial(n-1).")

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


# 3. Fibonacci Series
def fibonacci_demo():
    print("Program: Fibonacci Series")
    print("""
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
    """)
    print("Test Case 1: fibonacci(5) -> [0, 1, 1, 2, 3]")
    print("Test Case 2: fibonacci(7) -> [0, 1, 1, 2, 3, 5, 8]")
    print("Explanation: Adds last two numbers to generate next term.")

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


# 4. Armstrong Number
def armstrong_demo():
    print("Program: Armstrong Number Check")
    print("""
def is_armstrong(num):
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    return total == num
    """)
    print("Test Case 1: is_armstrong(153) -> True")
    print("Test Case 2: is_armstrong(123) -> False")
    print("Explanation: Armstrong number = sum of digits raised to the power of number of digits.")

def is_armstrong(num):
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    return total == num


# 5. Prime Number Check
def prime_demo():
    print("Program: Prime Number Check")
    print("""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    """)
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(10) -> False")
    print("Explanation: A prime number has only two factors: 1 and itself.")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# 6. GCD of Two Numbers
def gcd_demo():
    print("Program: GCD of Two Numbers")
    print("""
import math
def gcd(a, b):
    return math.gcd(a, b)
    """)
    print("Test Case 1: gcd(48, 18) -> 6")
    print("Test Case 2: gcd(7, 5) -> 1")
    print("Explanation: Uses math.gcd() to find greatest common divisor.")

import math
def gcd(a, b):
    return math.gcd(a, b)


# 7. LCM of Two Numbers
def lcm_demo():
    print("Program: LCM of Two Numbers")
    print("""
def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1
    """)
    print("Test Case 1: lcm(4, 6) -> 12")
    print("Test Case 2: lcm(7, 5) -> 35")
    print("Explanation: Increments the larger number until it is divisible by both.")

def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


# 8. Reverse a String
def reverse_string_demo():
    print("Program: Reverse a String")
    print("""
def reverse_string(s):
    return s[::-1]
    """)
    print("Test Case 1: reverse_string('hello') -> 'olleh'")
    print("Test Case 2: reverse_string('Python') -> 'nohtyP'")
    print("Explanation: Uses Python slicing with step -1.")

def reverse_string(s):
    return s[::-1]


# 9. Count Vowels
def count_vowels_demo():
    print("Program: Count Vowels in String")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
    """)
    print("Test Case 1: count_vowels('hello') -> 2")
    print("Test Case 2: count_vowels('sky') -> 0")
    print("Explanation: Loops through string and counts vowels.")

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# 10. Decimal to Binary
def dec_to_bin_demo():
    print("Program: Convert Decimal to Binary")
    print("""
def dec_to_bin(n):
    return bin(n)[2:]
    """)
    print("Test Case 1: dec_to_bin(5) -> '101'")
    print("Test Case 2: dec_to_bin(10) -> '1010'")
    print("Explanation: Uses Python's built-in bin() and removes '0b' prefix.")

def dec_to_bin(n):
    return bin(n)[2:]