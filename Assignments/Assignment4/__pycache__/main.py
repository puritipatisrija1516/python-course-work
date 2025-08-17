import myProg

def menu():
    print("\n====== FUNCTION BANK MENU ======")
    print("1. Palindrome Check")
    print("2. Factorial (Recursive)")
    print("3. Fibonacci Series")
    print("4. Armstrong Number Check")
    print("5. Prime Number Check")
    print("6. GCD of Two Numbers")
    print("7. LCM of Two Numbers")
    print("8. Reverse a String")
    print("9. Count Vowels in a String")
    print("10. Convert Decimal to Binary")
    print("0. Exit")
    print("================================")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '0':
        print("✅ Thank You for using the Function Bank!!")
        break

    elif choice == '1':
        myProg.palindrome_demo()
        s = input("Enter a string/number: ")
        print("➡ Palindrome:", myProg.is_palindrome(s))

    elif choice == '2':
        myProg.factorial_demo()
        n = int(input("Enter a number: "))
        print(f"➡ Factorial of {n} =", myProg.factorial(n))

    elif choice == '3':
        myProg.fibonacci_demo()
        n = int(input("Enter number of terms: "))
        print(f"➡ Fibonacci series ({n} terms):", myProg.fibonacci(n))

    elif choice == '4':
        myProg.armstrong_demo()
        n = int(input("Enter a number: "))
        if myProg.is_armstrong(n):
            print(f"✅ {n} is an Armstrong Number")
        else:
            print(f"❌ {n} is NOT an Armstrong Number")

    elif choice == '5':
        myProg.prime_demo()
        n = int(input("Enter a number: "))
        if myProg.is_prime(n):
            print(f"✅ {n} is Prime")
        else:
            print(f"❌ {n} is NOT Prime")

    elif choice == '6':
        myProg.gcd_demo()
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"➡ GCD of {a} and {b} =", myProg.gcd(a, b))

    elif choice == '7':
        myProg.lcm_demo()
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"➡ LCM of {a} and {b} =", myProg.lcm(a, b))

    elif choice == '8':
        myProg.reverse_string_demo()
        s = input("Enter a string: ")
        print("➡ Reversed string:", myProg.reverse_string(s))

    elif choice == '9':
        myProg.count_vowels_demo()
        s = input("Enter a string: ")
        print("➡ Vowel count:", myProg.count_vowels(s))

    elif choice == '10':
        myProg.dec_to_bin_demo()
        n = int(input("Enter a decimal number: "))
        print(f"➡ Binary of {n} =", myProg.dec_to_bin(n))

    else:
        print("⚠ Invalid choice! Please try again.")