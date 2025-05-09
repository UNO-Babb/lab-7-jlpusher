#Problem4.py
# #Project Euler problem 4

from NumberTests import isPalindrome

productsOfThree = []
for i in range(100,1000):
    for j in range(100,1000):
        productsOfThree.append(i*j)

productPalindrome3 = []

def main():
  for p in productsOfThree:
    if isPalindrome(p):
      productPalindrome3.append(p)
      
    largestPalindrome = max(productPalindrome3)
    print(largestPalindrome)
  

if __name__ == '__main__':
  main()
