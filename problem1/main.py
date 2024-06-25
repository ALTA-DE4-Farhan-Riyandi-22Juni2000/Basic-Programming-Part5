def prime_number(number):

  if number <= 1:
    return False
  elif number == 2 or number == 3 or number == 5 or number == 7:
    return True
  elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    return False
  else:
    return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
