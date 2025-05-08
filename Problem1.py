#Project Euler Problem 1

import NumberTests  #import from external file

def main():
  total = 0
  for i in range(1001):   #going through all the numbers up through 1000
    if NumberTests.isThreeOrFive(i):  #if number is 3 or 5 then we add to total
      total += i

  print(total)


if __name__ == '__main__':
  main()
