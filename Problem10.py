#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime

def main():
    total = 0
    
    for i in range(100000): #code works but is significantly delayed with the higher range.
        if isPrime(i):  
            total += i

    print(total)
  

if __name__ == '__main__':
  main()
