def prime_checker(number):
    divisors = []
    for i in range(1, number + 1, 1):
        if number % i == 0:
            divisors.append(i)
    # print(divisors)
    if divisors == [1, number]:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("enter a number: "))  # Check this number
prime_checker(number=n)