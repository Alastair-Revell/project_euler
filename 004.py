# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

max_pal = 0
for i in range(100,999):
    for j in range(100,999):
      mult = i * j
      if str(mult) == str(mult)[::-1]: #Check if the number is palindrome
          if mult > max_pal:
              max_pal = mult
print (max_pal)
