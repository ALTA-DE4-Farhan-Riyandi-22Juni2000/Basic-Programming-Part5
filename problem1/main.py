import math

def prime_number(number):
  if number < 2:
    return False

  sqrt_ceiling = math.ceil(math.sqrt(number))

  for i in range(2, sqrt_ceiling + 1):
    if number % i == 0 and i != number:
      return False

  return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
