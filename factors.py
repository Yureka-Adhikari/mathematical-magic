def factors(n):
    print(f"The factors of {n} are:")
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
            
number = int(input("Enter a number to find its factors: "))
factors(number)