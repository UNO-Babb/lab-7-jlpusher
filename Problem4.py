#Problem4.py
# #Project Euler problem 4

from NumberTests import isPalindrome

productsOfThree = []
for i in range(100,1000):
    for j in range(100,1000):
        productsOfThree.append(i*j)



def main():
  productPalindrome3 = []

  for p in productsOfThree:
    if isPalindrome(p):   
      productPalindrome3.append(p)
      largestPalindrome = max(productPalindrome3)
      print(largestPalindrome)
      #I can't get this to NOT print several values. This is due to being within the loop but if I pull it out then I get an error because the 'argument is empty'.
  

if __name__ == '__main__':
  main()
