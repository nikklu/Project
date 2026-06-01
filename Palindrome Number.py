def isPalindrome(a):
    if a<0:
        return False
    s=str(a)
    return s==s[::-1]
#Example usage:
number = 121
if isPalindrome(number):
    print(f"{number} is a palindrome.")